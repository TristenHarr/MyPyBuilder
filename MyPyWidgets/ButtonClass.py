import tkinter.ttk as ttk


class Button(ttk.Button):

    def __init__(self, frame, text, command):
        self.location = None
        super().__init__(master=frame,
                         text=text,
                         command=command,
                         width=1)
        self.widget = self

    def get(self):
        return self['text']

    def set(self, value):
        self['text'] = value

    def set_base_location(self, location):
        self.location = location

    def show_widget(self):
        self.grid(**self.location)

    def read(self):
        self.configure({'state': 'disabled'})

    def write(self):
        self.configure({'state': 'normal'})