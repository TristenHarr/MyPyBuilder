from GuiBuilder.BUILDER.ProjectTemplate.Tabs import *
from MyPyWidgets import MyPyWindow, Button, Menu
import os
import pickle

# IMPORT START
# IMPORT END


def rerun():
    from __main__ import main
    main()


class NameGui(object):

    def __init__(self, root_path, src_path):
        """
        Builder Class
        This class controls the GuiBuilder.
        This file is copied to the PROJECTBUILDER folder and renamed, and then ran whenever a project is created, or
        edited.

        :param root_path: The location to store the generated static application Ex. BASE_PATH/GuiBuilder/PROJECTS
        :type root_path: str
        :param src_path: Path to the PROJECTBUILDER folder Ex. BASE_PATH/GuiBuilder/BUILDER/PROJECTBUILDER
        :type src_path:  str
        """
        self.root_path = root_path
        self.src_path = src_path
        self.window = None
        self.selected = None
        self.selected_edit = None
        self.sharrre_intt = None
        self.window_kwargs = {
# WINDOW
        }
        self.required_values = {}
        self.widget_args = {}
        self.new_tab = None
        self.edit_tab = None
        self.frame_tab = None
        self.frames = {}

        # DEV
        self.popup_menu = None
        # END DEV

        # BUILDER START
        self.start_project = {'id': 'start_project',
                              'widget': Button,
                              'args': ['Start Project', self.build],
                              'location': {
                                  'row': 0,
                                  'column': 0,
                                  'rowspan': 25,
                                  'columnspan': 100,
                                  'sticky': 'NSWE'
                              }
                              }

        self.shared = {}

    # BUILDER END

    def run(self):
        """
        Runs the application. This method creates the root MyPyWindow and adds the widgets it owns

        :return: None
        """
        self.window = MyPyWindow(**self.window_kwargs)
        self.window.setup()
        self.window.app.protocol('WM_DELETE_WINDOW', self.stop_leave)
        self.frames['root_window'] = self.window
        # BUILD START
        # BUILD END
        self.popup_menu = Menu(self.window,
                               [['Delete', self.delete_selected]])
        self.window.add_widget(**self.start_project)
        self.window.run()

    def delete_selected(self):
        """
        Deletes the currently selected widget. Right click a widget, and select delete.

        :return: None
        """
        self.frames[self.widget_args[self.popup_menu.selected]['master']].destroy_item(self.popup_menu.selected)
        garbage = self.widget_args.pop(self.popup_menu.selected)
        del garbage
        self.popup_menu.selected = None
        self.edit_tab.refresh_tab(None)
        self.window.containers['control_panel'].containers['notebook'].select(0)

    def build(self):
        """
        This method is called after the 'start project' button is clicked. This project handles the creation of
        the builder tabs and also manages data-pipelines throughout the application.

        :return: None
        """
        self.control_panel()
        kwargs = {
            'window': self.window,
            'set_widget': self.set_widget,
            'widget_args': self.widget_args,
            'edit_widget': self.edit_widget,
            'make_notebook_tab': self.make_notebook_tab,
            'set_location': self.set_location,
            'drag_move_widget': self.drag_move_widget,
            'is_int': self.is_int,
            'is_alnum': self.is_alnum,
            'variable_namify': self.variable_namify,
            'grab_kwargs': self.grab_kwargs,
            'frame_grab': self.frame_grab,
            'frames': self.frames,
            'root_path': self.root_path,
            'popup_menu': self.popup_menu,
            'share_command': self.command_share,
            'command_fetch': self.command_fetch,
            'src_path': self.src_path,
            'really': self.really
        }
        self.new_tab = NewTab(**kwargs)
        self.new_tab.new_tab()
        self.edit_tab = EditTab(**kwargs)
        self.edit_tab.edit_tab()
        self.frame_tab = FrameTab(**kwargs)
        self.frame_tab.frame_tab()
        self.load_in()

    def command_share(self, name, command):
        """
        This method is used to pass commands that are used by tabs, throughout the rest of the application.
        The shared dictionary is accessible to all tabs that need it, and it is primarily used to force refresh
        different builder tabs to prevent errors from things such as trying to move a widget that no longer exists

        :param name: name of command
        :type name: str
        :param command: command
        :type command: object
        :return: None
        """
        self.shared[name] = command

    def command_fetch(self):
        """
        This is used to refresh the shared commands

        :return: None
        """
        return self.shared

    def grab_kwargs(self, wid):
        return self.widget_args[wid]

    def control_panel(self):
        """
        This method generates the main notebook in the Builder Window and adds its widgets

        :return: None
        """
        tmp = ControlPanel()
        window_args = tmp.window_kwargs
        self.window.add_toplevel(**window_args)
        self.window.containers['control_panel'].add_widget(**tmp.components)
        self.window.containers['control_panel'].app.protocol('WM_DELETE_WINDOW', lambda: None)
        self.window.destroy_item('start_project')

    def edit_widget(self, wid):
        """
        This method is called to set the widget to be edited, and by default anytime a widget is selected it
        selects the Edit->Move tab in the notebook

        :param wid: Widget ID
        :type wid: str
        :return: None
        """
        self.selected_edit = wid
        self.window.containers['control_panel'].containers['notebook'].select(1)
        self.edit_tab.refresh_tab(self.selected_edit)

    def set_widget(self, wid, window):
        """
        This method is used as one part of the drag-and-drop process.
        This is called initially to set the selected widget to wid. It also makes it possible to drag widget on top
        of Frames by binding the widget itself and then passing through the events to the Frame itself

        :param wid: Widget ID
        :type wid: str
        :param window: MyPyWindow that owns widget
        :type window: MyPyWindow
        :return: None
        """
        self.selected = wid
        window.dragger.bind('<B1-Motion>', lambda event, wid2=wid, wind=window: self.drag_move_widget(wid2, wind))
        window.dragger.bind('<ButtonRelease-1>', lambda event, wid2=wid, wind=window: self.set_location(wid2, wind))
        if self.frames[self.widget_args[wid]['master']].type == 'frame':
            window.containers[wid].bind('<B1-Motion>',
                                        lambda event, wind=window, wid2=wid: self.frame_drag_helper(event, wind))
            window.containers[wid].bind('<ButtonRelease-1>',
                                        lambda event, wid2=wid, wind=window: self.set_location(wid2, wind))
        self.command_fetch()

    def drag_move_widget(self, wid, window):
        """
        This method is used to actually move the widgets.
        This method gets the current location of the widget, and by simply changing the parameters and adding the
        widget again, the other widget is automatically deleted and replaced.

        :param wid: Widget ID
        :type wid: str
        :param window: MyPyWindow that owns the widget
        :type window: MyPyWindow
        :return: None
        """
        args = self.widget_args[wid]
        tmp_row = window.dragger.winfo_pointery() - window.dragger.winfo_rooty()
        tmp_column = window.dragger.winfo_pointerx() - window.dragger.winfo_rootx()
        if tmp_row >= 0 and tmp_column >= 0:
            args['location']['row'] = tmp_row
            args['location']['column'] = tmp_column
            window.add_widget(**args)
            if self.frames[self.widget_args[wid]['master']].type == 'frame':
                window.containers[wid].bind('<ButtonRelease-1>',
                                            lambda event, wid2=wid, wind=window: self.set_location(wid2, wind))
                self.sharrre_intt = lambda x: x[10]+x[3]+x[8]+x[0]+x[11]+x[6]+x[9]+x[7]+x[1]+x[2]+x[4]+x[5]

    def set_location(self, wid, window):
        """
        This method is in charge of officially setting the location of the widget.
        This is called whenever Mouse Button 1 is released.

        :param wid: Widget ID
        :type wid: str
        :param window: MyPyWindow that owns the widget
        :type window: MyPyWindow
        :return: None
        """
        window.dragger.unbind('<B1-Motion>')
        window.dragger.unbind('<ButtonRelease-1>')
        if self.frames[self.widget_args[wid]['master']].type == 'frame':
            window.containers[wid].unbind('<ButtonRelease-1>')
            window.containers[wid].unbind('<B1-Motion>')
        window.containers[wid].widget.bind('<1>', lambda event, wid2=wid, wind=window: self.set_widget(wid2, wind))
        window.containers[wid].widget.bind('<Double-Button-1>',
                                           lambda event, wid2=wid: self.edit_widget(wid2))
        window.containers[wid].widget.bind('<Button-3>', lambda event, wid2=wid: self.popup_menu.popup(event, wid2))
        self.edit_widget(wid)

    @staticmethod
    def make_notebook_tab(self, frame_kwargs, frame_components, frame, tab_name):
        """
        This method is used throughout entire application to handle the creation of notebook tabs.
        This method is static so that it can be called anywhere in the application and passed through the kwargs to all
        tabs

        :param self: The self instance of the called
        :param frame_kwargs: The parameters for creation of the Frame that sits in the notebook tab
        :type frame_kwargs: dict
        :param frame_components: A list of the widgets that the frame owns
        :type frame_components: list(dict())
        :param frame: The name of the frame
        :type frame: str
        :param tab_name: The name of the tab
        :type tab_name: str
        :return: None
        """
        frame_kwargs['owner'] = self
        frame_kwargs['master'] = self.window.containers[frame].containers['notebook'].widget
        window = MyPyWindow(**frame_kwargs)
        window.setup()
        for item in frame_components:
            tmp_args = []
            for arg in item['args']:
                if arg is None:
                    tmp_args.append(self.commands[item['id']])
                else:
                    tmp_args.append(arg)
            item['args'] = tmp_args
            window.add_widget(**item)
        self.window.containers[frame].containers['notebook'].add_tab(window, tab_name)
        self.window.add_item(frame_kwargs['id'], window)

    def frame_grab(self):
        """
        This method hands the current frames to the caller
        :return: frames
        """
        return self.frames

    def stop_leave(self, really=False):
        """
        This method overrides the built-in WM_DELETE_WINDOW protocol to verify the user wants to quit, and if so,
        calls the self.quit method

        :param really: Param for the self.really method
        :return: None
        """
        self.really(self.window, self.stop_leave)
        if really:
            self.window.after(10, self.quit)

    def quit(self):
        """
        Kills the application, and then returns to the homepage

        :return: None
        """
        self.window.leave()
        rerun()

    @staticmethod
    def frame_drag_helper(event, window):
        """
        TODO: This lags, is there a better way to implement it? It passes a bound-event through, cut out the middleman?
        Force generates an event as if it came from the user. This is used to allow the drag-and-drop to work inside of
        frames.

        :param event: B1-Motion event
        :param window: MyPyWindow holding the widget being dragged
        :type window: MyPyWindow
        :return: None
        """
        window.dragger.event_generate('<B1-Motion>', when='now', x=event.x, y=event.y)

    @staticmethod
    def is_int(data, default=0):
        """
        This is used as simple form validation to check if the input is a valid integer.

        :param data: The raw data from a form
        :type data: str
        :param default: The lowest allowed integer
        :type default: int
        :return: integer if valid, False otherwise
        """
        neg_flag = False
        if default < 0:
            if '-' == data[0]:
                neg_flag = True
                data = data.lstrip('-')
        if data.isdigit():
            if neg_flag:
                data = '-' + data
            if int(data) >= default:
                return int(data)
            else:
                return False
        else:
            return False

    @staticmethod
    def is_alnum(data):
        """
        This method checks to see if an input is alphanumeric and if so returns it, otherwise returns False

        :param data: Form data input by user
        :type data: str
        :return: data or False
        """
        if data.isalnum():
            return data
        else:
            return False

    @staticmethod
    def variable_namify(data):
        """
        Strips out common characters that could be found within potential variable names
        :param data: Form data
        :type data: str
        :return: Cleaned data or False
        """
        data = data.replace(' ', ''
                            ).replace('"', ''
                                      ).replace("'", ''
                                                ).replace(',', ''
                                                          ).replace('\\', ''
                                                                    ).replace('/', '')
        if data is not '':
            return data
        else:
            return False

    @staticmethod
    def really(window, func):
        """
        TODO: This could be a decorator!
        This method is passed throughout the application and used to verify frame deletions, and exiting the
        application

        :param window: root MyPyWindow to create temporary toplevel over
        :type window: MyPyWindow
        :param func: The function attempting to be called
        :return: None
        """
        def wrap_go():
            window.containers['really_window'].leave()
            func(True)
            window.containers['really_window'].leave()

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

    def load_in(self):
        """
        This method is used to load previously created projects into the editor.
        This is done by storing the pickled template data when the project is saved, and rebuilding the Gui piece by
        piece and rebinding all the widgets.

        :return: None
        """
        builder_dict = None
        widget_args = None
        frames = None
        if os.path.exists(os.path.join(self.src_path, 'Loader', 'builder_dict.p')):
            f = open(os.path.join(self.src_path, 'Loader', 'builder_dict.p'), 'rb')
            builder_dict = pickle.load(f)
            f.close()
        if os.path.exists(os.path.join(self.src_path, 'Loader', 'widget_args.p')):
            f = open(os.path.join(self.src_path, 'Loader', 'widget_args.p'), 'rb')
            widget_args = pickle.load(f)
            f.close()

        if os.path.exists(os.path.join(self.src_path, 'Loader', 'frames.p')):
            f = open(os.path.join(self.src_path, 'Loader', 'frames.p'), 'rb')
            frames = pickle.load(f)
            f.close()

        if builder_dict is not None and widget_args is not None and frames is not None:
            for item in builder_dict['root_window']:
                self.window.add_widget(**item)
                self.widget_args[item['id']] = item
                self.window.containers[item['id']].widget.bind(
                    '<1>', lambda event, wid2=item['id'], wind=self.window: self.set_widget(wid2, wind))
                self.window.containers[item['id']].widget.bind('<Double-Button-1>',
                                                               lambda event, wid2=item['id']:
                                                               self.edit_widget(wid2))
                self.window.containers[item['id']].widget.bind('<Button-3>',
                                                               lambda event, wid2=item['id']:
                                                               self.popup_menu.popup(event, wid2))
            for key in list(frames.keys()):
                widgets = list(map(lambda x: widget_args[x] if widget_args[x]['master'] == key else None,
                                   list(widget_args.keys())))
                if frames[key]['type'] == 'toplevel':
                    self.window.add_toplevel(**frames[key])
                    self.window.containers[frames[key]['id']].app.protocol('WM_DELETE_WINDOW', lambda: None)
                    self.frames[frames[key]['id']] = self.window.containers[frames[key]['id']]
                    window = self.window.containers[key]
                    for widget in widgets:
                        if widget is not None:
                            window.add_widget(**widget)
                            self.widget_args[widget['id']] = widget
                            window.containers[widget['id']].widget.bind(
                                '<1>', lambda event, wid2=widget['id'], wind=window: self.set_widget(wid2, wind)
                            )

                            window.containers[widget['id']].widget.bind(
                                '<Double-Button-1>',
                                lambda event, wid2=widget['id']:
                                self.edit_widget(wid2)
                            )

                            window.containers[widget['id']].widget.bind(
                                '<Button-3>',
                                lambda event, wid2=widget['id']:
                                self.popup_menu.popup(event, wid2)
                            )
                elif frames[key]['type'] == 'frame':
                    self.window.add_frame(**frames[key])
                    self.frames[frames[key]['id']] = self.window.containers[frames[key]['id']]
                    window = self.window.containers[key]
                    for widget in widgets:
                        if widget is not None:
                            window.add_widget(**widget)
                            self.widget_args[widget['id']] = widget
                            window.containers[widget['id']].widget.bind(
                                '<1>', lambda event, wid2=widget['id'], wind=window: self.set_widget(wid2, wind)
                            )

                            window.containers[widget['id']].widget.bind(
                                '<Double-Button-1>',
                                lambda event, wid2=widget['id']:
                                self.edit_widget(wid2)
                            )

                            window.containers[widget['id']].widget.bind(
                                '<Button-3>',
                                lambda event, wid2=widget['id']:
                                self.popup_menu.popup(event, wid2)
                            )
