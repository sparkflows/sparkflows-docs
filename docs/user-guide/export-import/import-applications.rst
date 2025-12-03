Import Applications
===============

Sparkflows enables you to import Applications as JSON files. These JSON files can be exported to use in another instance of Sparkflows.

Below are the steps for importing Applications.

Steps for Importing Applications
-------

1. You can Login to Sparkflows web server URL and follow below steps:

     * Go to the Project List page.
     * Select the project to import Applications to. 
     * Click on the Applications tab.

   You will land on a page similar to below:

   .. figure:: ../../_assets/user-guide/export-import/application_list_page.PNG
      :alt: userguide
      :width: 70%


2. Click on the ``Import`` button and select ``From Application JSON``.

   .. figure:: ../../_assets/user-guide/export-import/application_import_page.PNG
      :alt: userguide
      :width: 70%  
 

It will open a pop up where you can upload Application JSON file from your local computer and select any one of the option depending on Application availablity in that project with KEY, the available options are listed below:

Import Applications Configuration
-----------------

1. When importing to an existing Project, there are 3 possible options to choose from:
   
     * **Overwrite application if same key exists in the project**

       In this case, if the matching KEY is found, the existing project will be removed and replaced with the uploaded file.

     * **Create a new key if one already exists**

       In this case, if the matching KEY is found, the uploaded file will be assigned a new KEY.

     * **Create a new key**

       In this case, the uploaded file will always be assigned a new KEY.
   
   .. figure:: ../../_assets/user-guide/export-import/application_import_file.PNG
       :alt: userguide
       :width: 60%   
     
2. Once you click ``Import``, the Application should be available in Applications list page of specific project.

   .. figure:: ../../_assets/user-guide/export-import/application_imported.PNG
      :alt: userguide
      :width: 70%   
     
.. note:: Make sure that data pointed to the Application JSON File should be available on new instance of Sparkflows where you are Importing.
