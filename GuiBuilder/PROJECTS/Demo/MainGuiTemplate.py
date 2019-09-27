

class MainTemplate(object):

    def __init__(self, master):
        self.master = master
        self.components = {}
        self.window = None
        self.widget = {'type': 'root',
                       'master': None,
                       'title': 'ok',
                       'id': 'root_window',
                       'owner': self.master,
                       'base_location': {
                            'row': 0,
                            'column': 0,
                            'rowspan': 500,
                            'columnspan': 500,
                            'sticky': 'NSWE'
                            },
                       'row_offset': 0,
                       'column_offset': 0}
