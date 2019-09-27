import tkinter as tk
import tkinter.ttk as ttk


class DropDown(ttk.OptionMenu):

    def __init__(self, frame, default, values, command):
        self.location = None
        self.var = tk.StringVar()
        super().__init__(frame,
                         self.var,
                         *[default, *values],
                         command=command)
        self.widget = self

    def set_base_location(self, location):
        self.location = location

    def show_widget(self):
        self.grid(**self.location)

    def get(self):
        return self.var.get()

    def set(self, value):
        self.var.set(value)
