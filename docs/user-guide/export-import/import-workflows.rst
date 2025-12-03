Import Workflows
===============

Sparkflows enables you to import workflows as JSON files. These JSON files can be exported to use in another instance of Sparkflows.

Below are the steps for importing a workflow.

Steps for Importing Workflow
-------

1. You can Login to Sparkflows Web server URL and follow the below steps:

     * Go to the Project List page.
     * Select the project to import workflows to. 
     * Click on the Workflows tab.

   You will land on a page similar to below:

   .. figure:: ../../_assets/user-guide/export-import/wf_list.PNG
      :alt: userguide
      :width: 70%


2. Now, click the **Import** button and select **From Workflow JSONs**.

   .. figure:: ../../_assets/user-guide/export-import/wf_import_file.PNG
     :alt: userguide
     :width: 70%  
 

Once you select ``From Workflow JSONs``, it will display a pop up where you can upload workflow JSON/s files from your local computer and select any one of the option depending on workflow availablity in that project with UUIDs, the available options are listed below:

Import Configuration
-----------------

1. When importing to an existing Project, there are 3 possible options to choose from:

     * **Overwrite workflow if same UUID exists in the project**

       In this case, if matching UUIDs are found, the existing project will be removed and replaced with the uploaded file. 

     * **Create a new UUID if one already exists**

       In this case, if matching UUIDs are found, the uploaded file will be assigned a new UUID.

     * **Create a new UUID**

       In this case, the uploaded file will always be assigned a new UUID.

   .. figure:: ../../_assets/user-guide/export-import/wf_import_json.PNG
     :alt: userguide
     :width: 60%   
     
2. Once you click on ``Import``, the workflow should be available in workflow list page of specific project.

   .. figure:: ../../_assets/user-guide/export-import/wf_imported.PNG
     :alt: userguide
     :width: 70%   
     
.. note:: Make sure that data pointed to the workflow JSON File should be available on new instance of Sparkflows where you are importing.     
