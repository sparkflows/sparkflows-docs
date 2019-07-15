Reading CSV Files
=================

Here we create a DataSet over CSV files. Sparkflows is able to automatically infer the schema. Sparkflows uses the spark-csv library from Databricks for it.

Datasets
--------

The existing Datasets are displayed in the Datasets page of Specific application


.. figure:: ../../_assets/tutorials/dataset/1.PNG
   :alt: Dataset
   :align: center
   :width: 60%
   
Dataset Creation
----------------
 
- We now create a dataset over housing.csv file. It is a comma separated file. It also has a header row specifying the names for the various columns   


.. figure:: ../../_assets/tutorials/dataset/2.PNG
   :alt: Dataset
   :align: center
   :width: 60%
   
- In the ‘Create CSV DataSet’ page we will fill in the required fields as below.   


.. figure:: ../../_assets/tutorials/dataset/3.PNG
   :alt: Dataset
   :align: center
   :width: 60%
   
- Above we have specified a name for the DataSet we are creating, ‘Header’ is set to true indicating that the file has a header row, field delimiter is comma and we have also specified the path to the file.

- Once we have specified the above, we hit the ‘Update’ button. This brings up the sample data, infers the schema and displays it. We can change the column names and also the data types. Format column is used for specifying the format for date/time fields.

.. figure:: ../../_assets/tutorials/dataset/4.PNG
   :alt: Dataset
   :align: center
   :width: 60%

