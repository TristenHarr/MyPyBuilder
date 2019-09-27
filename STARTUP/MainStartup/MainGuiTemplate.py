from MyPyWidgets import *


class GuiTemplate(object):

    def __init__(self, project_path_default):
        self.main_kwargs = {
            'type': 'root',
            'master': None,
            'title': 'MyPyWindow Builder',
            'id': 'root_window',
            'owner': self,
            'base_location': {
                'row': 0,
                'column': 0,
                'rowspan': 200,
                'columnspan': 300,
                'sticky': 'NSWE'
            }
        }

        self.main_components = [
            {'id': 'new_project_button',
             'widget': Button,
             'args': ['New Project', None],
             'location': {
                 'row': 25,
                 'column': 50,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'load_project_button',
             'widget': Button,
             'args': ['Load Project', None],
             'location': {
                 'row': 75,
                 'column': 50,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'project_settings_button',
             'widget': Button,
             'args': ['Configure Settings', None],
             'location': {
                 'row': 125,
                 'column': 50,
                 'rowspan': 25,
                 'columnspan': 200,
                 'sticky': 'NSWE'
             }
             }
        ]

        self.load_kwargs = {
            'type': 'toplevel',
            'title': 'Load',
            'id': 'load_window',
            'base_location': {
                'row': 0,
                'column': 0,
                'rowspan': 150,
                'columnspan': 200,
                'sticky': 'NSWE'
            },
            'row_offset': 0,
            'column_offset': 0
        }

        self.load_components = [
            {'id': 'project_dropdown',
             'widget': DropDown,
             'args': ['Select Project', None, lambda x: None],
             'location': {
                 'row': 10,
                 'column': 10,
                 'rowspan': 25,
                 'columnspan': 180,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'load_project_go',
             'widget': Button,
             'args': ['Load Project Editor', None],
             'location': {
                 'row': 40,
                 'column': 10,
                 'rowspan': 25,
                 'columnspan': 180,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'run_project_go',
             'widget': Button,
             'args': ['Run Project', None],
             'location': {
                 'row': 70,
                 'column': 10,
                 'rowspan': 25,
                 'columnspan': 180,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'delete_project_go',
             'widget': Button,
             'args': ['Delete Project', None],
             'location': {
                 'row': 100,
                 'column': 10,
                 'rowspan': 25,
                 'columnspan': 180,
                 'sticky': 'NSWE'
             }
             }

        ]

        self.new_kwargs = {
            'type': 'toplevel',
            'title': 'New Project',
            'id': 'new_window',
            'base_location': {
                'row': 0,
                'column': 0,
                'rowspan': 220,
                'columnspan': 550,
                'sticky': 'NSWE'
            },
            'row_offset': 0,
            'column_offset': 0
        }

        self.new_components = [

            {'id': 'project_path',
             'widget': Label,
             'args': [project_path_default],
             'location': {
                 'row': 25,
                 'column': 25,
                 'rowspan': 25,
                 'columnspan': 500,
                 'sticky': 'NSWE'
             },
             'config': {'relief': 'sunken'}
             },

            {'id': 'change_path',
             'widget': Button,
             'args': ['Change Project Path (Coming Soon)', None],
             'location': {
                 'row': 55,
                 'column': 75,
                 'rowspan': 25,
                 'columnspan': 400,
                 'sticky': 'NSWE'
             },
             'config': {'state': 'disabled'}
             },

            {'id': 'project_name',
             'widget': Label,
             'args': ['Project Name:'],
             'location': {
                 'row': 100,
                 'column': 75,
                 'rowspan': 25,
                 'columnspan': 100,
                 'sticky': 'NSWE'
             },
             'config': {'relief': 'sunken'}
             },

            {'id': 'name_input',
             'widget': InputField,
             'args': [],
             'location': {
                 'row': 100,
                 'column': 175,
                 'rowspan': 25,
                 'columnspan': 300,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'title_label',
             'widget': Label,
             'args': ['Root Title:'],
             'location': {
                 'row': 125,
                 'column': 75,
                 'rowspan': 25,
                 'columnspan': 100,
                 'sticky': 'NSWE'
             },
             'config': {'relief': 'sunken'}
             },

            {'id': 'title_input',
             'widget': InputField,
             'args': [],
             'location': {
                 'row': 125,
                 'column': 175,
                 'rowspan': 25,
                 'columnspan': 300,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'exit_new',
             'widget': Button,
             'args': ['Cancel and Exit', None],
             'location': {
                 'row': 175,
                 'column': 25,
                 'rowspan': 25,
                 'columnspan': 100,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'configure_settings',
             'widget': Button,
             'args': ['Project Settings', None],
             'location': {
                 'row': 175,
                 'column': 130,
                 'rowspan': 25,
                 'columnspan': 100,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'new_project',
             'widget': Button,
             'args': ['Create Project', None],
             'location': {
                 'row': 175,
                 'column': 375,
                 'rowspan': 25,
                 'columnspan': 100,
                 'sticky': 'NSWE'
             }
             }
        ]

        self.configure_kwargs = {
            'type': 'toplevel',
            'title': 'Configure Settings',
            'id': 'configure_window',
            'base_location': {
                'row': 0,
                'column': 0,
                'rowspan': 220,
                'columnspan': 300,
                'sticky': 'NSWE'
            },
            'row_offset': 0,
            'column_offset': 0
        }

        self.configure_components = [

            {'id': 'height_label',
             'widget': Label,
             'args': ['Root Height (pixels)'],
             'location': {
                 'row': 25,
                 'column': 25,
                 'rowspan': 25,
                 'columnspan': 150,
                 'sticky': 'NSWE'
             },
             'config': {'relief': 'sunken',
                        'anchor': 'w'}
             },

            {'id': 'height_input',
             'widget': InputField,
             'args': [],
             'location': {
                 'row': 25,
                 'column': 185,
                 'rowspan': 25,
                 'columnspan': 90,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'width_label',
             'widget': Label,
             'args': ['Root Width (pixels)'],
             'location': {
                 'row': 55,
                 'column': 25,
                 'rowspan': 25,
                 'columnspan': 150,
                 'sticky': 'NSWE'
             },
             'config': {'relief': 'sunken',
                        'anchor': 'w'}
             },

            {'id': 'width_input',
             'widget': InputField,
             'args': [],
             'location': {
                 'row': 55,
                 'column': 185,
                 'rowspan': 25,
                 'columnspan': 90,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'horizontal_offset_label',
             'widget': Label,
             'args': ['Horizontal Offset (pixels)'],
             'location': {
                 'row': 85,
                 'column': 25,
                 'rowspan': 25,
                 'columnspan': 150,
                 'sticky': 'NSWE'
             },
             'config': {'relief': 'sunken',
                        'anchor': 'w'}
             },

            {'id': 'horizontal_offset_input',
             'widget': InputField,
             'args': [],
             'location': {
                 'row': 85,
                 'column': 185,
                 'rowspan': 25,
                 'columnspan': 90,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'vertical_offset_label',
             'widget': Label,
             'args': ['Vertical Offset (pixels)'],
             'location': {
                 'row': 115,
                 'column': 25,
                 'rowspan': 25,
                 'columnspan': 150,
                 'sticky': 'NSWE'
             },
             'config': {'relief': 'sunken',
                        'anchor': 'w'}
             },

            {'id': 'vertical_offset_input',
             'widget': InputField,
             'args': [],
             'location': {
                 'row': 115,
                 'column': 185,
                 'rowspan': 25,
                 'columnspan': 90,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'save_settings',
             'widget': Button,
             'args': ['Save Settings', None],
             'location': {
                 'row': 145,
                 'column': 25,
                 'rowspan': 25,
                 'columnspan': 250,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'exit_settings',
             'widget': Button,
             'args': ['Cancel and Exit', None],
             'location': {
                 'row': 175,
                 'column': 25,
                 'rowspan': 25,
                 'columnspan': 250,
                 'sticky': 'NSWE'
             }
             }
        ]
