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


