Mongodb
==========

Fire Insights has a processor that allows you to connect with Mongodb.


Workflow for Reading Data from MongoDB
---------------------------------------

The below workflow reads data in MongoDB and then prints the data.


.. figure:: ../../_assets/tutorials/mongodb/reads_mongodb.PNG
   :alt: ReadMongoDB
   :width: 70%

Below is the image that displays the dialog box for the ReadMongoDB Processor.

.. figure:: ../../_assets/tutorials/mongodb/Readmongodbprocessor.PNG
   :alt: ReadMongoDB
   :width: 90%
   
In the above dialog box, the ``Refresh Schema`` button infers the schema of the collections. Thus, it is able to pass down the output schema to the next Processor making it easy for us to build the workflow.   
   
Workflow Execution
------------------

When we execute the workflow, it reads in the sample collection from MongoDB and displays the first few lines.

We see that the sample data records that we wrote to MongoDB in the first/above workflow is read back now.

.. figure:: ../../_assets/tutorials/mongodb/workflowexecutionreadmongodb.PNG
   :alt: ReadMongoDB
   :width: 90%



Workflow for Loading data into MongoDB
---------------------------------------

The below workflow reads in the sample dataset which is in CSV format from HDFS. It then saves the data into MongoDB.

.. figure:: ../../_assets/tutorials/mongodb/save_mongo_db.PNG
   :alt: SaveMongoDB
   :width: 70%

The below image shows the dialog box for the SaveMongoDB Processor.

.. figure:: ../../_assets/tutorials/mongodb/savemongodbprocessor.PNG
   :alt: SaveMongoDB
   :width: 90%
   
Workflow Execution
------------------

When we execute the above workflow, it reads in the dataset from HDFS and loads it into the MongoDB.

.. figure:: ../../_assets/tutorials/mongodb/workflowexecutionsavemongodb.PNG
   :alt: SaveMongoDB
   :width: 90%
   
  
