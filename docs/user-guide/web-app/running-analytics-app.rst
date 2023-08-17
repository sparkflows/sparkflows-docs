Running Analytical App
==========

Once the Analytical App has been created, they can be executed.

This document explains in detail the steps required to execute Analytical App.

Step 1 : Open Applications Page
----------

#. Open the Project where the Analytical App is located.
#. Click the **Applications** to open the Applications Page.

    .. figure:: ../../_assets/web-app/run-app/app-page.png
       :alt: web-app
       :width: 65%

Step 2 : Start the Application Execution
----------

#. Click the **Run App** button located on the application card.

     .. figure:: ../../_assets/web-app/run-app/play-run-option.png
        :alt: web-app
        :width: 65%
   
Step 3 : Go Through Various Stages
-------------

Clicking on the Run App button would take you to the various stages of the Application. Below are the examples of various stages.

**Upload Stage**
+++++

In this Stage, you need to upload files. To upload :

#. Click **browse** and choose the file you want to upload to Databricks.

   Alternatively, you can simply drag and drop the file here.

   **Note :** Maximum file size allowed to upload is 1GB. 

      .. figure:: ../../_assets/web-app/run-app/run-stages.png
         :alt: web-app
         :width: 65%

#. Enter the **destination path** in the Destination Path Column.

   This is the location where your file will be uploaded.

      .. figure:: ../../_assets/web-app/run-app/upload-file.png
         :alt: web-app
         :width: 65%

   **Note :** 
   
   * If the path is missing in DBFS, it creates the folder and uploads the file. 

   * If no path is specified, it stores the file in the default **FileStore** folder.


#. Click the **Upload** button to upload the file to DBFS and see the CSV file data in tabular format. 

   **Note :** This dialog box will display the first 30 records.

       .. figure:: ../../_assets/web-app/run-app/file-info.png
          :alt: web-app
          :width: 65%

   **Note :** If match API columns were added during the upload, this dialog box will allow users to select and map fields to the columns using the dropdown list.

       .. figure:: ../../_assets/web-app/run-app/select-field.png
          :alt: web-app
          :width: 65%

   **Note :** When user selects fields but missed to map required columns then it will throw error as shown below :


       .. figure:: ../../_assets/web-app/run-app/error-notification.png
          :alt: web-app
          :width: 65%

   After successful mapping of fields, it will send the selected fields in comma separated format to the notebook.

   If field is not selected then, it will send blank data in comma separated format to the notebook.

#. You can browse DBFS and check if the file got uploaded successfully. To Check :
    
   Place the cursor on the **DATA** tab located in the top bar menu and click **DBFS**.

        .. figure:: ../../_assets/web-app/run-app/dbfs.png
           :alt: web-app
           :width: 65%

   On the DBFS Home page, simply search for the uploaded file name, and it will appear if the upload was successful.

        .. figure:: ../../_assets/web-app/run-app/search-file.png
           :alt: web-app
           :width: 65%
   
#. Click the **Next** button to move to the next stage.


**Parameter Stage**
+++++++

#. On this stage, Select the parameters of your interest.

   **Note :** Regardless of whether you click the **Back** or **Next** button, the selected value will persist, but you can modify it if necessary.

        .. figure:: ../../_assets/web-app/run-app/parameter-stage.png
           :alt: web-app
           :width: 65%
  

#. Click the **Next** button to move to the next stage.


**Run Stage**
+++++

#. Click the **Run** button to execute the app and view the results.

        .. figure:: ../../_assets/web-app/run-app/execute.png
           :alt: web-app
           :width: 65%

   **Note :**

     * In the Run stage you will execute the Analytics App with the added parameters in the previous stages.

     * You can click the **Back** button and change the value and run Analytics App again.

    
Step 4 : View Execution Results History
---------

Fire enables you to view execution history of each analytical app. To view, follow the steps given below :

#. Go to the **applications** page.
#. Click on the **View App** icon located in the action column to reach the **execution history** page.

        .. figure:: ../../_assets/web-app/run-app/view-execute-history.png
           :alt: web-app
           :width: 65%

   
#. Click on any of the **item or name** listed under **Activities History** column to view the execution result.

        .. figure:: ../../_assets/web-app/run-app/execute-name.png
           :alt: web-app
           :width: 65%





  

   


   












