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

        self.hello = Mainhello(self)
        self.hello.window = None
        self.hello_window = None
        self.hello_components = self.hello.components

        # &FRAMES
    def run(self):
        for widget in self.structure_components['root_window']:
            self.main_components[widget.__name__] = widget(self.main)
            self.main_window.add_widget(**self.main_components[widget.__name__].widget)
        self.main_window.setup()
        self.main_window.run()

    def show_hello(self):
        self.hello.widget['master'] = self.main_window
        if self.hello.widget['type'] == 'toplevel':
            self.main_window.add_toplevel(**self.hello.widget)
        else:
            self.main_window.add_frame(**self.hello.widget)
        self.hello.window = self.main_window.containers[self.hello.widget['id']]
        self.hello_window = self.hello.window
        for widget in self.structure_components['hello']:
            self.hello_components[widget.__name__] = widget(self.hello)
            self.hello_window.add_widget(**self.hello_components[widget.__name__].widget)

    # &SHOWFRAME
