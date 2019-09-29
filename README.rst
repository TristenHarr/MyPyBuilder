=====
MyPyBuilder
=====

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





