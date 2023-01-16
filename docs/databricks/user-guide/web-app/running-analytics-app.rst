Running Analytics App
=====================

Once the Analytics App has been created, they can be executed.

Below are the steps for executing an Analytics App.

Click on Run App Button
-------------------------

  .. figure:: ../../_assets/web-app/view-app.PNG
        :alt: web-app
        :width: 80%

Go through the various Stages
----------------------------

  .. figure:: ../../_assets/web-app/view-app1.PNG
        :alt: web-app
        :width: 80%



Examples of the various Stage Pages
-------

1 : Upload 
++++++++++

- Browse files you want to upload to databricks.

- Maximum file size allowed to upload is 1GB.

- Add destination path of dbfs where you want to upload the selected files.

- If the specified path is not there in dbfs then it will first create the folder in dbfs and then upload the file. If no path is specified it will store it inside ``FileStore`` folder

  .. figure:: ../../_assets/web-app/upload-file-1.PNG
        :alt: web-app
        :width: 80%

- Then, click on upload button to upload to DBFS and see the csv file data in tabular format. Modal will show first 30 records.

  .. figure:: ../../_assets/web-app/upload-file-2.PNG
          :alt: web-app
          :width: 80%

- You can browse dbfs and check if the file uploaded successfully.

  .. figure:: ../../_assets/web-app/upload-file-3.PNG
          :alt: web-app
          :width: 80%

- If match api columns are added in upload stage then, on upload below dialog will appear where user can select fields and map columns.

  .. figure:: ../../_assets/web-app/upload-file-4.png
          :alt: web-app
          :width: 80%

- When, user selects fields but missed to map required columns then it will throw error like below. 

  .. figure:: ../../_assets/web-app/upload-file-5.PNG
          :alt: web-app
          :width: 80%

- After successfully mapping of fields it will send selected fields in comma separated to notebook.
- If field is not selected then, it will send blank data in comma separated format to notebook. 

- Click on "NEXT" button to go to next stage.

2 : Parameters 
++++++++++

- Select the parameters of your interest

- If you click on "BACK" or "NEXT" button the selected value will remain as it is and you can change it if needed

  .. figure:: ../../_assets/web-app/parameters-1.PNG
          :alt: web-app
          :width: 80%


- Click on "NEXT" button to move to next page

3 : Run 
++++++++++

- In this stage you will execute the Analytics App with the added parameters in the earlier stages.

- You can click on back button and change the value and run Analytics App again.

- Click on "RUN" button to execute the app and view the results.

  .. figure:: ../../_assets/web-app/run.PNG
          :alt: web-app
          :width: 80%




