from GuiBuilder.BUILDER.ProjectTemplate.Tabs.FrameTab.FrameWidgetTemplate import FrameWidget
import os
from GuiBuilder.BUILDER.ProjectTemplate.WidgetTemplates.SplitClassGenerator import MultiGenerator
import shutil
import pickle


class FrameTab(object):

    def __init__(self, **kwargs):
        """
        This class is in charge of building/deleting/editing frames and toplevels.

        :param kwargs: Keyword args passed in from the main gui
        """
        self.window = kwargs['window']
        self.set_widget = kwargs['set_widget']
        self.edit_widget = kwargs['edit_widget']
        self.make_notebook_tab = kwargs['make_notebook_tab']
        self.grab_kwargs = kwargs['grab_kwargs']
        self.set_widget = kwargs['set_widget']
        self.edit_widget = kwargs['edit_widget']
        self.widget_args = kwargs['widget_args']
        self.frame_grab = kwargs['frame_grab']
        self.frames = kwargs['frames']
        self.root_path = kwargs['root_path']
        self.popup_menu = kwargs['popup_menu']
        self.command_fetch = kwargs['command_fetch']
        self.share_command = kwargs['share_command']
        self.share_command('refresh_edit', self.refresh_edit_frames)
        self.src_path = kwargs['src_path']
        self.really = kwargs['really']
        self.current_type = None

        self.widget_ids = []
        self.to_make = []

        self.edit_widgets = []
        self.edit_id = None

        self.commands = {'type_dropdown': lambda choice: self.choose_frame(choice),
                         'add_frame': self.add_frame,
                         'add_toplevel': self.add_toplevel,
                         'master_dropdown': self.frame_grab(),
                         'save_project': self.save_project,
                         'vertical_checkbox': self.scroll_check,
                         'horizontal_checkbox': self.scroll_check,
                         'choose_frame': self.frame_grab(),
                         'refresh_edit': self.refresh_edit_frames,
                         'edit_toplevel': self.reconfig_toplevel,
                         'vertical_checkboxf': lambda: self.scroll_check('edit_frame_frame'),
                         'horizontal_checkboxf': lambda: self.scroll_check('edit_frame_frame'),
                         'edit_frame': self.reconfig_frame,
                         'delete_frame': self.delete_frame,
                         'delete_toplevel': self.delete_frame}

    def reconfig_frame(self):
        """
        Reconfigures the frame.
        This is done by re-adding the frame with the new arguments.
        All widgets that the frame contains are first grabbed so that the can be put back onto the frame when
        the frame has been rebuilt.

        :return: None
        """
        self.add_frame(frame='edit_frame_frame')
        for widget in self.edit_widgets:
            self.window.containers[self.edit_id].add_widget(**widget)
            self.widget_args[widget['id']] = widget
            window = self.window.containers[self.edit_id]
            self.window.containers[self.edit_id].containers[widget['id']].widget.bind(
                '<1>', lambda event, wid2=widget['id'], wind=window: self.set_widget(wid2, wind))
            self.window.containers[self.edit_id].containers[widget['id']].widget.bind(
                '<Double-Button-1>', lambda event, wid2=widget['id']: self.edit_widget(wid2))
            self.window.containers[self.edit_id].containers[widget['id']].widget.bind(
                '<Button-3>', lambda event, wid2=widget['id']: self.popup_menu.popup(event, wid2))

    def delete_frame(self, really=False):
        """
        This method deletes the selected frame.
        This method utilizes the static method 'really' that is owned by the main gui to popup a window asking
        if the user is sure they want to delete the frame.
        If a frame is deleted, so are all items that it owns.

        :param really: Method to verify user wishes to delete frame
        :return: None
        """
        self.really(self.window, self.delete_frame)
        if really:
            bye = self.window.containers['edit_frame_frame'].containers['frame_id_input'].get()
            widgets = list(filter(
                lambda x: x is not None, map(
                    lambda x: self.widget_args[x] if self.widget_args[x]['master'] == bye else None,
                    list(self.widget_args.keys()))))
            for widget in widgets:
                self.widget_args.pop(widget['id'])
                self.window.containers[bye].containers.pop(widget['id'])

            self.frames.pop(bye)
            garbage = self.window.containers.pop(bye)
            if garbage.kwargs['type'] == 'frame':
                garbage.destroy()
            elif garbage.kwargs['type'] == 'toplevel':
                garbage.leave()
            self.refresh_edit_frames()

    def reconfig_toplevel(self):
        """
        This method is used to edit a toplevel. This method allows a user to change the title, and the size of a
        toplevel. All widgets the toplevel owns are added back to the toplevel.

        :return: None
        """
        self.window.containers[self.edit_id].leave()
        self.add_toplevel(frame='edit_frame_frame')
        for widget in self.edit_widgets:
            self.window.containers[self.edit_id].add_widget(**widget)
            self.widget_args[widget['id']] = widget
            window = self.window.containers[self.edit_id]
            self.window.containers[self.edit_id].containers[widget['id']].widget.bind(
                '<1>', lambda event, wid2=widget['id'], wind=window: self.set_widget(wid2, wind))
            self.window.containers[self.edit_id].containers[widget['id']].widget.bind(
                '<Double-Button-1>', lambda event, wid2=widget['id']: self.edit_widget(wid2))
            self.window.containers[self.edit_id].containers[widget['id']].widget.bind(
                '<Button-3>', lambda event, wid2=widget['id']: self.popup_menu.popup(event, wid2))

    def choose_edit_frame(self, *args):
        """
        This method ties to the dropdown to select the frame to edit. Whenever a tab is selected, the frames current
        widgets are destroyed, and then the correct widgets for the selected frame are then added to the frame

        :param args: selected frame
        :type args: list
        :return: None
        """
        for key in list(self.window.containers['edit_frame_frame'].containers.keys()):
            if key is not 'choose_frame':
                garbage = self.window.containers['edit_frame_frame'].containers.pop(key)
                garbage.destroy()
                del garbage
        tmp = FrameWidget()
        self.edit_widgets = list(filter(
            lambda x: x is not None,
            map(lambda x: self.widget_args[x] if self.widget_args[x]['master'] == args[0] else None,
                list(self.widget_args.keys()))))
        if args[0] == 'root_window':
            for item in tmp.edit_root:
                tmp_args = []
                for arg in item['args']:
                    if arg is None:
                        tmp_args.append(self.commands[item['id']])
                    else:
                        tmp_args.append(arg)
                item['args'] = tmp_args
                self.window.containers['edit_frame_frame'].add_widget(**item)
        elif self.window.containers[args[0]].type == 'toplevel':
            tmp_kwarg = self.frames[args[0]].kwargs
            for item in tmp.edit_toplevel:
                tmp_args = []
                for arg in item['args']:
                    if arg is None:
                        tmp_args.append(self.commands[item['id']])
                    else:
                        tmp_args.append(arg)
                item['args'] = tmp_args
                self.window.containers['edit_frame_frame'].add_widget(**item)
            self.edit_id = tmp_kwarg['id']
            self.window.containers['edit_frame_frame'].containers['frame_id_input'].set(tmp_kwarg['id'])
            self.window.containers['edit_frame_frame'].containers['frame_id_input'].configure({'state': 'disabled'})
            self.window.containers['edit_frame_frame'].containers['height_input'].set(
                tmp_kwarg['base_location']['rowspan'])
            self.window.containers['edit_frame_frame'].containers['width_input'].set(
                tmp_kwarg['base_location']['columnspan'])
            self.window.containers['edit_frame_frame'].containers['title_input'].set(
                tmp_kwarg['title'])
        elif self.window.containers[args[0]].type == 'frame':
            tmp_kwarg = self.frames[args[0]].kwargs
            for item in tmp.edit_frame:
                tmp_args = []
                for arg in item['args']:
                    if arg is None:
                        tmp_args.append(self.commands[item['id']])
                    else:
                        tmp_args.append(arg)
                item['args'] = tmp_args
                self.window.containers['edit_frame_frame'].add_widget(**item)
            self.edit_id = tmp_kwarg['id']
            if tmp_kwarg['scroll']['vertical'] or tmp_kwarg['scroll']['horizontal']:
                if tmp_kwarg['scroll']['vertical']:
                    self.window.containers['edit_frame_frame'].containers['vertical_checkboxf'].invoke()
                    tmp_kwarg['scroll_window_size']['columnspan'] += 20
                if tmp_kwarg['scroll']['horizontal']:
                    self.window.containers['edit_frame_frame'].containers['horizontal_checkboxf'].invoke()
                    tmp_kwarg['scroll_window_size']['rowspan'] += 20
                self.window.containers['edit_frame_frame'].containers['frame_id_input'].set(tmp_kwarg['id'])
                self.window.containers['edit_frame_frame'].containers['height_input'].set(
                    tmp_kwarg['scroll_window_size']['rowspan'])
                self.window.containers['edit_frame_frame'].containers['width_input'].set(
                    tmp_kwarg['scroll_window_size']['columnspan'])
                self.window.containers['edit_frame_frame'].containers['verticalbase_input'].set(
                    tmp_kwarg['base_location']['row'])
                self.window.containers['edit_frame_frame'].containers['horizontalbase_input'].set(
                    tmp_kwarg['base_location']['column'])
                self.window.containers['edit_frame_frame'].containers['insetwidth_input'].set(
                    tmp_kwarg['base_location']['columnspan'])
                self.window.containers['edit_frame_frame'].containers['insetheight_input'].set(
                    tmp_kwarg['base_location']['rowspan'])
            else:
                self.window.containers['edit_frame_frame'].containers['frame_id_input'].set(tmp_kwarg['id'])
                self.window.containers['edit_frame_frame'].containers['height_input'].set(
                    tmp_kwarg['base_location']['rowspan'])
                self.window.containers['edit_frame_frame'].containers['width_input'].set(
                    tmp_kwarg['base_location']['columnspan'])
                self.window.containers['edit_frame_frame'].containers['verticalbase_input'].set(
                    tmp_kwarg['base_location']['row'])
                self.window.containers['edit_frame_frame'].containers['horizontalbase_input'].set(
                    tmp_kwarg['base_location']['column'])

    def refresh_edit_frames(self):
        """
        This is used to refresh the edit frame

        :return: None
        """
        tmp = FrameWidget()
        for key in list(self.window.containers['edit_frame_frame'].containers.keys()):
            garbage = self.window.containers['edit_frame_frame'].containers.pop(key)
            garbage.destroy()
            del garbage
        for item in tmp.edit_components:
            tmp_args = []
            for arg in item['args']:
                if arg is None:
                    tmp_args.append(self.commands[item['id']])
                elif arg == 'hotfix':  # TODO: Remove hotfix for something more stable
                    tmp_args.append(self.choose_edit_frame)
                else:
                    tmp_args.append(arg)
            item['args'] = tmp_args
            self.window.containers['edit_frame_frame'].add_widget(**item)

    def frame_tab(self):
        """
        This method is called by the main gui to intitialize the Frame manager tabs
        :return: None
        """
        tmp = FrameWidget()
        self.make_notebook_tab(self,
                               tmp.window_kwargs,
                               tmp.components,
                               'control_panel',
                               'Frame Manager')
        self.refresh_frames()
        self.refresh_edit_frames()

    def refresh_frames(self):
        """
        This method is used to create the edit frames

        :return: None
        """
        tmp = FrameWidget()
        self.make_notebook_tab(self,
                               tmp.new_kwargs,
                               tmp.new_components,
                               'frame_manager_frame',
                               'New Frame')

        self.make_notebook_tab(self,
                               tmp.edit_kwargs,
                               tmp.edit_components,
                               'frame_manager_frame',
                               'Edit Frames')
        self.make_notebook_tab(self,
                               tmp.save_kwargs,
                               tmp.save_components,
                               'frame_manager_frame',
                               'Save Project')

    def choose_frame(self, frame):
        """
        This is used in the new frame tab to select whether the user wishes to make a new toplevel or a new frame

        :param frame: type of frame
        :type frame: str
        :return: None
        """
        tmp = FrameWidget()
        for key in list(self.window.containers['make_frame_frame'].containers.keys()):
            if key is not 'type_dropdown':
                garbage = self.window.containers['make_frame_frame'].containers.pop(key)
                garbage.destroy()
                del garbage
        if frame == 'Toplevel':
            for item in tmp.new_toplevel_components:
                tmp_args = []
                for arg in item['args']:
                    if arg is None:
                        tmp_args.append(self.commands[item['id']])
                    else:
                        tmp_args.append(arg)
                item['args'] = tmp_args
                self.window.containers['make_frame_frame'].add_widget(**item)
        elif frame == 'Frame':
            for item in tmp.new_frame_components:
                tmp_args = []
                for arg in item['args']:
                    if arg is None:
                        tmp_args.append(self.commands[item['id']])
                    else:
                        tmp_args.append(arg)
                item['args'] = tmp_args
                self.window.containers['make_frame_frame'].add_widget(**item)

    # TODO: Allow frames to be added to other frames, and toplevels and vice-versa
    def add_frame(self, frame='make_frame_frame'):
        """
        TODO: Validation of data
        This is used to add a frame to the root window

        :param frame: frame to pull the inputs from
        :return: None
        """
        width = int(self.window.containers[frame].containers['width_input'].get())
        height = int(self.window.containers[frame].containers['height_input'].get())
        wid = self.window.containers[frame].containers['frame_id_input'].get()
        vert_base = int(self.window.containers[frame].containers['verticalbase_input'].get())
        horiz_base = int(self.window.containers[frame].containers['horizontalbase_input'].get())
        # TODO: tmp is currently just a HACK, used to quickly get it working, clean this up
        tmp = ''
        if frame == 'edit_frame_frame':
            tmp = 'f'
        vert = int(self.window.containers[frame].containers['vertical_checkbox' + tmp].get())
        horiz = int(self.window.containers[frame].containers['horizontal_checkbox' + tmp].get())
        inset_width = 0
        inset_height = 0
        if vert or horiz:
            inset_width = int(self.window.containers[frame].containers['insetwidth_input'].get())
            inset_height = int(self.window.containers[frame].containers['insetheight_input'].get())
        kwargs = {
            'type': 'frame',
            'id': wid,
            'base_location': {
                'row': 0 if (vert or horiz) else vert_base,
                'column': 0 if (vert or horiz) else horiz_base,
                'rowspan': inset_height if (vert or horiz) else height,
                'columnspan': inset_width if (vert or horiz) else width,
                'sticky': 'NSWE'
            },
            'scroll': {
                'vertical': True if vert else False,
                'horizontal': True if horiz else False
            },
            'scroll_window_size': {
                'row': vert_base,
                'column': horiz_base,
                'columnspan': width,
                'rowspan': height,
                'sticky': 'NSWE'
            }
        }
        self.window.add_frame(**kwargs)
        self.frames[wid] = self.window.containers[wid]
        self.refresh_edit_frames()
        self.command_fetch()['refresh_add_widget']()

    def add_toplevel(self, frame='make_frame_frame'):
        """
        This is used to add a toplevel to the root window

        :param frame: frame to pull the input data from
        :return: None
        """
        width = int(self.window.containers[frame].containers['width_input'].get())
        height = int(self.window.containers[frame].containers['height_input'].get())
        title = self.window.containers[frame].containers['title_input'].get()
        wid = self.window.containers[frame].containers['frame_id_input'].get()
        kwargs = {'type': 'toplevel',
                  'title': title,
                  'id': wid,
                  'base_location': {
                      'row': 0,
                      'column': 0,
                      'rowspan': height,
                      'columnspan': width,
                      'sticky': 'NSWE'
                  },
                  'row_offset': 0,
                  'column_offset': 0
                  }
        self.window.add_toplevel(**kwargs)
        self.window.containers[wid].app.protocol('WM_DELETE_WINDOW', self.leave_stop)
        self.frames[wid] = self.window.containers[wid]
        self.refresh_edit_frames()
        self.command_fetch()['refresh_add_widget']()

    def scroll_check(self, frame='make_frame_frame'):
        """
        This method is called whenever a scroll-box is checked to create scrollable frames.
        This is used to determine if the inset_width and inset_height are neccesary, and if so to create the input
        boxes for them

        :param frame: frame to pull the input data from
        :return: None
        """
        tmp = FrameWidget()
        tmp_list = []
        for item in list(tmp.scroll_kwargs):
            if item['id'] in list(self.window.containers[frame].containers.keys()):
                tmp_list.append(self.window.containers[frame].containers.pop(item['id']))
        for item in tmp_list:
            item.destroy()
            del item
        tmp1 = ''
        if frame == 'edit_frame_frame':
            tmp1 = 'f'
        vert = int(self.window.containers[frame].containers['vertical_checkbox' + tmp1].get())
        horiz = int(self.window.containers[frame].containers['horizontal_checkbox' + tmp1].get())
        if vert or horiz:
            for item in tmp.scroll_kwargs:
                tmp_args = []
                for arg in item['args']:
                    if arg is None:
                        tmp_args.append(self.commands[item['id']])
                    else:
                        tmp_args.append(arg)
                item['args'] = tmp_args
                self.window.containers[frame].add_widget(**item)

    def save_project(self):
        """
        WARNING: DANGEROUS!

        IMPORTANT METHOD!!! DO NOT CHANGE UNLESS YOU KNOW WHAT YOU ARE DOING!


        This method is used to save the project. This is done by deleting anything currently in the project and
        then using the MultiBase.Generator class to generate the static pages.
        All data required to rebuild the Gui is also pickled and stored in the PROJECTBUILDER/project folder

        :return: None
        """
        shutil.rmtree(self.root_path)
        os.mkdir(self.root_path)
        shutil.rmtree(os.path.join(self.src_path, 'Loader'), True)
        open(os.path.join(self.root_path, '__init__.py'), 'a').close()
        builder_dict = {key: [] for key in list(self.frames.keys())}
        for key in self.widget_args.keys():
            builder_dict[self.widget_args[key]['master']].append(self.widget_args[key])
        make = MultiGenerator(os.getcwd(), self.root_path)
        make.setup(**self.window.kwargs)
        for widget in builder_dict['root_window']:
            make.add_widget(**widget)
        for key in list(builder_dict.keys()):
            if key != 'root_window':
                make.add_frame(**self.frames[key].kwargs)
                for widget in builder_dict[key]:
                    make.add_widget(**widget)
        os.mkdir(os.path.join(self.src_path, 'Loader'))

        f = open(os.path.join(self.src_path, 'Loader', 'builder_dict.p'), 'wb')
        pickle.dump(builder_dict, f)
        f.close()

        f = open(os.path.join(self.src_path, 'Loader', 'widget_args.p'), 'wb')
        pickle.dump(self.widget_args, f)
        f.close()

        frames = dict()
        for key in list(self.frames.keys()):
            if key is not 'root_window':
                frames[key] = self.copier(self.frames[key].kwargs)

        f = open(os.path.join(self.src_path, 'Loader', 'frames.p'), 'wb')
        pickle.dump(frames, f)
        f.close()

        make.finalize()

    def leave_stop(self):
        """
        TODO: get rid of this, replace with lambda: None
        :return: None
        """
        pass

    @staticmethod
    def copier(to_copy):
        """
        WARNING: DO NOT CHANGE UNLESS YOU UNDERSTAND WHY THIS IS DONE THIS WAY.
        copy() doesn't work because it creates a shallow copy, deepcopy can't be called because it uses pickle


        TODO: Wouldn't it be nice.. frozen = pickle.freeze(some_tkinter_thing), pickle.dump(frozen) LOWEST PRIORITY EVER
        This method is used to copy the frame kwargs but strip out all tkinter objects that cannot be pickled.

        :param to_copy: dictionary to copy
        :type to_copy: dict
        :return: dict that is cleaned up
        """
        tmp_dict = dict()
        for key in list(to_copy.keys()):
            if key not in ['owner', 'master']:
                tmp_dict[key] = to_copy[key]
        return tmp_dict
