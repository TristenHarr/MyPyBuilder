import tkinter.ttk as ttk
import tkinter as tk


class SpinBox(ttk.Spinbox):

    def __init__(self, frame, default, values, command):
        self.location = None
        self.var = tk.IntVar()
        super().__init__(master=frame,
                         values=values,
                         width=1,
                         textvariable=self.var,
                         command=command)
        self.widget = self
        self.set(default)

    def set_base_location(self, location):
        self.location = location

    def show_widget(self):
        self.grid(**self.location)
