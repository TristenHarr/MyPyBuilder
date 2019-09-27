from MyPyWidgets import *
window_height = 350


class ControlPanel(object):

    def __init__(self):
        self.window_kwargs = {
            'type': 'toplevel',
            'title': 'Builder',
            'id': 'control_panel',
            'base_location': {
                'row': 0,
                'column': 0,
                'rowspan': window_height,
                'columnspan': 400,
                'sticky': 'NSWE'
            },
            'row_offset': -50,
            'column_offset': 400
        }

        self.components = {'id': 'notebook',
                           'widget': NoteBook,
                           'args': [],
                           'location': {
                               'row': 0,
                               'column': 0,
                               'rowspan': window_height,
                               'columnspan': 400,
                               'sticky': 'NSWE'
                           }
                           }

        self.really_kwargs = {
            'type': 'toplevel',
            'title': 'Really?',
            'id': 'really_window',
            'base_location': {
                'row': 0,
                'column': 0,
                'rowspan': 90,
                'columnspan': 100,
                'sticky': 'NSWE'
            }
        }

        self.really_components = [
            {'id': 'really_label',
             'widget': Label,
             'args': ['Are you sure?'],
             'location': {
                 'row': 10,
                 'column': 10,
                 'rowspan': 25,
                 'columnspan': 80,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'really_go',
             'widget': Button,
             'args': ['Yes', None],
             'location': {
                 'row': 40,
                 'column': 10,
                 'rowspan': 25,
                 'columnspan': 35,
                 'sticky': 'NSWE'
             }
             },

            {'id': 'really_cancel',
             'widget': Button,
             'args': ['No', None],
             'location': {
                 'row': 40,
                 'column': 55,
                 'rowspan': 25,
                 'columnspan': 35,
                 'sticky': 'NSWE'
             }
             }
        ]
