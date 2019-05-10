Reading and Writing from MongoDB
================================

MongoDB is a document database with the scalability and flexibility that you want with the querying and indexing that you need, Here we are loading data from HDFS  and Saving it into MongoDB.

Workflow for Loading data into MongoDB
---------------------------------------

The below workflow reads in the Sample Dataset which is in CSV format from HDFS.

It then saves the data into MongoDB.


.. figure:: ../../_assets/tutorials/mongodb/Savemongodb.PNG
   :alt: SaveMongoDB
   :align: center
   :width: 60%

The below diagram shows the dialog box for the SaveMongoDB Processor.

.. figure:: ../../_assets/tutorials/mongodb/savemongodbprocessor.PNG
   :alt: SaveMongoDB
   :align: center
   :width: 60%
   
Workflow Execution
------------------

When we execute the Workflow, it reads in the dataset from HDFS and loads it into MongoDB.

.. figure:: ../../_assets/tutorials/mongodb/workflowexecutionsavemongodb.PNG
   :alt: SaveMongoDB
   :align: center
   :width: 60%

   
