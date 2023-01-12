Create Dataset on CSV Files
=================

When working with data in Fire Insights, the first step is to create a dataset that you plan to process subsequently. Dataset is a wrapper around your data which makes it easy to handle it in Sparkflows workbench.

When datasets are created, Fire Insights automatically infers the schema using Spark-CSV library from Databricks.

Datasets List
--------

When you open any application, all existing Datasets specific to the application are displayed in the Datasets tab.


.. figure:: ../../_assets/tutorials/dataset/DatasetsDetails.png
   :alt: Dataset
   :width: 90%
   
Dataset Creation
----------------
 
Choose type of Dataset to Create
+++++++++++++++++++++++++++++++++

Navigate to the "Datasets" tab in your application. Click on the "Create" button and choose "Dataset".
In the pop-up choose "CSV" and then click "OK".

.. figure:: ../../_assets/tutorials/dataset/CreateDataSet.png
   :alt: Dataset
   :width: 90%

Dataset Details
+++++++++++++++

Clicking "OK" will take you to Dataset Details page where you can enter information about your dataset. In the screenshot below, we create a dataset from a Clickthru.csv file. It is a comma separated file with a header row specifying the names of the various columns.   


.. figure:: ../../_assets/tutorials/dataset/DatasetFileContentView.png
   :alt: Dataset
   :width: 90%
   
For the Clickthru.csv file, we will fill in the required fields as below.   


.. figure:: ../../_assets/tutorials/dataset/DataSetForm.png
   :alt: Dataset
   :width: 90%
   
We specified a name for the dataset we are creating. ‘Header’ is set to true indicating that the file has a header row, field delimiter is comma and we also specified the path to the file.

Update Sample data/schema
++++++++++++++++++++++++++

Once we have specified the above, we hit the ‘Update Sample data/schema’ button. This brings up the sample data, infers the schema and displays it. We can change the column names and also the data types. Format column is used for specifying the format for date/time fields.

.. figure:: ../../_assets/tutorials/dataset/DataSetSchemaUpdate.png
   :alt: Dataset
   :width: 90%


.. figure:: ../../_assets/tutorials/dataset/SampleDataset.png
   :alt: Dataset
   :width: 90%


Save the Dataset
++++++++++++++++

Clicking the ‘Save’ button creates the new dataset. The dataset is now ready for use in any workflow within the specific application.

.. figure:: ../../_assets/tutorials/dataset/SaveDataset.png
   :alt: Dataset
   :width: 90%
   
You can find your created dataset in dataset list page.
  
.. figure:: ../../_assets/tutorials/dataset/CreatedDatasetList.png
   :alt: Dataset
   :width: 90%  
