Writing to JSON Files
=====================

Fire Insights enables you to write your DataFrame to JSON Files.


Workflow for writing to JSON file
----------------------


.. figure:: ../../_assets/tutorials/read-write/writing-json/Capture1.png
   :alt: JSONWorkflow
   :width: 60%
   

Reading From Dataset
----------------------

Node ``TransactionDataset`` creates DataFrame of your dataset named 'Transaction Dataset' by reading data from HDFS, HIVE etc. which had been defined earlier in Fire by using the Dataset feature. As a user you just have to select the Dataset of your interest and configure the details as shown below.


.. figure:: ../../_assets/tutorials/read-write/writing-json/Capture2.png
   :alt: NodeDatasetStructured
   :align: center
   :width: 60%


SaveJSON Processor Configuration
--------------------


Node ``SaveJSON`` saves DataFrame into the specified path in JSON Format. When running on Hadoop, JSON files gets saved into HDFS.

   
.. figure:: ../../_assets/tutorials/read-write/writing-json/Capture3.png
   :alt: JSONWorkflow
   :width: 60%
