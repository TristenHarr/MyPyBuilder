from GuiBuilder.STARTUP.Install import InstallProjects, InstallSettings
import os
import shutil


def install():
    demo_project = os.path.join(os.getcwd(), 'GuiBuilder', 'PROJECTS', 'Demo')
    demo_src = os.path.join(os.getcwd(), 'GuiBuilder', 'BUILDER', 'PROJECTBUILDER', 'Demo')
    settings_path = os.path.join(os.getcwd(), 'GuiBuilder', 'STARTUP', 'Settings')
    if os.path.exists(demo_project):
        shutil.move(demo_project, os.path.join(os.getcwd(), 'GuiBuilder'))
    if os.path.exists(demo_src):
        shutil.move(demo_src, os.path.join(os.getcwd(), 'GuiBuilder', 'STARTUP'))
    if os.path.exists(os.path.join(os.getcwd(), 'GuiBuilder', 'PROJECTS')):
        shutil.rmtree(os.path.join(os.getcwd(), 'GuiBuilder', 'PROJECTS'))
        os.mkdir(os.path.join(os.getcwd(), 'GuiBuilder', 'PROJECTS'))
        open(os.path.join(os.getcwd(), 'GuiBuilder', 'PROJECTS', '__init__.py'), 'a').close()
    if os.path.exists(os.path.join(os.getcwd(), 'GuiBuilder', 'BUILDER', 'PROJECTBUILDER')):
        shutil.rmtree(os.path.join(os.getcwd(), 'GuiBuilder', 'BUILDER', 'PROJECTBUILDER'))
        os.mkdir(os.path.join(os.getcwd(), 'GuiBuilder', 'BUILDER', 'PROJECTBUILDER'))
        open(os.path.join(os.getcwd(), 'GuiBuilder', 'BUILDER', 'PROJECTBUILDER', '__init__.py'), 'a').close()
    builder_settings = os.path.join(settings_path, 'builder_settings.json')
    project_settings = os.path.join(settings_path, 'project_settings.json')
    InstallSettings(builder_settings).factory_settings()
    InstallProjects(project_settings).factory_settings()
    demo = None
    if os.path.exists(os.path.join(os.getcwd(), 'GuiBuilder', 'Demo')):
        shutil.move(os.path.join(os.getcwd(), 'GuiBuilder', 'Demo'),
                    os.path.join(os.getcwd(), 'GuiBuilder', 'PROJECTS'))
    if os.path.exists(os.path.join(os.getcwd(), 'GuiBuilder', 'STARTUP', 'Demo')):
        shutil.move(os.path.join(os.getcwd(), 'GuiBuilder', 'STARTUP', 'Demo'),
                    os.path.join(os.getcwd(), 'GuiBuilder', 'BUILDER', 'PROJECTBUILDER'))
        demo = 'Demo'
    InstallProjects(project_settings, demo).factory_settings()
