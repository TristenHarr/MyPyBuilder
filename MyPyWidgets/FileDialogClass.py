from tkinter import filedialog


class FileDialog(object):

    def __init__(self, initialdir, file_type):
        if file_type == 'dir':
            self.choice = filedialog.askdirectory(initialdir=initialdir)

    def response(self):
        return self.choice
