Create Dataset on Parquet Files
=====================

Fire Insights supports reading from several file formats including Parquet Files. Parquet Files have schema embedded in them. Fire Insights is able to extract schema of Parquet Files automatically.

Datasets
--------

The existing datasets are displayed in the DataSets page of specific application.

.. figure:: ../../_assets/tutorials/dataset/DatasetsDetails.png
   :alt: Dataset
   :width: 100%
   
Dataset Creation
----------------

Navigate to the "Datasets" tab in your application where you want to create a new dataset. Click on the "Create" button and choose the dataset type from the pop-up. It will navigate you to create dataset page of type Parquet. Now we create a dataset for people.parquet. It is a Parquet File.

.. figure:: ../../_assets/tutorials/dataset/CreateDatasetParquet.png
   :alt: Dataset
   :width: 100%

In the ‘Create DataSet’ page fill in the required fields as below.

.. figure:: ../../_assets/tutorials/dataset/DatasetFormParquet.png
   :alt: Dataset
   :width: 100%

Specify the name of the dataset you are creating.

After specifying name and path, click the ‘Update Sample Data Schema’ button. This brings up the sample data, extracts the schema and displays it. Below we see that there are 2 fields : Label and Text. Label is of type double and text is of type string.


.. figure:: ../../_assets/tutorials/dataset/SampleDatasetParquet.png
   :alt: Dataset
   :width: 100%
   
Clicking the ‘Save’ button creates the new DataSet for us.

.. figure:: ../../_assets/tutorials/dataset/SaveDatasetParquet.png
   :alt: Dataset
   :width: 100%

Now you are ready to use the dataset in your workflows.
