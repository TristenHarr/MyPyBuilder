from GuiBuilder.BUILDER.ProjectTemplate.Tabs.NewTab.NewWidgetTemplate import NewWidget
from MyPyWidgets import *


class NewTab(object):

    def __init__(self, **kwargs):
        """
        This is the most important tab. This is used to add new widgets to the Gui.

        :param kwargs: Key-word arguments passed in by the main gui
        """
        self.window = kwargs['window']
        self.set_widget = kwargs['set_widget']
        self.widget_args = kwargs['widget_args']
        self.edit_widget = kwargs['edit_widget']
        self.set_location = kwargs['set_location']
        self.make_notebook_tab = kwargs['make_notebook_tab']
        self.is_int = kwargs['is_int']
        self.is_alnum = kwargs['is_alnum']
        self.variable_namify = kwargs['variable_namify']
        self.frame_grab = kwargs['frame_grab']
        self.popup_menu = kwargs['popup_menu']
        self.command_fetch = kwargs['command_fetch']
        self.share_command = kwargs['share_command']
        self.share_command('refresh_add_widget', self.new_mode)

        self.commands = {
            'builder_mode': self.new_tab,
            'new_mode': self.new_mode,
            'add_button': self.add_widget,
            'frame_drop': self.frame_grab()
        }

        # This allows the objects to be instantiated correctly
        self.args_lookup = {
            'Button': lambda x: [x, None],
            'DropDown': lambda x: [x, [], None],
            'InputField': lambda x: [x],
            'Label': lambda x: [x],
            'CheckButton': lambda x: [x, None],
            'SpinBox': lambda x: [x, [], None],
            'RadioButton': lambda x: [x, None, None]
        }

        self.widgets_lookup = {
            'Button': Button,
            'DropDown': DropDown,
            'InputField': InputField,
            'Label': Label,
            'CheckButton': CheckButton,
            'SpinBox': SpinBox,
            'RadioButton': RadioButton
        }

    def new_tab(self):
        """
        This is called in the main gui to create the new widget tab

        :return: None
        """
        tmp = NewWidget()
        self.make_notebook_tab(self,
                               tmp.window_kwargs,
                               tmp.components,
                               'control_panel',
                               'Create Widget')

    def new_mode(self, *args):
        """
        Called by the dropdown, selects which type of widget to create

        :param args: a list from the dropdown that holds the widget type
        :type args: list
        :return: None
        """
        del args
        widgets = NewWidget().new_components
        for item in widgets:
            tmp_args = []
            for arg in item['args']:
                if arg is None:
                    tmp_args.append(self.commands[item['id']])
                else:
                    tmp_args.append(arg)
            item['args'] = tmp_args
            self.window.containers['new_frame'].add_widget(**item)

    def add_widget(self, *args):
        """
        TODO: Get rid of *args, replace with lambda x: call()
        This adds the widget to the gui. It pulls in the data for creation from the Gui, validates it, and makes the
        widget

        :param args: Doesn't matter
        :return: None
        """
        del args
        choices = {'new_mode': lambda x: x,
                   'width_input': lambda x: self.is_int(x, 1),
                   'height_input': lambda x: self.is_int(x, 1),
                   'vertical_input': lambda x: self.is_int(x),
                   'horizontal_input': lambda x: self.is_int(x),
                   'id_input': lambda x: self.variable_namify(x),
                   'frame_drop': lambda x: x if x != 'Master Frame (Default: root_window)' else 'root_window'
                   }
        flag = True
        for key in list(choices.keys()):
            choices[key] = choices[key](self.window.containers['new_frame'].containers[key].get())
            if choices[key] is False:
                flag = False
        if choices['id_input'] in list(self.widget_args.keys()):
            flag = False
        if flag:
            args = {
                'master': choices['frame_drop'],
                'id': choices['id_input'],
                'widget': self.widgets_lookup[choices['new_mode']],
                'args': self.args_lookup[choices['new_mode']](choices['id_input']),
                'location': {
                    'row': choices['vertical_input'],
                    'column': choices['horizontal_input'],
                    'rowspan': choices['height_input'],
                    'columnspan': choices['width_input'],
                    'sticky': 'NSWE'
                }
            }

            if choices['frame_drop'] == 'root_window':
                self.window.add_widget(**args)
                self.widget_args[choices['id_input']] = args
                self.window.containers[choices['id_input']].widget.bind(
                    '<1>', lambda event, wid2=choices['id_input'], wind=self.window: self.set_widget(wid2, wind))
                self.window.containers[choices['id_input']].widget.bind('<Double-Button-1>',
                                                                        lambda event, wid2=choices['id_input']:
                                                                        self.edit_widget(wid2))
                self.window.containers[choices['id_input']].widget.bind('<Button-3>',
                                                                        lambda event, wid2=choices['id_input']:
                                                                        self.popup_menu.popup(event, wid2))
            else:
                self.window.containers[choices['frame_drop']].add_widget(**args)
                self.widget_args[choices['id_input']] = args
                window = self.window.containers[choices['frame_drop']]
                self.window.containers[
                    choices['frame_drop']
                ].containers[choices['id_input']].widget.bind(
                    '<1>', lambda event, wid2=choices['id_input'], wind=window: self.set_widget(wid2, wind))

                self.window.containers[choices['frame_drop']].containers[choices['id_input']].widget.bind(
                    '<Double-Button-1>',
                    lambda event, wid2=choices['id_input']:
                    self.edit_widget(wid2))

                self.window.containers[choices['frame_drop']].containers[choices['id_input']].widget.bind(
                    '<Button-3>',
                    lambda event, wid2=choices['id_input']:
                    self.popup_menu.popup(event, wid2))
            iter_id = int(self.window.containers['new_frame'].containers['iter_id'].get())
            if iter_id:
                tmp = str(args['id'])
                num = ''
                var = ''
                for item in tmp[::-1]:
                    if item.isdigit():
                        num += item
                    else:
                        var += item
                num = '0' if num == '' else num
                var = var[::-1] + str(int(num[::-1])+1)
                self.window.containers['new_frame'].containers['id_input'].set(var)
            iter_loc = int(self.window.containers['new_frame'].containers['iter_loc'].get())
            if iter_loc:
                tmp_horiz = args['location']['column'] + 10
                tmp_vert = args['location']['row'] + 10
                self.window.containers['new_frame'].containers['horizontal_input'].set(tmp_horiz)
                self.window.containers['new_frame'].containers['vertical_input'].set(tmp_vert)
        self.command_fetch()['refresh_edit']()
