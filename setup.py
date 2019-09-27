from setuptools import setup

setup(
    name='MyPyBuilder',
    version='1.0',
    packages=['GuiBuilder', 'GuiBuilder.BUILDER', 'GuiBuilder.BUILDER.PROJECTBUILDER',
              'GuiBuilder.BUILDER.PROJECTBUILDER.Stuffs', 'GuiBuilder.BUILDER.PROJECTBUILDER.Wicked',
              'GuiBuilder.BUILDER.ProjectTemplate', 'GuiBuilder.BUILDER.ProjectTemplate.Tabs',
              'GuiBuilder.BUILDER.ProjectTemplate.Tabs.NewTab', 'GuiBuilder.BUILDER.ProjectTemplate.Tabs.EditTab',
              'GuiBuilder.BUILDER.ProjectTemplate.Tabs.FrameTab', 'GuiBuilder.STARTUP', 'GuiBuilder.STARTUP.Install',
              'GuiBuilder.STARTUP.MainStartup', 'GuiBuilder.PROJECTS', 'GuiBuilder.PROJECTS.Stuffs',
              'GuiBuilder.PROJECTS.Stuffs.Components', 'GuiBuilder.PROJECTS.Stuffs.Components.MainWidgets',
              'GuiBuilder.PROJECTS.Wicked', 'GuiBuilder.PROJECTS.Wicked.Components',
              'GuiBuilder.PROJECTS.Wicked.Components.MainWidgets', 'MyPyWidgets'],
    url='www.nothingyet.com',
    license='LICENSE',
    author='Tristen Harr',
    author_email='Noneyet@somesite.com',
    description='Drag and Drop Tkinter Gui Builder',
    longdescription='README.rst'
)
