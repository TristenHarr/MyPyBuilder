# Project TODO List

* Extract the seperate Widget Classes to use the Tkinter defaults projectwide (High Priority)

* Add Notebooks, Tabs, Progressbar, Sizegrip... etc. (Medium Priority)

* Simplify structure in generated widgets class. (High Priority)

...Currently all logic code should be written in the MainGui.py file generated, wether through imported classes,
...or written directly into the file. If you want to link a function call to function abc() to a button "btn" on the main window
...and abc() is in the MainGui.py file, you would go to MyPyBuilder/GuiBuilder/PROJECTS/Project_Name/Components/MainWidgets/Button_btn.py
...and in function btn_button_go() you would type self.master.master.abc() this should also have an alias. Maybe self.wind.abc()?

* Make it possible to nest frames and Toplevels. (Medium Priority)

...This is possible, but I disabled the feature because it breaks the drag-and-drop inside the nested frames, and also because
...when the code is generated for the project file it doesn't know how to handle this instance. It would be some kind of recursion where
...all frames/toplevels are stored inside the ../Components/Frames directory (along with their widgets stored in respective directories)
...but it would change the way that the Main_frameName_Frame.py file stored it's "owner" in the widgets dict, and the way the MainGui.py 
...file handled the creation of frames.

* Create More comprehensive documentation. (High Priority)

...Write better documentation for the code files, and also create a short series of "How-to" videos to post on youtube explaining how
...to use the builder.

* Fix the frame_drag_helper() method in GuiBuilder/BUILDER/ProjectTemplate/RootTemplate.py (Medium Priority)

...More details in comment in source. (See Line 317)

* Turn the really() method into a decorator (Low Priority)

...The really method pops up a window that says "Are you sure?" when making big changes, such as deleting frames, exiting the application, etc.
...More details in GuiBuilder/BUILDER/ProjectTemplate/Roso otTemplate.py (See Line 390)

* Remove the hotfix in the refresh_edit_frames() method found in GuiBuilder/BUILDER/ProjectTemplates/Tabs/FrameTab/FrameTabBuild.py (High Priority)

...I have a feeling this one could potentially be tricky, If I remember correctly I spent a solid 2 hours before just saying "screw it" and 
...implementing a quick and dirty fix. It has to do with how the widgets on a frame that is being edited are handled. So if you have a frame
...with a bunch of buttons/dropdowns/etc. and you want to resize the frame, it handles deleting the existing frame, then taking all the widgets
...that were on the frame and placing them on a new frame of the correct size. (See Line 235)

* Fix the tmp hack in the add_frame() method found in GuiBuilder/BUILDER/ProjectTemplate/Tabs/FrameTab/FrameTabBuild.py

...This has to do with how the vertical and horizontal scrolling of frames in handled when editing the frame. (See line 329)

## FUTURES

*Create a Dynamic Form Builder

...This is one of my biggest hopes for an additional feature. I don't just want something thats so static. I want dynamic forms.
...An example: Form-Group objects, where you have a dropdown and if option A is selected, then another dropdown with Option_A_Choices pops up,
...Then if Option_B is selected maybe input fields pop-up pertaining to option B. This could be implemented using "Form States"
...So maybe the default is "Choose an option" in the dropdown, this is form state 1, and it tells the form to disable the second dropdown.
...Once an option is selected, it changes to form state 2, and it goes and gets the required items to generate the next dropdown based on option A
...This is one of the primary goals, because many times we build forms where there is a Form-Logic of "When option A is selected then this other
...form aspect becomes available, and is populated like _____"

* Add styling to the GuiBuilder.

...Right click a widget, and select "Style Widget" and have options for colors, and other built-in tkinter styling





