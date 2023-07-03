Export and Import Analytical Apps
=======================

Fire enables you to export your Analytical App and download them to your computer. It then also enables you to import your Analytical App back into any instance of Fire. This is useful when you need to move or copy your Analytical App from one environment to another. 

This document explains in detail the steps required to export and import Analytical Apps.

Exporting Analytical App
--------

Fire allows you to export Analytical App and download them to your computer. To export, follow the below steps :

Step 1 : Go to the Analytical Apps Page
..................

#. Open the **project** where your Analytical App is located.
#. Click on the **Applications** tab.

Step 2 : Export the App
..............

#. Click on the **Export App** button located next to the app that is to be exported.

   .. figure:: ../../_assets/web-app/export-import/export-button.png
      :alt: web-app
      :width: 65%
     
   Fire will now export Analytical App and download them to your computer as JSON file.

   .. figure:: ../../_assets/web-app/export-import/app-download.png
      :alt: web-app
      :width: 65%
     
Importing Analytical App
--------

Fire allows you to import Analytical App. To import, follow the below steps :

Step 1 : Go to the Analytical Apps Page
.............

#. Open the **project** where you want to import Analytical App.
#. Click on the **Applications** tab.

Step 2 : Import the App 
...............

**Import the App Using Import Option :**

#. Click on the **Import** button. From the dropdown list, choose **Import** from the dropdown list.
    
   .. figure:: ../../_assets/web-app/export-import/import-button.png
      :alt: web-app
      :width: 65%
    
#. In the Upload JSON File window, browse and choose or drop the JSON file from your computer to Import from. 
   
   You must have downloaded this JSON file from Fire during the export process.
  
   .. figure:: ../../_assets/web-app/export-import/browse-file.png
      :alt: web-app
      :width: 65%

#. Choose Import options from three options available :

   * Overwite application if same key exists in the application.
   * Create a new key if one already exists.
   * Create a new key.

   .. figure:: ../../_assets/web-app/export-import/upload-json-file.png
      :alt: web-app
      :width: 65%

   **Note:** We have chosen the second option. 
    
#. Click on the **Import** button. You can see the imported app in Analytical App page.

   .. figure:: ../../_assets/web-app/export-import/app-import.png
      :alt: web-app
      :width: 65%

**Import the App Using Import into Databricks Option :**

#. Click on the **Import** button. From the dropdown list, choose **Import into databricks** from the dropdown list.
   
   .. figure:: ../../_assets/web-app/export-import/import-button.png
      :alt: web-app
      :width: 65%

#. In the Upload JSON File window, browse and choose or drop the JSON file from your computer to Import from. 
   
   You must have downloaded this JSON file from Fire during the export process.
  
   .. figure:: ../../_assets/web-app/export-import/databricks-browse-file.png
      :alt: web-app
      :width: 65%

#. Choose either of the Import by Key options from three options available :

   * Overwite application if same key exists in the application.
   * Create a new key if one already exists.
   * Create a new key.

   **Note:** We have chosen the first option.  

#. Choose either of the Import by JobID options from the three options available :

   * **Existing JobID in Analytical Apps :**

     .. figure:: ../../_assets/web-app/export-import/job-id1.png
        :alt: web-app
        :width: 65%
  
   **Note :** Analytical App is imported with existing jobId present in exported JSON file.
   
   * **Use Existing Job with Matching Notebook Path If Exists or Create a New Job :**

     In this condition user can enter notebook path in the input box or else it will check from exported json file whether databricks job is present or not. 

     If matching job is present that Job is used else new job is created with that notebook path using current connection.

     .. figure:: ../../_assets/web-app/export-import/job-id2.png
        :alt: web-app
        :width: 65%

   * **Create New Job with Notebook Path :**

     In this condition, the user can enter the notebook path in the input box.
     
     Otherwise, it will take the notebook path from the exported file to create a new Databricks job using the current connection.

     .. figure:: ../../_assets/web-app/export-import/job-id3.png
        :alt: web-app
        :width: 65%

#. Click on the **Import** button. Fire will now import the Analytical App to the specified location.

 




  




