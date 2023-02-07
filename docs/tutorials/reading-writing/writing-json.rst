Save as JSON Files
=====================

Fire Insights enables you to write your DataFrame to JSON Files.


Workflow for writing as JSON files
----------------------


.. figure:: ../../_assets/tutorials/read-write/writing-json/SaveJSON.png
   :alt: JSONWorkflow
   :width: 45%
   

Reading from dataset
----------------------

Node ``TransactionDataset`` creates DataFrame of your dataset named 'Transaction Dataset' by reading data from HDFS, HIVE etc. which have been defined earlier in Fire by using the Dataset feature. As a user you just have to select the Dataset of your interest and configure the details as shown below.


.. figure:: ../../_assets/tutorials/read-write/writing-json/7.PNG
   :alt: NodeDatasetStructured
   :width: 80%

Processor output
----------------

.. figure:: ../../_assets/tutorials/read-write/writing-json/8.PNG
   :alt: NodeDatasetStructured
   :width: 80%

SaveJSON Processor Configuration
--------------------


Node ``SaveJSON`` saves DataFrame into the specified path in JSON Format. When running on Hadoop, JSON files gets saved into HDFS.

   
.. figure:: ../../_assets/tutorials/read-write/writing-json/9.PNG
   :alt: JSONWorkflow
   :width: 80%

Once the workflow is executed successfully the json file will be saved to specified location.

.. figure:: ../../_assets/tutorials/read-write/writing-json/10.PNG
   :alt: JSONWorkflow
   :width: 80%
