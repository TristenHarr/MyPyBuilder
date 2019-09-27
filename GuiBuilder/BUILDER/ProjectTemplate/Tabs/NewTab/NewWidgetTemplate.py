from MyPyWidgets import DropDown, InputField, Label, Button, CheckButton
frame_height = 350


class NewWidget(object):

    def __init__(self):
        self.window_kwargs = {
            'type': 'frame',
            'id': 'new_frame',
            'base_location': {
                'row': 0,
                'column': 0,
                'rowspan': frame_height,
                'columnspan': 400,
                'sticky': 'NSWE'
            },
            'scroll': {
                'vertical': False,
                'horizontal': False
            }
        }

        self.components = [

            {'id': 'new_mode',
             'widget': DropDown,
             'args': ['Widget Type', ['Button',
                                      'DropDown',
                                      'InputField',
                                      'Label',
                                      'CheckButton',
                                      'SpinBox',
                                      'RadioButton'],
                      None],
             'location': {
                 'row': 0,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 400,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'width_label',
             'widget': Label,
             'args': ['Width: (Pixels)'],
             'location': {
                 'row': 30,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             },
             'config': {'relief': 'sunken'}
             },

            {'id': 'width_input',
             'widget': InputField,
             'args': [100],
             'location': {
                 'row': 30,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'height_label',
             'widget': Label,
             'args': ['Height: (Pixels)'],
             'location': {
                 'row': 60,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             },
             'config': {'relief': 'sunken'}
             },

            {'id': 'height_input',
             'widget': InputField,
             'args': [25],
             'location': {
                 'row': 60,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'vertical_label',
             'widget': Label,
             'args': ['Vertical Base (Pixels)'],
             'location': {
                 'row': 90,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             },
             'config': {'relief': 'sunken'}
             },

            {'id': 'vertical_input',
             'widget': InputField,
             'args': [0],
             'location': {
                 'row': 90,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'horizontal_label',
             'widget': Label,
             'args': ['Horizontal Base (Pixels)'],
             'location': {
                 'row': 120,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             },
             'config': {'relief': 'sunken'}
             },

            {'id': 'horizontal_input',
             'widget': InputField,
             'args': [0],
             'location': {
                 'row': 120,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'id_label',
             'widget': Label,
             'args': ['Widget Programmer ID'],
             'location': {
                 'row': 150,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             },
             'config': {'relief': 'sunken'}
             },

            {'id': 'id_input',
             'widget': InputField,
             'args': ['tmp'],
             'location': {
                 'row': 150,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'iter_id',
             'widget': CheckButton,
             'args': ['Iterative ID', lambda: None],
             'location': {
                 'row': 180,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'iter_loc',
             'widget': CheckButton,
             'args': ['Iterative Location', lambda: None],
             'location': {
                 'row': 180,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             }
        ]

        self.new_components = [
            {'id': 'frame_drop',
             'widget': DropDown,
             'args': ['Master Frame (Default: root_window)', None, lambda x: None],
             'location': {
                 'row': 210,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 400,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'add_button',
             'widget': Button,
             'args': ['Add Widget', None],
             'location': {
                 'row': 240,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 400,
                 'sticky': 'NSWE'
             }
             }
        ]
