from GuiBuilder.BUILDER.ProjectTemplate.Tabs.EditTab.EditWidgetTemplate import EditWidget


class EditTab(object):

    def __init__(self, **kwargs):
        """
        This class controls the Edit Tab for widgets

        :param kwargs: All keyword args passed in by the MainGui
        """
        self.window = kwargs['window']
        self.set_widget = kwargs['set_widget']
        self.edit_widget = kwargs['edit_widget']
        self.make_notebook_tab = kwargs['make_notebook_tab']
        self.grab_kwargs = kwargs['grab_kwargs']
        self.set_widget = kwargs['set_widget']
        self.edit_widget = kwargs['edit_widget']
        self.widget_args = kwargs['widget_args']
        self.popup_menu = kwargs['popup_menu']
        self.command_fetch = kwargs['command_fetch']
        self.is_int = kwargs['is_int']

        self.tmp_args = None
        self.commands = {
            'selected_widget': None,
            'nw_move': lambda: self.bump_move('nw'),
            'n_move': lambda: self.bump_move('n'),
            'ne_move': lambda: self.bump_move('ne'),
            'w_move': lambda: self.bump_move('w'),
            'c_move': lambda: self.bump_move('c'),
            'e_move': lambda: self.bump_move('e'),
            'sw_move': lambda: self.bump_move('sw'),
            's_move': lambda: self.bump_move('s'),
            'se_move': lambda: self.bump_move('se'),
            'windoww_input': self.windoww_input(),
            'windowh_input': self.windowh_input(),
            'X_input': None,
            'Y_input': None,
            'move_submit': self.move_submit,

            'nw_stretch': lambda: self.bump_stretch('nw'),
            'n_stretch': lambda: self.bump_stretch('n'),
            'ne_stretch': lambda: self.bump_stretch('ne'),
            'w_stretch': lambda: self.bump_stretch('w'),
            'c_stretch': lambda: self.bump_stretch('c'),
            'e_stretch': lambda: self.bump_stretch('e'),
            'sw_stretch': lambda: self.bump_stretch('sw'),
            's_stretch': lambda: self.bump_stretch('s'),
            'se_stretch': lambda: self.bump_stretch('se'),
            'XS_input': None,
            'YS_input': None,
            'resize_submit': self.resize_submit
        }

        self.selected_args = None

    def edit_tab(self):
        """
        This method creates the initial edit tab by calling the make_notebook_tab and handing in it's arguments

        :return: None
        """
        tmp = EditWidget()
        self.make_notebook_tab(self,
                               tmp.control_panel_kwargs,
                               tmp.control_panel_components,
                               'control_panel',
                               'Edit Widget')

    def refresh_tab(self, selected):
        """
        This method refreshes the edit tab after something has been changed

        :param selected: The currently selected widget to display information for
        :return: None
        """
        if selected is None:
            for key in list(self.window.containers['edit_frame'].containers.keys()):
                garbage = self.window.containers['edit_frame'].containers.pop(key)
                garbage.destroy()
                del garbage
        else:
            self.commands['selected_widget'] = selected
            self.commands['X_input'] = self.x_input()
            self.commands['Y_input'] = self.y_input()
            self.commands['XS_input'] = self.xs_input()
            self.commands['YS_input'] = self.ys_input()
            for key in list(self.window.containers['edit_frame'].containers.keys()):
                garbage = self.window.containers['edit_frame'].containers.pop(key)
                garbage.destroy()
                del garbage

            tmp = EditWidget()
            widgets = tmp.control_panel_components
            for item in widgets:
                tmp_args = []
                for arg in item['args']:
                    if arg is None:
                        tmp_args.append(self.commands[item['id']])
                    else:
                        tmp_args.append(arg)
                item['args'] = tmp_args
                self.window.containers['edit_frame'].add_widget(**item)

            self.make_notebook_tab(self,
                                   tmp.move_frame_kwargs,
                                   tmp.move_frame_components,
                                   'edit_frame',
                                   'Move Widget')

            self.make_notebook_tab(self,
                                   tmp.resize_frame_kwargs,
                                   tmp.resize_frame_components,
                                   'edit_frame',
                                   'Resize Widget')

    def bump_move(self, direction):
        """
        This method bumps the widget in whichever direction the user chooses.

        :param direction: Direction to bump
        :type direction: str
        :return: None
        """
        self.tmp_args = self.grab_kwargs(self.commands['selected_widget'])
        window = self.tmp_args['master']
        if window == 'root_window':
            window = self.window
        else:
            window = self.window.containers[window]
        directions = list(direction)
        max_column = window.base_location['columnspan'] - self.tmp_args['location']['columnspan']
        max_row = window.base_location['rowspan'] - self.tmp_args['location']['rowspan']
        current_row = self.tmp_args['location']['row']
        current_column = self.tmp_args['location']['column']
        increment = self.is_int(self.window.containers['edit_move_frame'].containers['increment'].get())
        if increment is not False:
            for item in directions:
                if item == 'c':
                    self.tmp_args['location']['row'] = max_row // 2
                    self.tmp_args['location']['column'] = max_column // 2
                elif item == 'n':
                    if current_row - increment >= 0:
                        self.tmp_args['location']['row'] = current_row - increment
                    else:
                        self.tmp_args['location']['row'] = 0
                elif item == 'e':
                    if current_column + increment <= max_column:
                        self.tmp_args['location']['column'] = current_column + increment
                    else:
                        self.tmp_args['location']['column'] = max_column
                elif item == 's':
                    if current_row + increment <= max_row:
                        self.tmp_args['location']['row'] = current_row + increment
                    else:
                        self.tmp_args['location']['row'] = max_row
                elif item == 'w':
                    if current_column - increment >= 0:
                        self.tmp_args['location']['column'] = current_column - increment
                    else:
                        self.tmp_args['location']['column'] = 0
                window.add_widget(**self.tmp_args)
                self.widget_args[self.commands['selected_widget']] = self.tmp_args
                window.containers[self.commands['selected_widget']].widget.bind(
                    'Double-Button-1', lambda event, wid2=self.commands['selected_widget']: self.edit_widget(wid2))
                window.containers[self.commands['selected_widget']].widget.bind(
                    '<1>',
                    lambda event, wid2=self.commands['selected_widget'], wind=window: self.set_widget(wid2, wind))
                window.containers[self.commands['selected_widget']].widget.bind(
                    '<Button-3>',
                    lambda event, wid2=self.commands['selected_widget']: self.popup_menu.popup(event, wid2))
                self.window.containers['edit_move_frame'].containers['Y_input'].set(self.y_input())
                self.window.containers['edit_move_frame'].containers['X_input'].set(self.x_input())
            self.command_fetch()['refresh_edit']()

    def bump_stretch(self, direction):
        """
        This method stretches the widget in whichever direction the user selects.
        IMPORTANT NOTE: Negative stretching IS allowed.

        :param direction: The direction to stretch
        :type direction: str
        :return: None
        """
        self.tmp_args = self.grab_kwargs(self.commands['selected_widget'])
        window = self.tmp_args['master']
        if window == 'root_window':
            window = self.window
        else:
            window = self.window.containers[window]
        directions = list(direction)
        max_column = window.base_location['columnspan']
        current_column = self.tmp_args['location']['column']
        current_columnspan = self.tmp_args['location']['columnspan']
        max_row = window.base_location['rowspan']
        current_row = self.tmp_args['location']['row']
        current_rowspan = self.tmp_args['location']['rowspan']
        increment = self.is_int(self.window.containers['edit_resize_frame'].containers['increment'].get(), -400)
        if increment is not False:
            for item in directions:
                if item == 'c':
                    self.tmp_args['location']['columnspan'] = 1
                    self.tmp_args['location']['rowspan'] = 1
                elif item == 'n':
                    if current_row - increment >= 0 and current_rowspan + increment > 0:
                        self.tmp_args['location']['row'] -= increment
                        self.tmp_args['location']['rowspan'] = current_rowspan + increment
                    else:
                        if current_rowspan + increment <= 0:
                            self.tmp_args['location']['rowspan'] = 1
                        else:
                            self.tmp_args['location']['row'] = 0
                            self.tmp_args['location']['rowspan'] = current_rowspan + current_row
                elif item == 'e':
                    if (current_column + increment + current_columnspan) <= max_column and \
                            (current_columnspan + increment) > 0:
                        self.tmp_args['location']['columnspan'] = current_columnspan + increment
                    else:
                        if current_columnspan + increment <= 0:
                            self.tmp_args['location']['columnspan'] = 1
                        else:
                            self.tmp_args['location']['columnspan'] = max_column - current_column
                elif item == 's':
                    if current_row + increment + current_rowspan <= max_row and current_rowspan + increment > 0:
                        self.tmp_args['location']['rowspan'] = current_rowspan + increment
                    else:
                        if current_rowspan + increment <= 0:
                            self.tmp_args['location']['rowspan'] = 1
                        else:
                            self.tmp_args['location']['rowspan'] = max_row - current_row
                elif item == 'w':
                    if current_column - increment >= 0 and current_columnspan + increment > 0:
                        self.tmp_args['location']['column'] -= increment
                        self.tmp_args['location']['columnspan'] = current_columnspan + increment
                    else:
                        if current_columnspan + increment <= 0:
                            self.tmp_args['location']['columnspan'] = 1
                        else:
                            self.tmp_args['location']['column'] = 0
                            self.tmp_args['location']['columnspan'] = current_columnspan + current_column
            window.add_widget(**self.tmp_args)
            self.widget_args[self.commands['selected_widget']] = self.tmp_args
            window.containers[self.commands['selected_widget']].widget.bind(
                'Double-Button-1', lambda event, wid2=self.commands['selected_widget']: self.edit_widget(wid2))
            window.containers[self.commands['selected_widget']].widget.bind(
                '<1>', lambda event, wid2=self.commands['selected_widget'], wind=window: self.set_widget(wid2, wind))
            window.containers[self.commands['selected_widget']].widget.bind(
                '<Button-3>', lambda event, wid2=self.commands['selected_widget']: self.popup_menu.popup(event, wid2))
            self.window.containers['edit_resize_frame'].containers['YS_input'].set(self.ys_input())
            self.window.containers['edit_resize_frame'].containers['XS_input'].set(self.xs_input())
            self.command_fetch()['refresh_edit']()

    # TODO: The below always show the info for the Root window, not the frame/toplevel the widget is on. FIXME
    def windoww_input(self):
        """
        Grabs the base window width
        :return: base window width
        """
        return self.window.base_location['columnspan']

    def windowh_input(self):
        """
        Grabs the base window height
        :return: base window height
        """
        return self.window.base_location['rowspan']

    def x_input(self):
        self.tmp_args = self.grab_kwargs(self.commands['selected_widget'])
        return self.tmp_args['location']['column']

    def y_input(self):
        self.tmp_args = self.grab_kwargs(self.commands['selected_widget'])
        return self.tmp_args['location']['row']

    def xs_input(self):
        self.tmp_args = self.grab_kwargs(self.commands['selected_widget'])
        return self.tmp_args['location']['columnspan']

    def ys_input(self):
        self.tmp_args = self.grab_kwargs(self.commands['selected_widget'])
        return self.tmp_args['location']['rowspan']

    def resize_submit(self):
        """
        This method is called by the resize submit button. This allows the user to manually resize the widget

        :return: None
        """
        columnspan = self.is_int(self.window.containers['edit_resize_frame'].containers['XS_input'].get(), 1)
        rowspan = self.is_int(self.window.containers['edit_resize_frame'].containers['YS_input'].get(), 1)
        window = self.tmp_args['master']
        if columnspan and rowspan:
            if window == 'root_window':
                window = self.window
            else:
                window = self.window.containers[window]
            self.tmp_args = self.grab_kwargs(self.commands['selected_widget'])
            self.tmp_args['location']['rowspan'] = rowspan
            self.tmp_args['location']['columnspan'] = columnspan
            window.add_widget(**self.tmp_args)
            self.widget_args[self.commands['selected_widget']] = self.tmp_args
            window.containers[self.commands['selected_widget']].widget.bind(
                'Double-Button-1', lambda event, wid2=self.commands['selected_widget']: self.edit_widget(wid2))
            window.containers[self.commands['selected_widget']].widget.bind(
                '<1>', lambda event, wid2=self.commands['selected_widget'], wind=window: self.set_widget(wid2, wind))
            window.containers[self.commands['selected_widget']].widget.bind(
                '<Button-3>', lambda event, wid2=self.commands['selected_widget']: self.popup_menu.popup(event, wid2))
            self.window.containers['edit_resize_frame'].containers['YS_input'].set(self.ys_input())
            self.window.containers['edit_resize_frame'].containers['XS_input'].set(self.xs_input())
            self.command_fetch()['refresh_edit']()

    def move_submit(self):
        """
        This method is called by the move submit button and is used to manually move the button
        :return: None
        """
        column = self.is_int(self.window.containers['edit_move_frame'].containers['X_input'].get())
        row = self.is_int(self.window.containers['edit_move_frame'].containers['Y_input'].get())
        if column is not False and row is not False:
            self.tmp_args = self.grab_kwargs(self.commands['selected_widget'])
            window = self.tmp_args['master']
            if window == 'root_window':
                window = self.window
            else:
                window = self.window.containers[window]
            self.tmp_args['location']['row'] = row
            self.tmp_args['location']['column'] = column
            window.add_widget(**self.tmp_args)
            self.widget_args[self.commands['selected_widget']] = self.tmp_args
            window.containers[self.commands['selected_widget']].widget.bind(
                'Double-Button-1', lambda event, wid2=self.commands['selected_widget']: self.edit_widget(wid2))
            window.containers[self.commands['selected_widget']].widget.bind(
                '<1>', lambda event, wid2=self.commands['selected_widget'], wind=window: self.set_widget(wid2, wind))
            window.containers[self.commands['selected_widget']].widget.bind(
                '<Button-3>', lambda event, wid2=self.commands['selected_widget']: self.popup_menu.popup(event, wid2))
            self.window.containers['edit_move_frame'].containers['Y_input'].set(self.y_input())
            self.window.containers['edit_move_frame'].containers['X_input'].set(self.x_input())
            self.command_fetch()['refresh_edit']()
