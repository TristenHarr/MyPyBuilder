from MyPyWidgets import *
from GuiBuilder.PROJECTS.Demo import *


class Gui(object):

    def __init__(self):
        self.main = MainTemplate(self)
        self.main.window = MyPyWindow(**self.main.widget)
        self.main_window = self.main.window
        self.main_components = self.main.components
        self.structure = BuildHelper()
        self.structure_components = self.structure.components

        # &FRAMES
    def run(self):
        for widget in self.structure_components['root_window']:
            self.main_components[widget.__name__] = widget(self.main)
            self.main_window.add_widget(**self.main_components[widget.__name__].widget)
        self.main_window.setup()
        self.main_window.run()

    # &SHOWFRAME
