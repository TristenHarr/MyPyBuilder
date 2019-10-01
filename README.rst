=====
MyPyBuilder
=====

What is MyPyBuilder?
--------
MyPyBuilder is a Drag-and-Drop GUI builder that wraps the tkinter library.

* Windows and Widgets automatically resize when the window is stretched.
* The GUI code is generated for you, all you do is write the logic.
* Allows you to build multiple different projects at once, keeping them all organized for you.
* Works with PyInstaller, so finished applications can be turned into executable's and shipped.
* Does not require any imports to use, as it is built entirely on built-ins.
* Forces widgets and windows to be the size you want, not some weird size tkinter decides they should be.
* Makes it easy to make scrollable frames, toplevel windows, and writes the logic for making them appear for you.

Why Use MyPyBuilder over other GUI Builders?
--------
MyPyBuilder **IS NOT** designed with the primary purpose of making commercial applications to offer to customers. 
MyPyBuilder is designed to be used as an extremely fast way to skin a python script.

* MyPyBuilder is designed with a minimal interface so that you don't have a bunch of windows and options getting in the way
* MyPyBuilder was designed specifically with engineering research labs in mind, allowing existing testing/verification scripts that run via command line to be skinned with a GUI in 10-20 minutes. 
* MyPyBuilder is designed with a minimal learning curve compared to many currently available GUI builders.
* MyPyBuilder is implemented in 100% pure python code, so changing things doesn't require knowing another GUI language.

Oftentimes we write a script that for one reason or another ends up needing a GUI. The script takes us 10 minutes to write, and but the GUI can sometimes take hours. MyPyBuilder is different. MyPyBuilder is designed to make building a GUI just as fast as writing the code that runs it.


**KEEP IN MIND WHEN DEVELOPING THAT THIS IS A BETA RELEASE OF THE APPLICATION. CHANGES WILL BE MADE THAT COULD POTENTIALLY BREAK BACKWARDS COMPATIBILITY**


Setting up and running the application for the first time.
--------

Download/Form the repo in it's entirety and open in your IDE of choice, or run directly from the command line.
The file you want to run is the __main__.py file. The project should take care of the setup for you, if there are any issues/bugs at any point in time, and you want to start over from scratch (BEWARE THIS WILL DELETE ANY PROJECTS YOU HAVE CREATED) or if you have issues getting started, go to the version.txt file, and set the version number equal to 0.0. (This will clean out all projects except for the project titled Demo)



Important Information to Take Note Of
--------
The functionality of the drag and drop builder is made to be as intuitive as possible. (With that said, youtube tutorials will be released in the coming future) Take special care when naming widgets/frames to use a unique ID that describes to you what the button/dropdown/etc is for. These ID's are what will be used to generate all methods/code files/etc. for the project. Beware that if a widget ID is in use, and if you attempt to make another widget with the same ID nothing will happen. (In the future perhaps an alert will pop-up)



Configuring the Project Settings
--------
**THIS MUST BE DONE BEFORE THE PROJECT IS BUILT. IT CANNOT BE CHANGED (EASILY) LATER!** (A Fix to this is coming soon)

**Note**: To change the size of a project later, you can go into the GuiBuilder/PROJECTS/Name_Of_Project/MainGuiTemplate.py file
and edit the rowspan/columnspan directly. To reflect these changes in the GuiBuilder, go into the GuiBuilder/BUILDER/PROJECTBUILDER/Name_Of_Project/MainGuiBuilderName_Of_Project.py file and edit the 
self.window_kwargs['base_location']['rowspan'] and self.window_kwargs['base_location']['columnspan'].
**IF YOU MANUALLY EDIT THE WINDOW SIZE TO MAKE IT SMALLER AND A WIDGET IS CURRENTLY LOCATED OUTSIDE OF THE NEW WINDOW SIZE THE PROJECT WILL CRASH**

When you first run the application, if you select the **Configure Settings** button you can specify the window width and height 
(**Root Height/Width**) This is the size the main window will be in pixels. The window will be loaded in the center of the screen by default. If you wish to load it in a different location you can use the **Horizontal Offset** and **Vertical Offset** to force the window to appear in a different location on the screen. 
**BUG** The Horizontal and Vertical Offset currently has issues when rendering the final application. This will be fixed shortly and is a quick fix.
When you have finished configuring the settings simply click the **Save Settings** button.


Starting a New Project
--------
In the main startup window select the **New Project** button. In the current implementation the project path cannot be changed. (This will be fixed in the future, and it has to do with the fact that for each new project there is an entire assortment of directories and folders created dynamically, including one for the builder, and one for the final application) 
Input a **Project Name** and then input the **Root Title** (The title at the top of the window)
If you have not done so already, you can click the **Project Settings** to configure the settings for the project. (See Above)
When you are ready to start the project click **Create Project** and the click the **Start Project** button in the window that pops up.


Loading an Existing Project
--------
In the main startup window click the **Load Project** button. In the window that pops up select the project you would like to load.
If you wish to go into the Gui Builder to edit the project, click the **Load Project Editor** button. 
If you wish to view what the project currently looks like as a standalone application click the **Run Project** button. 
**IMPORTANT NOTE**: If you build this super cool project and then click the **Run Project** button, chances are it will fail. This is because in the guibuilder the **Widget ID's** are set as the default values, but that isn't the case in the final project, in which it is your job to specify the basic widget information. **See The Coding The Logic Section**


Deleting an Existing Project
--------
In the main startup window click the **Load Project** button. From there, select the project you wish to delete from the dropdown, and 
select **Delete Project**

**NOTE TO PROJECT CONTRIBUTORS**:
While in the process of developing the project, chances are you will quickly find yourself inundated with as many as 50+ projects at any given time. (Make a change, start a new project to test it, then repeat) Instead of going through all these projects one-by-one, if you open the version.txt file, and set the verion number = 0.0, when you re-run the __main__.py program, it will by default delete every project except the one titled "Demo".

Using the Create Widget Tab
--------
This tab is used for creating widgets. 
**Note**: Do not worry much about position and size, as it is easier to edit later. The **Widget Programmer ID** CANNOT be edited later.

- The width input specifies the width of the widget.
- The heigh input specifies the height of the widget.
- The Vertical Base specifies the Y-coordinate of the widget. With 0 being the top of the frame.
- The Horizontal Base specifies the X-coordinate of the widget. With 0 being the left side of the frame.
- The **Widget Programmer ID** is the ID that you will use when implementing the logic behind widgets. Take care to name this something   that makes sense.
- The **Master Frame Dropdown** specifies which frame/toplevel the widget should be added to, and defaults to the main window.

There are two additional special features contained in this tab to make life easier for you. The first feature is the iterative id. 
When the **Iterative ID** is checked, whatever the current **Widget Programmer ID** value is, will iterate whenever a widget is added.
This allows you to add a bunch of widgets that are likely related to eachother without having to go change the ID over and over.
For Example:
   John is building a calculator application. He needs buttons from 0 to 9. 
   John checks the **Iterative ID** checkbox and in the **Widget Programmer ID** he types "calc_button0"
   John selects "Button" from the widget dropdown, and then proceeds to simply press Add widget.
   The programmer ID changes to calc_button1, then calc_button2, etc. 

The second special feature is the **Iterative Location** checkbox. In the above example all of John's buttons would appear in the same location. Meaning that if John made buttons 0-9, they would all be stacked and he would only be able to see calc_button9, and then under that would be button8, etc. The iterative location offsets the buttons slightly, so that they still appear stacked, but they are in a diagonal line moving down and to the right.


Making Widgets Resize with the window
--------
Nothing to see here, All Widgets resize automagically. The sizes you set in the GuiBuilder are just the initial sizes. Stretch the window and the widgets will resize with the window. 


Using the Edit Widget Tab
--------
**Note**: To delete a widget, simply right click it and select delete.
When the programmer clicks on a widget, that widget is opened in the Edit widget tab.

The Edit widget tab is what allows you to resize a widget, and to move it around on the page. (You can also drag and drop the widget)
When building the application I found drag-and-drop was awesome, but not when you needed to nudge the widget a few pixels to the left or to the right. **The currently selected widget will be displayed in the top of the tab**


**Move Widget Tab**
The move widget tab is comprised of 9 buttons, along with relevant input fields. When a widget is selected, to move that widget in a specific direction, simply "bump" the widget that direction by clicking one of the buttons. The widget will never scroll of the window, if moving **sw** (south-west) for example and the widget hits the bottom of the window, it will then simply move west on continued clicks. 

The **CENTER** button will always move a widget to the center of the window it is placed in.

The **Bump Increment** is the amount to "bump" the widget when the button is clicked. When set to 1, it will move the widget 1 pixel in that direction. Users CAN type in a specific value directly, and the spinnerBox is simply set with some default values.

The Window Width and Height are displayed in this tab as a reference to the programmer.

Also available is an input for the **X-Coordinate** and the **Y-Coordinate** which can be used to place the widget at a specific pixel location on the screen when the **Move Widget** button is clicked. (The top-left corner will be placed at that location)


**Resize Widget Tab**
The resize widget tab layout is very similar to the move widget tab, but instead of moving the widget, it is used to resize the widget.
**Note**: The "Stretch Increment CAN be a negative value"
I have found this to be extremely useful in comparison with many Gui builders, because normally widgets automatically resize extending down, and to the right. 

The **Stretch Increment** allows the user to specify how much they wish to stretch the button. For example if the stretch increment is set to 7, and the "W" button is clicked, the widget will stretch from its current location, growing 7 pixels to the left. 
**Did You Accidentally Make A Wiget Too Large?** Simply set the **Stretch Increment** to a negative value, and then select which side should shrink. 

The **SQUARE** button will revert the widget to a size of 1x1 (This will likely be changed in the future)

The Window Width and Height are displayed in this tab as a reference to the programmer.

Also included in this tab are the **Width** and **Height** fields. This allows the user to specify a specific width and height they would like the widget to be, and then set it to that size by clicking **Resize Widget**.



Using the Frame Manager Tab
--------
The frame manager tab allows you to add/manage frames, scrollable frames, and toplevels. 

**New Frame Tab**
The new frame tab allows you to create a new frame or toplevel for the project. (Currently Frames and Toplevels cannot be nested. This is a high-priority item on the TODO list for the project and will hopefully be coming soon!)

The first choice you must make when in the New Frame Tab is if you wish to add a Frame, or a Toplevel.

**Creating a New FRAME**
**Note**: New Frames will have a green background in the editor. This is simply so you can see the frame, and this isn't the case when 
running the application later.

**Note**: If you create a scrollable frame and the main window resizes, no need to panic! The scroll frame will resize to the specified size as soon as a widget is added to it.

The first thing you need to specify when creating a new frame is the Frame ID. This is the unique identifier for the frame in the project. Once this has been completed, Go ahead and specify the **Frame Width** and **Frame Height**. 
If this frame is going to be a scrollable frame, the **Frame Width** and **Frame Height** will end up being the size of the viewing window. (The size of the window with the scroll-bars, not the size of the inside window that scrolls around) 
The next step is to specify the Vertical Base and Horizontal Base. (See the Create Widget Tab)
**If the frame will be scrollable**
If the frame is going to be scrollable you can fill out the checkboxes to make it scroll vertically, horizontally, or both!
If selected, another field pops up asking you for the **Inset-Width** and the **Inset-Height**. This specifies the size of the inner-window, and should be **LARGER** than the frame width and height. 
Once completed you can go ahead and click **Add Frame** to add the frame to the main window.


**Creating a New TOPLEVEL**
A Toplevel is a window that pops up seperately. 
**Note**: When you initially create a toplevel it will be size 0, but don't worry! It will resize to the size you wanted as soon as you add a widget.

**Note**: When a Toplevel is added in the GuiBuilder, it cannot be closed. This behaviour isn't the case in the final project. If it's getting in the way, simply minimize the window.

Creating a new toplevel is even easier than creating a frame. First create the **Toplevel ID** which is the unique ID used to identify the toplevel. The next step is to specify the **Toplevel Height** and the **Toplevel Width** which tells the Toplevel how big you would like it to be. The last step is to set a Title for the Toplevel. The Title is what will display at the top of the window.
(Window Icons are coming soon!) From there, simply click the **Add Toplevel** button to add your new toplevel.



**Edit Frames Tab**
This tab is used to edit existing frames. Perhaps you forgot about a button you needed and need to make the window a little bigger.
This tab is also where you can **DELETE** frames and toplevels you do not need.

**BUG** Currently there are issues with scrollable frames. Changing a Normal Frame to a Scrollable frame will fail, and not allow you to add widgets to the frame. Resizing scrollable frames, and other edit-tools involving scrollable frames are encountering issues. This will be fixed ASAP!!! For the time being, if you encounter an issue with duplicating frames, save the project, exit it, and reload it.

**Note**: Although the ID is shown as an editable field, changing the ID will cause the frame to be duplicated.

**Note**: When editing the size/location of a frame/toplevel the widgets currently added to the frame/toplevel will be put in the same location when reconfigured.

**Note**: If a Frame isn't popping up in the dropdown after loading a project or creating a new frame, click the **Refresh Frames** button.

To use the Edit Frame Tab, see **Creating a New TOPLEVEL** and **Creating a New FRAME**. 


**Save Project Tab**
This tab is how you save the current project. 
**YOU MUST SAVE THE PROJECT BEFORE CLOSING AS AUTOSAVE IS NOT YET AVAILABLE**
(In the future it will likely be moved to a button on the top or bottom of the Builder window and always visible.)



Exiting the Gui Builder
--------
As you may have noticed, many of the buttons that close the window (X button) do not work. This is to ensure functionality of the application. If you could close the builder window, you... well you wouldn't be able to build anything anymore. 

**To Exit the Gui Builder hit the X button on the Main Window of the project. (root_window)**


Coding The Logic
--------
**IMPORTANT: IF YOU WRITE LOGIC, THEN GO BACK AND EDIT THE GUI IN THE GUI BUILDER AND SAVE IT, THE LOGIC WILL BE OVERWRITTEN. (An attemped fix for this is in the works)**

**For this section we will be working with a Project titled Demo**

**This Section is likely the most important section in the entire document.**
When you create a project with the GuiBuilder you probably think "Neat, I Got this cool gui built! How do I actually make it functional?" This section will give an overview of how to actually insert the logic into your newly built GUI and some recommendations for getting everything to work.

**Where Do I Find The Final Application? What's The Directory Structure Look Like?**
The code that gets generated for the Application is going to be stored inside the GuiBuilder/PROJECTS directory. So, for the project Demo, it will be the GuiBuilder/Projects/Demo directory.
Inside this directory you will find the following layout:

::

 Demo
 |
 |--- Components
 |    |
 |    |--- Frames
 |    |
 |    |--- MainWidgets
 |    |    |
 |    |    |--- __init__.py
 |    |
 |    |--- __init__.py
 |    |
 |    |--- Builder_Helper.py
 |
 |--- __init__.py
 |
 |--- __main__.py
 |
 |--- MainGui.py
 |
 |--- MainGuiTemplate.py

The MainGui.py file is where you will write/use all the logic code for the project.
**Recommendation**: Write all the logic in a seperate class/classes, and then import it into the MainGui.py file.

Buttons:
   If you create a button on the main window of the Gui with the **Widget ID** of click_me this is how you would make it operational.
   Lets say you want to print **"hello"** to the console when the button is clicked and you want the button text to be **"Clickity"**
   In Demo/Components/MainWidgets/Button_click_me.py you will find the button.
   There will be two functions generated for you in this file.
   
   .. code-block:: python
   
        def click_me_button_fill(self):
            """
            Return the text value of click_me_button displayed on the gui
            """
            return 'click_me'

        def click_me_button_go(self, *args):
            """
            Function Called when click_me_button is clicked
            """
            print('click_me')
            
   By changing the return value in the click_me_button_fill() you are specifying the text to display on the button.
   If you wanted the button to say "Clickity" you would change the return line to
    
   .. code-block:: python
    
       return "Clickity"
   
   The click_me_button_go() method specifies what to do when the button is clicked.
   It is not recommended but will work to simply write the code logic inside this method.
   
   The reccomended way of doing things however is to write the code logic in the MainGui.py file.
   Assume there is a function written in MainGui.py as follows:
   
   .. code-block:: python
       def click_me_go(self):
           print("hello")
   
   In the Button_click_me.py file you then would change the click_me_button_go() method to
   
   .. code-block:: python
   
       def click_me_button_go(self, *args):
           """
           Function Called when click_me_button is clicked
           """
           self.master.master.click_me_go()
           
**Lets Talk About the way things are Structured**
Assume we have a project called Demo2. This project has 1 scrollable frame (ID ScrollFrame), 1 toplevel (ID TopLevel), and 3 buttons. (1 button on each window/frame)
This is what our MainGui.py file is going to look like:
    
    .. code-block:: python
    
		from MyPyWidgets import *
		from GuiBuilder.PROJECTS.Demo2 import *


		class Gui(object):

			def __init__(self):
				self.main = MainTemplate(self)
				self.main.window = MyPyWindow(**self.main.widget)
				self.main_window = self.main.window
				self.main_components = self.main.components
				self.structure = BuildHelper()
				self.structure_components = self.structure.components

				self.TopLevel = MainTopLevel(self)
				self.TopLevel.window = None
				self.TopLevel_window = None
				self.TopLevel_components = self.TopLevel.components

				self.ScrollFrame = MainScrollFrame(self)
				self.ScrollFrame.window = None
				self.ScrollFrame_window = None
				self.ScrollFrame_components = self.ScrollFrame.components

				# &FRAMES
			def run(self):
				for widget in self.structure_components['root_window']:
					self.main_components[widget.__name__] = widget(self.main)
					self.main_window.add_widget(**self.main_components[widget.__name__].widget)
				self.main_window.setup()
				self.main_window.run()

			def show_TopLevel(self):
				self.TopLevel.widget['master'] = self.main_window
				if self.TopLevel.widget['type'] == 'toplevel':
					self.main_window.add_toplevel(**self.TopLevel.widget)
				else:
					self.main_window.add_frame(**self.TopLevel.widget)
				self.TopLevel.window = self.main_window.containers[self.TopLevel.widget['id']]
				self.TopLevel_window = self.TopLevel.window
				for widget in self.structure_components['TopLevel']:
					self.TopLevel_components[widget.__name__] = widget(self.TopLevel)
					self.TopLevel_window.add_widget(**self.TopLevel_components[widget.__name__].widget)

			def show_ScrollFrame(self):
				self.ScrollFrame.widget['master'] = self.main_window
				if self.ScrollFrame.widget['type'] == 'toplevel':
					self.main_window.add_toplevel(**self.ScrollFrame.widget)
				else:
					self.main_window.add_frame(**self.ScrollFrame.widget)
				self.ScrollFrame.window = self.main_window.containers[self.ScrollFrame.widget['id']]
				self.ScrollFrame_window = self.ScrollFrame.window
				for widget in self.structure_components['ScrollFrame']:
					self.ScrollFrame_components[widget.__name__] = widget(self.ScrollFrame)
					self.ScrollFrame_window.add_widget(**self.ScrollFrame_components[widget.__name__].widget)

			# &SHOWFRAME

Heres what everything means.

The **show** methods:
    Sometimes we want a frame or a toplevel window to not be visible initially, maybe the user needs to click a "settings" button that
    causes the toplevel to pop-up. Thats what these methods are for. For each frame/toplevel you create, you will have a show_ID       	     method. When this method is called, the window/frame will be built. 
	**What if I want the Frame/Toplevel to show up when the application is initially started?**
	Simple, just add:
	
	.. code-block:: python
	
	    self.show_ScrollFrame()
	between the
	
	.. code-block:: python
	
	    self.main_window.setup()
	and the 
	
	.. code-block:: python
	
	    self.main_window.run()
	lines in the run() method.

**Templates and Main Classes**
The entire project is built to keep the locations/sizes/etc of widgets/windows seperated from the code that places them and tells them
what to do. Each frame or window has a dictionary of all it's components. These components are the buttons/dropdowns/etc that the frame owns. This is where the self.master.master line of code comes along. For Widgets contained on the main window, the direct master of those widgets is the class contained in the MainGuiTemplate.py file. The master of the class conatined in MainGuiTemplate.py (MainTemplate() class) is the Gui() class which is the class in MainGui().

If a widget is owned by a frame, or a toplevel widget, the layout is very similar. The master of the widget is the toplevel itself, and the master of that toplevel is the Gui() class. This means that to access a function from the Gui() class, no matter what frame/window
you are in, you can use:

.. code-block:: python

    self.master.master.Some_Function_I_Want()

The last piece of the puzzle is linking widgets together. Lets say that we wanted to make it so Button3 which is contained on the ScrollFrame called Button2 which is contained on the TopLevel when it was clicked.
For this the code looks a bit strange, but the nice thing is that the structure remains the same. The one important thing to keep in 
mind is the way the class names are created. If I give something a Widget ID of Button2, the class name inside the Button_Button2.py file will be Button2Button, likewise a DropDown named "Thing" has a class name of ThingDropDown.

So knowing that
1. Button2 is owned by TopLevel
2. Button2 has a class of ButtonButton2
3. The function called when Button2 is clicked is Button2_button_go()

The code written inside the Button3_button_go() method to simulate a click of Button2 would be

.. code-block:: python

    self.master.master.TopLevel_components["ButtonButton2"].Button2_button_go()

This might look a bit tricky, but keep in mind that although the line seems complex, the self.master.master is simply accessing the MainGui, which means it's essentially the same as just self.TopLevel_Components["ButtonButton2"].Button2_button_go()
In the future there are plans to implement an alias accross the board for the main window, perhaps something like:

.. code-block:: python

    self.w = self.master.master
Which turns that nasty long line into:

.. code-block:: python

    self.w.TopLevel_components["ButtonButton2"].Button2_button_go()
	

I've built all the logic, so what's next?
--------

To run the application simply run the __main__.py file inside the Project! Lets say you want to ship the application as a standalone application. That's actually pretty simple. 

Make a new directory with whatever you want the project to be named. Inside that directory, you want to put 2 things.

1. Place the Project directory (GuiBuilder/PROJECTS/Project_I_Want_To_Ship) inside the new directory.
2. Place the MyPyWidgets directory (GuiBuilder/MyPyWidgets) inside the new directory.

And you are done!
