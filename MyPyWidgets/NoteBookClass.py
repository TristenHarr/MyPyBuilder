import tkinter.ttk as ttk


class NoteBook(ttk.Notebook):

    def __init__(self, frame):
        self.location = None
        super().__init__(master=frame)
        self.widget = self

    def add_tab(self, frame, tab_id):
        self.widget.add(frame, text=tab_id)

    def set_base_location(self, location):
        self.location = location

    def show_widget(self):
        self.grid(**self.location)
