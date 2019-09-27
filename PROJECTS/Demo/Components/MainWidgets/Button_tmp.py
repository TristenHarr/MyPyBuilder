from MyPyWidgets import *


class Buttontmp(object):

    def __init__(self, master):
        self.master = master
        self.widget = {
            'master': 'root_window',
            'id': 'tmp',
            'widget': Button,
            'args': [self.tmp_button_fill(),
                     self.tmp_button_go],
            'location': {
                'row': 265,
                'column': 294,
                'rowspan': 25,
                'columnspan': 100,
                'sticky': 'NSWE'
            }
        }

    #&FUNCTIONS
    def tmp_button_fill(self):
        """
        Return the text value of tmp_button displayed on the gui
        """
        return 'tmp'

    def tmp_button_go(self, *args):
        """
        Function Called when tmp_button is clicked
        """
        print('tmp')

