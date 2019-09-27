import json


class InstallSettings(object):

    def __init__(self, path, settings=None):
        self.path = path
        if settings is None:
            self.default_window = {
                'type': 'root',
                'master': None,
                'title': 'Root Window',
                'id': 'root_window',
                'owner': None,
                'base_location': {
                    'row': 0,
                    'column': 0,
                    'rowspan': 500,
                    'columnspan': 500,
                    'sticky': 'NSWE'
                },
                'row_offset': 0,
                'column_offset': 0
            }
        else:
            self.default_window = settings

    def factory_settings(self):
        f = open(self.path, 'w')
        json.dump(self.default_window, f)
        f.close()
