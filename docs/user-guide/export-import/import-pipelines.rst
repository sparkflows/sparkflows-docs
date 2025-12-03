Import Pipelines
==============

Sparkflows enables you to import Pipelines as JSON files. These JSON files can be exported to use in another instance of Sparkflows. 

Below are the steps for importing a Pipeline.

Steps for Importing a Pipeline
-------

1. You can Login to Sparkflows Web server URL and follow the below steps:

     * Go to the Project List page.
     * Select the project to import Pipeline to. 
     * Click the Pipeline tab.

   You will land on a page similar to below:

   .. figure:: ../../_assets/user-guide/export-import/pipeline_list.PNG
     :alt: userguide
     :width: 70%


2. Now, click the ``Import`` button, as shown below:

   .. figure:: ../../_assets/user-guide/export-import/pipeline_import_page.PNG
     :alt: userguide
     :width: 70%  
 
 
   It will take you to new window, where you can upload Pipeline JSON file from your local Computer and select any one of the option depending on Pipelines availablity in that project with UUIDs, the available options are listed below:

Import Pipelines Configuration
-----------------

1. When importing to an existing Project, there are 3 possible options to choose from:
   
     * **Overwrite pipeline if same UUID exists in the project**

       In this case, if matching UUIDs are found, the existing project will be removed and replaced with the uploaded file.

     * **Create a new UUID if one already exists**

       In this case, if matching UUIDs are found, the uploaded file will be assigned a new UUID. 

     * **Create a new UUID**

       In this case, the uploaded file will always be assigned a new UUID.

  .. figure:: ../../_assets/user-guide/export-import/pipeline_import_file.PNG
          :alt: userguide
          :width: 60%  

2. On clicking the **Import** button, a success message will get displayed.

  .. figure:: ../../_assets/user-guide/export-import/pipeline_import_success.png
     :alt: userguide
     :width: 60% 

  Now, the pipeline should be available in Pipelines list page of specific project.

  .. figure:: ../../_assets/user-guide/export-import/pipeline_imported.PNG
     :alt: userguide
     :width: 70%   
     
.. note:: Make sure that data pointed to the Pipeline JSON File should be available on new instance of Sparkflows where you are importing.

