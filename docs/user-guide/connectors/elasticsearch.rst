Elasticsearch
================

Fire Insights has a processor that allows you to connect with elasticsearch.

Reading from Elasticsearch
================

Reading data from Elastic Search is easy. Drag and drop 'ReadElasticSearch' processor into your workflow and configure it.

Elastic Search Read Processor Configuration
---------------

The screenshot below shows the dialog box for the Elastic Search Read Processor.

.. figure:: ../../_assets/tutorials/dataset/22_a.PNG
   :alt: Dataset
   :width: 90%  
 
 
In the dialog above, 'Refresh Schema' button infers the schema of the index. Thus it is able to pass down the output schema to the next processor making it easy to build workflows.


The SQL field specifies the SQL to be used for reading from Elastic Search. It allows you to limit the columns of interest, and apply clauses etc.


The Elastic Search Processor understands the SQL and translates it into the appropriate QueryDSL. The connector pushes down the operations directly to the source, where the data is efficiently filtered out so that only the required data is streamed back to Spark. This significantly increases the query performance and minimizes the CPU, memory and I/O operations on both Spark and Elastic Search Clusters.


Workflow
---------

The example workflow below reads the data from the sparkflows/housing index in Elastic Search and prints out the first few lines.


.. figure:: ../../_assets/tutorials/dataset/21_a.PNG
   :alt: Workflow
   :width: 70% 


Workflow Execution
------------------


When the example workflow above is executed, it reads in the index from Elastic Search and displays the first few lines.


.. figure:: ../../_assets/tutorials/dataset/23.PNG
   :alt: Workflow Execution
   :width: 90%
   

Writing to Elasticsearch
======================================

Elastic Search is often used for indexing, searching and analyzing datasets. Fire Insights makes it easy to write data to Elastic Search.

Elasticsearch-hadoop provides native integration between Elasticsearch and Apache Spark. In the example below, we will first load data from HDFS into Elastic Search and then read it back into Apache Spark from Elastic Search.

If your data is already in Elastic Search, skip to "Workflow for Reading data from Elastic Search". 



Workflow
-----------

Create a new empty workflow. Drag and drop the source dataset from which you want to load data into Elastic Search. If you don't have a dataset for the source data, create one. 

Once the source processor is on the workflow canvas, drag and drop "SaveElasticSearch" processor in the workflow. Configure your Elastic Search processor in the dialog box shown below.

.. figure:: ../../_assets/tutorials/dataset/EsCofig.PNG
   :alt: Dataset
   :width: 90%


After configuring "SaveElasticSearch" processor, connect your data source processor to Elastic Search processor.


The example workflow below reads a Housing Dataset which is in CSV format from HDFS. The 'SaveElasticSearch' takes in the incoming data and loads it into the Elastic Search Index 'sparkflows/housing'.


.. figure:: ../../_assets/tutorials/dataset/esworkflow.PNG
   :alt: Dataset
   :width: 70%


Workflow Execution
------------------


When the workflow above is executed, it reads in the dataset and saves it into Elasticsearch.


.. figure:: ../../_assets/tutorials/dataset/20.PNG
   :alt: Dataset
   :width: 90%
   
   
