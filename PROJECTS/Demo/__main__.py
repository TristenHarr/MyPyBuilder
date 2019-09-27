from GuiBuilder.PROJECTS.Demo.MainGui import Gui


class Main(object):

    def __init__(self):
        self.app = Gui()
        self.app.run()


if __name__ == '__main__':
    Main()
