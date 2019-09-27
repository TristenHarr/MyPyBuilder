import tkinter as tk


class Label(tk.Label):

    def __init__(self, frame, text):
        self.location = None
        self.var = tk.StringVar()
        super().__init__(master=frame,
                         textvariable=self.var,
                         width=1)
        self.var.set(text)
        self.widget = self

    def set(self, value):
        self.var.set(value)

    def get(self):
        return self.var.get()

    def set_base_location(self, location):
        self.location = location

    def show_widget(self):
        self.grid(**self.location)
