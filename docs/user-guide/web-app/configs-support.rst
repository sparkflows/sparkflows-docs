Configs Support in Analytical Apps
==================================

Step 1 : Setting-up the Application
-------------------------------

#. Create an analytical application and add stages to it.
#. Create a stage with different components like textfield,select,button and so on.
#. Now, click on the Add/Select configuration icon.
#. After clicking on the Add/Select configuration icon, click on the Add Config button to add the App configuration with their properties.

   NAME : Add a name for configuration.
   SELECT TYPE : Choose type(textfield,select,select boxes,button,checkbox,radio) from the dropdown.
   PROPERTY NAME : Add the same property name which is given to a specific component while creating a stage in an application whose configuration needs to be overridden.
   VALUES : Add Values which need to be overridden for a given property name of a specified component. 
   NOTE: Add comma separated values for select or select boxes or radio type
   LABEL:  Add a Label which needs to be overridden for a given property name of a specified component.
   DEFAULT VALUE:  Add default value which needs to be overridden for a given property name of a specified component.
   NOTE: Add comma separated default values for select(if Multiple Value property is checked in that specific component) or select boxes type

#. After Adding the above properties in configuration it would look like below and then click on Save button.
#. After saving app configuration it would be seen as a list in the App Config popup.


Step 2 : Actions on the App Configurations
----------------------------------------

#. To select or deselect the app configuration, click on the Star icon.
#. Click on the Edit icon to edit selected app configuration.
#. Click on the Delete icon to delete selected app configuration.

Step 3 : Running the Application
--------------------------------

#. If no app configuration is selected, default form will be loaded. 
#. If a specific app configuration is selected, form will be loaded based on the properties added in configuration.






