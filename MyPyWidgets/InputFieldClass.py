import tkinter as tk


class InputField(tk.Entry):

    def __init__(self, frame, default=None):
        self.location = None
        self.var = tk.StringVar()
        super().__init__(master=frame,
                         textvariable=self.var,
                         justify='center',
                         width=1)
        self.widget = self
        if default is not None:
            self.var.set(default)

    def set(self, value):
        self.var.set(value)

    def get(self):
        return self.var.get()

    def set_base_location(self, location):
        self.location = location

    def show_widget(self):
        self.grid(**self.location)