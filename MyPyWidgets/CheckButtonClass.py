import tkinter as tk


class CheckButton(tk.Checkbutton):

    def __init__(self, frame, text, command):
        self.location = None
        self.var = tk.IntVar()
        super().__init__(master=frame,
                         text=text,
                         variable=self.var,
                         command=command)
        self.widget = self

    def set(self, value):
        self.var.set(value)

    def get(self):
        return self.var.get()

    def set_base_location(self, location):
        self.location = location

    def show_widget(self):
        self.grid(**self.location)
