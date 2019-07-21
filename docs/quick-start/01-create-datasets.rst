Step 3 : Create Dataset
=========================

Before any data can be used in a workflow, it needs to be wrapped in a dataset. If you uploaded csv files in the previous step, in this step you will wrap them in a dataset. 

The steps involved in creating a dataset are:

  - *Open the Application where you want to create dataset*
  - *Click on "Datasets" tab*
  - *Click on "Create" and choose "Dataset"*
  - *Select your dataset type and enter the fields in the dialog*
  - *Update the schema of the Dataset*
  - *Click "Save"*
  
 When you open your application, all existing datasets specific to the application are displayed in the Datsets tab.
 
 .. figure:: ../_assets/tutorials/dataset/1.PNG
   :alt: Dataset
   :align: center
   :width: 60%

 Click on "Create" and choose "Dataset" from the dropdown. 
 
 .. figure:: ../_assets/tutorials/dataset/10.PNG
   :alt: Dataset
   :align: center
   :width: 60%

 
 In the pop-up choose “CSV” and then click “OK”.
 
 In the screenshot below, we create a dataset from a housing.csv file. It is a comma separated file with a header row specifying the names of the various columns.
 
 .. figure:: ../_assets/tutorials/dataset/2.PNG
   :alt: Dataset
   :align: center
   :width: 60%
   


Fill in the required fields as below.

- *NAME* : Name of the New Dataset we are creating.
- *DESCRIPTION** : Description of the new dataset
- *HAS HEADER ROW* : Indicate whether the dataset has a header row specifying the name of the columns or not
- *DELIMITER* : Indicates the delimiter to be used between the fields in the data
- *PATH** : Path for the location of the file or directory containing the data files for the dataset


 
 .. figure:: ../_assets/tutorials/dataset/3.PNG
   :alt: Dataset
   :align: center
   :width: 60%
 
 
- Update the Schema of the Dataset


Now click on ``Update`` to update the Schema of the Dataset. It would display sample data for the dataset followed by the Schema.

In this case, the data file did not have a header row. So Fire gave it standard column names of ``C0, C1`` etc.

You can update the column names in the schema based on your data.
 
 .. figure:: ../_assets/tutorials/dataset/4.PNG
   :alt: Dataset
   :align: center
   :width: 60%
  

Now click on "Save' to save the new dataset and you are ready to use it in your workflows.







 
 
 
 
 
 
 
 



