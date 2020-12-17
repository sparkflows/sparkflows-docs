Writing to Parquet Files
========================

Fire Insights enables you to write your Dataframe to Parquet Files.


Workflow for writing to Parquet file
----------------

Below is a workflow example which reads in transaction data. It then writes it out to Parquet files.


.. figure:: ../../_assets/tutorials/read-write/writing-parquet/Parquet_workflow.PNG
   :alt: ParquetWorkflow
   :align: center
   :width: 60%
   
   
DatasetStructured Processor
--------------------------
   
Node ``TransactionDataset`` creates a Dataframe of your dataset named ``Transaction Dataset`` by reading data from HDFS, HIVE etc. which had been defined earlier in Fire by using the Dataset feature.

As a user you have to select the Dataset of your interest as shown below.


.. figure:: ../../_assets/tutorials/read-write/writing-parquet/NodeDatasetStructured.PNG
   :alt: NodeDatasetStructured
   :align: center
   :width: 60%


SaveParquet Processor
---------------------

``SaveParquet`` processor saves the incoming DataFrame into the specified path in Parquet Format. When running on Hadoop, Parquet files gets saved into HDFS.

The DataFrame might be written as multiple part files in the specified folder, depending on the size and partition of the DataFrame.


.. figure:: ../../_assets/tutorials/read-write/writing-parquet/SaveParquet.PNG
   :alt: SaveParquet
   :align: center
   :width: 60%



