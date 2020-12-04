Running Analytics App
=====================

Once the Analytics App has been created, they can be executed.

Below are the steps for executing an Analytics App.

Click on Analytics App Name to go to view Analytics App page
-------------------------

  .. figure:: ../_assets/web-app/view-app.PNG
        :alt: web-app
        :width: 60%

View all the stages depending upon index of added stages
----------------------------

  .. figure:: ../_assets/web-app/view-app1.PNG
        :alt: web-app
        :width: 60%



Examples of the various Stage Pages
-------

1 : Upload 
++++++++++

- Browse files you want to upload to databricks.

- Add destination path of dbfs where you want to upload choose file.

- If added path is not there in dbfs then it will first create thet folder in dbfs and then upload the file.

  .. figure:: ../_assets/web-app/upload-file-1.PNG
        :alt: web-app
        :width: 60%

- Then, click on upload button to upload to DBFS and see the csv file data in tabular format.

  .. figure:: ../_assets/web-app/upload-file-2.PNG
          :alt: web-app
          :width: 60%

- Can browse dbfs and check if the file uploaded successfully.

  .. figure:: ../_assets/web-app/upload-file-3.PNG
          :alt: web-app
          :width: 60%


- Click on "NEXT" button to go to next stage.

2 : Parameters 
++++++++++

- Select the parameters of your interest

- If we click on "BACK" or "NEXT" button the selected value will remain as it is and can change if wanted to.

  .. figure:: ../_assets/web-app/parameters-1.PNG
          :alt: web-app
          :width: 60%


- Click on "NEXT" button to move to next page

3 : Run 
++++++++++

- In this we will execute the Analytics App with the added parameters in the earlier stages.

- Can click on back button and change the value and can run Analytics App again.

- Click on "RUN" button and can see the results.

  .. figure:: ../_assets/web-app/run.PNG
          :alt: web-app
          :width: 60%




