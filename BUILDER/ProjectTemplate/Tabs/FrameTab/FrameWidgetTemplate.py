from MyPyWidgets import Label, DropDown, InputField, Button, CheckButton, NoteBook
frame_height = 350
tab_height = 300


class FrameWidget(object):

    def __init__(self):
        self.window_kwargs = {
            'type': 'frame',
            'id': 'frame_manager_frame',
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
            {'id': 'selected_frame',
             'widget': Label,
             'args': ['MORE COMING SOON'],
             'location': {
                 'row': 0,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             },
             'config': {'relief': 'sunken'}
             },

            {'id': 'refresh_edit',
             'widget': Button,
             'args': ['Refresh Frames', None],
             'location': {
                 'row': 0,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
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

        self.new_kwargs = {
            'type': 'frame',
            'id': 'make_frame_frame',
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

        self.new_components = [
            {'id': 'type_dropdown',
             'widget': DropDown,
             'args': ['Frame Type', ['Toplevel',
                                     'Frame'],
                      None],
             'location': {
                 'row': 0,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 400,
                 'sticky': 'NSWE'
             }
             }
        ]

        self.new_toplevel_components = [
            {'id': 'master_dropdown',
             'widget': DropDown,
             'args': ['root_window', None, lambda x: None],
             'location': {
                 'row': 30,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 400,
                 'sticky': 'NSWE'
             },
             'config': {'state': 'disabled'}
             },

            {'id': 'frame_id_label',
             'widget': Label,
             'args': ['Toplevel ID'],
             'location': {
                 'row': 60,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'frame_id_input',
             'widget': InputField,
             'args': [],
             'location': {
                 'row': 60,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'height_label',
             'widget': Label,
             'args': ['Toplevel Height'],
             'location': {
                 'row': 90,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'height_input',
             'widget': InputField,
             'args': [],
             'location': {
                 'row': 90,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'width_label',
             'widget': Label,
             'args': ['Toplevel Width'],
             'location': {
                 'row': 120,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'width_input',
             'widget': InputField,
             'args': [],
             'location': {
                 'row': 120,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'title_label',
             'widget': Label,
             'args': ['Toplevel Title'],
             'location': {
                 'row': 150,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'title_input',
             'widget': InputField,
             'args': [],
             'location': {
                 'row': 150,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'add_toplevel',
             'widget': Button,
             'args': ['Add Toplevel', None],
             'location': {
                 'row': 180,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 400,
                 'sticky': 'NSWE'
             }
             }
        ]

        self.new_frame_components = [
            {'id': 'master_dropdown',
             'widget': DropDown,
             'args': ['root_window', None, lambda x: None],
             'location': {
                 'row': 30,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 400,
                 'sticky': 'NSWE'
             },
             'config': {'state': 'disabled'}
             },

            {'id': 'frame_id_label',
             'widget': Label,
             'args': ['Frame ID'],
             'location': {
                 'row': 60,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'frame_id_input',
             'widget': InputField,
             'args': [],
             'location': {
                 'row': 60,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'width_label',
             'widget': Label,
             'args': ['Frame Width'],
             'location': {
                 'row': 90,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'width_input',
             'widget': InputField,
             'args': [],
             'location': {
                 'row': 90,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'height_label',
             'widget': Label,
             'args': ['Frame Height'],
             'location': {
                 'row': 120,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'height_input',
             'widget': InputField,
             'args': [],
             'location': {
                 'row': 120,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'verticalbase_label',
             'widget': Label,
             'args': ['Vertical Base (pixels)'],
             'location': {
                 'row': 150,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'verticalbase_input',
             'widget': InputField,
             'args': [],
             'location': {
                 'row': 150,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'horizontalbase_label',
             'widget': Label,
             'args': ['Horizontal Base (Pixels)'],
             'location': {
                 'row': 180,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'horizontalbase_input',
             'widget': InputField,
             'args': [],
             'location': {
                 'row': 180,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'vertical_checkbox',
             'widget': CheckButton,
             'args': ['Vertical Scroll', None],
             'location': {
                 'row': 210,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'horizontal_checkbox',
             'widget': CheckButton,
             'args': ['Horiz. Scroll', None],
             'location': {
                 'row': 210,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'add_frame',
             'widget': Button,
             'args': ['Add Frame', None],
             'location': {
                 'row': 270,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 400,
                 'sticky': 'NSWE'
             }
             }

        ]

        self.scroll_kwargs = [
            {'id': 'insetwidth_label',
             'widget': Label,
             'args': ['Inset-Width'],
             'location': {
                 'row': 240,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 100,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'insetwidth_input',
             'widget': InputField,
             'args': [],
             'location': {
                 'row': 240,
                 'column': 100,
                 'rowspan': 25,
                 'columnspan': 100,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'insetheight_label',
             'widget': Label,
             'args': ['Inset-Height'],
             'location': {
                 'row': 240,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 100,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'insetheight_input',
             'widget': InputField,
             'args': [],
             'location': {
                 'row': 240,
                 'column': 300,
                 'rowspan': 25,
                 'columnspan': 100,
                 'sticky': 'NSWE'
             }
             }
        ]

        self.edit_kwargs = {
            'type': 'frame',
            'id': 'edit_frame_frame',
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

        self.edit_components = [
            {'id': 'choose_frame',
             'widget': DropDown,
             'args': ['Select Frame', None, 'hotfix'],
             'location': {
                 'row': 0,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 400,
                 'sticky': 'NSWE'
             }
             }
        ]

        self.edit_frame = [
            {'id': 'frame_id_label',
             'widget': Label,
             'args': ['Frame ID'],
             'location': {
                 'row': 60,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'frame_id_input',
             'widget': InputField,
             'args': [],
             'location': {
                 'row': 60,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'width_label',
             'widget': Label,
             'args': ['Frame Width'],
             'location': {
                 'row': 90,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'width_input',
             'widget': InputField,
             'args': [],
             'location': {
                 'row': 90,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'height_label',
             'widget': Label,
             'args': ['Frame Height'],
             'location': {
                 'row': 120,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'height_input',
             'widget': InputField,
             'args': [],
             'location': {
                 'row': 120,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'verticalbase_label',
             'widget': Label,
             'args': ['Vertical Base (pixels)'],
             'location': {
                 'row': 150,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'verticalbase_input',
             'widget': InputField,
             'args': [],
             'location': {
                 'row': 150,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'horizontalbase_label',
             'widget': Label,
             'args': ['Horizontal Base (Pixels)'],
             'location': {
                 'row': 180,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'horizontalbase_input',
             'widget': InputField,
             'args': [],
             'location': {
                 'row': 180,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'vertical_checkboxf',
             'widget': CheckButton,
             'args': ['Vertical Scroll', None],
             'location': {
                 'row': 210,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'horizontal_checkboxf',
             'widget': CheckButton,
             'args': ['Horiz. Scroll', None],
             'location': {
                 'row': 210,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'delete_frame',
             'widget': Button,
             'args': ['Delete Frame', None],
             'location': {
                 'row': 240,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 400,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'edit_frame',
             'widget': Button,
             'args': ['Reconfigure Frame', None],
             'location': {
                 'row': 270,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 400,
                 'sticky': 'NSWE'
             }
             }
        ]

        self.edit_toplevel = [
            {'id': 'frame_id_label',
             'widget': Label,
             'args': ['Toplevel ID'],
             'location': {
                 'row': 60,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'frame_id_input',
             'widget': InputField,
             'args': [],
             'location': {
                 'row': 60,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'height_label',
             'widget': Label,
             'args': ['Toplevel Height'],
             'location': {
                 'row': 90,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'height_input',
             'widget': InputField,
             'args': [],
             'location': {
                 'row': 90,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'width_label',
             'widget': Label,
             'args': ['Toplevel Width'],
             'location': {
                 'row': 120,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'width_input',
             'widget': InputField,
             'args': [],
             'location': {
                 'row': 120,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'title_label',
             'widget': Label,
             'args': ['Toplevel Title'],
             'location': {
                 'row': 150,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'title_input',
             'widget': InputField,
             'args': [],
             'location': {
                 'row': 150,
                 'column': 200,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'delete_toplevel',
             'widget': Button,
             'args': ['Delete Toplevel', None],
             'location': {
                 'row': 210,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 400,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'edit_toplevel',
             'widget': Button,
             'args': ['Reconfigure Toplevel', None],
             'location': {
                 'row': 240,
                 'column': 0,
                 'rowspan': 25,
                 'columnspan': 400,
                 'sticky': 'NSWE'
             }
             }
        ]

        self.edit_root = [
            {'id': 'tmp_label',
             'widget': Label,
             'args': ['Coming Soon'],
             'location': {
                 'row': 60,
                 'column': 0,
                 'rowspan': 50,
                 'columnspan': 400,
                 'sticky': 'NSWE'
             }
             }
        ]

        self.save_kwargs = {
            'type': 'frame',
            'id': 'save_frame_frame',
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

        self.save_components = [
            {'id': 'save_project',
             'widget': Button,
             'args': ['Save Project', None],
             'location': {
                 'row': 10,
                 'column': 0,
                 'rowspan': 50,
                 'columnspan': 400,
                 'sticky': 'NSWE'
             }
             }
        ]
