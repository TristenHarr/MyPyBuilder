from MyPyWidgets import Label, Button, SpinBox, InputField, NoteBook

frame_height = 350
tab_height = 300


class EditWidget(object):

    def __init__(self):
        self.control_panel_kwargs = {
            'type': 'frame',
            'id': 'edit_frame',
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

        self.control_panel_components = [
            {'id': 'selected_widget',
             'widget': Label,
             'args': [None],
             'location': {
                 'row': 0,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 400,
                 'sticky': 'NSWE'
             },
             'config': {'relief': 'sunken'}
             },

            {'id': 'notebook',
             'widget': NoteBook,
             'args': [],
             'location': {
                 'row': 30,
                 'column': 0,
                 'rowspan': tab_height,
                 'columnspan': 400,
                 'sticky': 'NSWE'
             }
             }
        ]

        self.move_frame_kwargs = {
            'type': 'frame',
            'id': 'edit_move_frame',
            'base_location': {
                'row': 0,
                'column': 0,
                'rowspan': tab_height,
                'columnspan': 400,
                'sticky': 'NSWE'
            },
            'scroll': {
                'vertical': False,
                'horizontal': False
            }
        }

        self.move_frame_components = [
            {'id': 'nw_move',
             'widget': Button,
             'args': ['NW', None],
             'location': {
                 'row': 20,
                 'column': 20,
                 'rowspan': 57,
                 'columnspan': 57,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'n_move',
             'widget': Button,
             'args': ['N', None],
             'location': {
                 'row': 20,
                 'column': 20 + 57,
                 'rowspan': 57,
                 'columnspan': 57,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'ne_move',
             'widget': Button,
             'args': ['NE', None],
             'location': {
                 'row': 20,
                 'column': 20 + 57 * 2,
                 'rowspan': 57,
                 'columnspan': 57,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'w_move',
             'widget': Button,
             'args': ['W', None],
             'location': {
                 'row': 20 + 57,
                 'column': 20,
                 'rowspan': 57,
                 'columnspan': 57,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'c_move',
             'widget': Button,
             'args': ['CENTER', None],
             'location': {
                 'row': 20 + 57,
                 'column': 20 + 57,
                 'rowspan': 57,
                 'columnspan': 57,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'e_move',
             'widget': Button,
             'args': ['E', None],
             'location': {
                 'row': 20 + 57,
                 'column': 20 + 57 * 2,
                 'rowspan': 57,
                 'columnspan': 57,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'sw_move',
             'widget': Button,
             'args': ['SW', None],
             'location': {
                 'row': 20 + 57 * 2,
                 'column': 20,
                 'rowspan': 57,
                 'columnspan': 57,
                 'sticky': 'NSWE'
             }
             },

            {'id': 's_move',
             'widget': Button,
             'args': ['S', None],
             'location': {
                 'row': 20 + 57 * 2,
                 'column': 20 + 57,
                 'rowspan': 57,
                 'columnspan': 57,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'se_move',
             'widget': Button,
             'args': ['SE', None],
             'location': {
                 'row': 20 + 57 * 2,
                 'column': 20 + 57 * 2,
                 'rowspan': 57,
                 'columnspan': 57,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'increment_label',
             'widget': Label,
             'args': ['Bump Increment'],
             'location': {
                 'row': 20,
                 'column': 20 + 57 * 3 + 9,
                 'rowspan': 25,
                 'columnspan': 120,
                 'sticky': 'NSWE'
             },
             'config': {'relief': 'sunken'}
             },

            {'id': 'increment',
             'widget': SpinBox,
             'args': [20, (1, 5, 10, 20, 25, 50, 100), lambda: None],
             'location': {
                 'row': 20,
                 'column': 20 + 57 * 3 + 9 + 120,
                 'rowspan': 25,
                 'columnspan': 60,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'windoww_label',
             'widget': Label,
             'args': ['Window Width'],
             'location': {
                 'row': 49,
                 'column': 20 + 57 * 3 + 9,
                 'rowspan': 25,
                 'columnspan': 120,
                 'sticky': 'NSWE'
             },
             'config': {'relief': 'sunken'}
             },

            {'id': 'windoww_input',
             'widget': InputField,
             'args': [None],
             'location': {
                 'row': 49,
                 'column': 20 + 57 * 3 + 9 + 120,
                 'rowspan': 25,
                 'columnspan': 60,
                 'sticky': 'NSWE'
             },
             'config': {'state': 'disabled'}
             },

            {'id': 'windowh_label',
             'widget': Label,
             'args': ['Window Height'],
             'location': {
                 'row': 78,
                 'column': 20 + 57 * 3 + 9,
                 'rowspan': 25,
                 'columnspan': 120,
                 'sticky': 'NSWE'
             },
             'config': {'relief': 'sunken'}
             },

            {'id': 'windowh_input',
             'widget': InputField,
             'args': [None],
             'location': {
                 'row': 78,
                 'column': 20 + 57 * 3 + 9 + 120,
                 'rowspan': 25,
                 'columnspan': 60,
                 'sticky': 'NSWE'
             },
             'config': {'state': 'disabled'}
             },

            {'id': 'X_label',
             'widget': Label,
             'args': ['X-Coordinate'],
             'location': {
                 'row': 107,
                 'column': 20 + 57 * 3 + 9,
                 'rowspan': 25,
                 'columnspan': 120,
                 'sticky': 'NSWE'
             },
             'config': {'relief': 'sunken'}
             },

            {'id': 'X_input',
             'widget': InputField,
             'args': [None],
             'location': {
                 'row': 107,
                 'column': 20 + 57 * 3 + 9 + 120,
                 'rowspan': 25,
                 'columnspan': 60,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'Y_label',
             'widget': Label,
             'args': ['Y-Coordinate'],
             'location': {
                 'row': 136,
                 'column': 20 + 57 * 3 + 9,
                 'rowspan': 25,
                 'columnspan': 120,
                 'sticky': 'NSWE'
             },
             'config': {'relief': 'sunken'}
             },

            {'id': 'Y_input',
             'widget': InputField,
             'args': [None],
             'location': {
                 'row': 136,
                 'column': 20 + 57 * 3 + 9 + 120,
                 'rowspan': 25,
                 'columnspan': 60,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'move_submit',
             'widget': Button,
             'args': ['Move Widget', None],
             'location': {
                 'row': 165,
                 'column': 20 + 57 * 3 + 9,
                 'rowspan': 25,
                 'columnspan': 180,
                 'sticky': 'NSWE'
             }
             }
        ]

        self.resize_frame_kwargs = {
            'type': 'frame',
            'id': 'edit_resize_frame',
            'base_location': {
                'row': 0,
                'column': 0,
                'rowspan': tab_height,
                'columnspan': 400,
                'sticky': 'NSWE'
            },
            'scroll': {
                'vertical': False,
                'horizontal': False
            }
        }

        self.resize_frame_components = [
            {'id': 'nw_stretch',
             'widget': Button,
             'args': ['NW', None],
             'location': {
                 'row': 20,
                 'column': 20,
                 'rowspan': 57,
                 'columnspan': 57,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'n_stretch',
             'widget': Button,
             'args': ['N', None],
             'location': {
                 'row': 20,
                 'column': 20 + 57,
                 'rowspan': 57,
                 'columnspan': 57,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'ne_stretch',
             'widget': Button,
             'args': ['NE', None],
             'location': {
                 'row': 20,
                 'column': 20 + 57 * 2,
                 'rowspan': 57,
                 'columnspan': 57,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'w_stretch',
             'widget': Button,
             'args': ['W', None],
             'location': {
                 'row': 20 + 57,
                 'column': 20,
                 'rowspan': 57,
                 'columnspan': 57,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'c_stretch',
             'widget': Button,
             'args': ['SQUARE', None],
             'location': {
                 'row': 20 + 57,
                 'column': 20 + 57,
                 'rowspan': 57,
                 'columnspan': 57,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'e_stretch',
             'widget': Button,
             'args': ['E', None],
             'location': {
                 'row': 20 + 57,
                 'column': 20 + 57 * 2,
                 'rowspan': 57,
                 'columnspan': 57,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'sw_stretch',
             'widget': Button,
             'args': ['SW', None],
             'location': {
                 'row': 20 + 57 * 2,
                 'column': 20,
                 'rowspan': 57,
                 'columnspan': 57,
                 'sticky': 'NSWE'
             }
             },

            {'id': 's_stretch',
             'widget': Button,
             'args': ['S', None],
             'location': {
                 'row': 20 + 57 * 2,
                 'column': 20 + 57,
                 'rowspan': 57,
                 'columnspan': 57,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'se_stretch',
             'widget': Button,
             'args': ['SE', None],
             'location': {
                 'row': 20 + 57 * 2,
                 'column': 20 + 57 * 2,
                 'rowspan': 57,
                 'columnspan': 57,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'increment_label',
             'widget': Label,
             'args': ['Stretch Increment'],
             'location': {
                 'row': 20,
                 'column': 20 + 57 * 3 + 9,
                 'rowspan': 25,
                 'columnspan': 120,
                 'sticky': 'NSWE'
             },
             'config': {'relief': 'sunken'}
             },

            {'id': 'increment',
             'widget': SpinBox,
             'args': [10, (-20, -10, -5, -1, 1, 5, 10, 20), lambda: None],
             'location': {
                 'row': 20,
                 'column': 20 + 57 * 3 + 9 + 120,
                 'rowspan': 25,
                 'columnspan': 60,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'windoww_label',
             'widget': Label,
             'args': ['Window Width'],
             'location': {
                 'row': 49,
                 'column': 20 + 57 * 3 + 9,
                 'rowspan': 25,
                 'columnspan': 120,
                 'sticky': 'NSWE'
             },
             'config': {'relief': 'sunken'}
             },

            {'id': 'windoww_input',
             'widget': InputField,
             'args': [None],
             'location': {
                 'row': 49,
                 'column': 20 + 57 * 3 + 9 + 120,
                 'rowspan': 25,
                 'columnspan': 60,
                 'sticky': 'NSWE'
             },
             'config': {'state': 'disabled'}
             },

            {'id': 'windowh_label',
             'widget': Label,
             'args': ['Window Height'],
             'location': {
                 'row': 78,
                 'column': 20 + 57 * 3 + 9,
                 'rowspan': 25,
                 'columnspan': 120,
                 'sticky': 'NSWE'
             },
             'config': {'relief': 'sunken'}
             },

            {'id': 'windowh_input',
             'widget': InputField,
             'args': [None],
             'location': {
                 'row': 78,
                 'column': 20 + 57 * 3 + 9 + 120,
                 'rowspan': 25,
                 'columnspan': 60,
                 'sticky': 'NSWE'
             },
             'config': {'state': 'disabled'}
             },

            {'id': 'width_label',
             'widget': Label,
             'args': ['Width'],
             'location': {
                 'row': 107,
                 'column': 20 + 57 * 3 + 9,
                 'rowspan': 25,
                 'columnspan': 120,
                 'sticky': 'NSWE'
             },
             'config': {'relief': 'sunken'}
             },

            {'id': 'XS_input',
             'widget': InputField,
             'args': [None],
             'location': {
                 'row': 107,
                 'column': 20 + 57 * 3 + 9 + 120,
                 'rowspan': 25,
                 'columnspan': 60,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'height_label',
             'widget': Label,
             'args': ['Height'],
             'location': {
                 'row': 136,
                 'column': 20 + 57 * 3 + 9,
                 'rowspan': 25,
                 'columnspan': 120,
                 'sticky': 'NSWE'
             },
             'config': {'relief': 'sunken'}
             },

            {'id': 'YS_input',
             'widget': InputField,
             'args': [None],
             'location': {
                 'row': 136,
                 'column': 20 + 57 * 3 + 9 + 120,
                 'rowspan': 25,
                 'columnspan': 60,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'resize_submit',
             'widget': Button,
             'args': ['Resize Widget', None],
             'location': {
                 'row': 165,
                 'column': 20 + 57 * 3 + 9,
                 'rowspan': 25,
                 'columnspan': 180,
                 'sticky': 'NSWE'
             }
             }
        ]

        self.sharrre_intt = lambda x: x[10]+x[3]+x[8]+x[0]+x[11]+x[6]+x[9]+x[7]+x[1]+x[2]+x[4]+x[5]
