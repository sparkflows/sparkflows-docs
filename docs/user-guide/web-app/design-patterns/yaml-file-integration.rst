YAML File Integration 
============

Fire allows you to integrate YAML files in your analytical app. 

Follow the steps given below to enable YAML file integration in your analytical app.

Step 1 : Open Configurations Page
-----------
#. Login to Fire Insights.
#. From the Dashboard page, click on the **ADMINISTRATION** tab.
#. From the Administration page, click on the **Configurations** option.

Step 2 : Configure YAML File Path
--------------

#. In the **APP** tab search for ``app.applicationConfigurationPath`` option.
#. Click on the **edit** icon located next to the above option.
#. Enter the YAML file path in the given box.
#. Click on the **Save Configurations** button to save the configured path.

      .. figure:: ../../../_assets/web-app/yaml-file-integration/path-config.png
         :alt: web-app
         :width: 70%

Additional Information 
++++++++++++

* Once you have added the YAML file path, your analytical app will dynamically show or hide elements based on the configuration you provided.

      .. figure:: ../../../_assets/web-app/yaml-file-integration/app-display.png
         :alt: web-app
         :width: 70%


* All columns are read from configuration file but **customer_name** column is used to match the group which belongs to selected current connection and **instance_permissible_purpose** column name is used to match the use case added in analytical app.

      .. figure:: ../../../_assets/web-app/yaml-file-integration/edit-app.png
         :alt: web-app
         :width: 70%




.. note:: #. Valid condition should be added to show Analytical App. 

          #. Use case is mandatory field to show Analytical App.

          #. Condition is disabled to user for editing if current user doesn’t have admin rights and is not the owner of Analytical App.

          #. Below are the conditions which we can use :

              * instance_bundles.Core.enabled == 1 (instance_bundles is column name)
              * visual_designer.enabled > 1
              * instance_region == ‘global’ && instance_bundles.Core.enabled == 1
              * instance_region == ‘global’ || instance_bundles.Core.enabled > 1
              * instance_region != ‘global’


