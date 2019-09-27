import tkinter as tk


class Menu(tk.Menu):

    def __init__(self, frame, options=None):
        self.location = None
        self.selected = None
        super().__init__(master=frame,
                         tearoff=0)
        self.widget = self
        if options is not None:
            for option in options:
                self.add_option(*option)

    def set_base_location(self, location):
        self.location = location

    def show_widget(self):
        self.grid(**self.location)

    def add_option(self, option, command):
        self.add_command(label=option,
                         command=command)

    def popup(self, event, wid):
        self.selected = wid
        try:
            self.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.grab_release()
