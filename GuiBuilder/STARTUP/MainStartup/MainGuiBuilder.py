import os
from GuiBuilder.STARTUP.Install import SettingsLoader, InstallSettings, InstallProjects, DeleteProject
from MyPyWidgets import *
from GuiBuilder.STARTUP.MainStartup.MainGuiTemplate import GuiTemplate
import shutil
from GuiBuilder.BUILDER.ProjectTemplate.Tabs.ControlPanelTemplate import ControlPanel
from importlib import import_module as imp


def rerun():
    from __main__ import main
    main()


class GuiBuilder(object):

    def __init__(self, cwd):
        self.cwd = cwd
        self.v = Validator
        self.paths = {
            'cwd': self.cwd,
            'builder_settings': os.path.join(self.cwd, 'GuiBuilder', 'STARTUP', 'Settings', 'builder_settings.json'),
            'project_settings': os.path.join(self.cwd, 'GuiBuilder', 'STARTUP', 'Settings', 'project_settings.json'),
            'projects_path': os.path.join(self.cwd, 'GuiBuilder', 'PROJECTS'),
            'src_path': os.path.join(self.cwd, 'GuiBuilder', 'BUILDER', 'PROJECTBUILDER'),
            'src_template': os.path.join(self.cwd, 'GuiBuilder', 'BUILDER', 'ProjectTemplate')
        }
        self.project_choices = SettingsLoader(self.paths['project_settings']).fetch_settings()
        self.commands = {
            'save_settings': self.make_configure_settings,
            'exit_settings': self.exit_settings,
            'change_path': self.change_path,
            'exit_new': self.exit_new,
            'configure_settings': self.configure_settings,
            'new_project': self.make_new_project,
            'new_project_button': self.new_project,
            'load_project_button': self.load_project,
            'project_settings_button': self.configure_settings,
            'project_dropdown': self.project_choices,
            'load_project_go': self.load_project_go,
            'delete_project_go': self.delete_project,
            'run_project_go': self.run_project_go
        }
        self.template = None
        self.workspace = None

    def run(self):
        self.template = GuiTemplate(self.paths['projects_path'])
        self.template.main_kwargs['owner'] = self
        self.workspace = MyPyWindow(**self.template.main_kwargs)
        self.workspace.setup()
        self.build_widgets(self.template.main_components,
                           self.commands,
                           self.workspace)
        if len(self.project_choices) == 0:
            self.workspace.containers['load_project_button'].configure({'state': 'disabled'})
        self.workspace.run()

    def new_project(self):
        self.kill_toplevel('new_window', self.workspace.containers)
        self.workspace.add_toplevel(**self.template.new_kwargs)
        self.build_widgets(self.template.new_components,
                           self.commands,
                           self.workspace.containers['new_window'])

    def configure_settings(self):
        self.kill_toplevel('configure_window', self.workspace.containers)
        self.workspace.add_toplevel(**self.template.configure_kwargs)
        self.build_widgets(self.template.configure_components,
                           self.commands,
                           self.workspace.containers['configure_window'])
        self.display_settings()

    def load_project(self):
        self.kill_toplevel('load_window', self.workspace.containers)
        self.workspace.add_toplevel(**self.template.load_kwargs)
        self.build_widgets(self.template.load_components,
                           self.commands,
                           self.workspace.containers['load_window'])

    def load_project_go(self):
        project = self.workspace.containers['load_window'].containers['project_dropdown'].get()
        module = 'GuiBuilder.BUILDER.PROJECTBUILDER.{n}.MainGuiBuilder{n}'.format(n=project)
        gui_obj = getattr(imp(module), '{}Gui'.format(project))
        loaded_application = gui_obj(os.path.join(self.paths['projects_path'], '{}'.format(project)),
                                     os.path.join(self.paths['src_path'], project))
        self.workspace.leave()
        loaded_application.run()

    def run_project_go(self):
        project = self.workspace.containers['load_window'].containers['project_dropdown'].get()
        module = 'GuiBuilder.PROJECTS.{}.__main__'.format(project)
        run_project = getattr(imp(module), 'Main')
        run_project()

    def delete_project(self, really=False):
        project = self.workspace.containers['load_window'].containers['project_dropdown'].get()
        self.really(self.workspace.containers['load_window'], self.delete_project)
        if really:
            DeleteProject(self.paths['project_settings'], project).factory_settings()
            if os.path.exists(os.path.join(self.paths['projects_path'], project)):
                shutil.rmtree(os.path.join(self.paths['projects_path'], project))
            if os.path.exists(os.path.join(self.paths['src_path'], project)):
                shutil.rmtree(os.path.join(self.paths['src_path'], project))
            self.workspace.leave()
            rerun()

    def make_configure_settings(self):
        form_data = self.v.field_retrieve(
            self.workspace.containers['configure_window'].containers,
            ['width_input', 'height_input', 'vertical_offset_input', 'horizontal_offset_input'],
            [self.v.is_int, self.v.is_int, self.v.is_int, self.v.is_int], [[1], [1], [-800], [-800]])
        if form_data['_valid']:
            default_window = {'type': 'root',
                              'master': None,
                              'title': None,
                              'id': 'root_window',
                              'owner': None,
                              'base_location': {
                                  'row': 0,
                                  'column': 0,
                                  'rowspan': form_data['height_input'],
                                  'columnspan': form_data['width_input'],
                                  'sticky': 'NSWE'
                              },
                              'row_offset': form_data['vertical_offset_input'],
                              'column_offset': form_data['horizontal_offset_input']
                              }
            InstallSettings(self.paths['builder_settings'], default_window).factory_settings()
            self.workspace.containers['configure_window'].leave()

    def make_new_project(self):
        form_data = self.v.field_retrieve(self.workspace.containers['new_window'].containers,
                                          ['project_path', 'name_input', 'title_input'],
                                          [self.v.is_path, self.v.file_namify, self.v.not_empty],
                                          [[], [], []])
        if form_data['_valid']:
            if form_data['name_input'] in self.project_choices:
                self.workspace.containers['new_window'].containers['name_input'].configure({'bg': 'red'})
            else:
                self.build_project_dist(form_data['project_path'], form_data['name_input'])
                self.build_project_src(self.paths['src_path'], form_data['name_input'], form_data['title_input'])
                module = 'GuiBuilder.BUILDER.PROJECTBUILDER.{n}.MainGuiBuilder{n}'.format(n=form_data['name_input'])
                gui_obj = getattr(imp(module), '{}Gui'.format(form_data['name_input']))
                InstallProjects(self.paths['project_settings'], form_data['name_input']).factory_settings()
                new_application = gui_obj(
                    os.path.join(self.paths['projects_path'], '{}'.format(form_data['name_input'])),
                    os.path.join(self.paths['src_path'], form_data['name_input']))
                self.workspace.leave()
                new_application.run()

    def build_project_src(self, path, new_name, window_title):
        os.mkdir(os.path.join(path, new_name))
        open(os.path.join(path, new_name, '__init__.py'), 'a').close()
        shutil.copy(os.path.join(self.paths['src_template'], 'RootTemplate.py'), os.path.join(path, new_name))
        old_file = os.path.join(path, new_name, 'RootTemplate.py')
        new_file = os.path.join(path, new_name, 'MainGuiBuilder{}.py'.format(new_name))
        os.rename(old_file, new_file)
        f = open(new_file, 'r')
        my_list = f.readlines()
        f.close()
        lst = str(SettingsLoader(self.paths['builder_settings']).fetch_settings()
                  ).lstrip('{').rstrip('}').replace(', ', ',\n&').split('&')
        tmp_list = []
        for item in my_list:
            item = item.replace('Name', new_name.lower().capitalize())
            item = item.replace('name', new_name.lower())
            if item == '# WINDOW\n':
                stack = 0
                for line in lst:
                    if 'owner' in line:
                        line = line.split(':')[0] + ': self,\n'
                    elif 'title' in line:
                        line = line.split(':')[0] + ': "{}",\n'.format(window_title)
                    tmp_list.append('            ' + '                  ' * stack + line)
                    if '{' in line:
                        stack += 1
                    elif '}' in line:
                        stack -= 1
                tmp_list.append('\n')
            else:
                tmp_list.append(item)
        f = open(new_file, 'w')
        f.writelines(tmp_list)
        f.close()

        # TODO: FINISH ME

    def display_settings(self):
        tmp = SettingsLoader(self.paths['builder_settings']).fetch_settings()
        self.workspace.containers['configure_window'].containers['width_input'].set(
            tmp['base_location']['columnspan']
        )
        self.workspace.containers['configure_window'].containers['height_input'].set(
            tmp['base_location']['rowspan']
        )
        self.workspace.containers['configure_window'].containers['horizontal_offset_input'].set(
            tmp['column_offset']
        )
        self.workspace.containers['configure_window'].containers['vertical_offset_input'].set(
            tmp['row_offset']
        )

    def exit_settings(self):
        self.workspace.containers['configure_window'].leave()

    def exit_new(self):
        self.workspace.containers['new_window'].leave()

    def change_path(self):
        f = FileDialog(self.paths['projects_path'], 'dir').response()
        self.workspace.containers['new_window'].containers['project_path'].set(f)
        self.workspace.containers['new_window'].app.lift()

    @staticmethod
    def build_project_dist(path, new_name):
        os.mkdir(os.path.join(path, new_name))
        open(os.path.join(path, new_name, '__init__.py'), 'a').close()

    @staticmethod
    def build_widgets(widgets, commands, workspace):
        for widget in widgets:
            tmp_args = []
            for arg in widget['args']:
                if arg is None:
                    tmp_args.append(commands[widget['id']])
                else:
                    tmp_args.append(arg)
            widget['args'] = tmp_args
            workspace.add_widget(**widget)

    @staticmethod
    def kill_toplevel(top_id, containers):
        if top_id in list(containers.keys()):
            garbage = containers.pop(top_id)
            garbage.leave()
            del garbage

    @staticmethod
    def really(window, func):
        def wrap_go():
            window.containers['really_window'].leave()
            func(True)

        def wrap_cancel():
            window.containers['really_window'].leave()

        tmp = ControlPanel()
        window.add_toplevel(**tmp.really_kwargs)
        for item in tmp.really_components:
            tmp_args = []
            for arg in item['args']:
                if arg is None:
                    if item['id'] == 'really_go':
                        tmp_args.append(wrap_go)
                    elif item['id'] == 'really_cancel':
                        tmp_args.append(wrap_cancel)
                else:
                    tmp_args.append(arg)
            item['args'] = tmp_args
            window.containers['really_window'].add_widget(**item)
