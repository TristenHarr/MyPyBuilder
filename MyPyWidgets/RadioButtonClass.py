import tkinter as tk
# TODO: Implement a Group-Function that can be called, and handed in a group of radio-button id's and group them


class RadioButton(tk.Radiobutton):

    def __init__(self, frame, text, value, command):
        self.location = None
        super().__init__(master=frame,
                         text=text,
                         value=value,
                         command=command,
                         height=1,
                         width=1
                         )
        self.widget = self

    def set_var(self, var):
        self.configure({'variable': var})

    def set_base_location(self, location):
        self.location = location

    def show_widget(self):
        self.grid(**self.location)
