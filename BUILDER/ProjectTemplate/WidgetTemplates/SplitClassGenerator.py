import os
from MyPyWidgets import *


class MultiGenerator(object):

    def __init__(self, working_directory, final_destination):
        """
        TODO: Fix templates so that there are no PEP violations (spacing, # newlines, etc.)
        This class generates the static Project folder.

        :param working_directory: The current working directory
        :param final_destination: The Project Destination
        """
        self.cwd = working_directory
        self.final_destination = final_destination
        self.name = os.path.basename(final_destination)

        self.lookup = {
            Button: 'Button',
            DropDown: 'DropDown',
            CheckButton: 'CheckButton',
            InputField: 'InputField',
            Label: 'Label',
            RadioButton: 'RadioButton',
            SpinBox: 'SpinBox'
        }

        self.paths = {
            'Cwd': self.cwd,
            'Templates': os.path.join(self.cwd, 'GuiBuilder', 'BUILDER', 'ProjectTemplate', 'WidgetTemplates'),
            'Components': os.path.join(self.final_destination, 'Components'),
            'Components__init__': os.path.join(self.final_destination, 'Components', '__init__.py'),
            'Project__init__': os.path.join(self.final_destination, '__init__.py'),
            'Frames': os.path.join(self.final_destination, 'Components', 'Frames'),
            'MainWidgets': os.path.join(self.final_destination, 'Components', 'MainWidgets'),
            'Final': self.final_destination,
            'Builder_Helper': os.path.join(self.final_destination, 'Components', 'Builder_Helper.py'),
            'MainGui': os.path.join(self.final_destination, 'MainGui.py'),
            'MainGuiTemplate': os.path.join(self.final_destination, 'MainGuiTemplate.py')
        }

        self.modules = [os.path.join(self.final_destination, 'Components'),
                        os.path.join(self.final_destination, 'Components', 'Frames'),
                        os.path.join(self.final_destination, 'Components', 'MainWidgets')
                        ]

        self.templates = {
            '__main__': self.load_template('MainTemplate.txt'),
            'BuilderHelper': self.load_template('BuildHelperTemplate.txt'),
            'Root': self.load_template('RootTemplate.txt'),
            'RootFrame': self.load_template('RootFrameTemplate.txt'),
            'MultiBase': self.load_template('MultiBaseTemplate.txt'),
            'Widget': self.load_template('WidgetTemplate.txt'),
            'Components__init__': self.load_template('Components__init__Template.txt'),
            'Project__init__': self.load_template('Project__init__Template.txt'),
            'ProjectFrame__init__': self.load_template('ProjectFrame__init__.txt'),
            'MainWidgets__init__': self.load_template('MainWidgets__init__Template.txt'),
            'CustomFrame__init__': self.load_template('CustomFrame__init__Template.txt'),
            'Frame__init__': self.load_template('Frame__init__Template.txt'),
            'MainGuiFrames': self.load_template('MainGuiFramesTemplate.txt'),
            'MainGuiShowFrame': self.load_template('MainGuiShowFrameTemplate.txt'),
            'Button': self.load_template('ButtonTemplate.txt'),
            'CheckButton': self.load_template('CheckButtonTemplate.txt'),
            'DropDown': self.load_template('DropDownTemplate.txt'),
            'InputField': self.load_template('InputFieldTemplate.txt'),
            'Label': self.load_template('LabelTemplate.txt'),
            'ListBox': self.load_template('ListBoxTemplate.txt'),
            'RadioButton': self.load_template('RadioButtonTemplate.txt'),
            'SpinBox': self.load_template('SpinBoxTemplate.txt')
        }

        self.frames = ['root']

    def setup(self, **kwargs):
        """
        This is used to build initial directories and __init__ files

        :param kwargs: The root keyword arguments used to build the tk.Tk window (A MyPyWindow)
        :return: None
        """
        self.build_base_modules()
        self.build_builder_helper()
        self.build_project_init()
        self.build_components_init()
        self.build_main()
        self.create_main_gui_template(**kwargs)

    def build_main(self):
        """
        Builds the __main__.py file for the project from the template.

        :return: None
        """
        f = open(os.path.join(self.final_destination, '__main__.py'), 'a')
        for line in self.templates['__main__']:
            f.write(self.map_replace(line, ['&NAME'], [self.name]))
        f.close()

    def build_components_init(self):
        """
        Builds the Components/__init__.py file from the template.

        :return: None
        """
        f = open(self.paths['Components__init__'], 'w')
        for line in self.templates['Components__init__']:
            f.write(self.map_replace(line, ['&NAME'], [self.name]))
        f.close()

    def build_project_init(self):
        """
        Builds the Project/__init__.py file from the template

        :return: None
        """
        f = open(self.paths['Project__init__'], 'w')
        for line in self.templates['Project__init__']:
            f.write(self.map_replace(line, ['&NAME'], [self.name]))
        f.close()

    def build_base_modules(self):
        """
        Builds required directories from self.modules

        :return: None
        """
        for path in self.modules:
            os.mkdir(path)

    def build_builder_helper(self):
        """
        Sets up imports for the BuilderHelper.py file

        :return: None
        """
        f = open(self.paths['Builder_Helper'], 'w')
        for line in self.templates['BuilderHelper']:
            if '&NAME' in line:
                line = line.replace('&NAME', self.name)
            f.write(line)
        f.close()

    def create_main_gui_template(self, **kwargs):
        """
        Creates the MainGuiTemplate.py file

        :param kwargs: Keyword arguments handed in from save method
        :return: None
        """
        f = open(self.paths['MainGuiTemplate'], 'w')
        for line in self.templates['Root']:
            f.write(self.map_replace(line,
                                     ['&CLASSNAME', '&TITLE', "'&ROWSPAN'",
                                      "'&COLUMNSPAN'", '&TYPE', '&ID'
                                      ],
                                     ['MainTemplate', kwargs['title'], str(kwargs['base_location']['rowspan']),
                                      str(kwargs['base_location']['columnspan']), kwargs['type'], kwargs['id']
                                      ]))
        f.close()

    def add_widget(self, **kwargs):
        """
        Generates each widget its own file in the correct directory, and adds imports to required __init__ files.

        :param kwargs: Key-word arguments for the widget
        :return: None
        """
        replacement_dict = {
            "&ID": kwargs['id'],
            "&MASTER": kwargs['master'],
            "'&ROW'": str(kwargs['location']['row']),
            "'&COLUMN'": str(kwargs['location']['column']),
            "'&ROWSPAN'": str(kwargs['location']['rowspan']),
            "'&COLUMNSPAN'": str(kwargs['location']['columnspan']),
            'NAME': kwargs['id']
        }

        kwargs['widget'] = self.lookup[kwargs['widget']]
        tmp_file = '{}_{}'.format(kwargs['widget'], kwargs['id'])
        tmp_class = '{}{}'.format(kwargs['widget'], kwargs['id'])
        if kwargs['master'] == 'root_window':
            self.mainwidgets_init_append(tmp_file, tmp_class)
            f = open(os.path.join(self.paths['MainWidgets'], '{}.py'.format(tmp_file)), 'a')
        else:
            tmp_folder = 'Frame_{}_Widgets'.format(kwargs['master'])
            self.customwidgets_init_append(tmp_folder, tmp_file, tmp_class)
            f = open(os.path.join(self.paths['Frames'], tmp_folder, '{}.py'.format(tmp_file)), 'a')
        for line in self.templates['Widget']:
            f.write(self.map_replace(line, ['&CLASSNAME'], [tmp_class]))
        for line in self.templates[kwargs['widget']]:
            for key in list(replacement_dict.keys()):
                if key in line:
                    line = line.replace(key, replacement_dict[key])
            f.write(line)
        f.close()
        self.builder_helper_add_widget(kwargs['master'], tmp_class)

    def builder_helper_add_widget(self, master, clss):
        """
        Adds a widget to the builder_helper which allows all widgets to be accessed in a hierarchical order

        :param master: Widget's master
        :param clss: Class name
        :return: None
        """
        if master == 'root_window':
            master = 'root'
        tmp_list = self.list_lines(self.paths['Builder_Helper'])
        f = open(self.paths['Builder_Helper'], 'w')
        for line in tmp_list:
            f.write(self.map_replace(line, ['&{}'.format(master)], ['{},\n                &{}'.format(clss, master)]))
        f.close()

    def mainwidgets_init_append(self, file, clss):
        """
        Adds imports to mainwidgets __init__
        :param file: Name of widget file
        :param clss: Widget class
        :return: None
        """
        f = open(os.path.join(self.paths['MainWidgets'], '__init__.py'), 'a')
        for line in self.templates['MainWidgets__init__']:
            f.write(self.map_replace(line, ['&NAME', '&FILE', '&CLASS'], [self.name, file, clss]))
        f.close()

    def customwidgets_init_append(self, folder, file, clss):
        """
        Adds imports to customframes __init__

        :param folder: The folder holding the frames widgets
        :param file: Name of widget file
        :param clss: Widget class
        :return: None
        """
        f = open(os.path.join(self.paths['Frames'], folder, '__init__.py'), 'a')
        for line in self.templates['CustomFrame__init__']:
            f.write(self.map_replace(line, ['&NAME', '&FOLDER', '&FILE', '&CLASS'], [self.name, folder, file, clss]))

    def add_frame(self, **kwargs):
        """
        Creates directories and files for new frames or toplevels.

        :param kwargs: Key-Word arguments for the frame/toplevel
        :return: None
        """
        tmp_folder = 'Frame_{}_Widgets'.format(kwargs['id'])
        tmp_file = 'Main_{}_Frame'.format(kwargs['id'])
        os.mkdir(os.path.join(self.paths['Frames'], tmp_folder))
        open(os.path.join(self.paths['Frames'], tmp_folder, '__init__.py'), 'a').close()
        f = open(os.path.join(self.paths['Frames'], '{}.py'.format(tmp_file)), 'a')
        if kwargs['type'] == 'toplevel':
            for line in self.templates['Root']:
                f.write(self.map_replace(
                    line,
                    ['&CLASSNAME',                              '&TITLE',
                     "&ID",                                     "&TYPE",
                     "'&ROWSPAN'",                              "'&COLUMNSPAN'"],
                    ['Main{}'.format(kwargs['id']),             kwargs['title'],
                     kwargs['id'],                              kwargs['type'],
                     str(kwargs['base_location']['rowspan']),   str(kwargs['base_location']['columnspan'])])
                )
        elif kwargs['type'] == 'frame':
            for line in self.templates['RootFrame']:
                f.write(self.map_replace(
                    line,
                    ['&CLASSNAME',                                  '&TYPE',
                     '&ID',                                         "'&ROW'",
                     "'&COLUMN'",                                   "'&RSPAN'",
                     "'&CSPAN'",                                    '&VERTICAL',
                     '&HORIZONTAL',                                 "'&SCROLLROW'",
                     "'&SCROLLCOLUMN'",                             "'&SCROLLRSPAN'",
                     "'&SCROLLCSPAN'"],
                    ['Main{}'.format(kwargs['id']),                 kwargs['type'],
                     kwargs['id'],                                  str(kwargs['base_location']['row']),
                     str(kwargs['base_location']['column']),        str(kwargs['base_location']['rowspan']),
                     str(kwargs['base_location']['columnspan']),    str(kwargs['scroll']['vertical']),
                     str(kwargs['scroll']['horizontal']),           str(kwargs['scroll_window_size']['row']),
                     str(kwargs['scroll_window_size']['column']),   str(kwargs['scroll_window_size']['rowspan']),
                     str(kwargs['scroll_window_size']['columnspan'])]
                )
                )

        f.close()
        self.frames.append(kwargs['id'])
        self.append_frame_init(tmp_file, tmp_folder)
        self.builder_helper_add_frame(kwargs['id'])
        self.main_gui_init_add_frame(kwargs['id'])

    def append_frame_init(self, file, folder):
        """
        Generates __init__ for the frames

        :param file: File to import from
        :param folder: Folder to import from
        :return: None
        """
        f = open(os.path.join(self.paths['Frames'], '__init__.py'), 'a')
        for line in self.templates['Frame__init__']:
            f.write(self.map_replace(line, ['&NAME', '&FILE', '&FOLDER'], [self.name, file, folder]))
        f.close()

    def builder_helper_add_frame(self, fid):
        """
        Adds frame information to the builder helper

        :param fid: Frame ID
        :return: None
        """
        tmp_list = self.list_lines(self.paths['Builder_Helper'])
        f = open(self.paths['Builder_Helper'], 'w')
        for line in tmp_list:
            if '  # &NEW' in line:
                line = line.replace('  # &NEW', ',\n')
                f.write(line)
                line = "            '{}': [\n".format(fid)
                f.write(line)
                line = '                &{}\n'.format(fid)
                f.write(line)
                line = '            ]  # &NEW\n'
            f.write(line)
        f.close()

    def main_gui_init_add_frame(self, fid):
        """
        Adds the show_frame to the maingui.
        IMPORTANT NOTE:
        The functions build the frames/toplevels, so they must be called in the .run() to make them appear immediately

        :param fid: Frame ID
        :return: None
        """
        f = open(self.paths['Project__init__'], 'a')
        for line in self.templates['ProjectFrame__init__']:
            f.write(self.map_replace(line, ['&NAME', '&ID'], [self.name, fid]))
        f.close()

    def finalize_builder_helper(self):
        """
        Finishes creating the Builder Helper

        :return: None
        """
        tmp_list = self.list_lines(self.paths['Builder_Helper'])
        f = open(self.paths['Builder_Helper'], 'w')
        i = 0
        for i, line in enumerate(tmp_list[:-1]):
            for frame in self.frames:
                if '&{}'.format(frame) in tmp_list[i + 1]:
                    line = line.replace(',', '')
                elif '&{}'.format(frame) in line:
                    line = ''
            f.write(line)
        else:
            if i != 0:
                f.write(tmp_list[i + 1])
        f.close()

    def finalize_main_gui(self):
        """
        This is used to finalize the main gui by adding in the custom frames info, and generating the
        show_frame functions.

        :return: None
        """
        f = open(self.paths['MainGui'], 'w')
        for line in self.templates['MultiBase']:
            line = self.map_replace(line, ['&NAME'], [self.name])
            if '# &FRAMES' in line:
                for frame in self.frames:
                    if frame is not 'root':
                        self.main_gui_frame(frame, f)
            elif '# &SHOWFRAME' in line:
                for frame in self.frames:
                    if frame is not 'root':
                        self.main_gui_show_frame(frame, f)
            f.write(line)
        f.close()

    def finalize(self):
        """
        Called by the save method to finish building the Static Project

        :return: None
        """
        self.finalize_builder_helper()
        self.finalize_main_gui()

    def main_gui_frame(self, frame, file):
        """
        Creates the self. args for the __init__ in the main gui for the given frames

        :param frame: Name of the frame
        :param file: The file to write to
        :return: None
        """
        for line in self.templates['MainGuiFrames']:
            file.write(self.map_replace(line, ['&FRAME'], [frame]))

    def main_gui_show_frame(self, frame, file):
        """
        Generates the show_frame methods for the main_gui

        :param frame: Name of frame
        :param file: MainGuiFile
        :return: None
        """
        for line in self.templates['MainGuiShowFrame']:
            file.write(self.map_replace(line, ['&FRAME'], [frame]))

    def load_template(self, template):
        """
        Loads in list of lines in given template name
        :param template: KeyName of template. Ex: templates[KeyName]
        :return: List of lines in the file
        """
        return self.list_lines(os.path.join(self.paths['Templates'], template))

    @staticmethod
    def list_lines(file):
        """
        Given a file, opens it and returns a list of it's lines

        :param file: File path
        :return: List of lines in file
        """
        f = open(file, 'r')
        tmp_list = f.readlines()
        f.close()
        return tmp_list

    @staticmethod
    def map_replace(line, old, new):
        """
        This is used to replace the old values in a line with the new values
        :param line: Line to search and replace
        :param old: list of the things to be replaced   Ex. ['&NAME', '&ID']
        :param new: list of the things to replace with. Ex. [a_name,   a_id]
        :return: line with new values
        """
        for i, item in enumerate(old):
            line = line.replace(item, new[i])
        return line
