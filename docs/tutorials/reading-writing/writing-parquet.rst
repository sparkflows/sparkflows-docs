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


Node ``TransactionDataset`` creates Dataframe of your dataset named 'Transaction Dataset' by reading data from HDFS, HIVE etc. which had been defined earlier in Fire by using the Dataset feature. 
As a user you just have to select the Dataset of your interest and configure the details as shown below.



.. figure:: ../../_assets/tutorials/read-write/writing-parquet/NodeDatasetStructured.PNG
   :alt: NodeDatasetStructured
   :align: center
   :width: 60%

SaveParquet Processor Configuration
-----------------------------------

``SaveParquet`` node saves dataframe into the specified path in Parquet Format. When running on Hadoop, Parquet files gets saved into HDFS.


.. figure:: ../../_assets/tutorials/read-write/writing-parquet/SaveParquet.PNG
   :alt: SaveParquet
   :align: center
   :width: 60%



