Configs Support in Analytical Apps
==================================

Step 1 : Setting-up the Application
-------------------------------

#. Create an analytical application and add stages to it.
   
   .. figure:: ../../_assets/web-app/configs-support/create-app.png
      :alt: web-app
      :width: 65%

#. Create a stage with different components like textfield, select, button and so on.

   .. figure:: ../../_assets/web-app/configs-support/create-stage.png
      :alt: web-app
      :width: 65%

#. Now, click on the **Add/Select configuration** icon.

   .. figure:: ../../_assets/web-app/configs-support/select-config-btn.png
      :alt: web-app
      :width: 65%

#. After clicking on the Add/Select configuration icon, click on the **Add Config** button to add the App configuration with their properties.

   .. figure:: ../../_assets/web-app/configs-support/add-config.png
      :alt: web-app
      :width: 65%

   .. figure:: ../../_assets/web-app/configs-support/add-config1.png
      :alt: web-app
      :width: 65%
   
   **NAME:** Add a name for configuration.
   
   **SELECT TYPE:** Choose type (textfield, select, select boxes, button, checkbox, radio) from the dropdown.
   
   **PROPERTY NAME:** Add the same property name which is given to a specific component while creating a stage in an application whose configuration needs to be overridden.

   .. figure:: ../../_assets/web-app/configs-support/property-name.png
      :alt: web-app
      :width: 65%
   
   **VALUES:** Add Values which need to be overridden for a given property name of a specified component. 
   
   .. NOTE:: Add comma separated values for select or select boxes or radio type.
   
   **LABEL:**  Add a Label which needs to be overridden for a given property name of a specified component.
   
   **DEFAULT VALUE:**  Add default value which needs to be overridden for a given property name of a specified component.
   
   .. NOTE:: Add comma separated default values for select (if Multiple Value property is checked in that specific component) or select boxes type.

#. After adding the above properties, the configuration window would look like the image given below. Next, click on the **Save** button.

   .. figure:: ../../_assets/web-app/configs-support/edit-config.png
      :alt: web-app
      :width: 65%


#. After saving the app configuration, it would be seen as a list in the App Config popup as shown below.

   .. figure:: ../../_assets/web-app/configs-support/config-list.png
      :alt: web-app
      :width: 65%


Step 2 : Actions on the App Configurations
----------------------------------------

#. To select or deselect the app configuration, click on the **Star** icon.

   .. figure:: ../../_assets/web-app/configs-support/star-icon.png
      :alt: web-app
      :width: 65%

#. Click on the **Edit** icon to edit the selected app configuration.

   .. figure:: ../../_assets/web-app/configs-support/edit.png
      :alt: web-app
      :width: 65%

#. Click on the **Delete** icon to delete the selected app configuration.

   .. figure:: ../../_assets/web-app/configs-support/delete.png
      :alt: web-app
      :width: 65%

Step 3 : Running the Application
--------------------------------

#. If no app configuration is selected, default form will be loaded. 

   .. figure:: ../../_assets/web-app/configs-support/run-1.png
      :alt: web-app
      :width: 65%

#. If a specific app configuration is selected, form will be loaded based on the properties added in configuration.

   .. figure:: ../../_assets/web-app/configs-support/run-2.png
      :alt: web-app
      :width: 65%






