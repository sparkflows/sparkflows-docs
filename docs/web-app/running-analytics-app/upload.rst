Upload 
==============

- Browse files you want to upload to databricks.

- Add destination path of dbfs where you want to upload choose file.

- If added path is not there in dbfs then it will first create the folder in dbfs and then upload the file. If no path is added it will store inside ``FileStore`` folder

  .. figure:: ../../_assets/web-app/upload-file-1.PNG
        :alt: web-app
        :width: 60%

- Then, click on upload button to upload to DBFS and see the csv file data in tabular format. Modal will show first 30 records.

  .. figure:: ../../_assets/web-app/upload-file-2.PNG
          :alt: web-app
          :width: 60%

- You can browse dbfs and check if the file uploaded successfully.

  .. figure:: ../../_assets/web-app/upload-file-3.PNG
          :alt: web-app
          :width: 60%

- If match api columns are added in upload stage then, on upload below dialog will appear where user can select fields and map columns.

  .. figure:: ../../_assets/web-app/upload-file-4.png
          :alt: web-app
          :width: 60%

- When, user select fields but missed to map required columns then it will throw error like below. 

  .. figure:: ../../_assets/web-app/upload-file-5.PNG
          :alt: web-app
          :width: 60%

- After successfully mapping of fields it will send selected fields in comma separated to notebook.
- If field is not selected then, it will send blank data in comma separated format to notebook. 

- Click on "NEXT" button to go to next stage.
