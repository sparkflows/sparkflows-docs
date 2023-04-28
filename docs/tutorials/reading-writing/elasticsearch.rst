Read and Write ElasticSearch
======================================

Elastic Search is often used for indexing, searching and analyzing datasets. Fire Insights makes it easy to read data from Elastic Search, clean and transform it as needed.

Elasticsearch-hadoop provides native integration between Elasticsearch and Apache Spark. In the example below, we will first load data from HDFS into Elastic Search and then read it back into Apache Spark from Elastic Search.

If your data is already in Elastic Search, skip to "Workflow for Reading data from Elastic Search". 



Loading data into Elastic Search
---------------------------------

Create a new empty workflow. Drag and drop the source dataset from which you want to load data into Elastic Search. If you don't have a dataset for the source data, create one. 

Once the source processor is on the workflow canvas, drag and drop "Save ElasticSearch" processor in the workflow. Configure your Elastic Search processor in the dialog box shown below.

.. figure:: ../../_assets/tutorials/dataset/EsCofig.PNG
   :alt: Dataset
   :width: 60%


After configuring "Save ElasticSearch" processor, connect your data source processor to Elastic Search processor.


The sample workflow below reads a Housing Dataset which is in CSV format from HDFS. The 'Save ElasticSearch' takes in the incoming data and loads it into the Elastic Search Index 'sparkflows/housing'.


.. figure:: ../../_assets/tutorials/dataset/save-elastic-wf.png
   :alt: Dataset
   :width: 60%


Workflow Execution
------------------


When the sample workflow above is executed, it reads in the dataset from HDFS and saves it into Elasticsearch.


.. figure:: ../../_assets/tutorials/dataset/20.PNG
   :alt: Dataset
   :width: 60%


Reading data from Elastic Search
----------------------------------


Reading data from Elastic Search is easy. Drag and drop 'ReadElasticSearch' processor into your workflow and configure it.
The screenshot below shows the dialog box for the Elastic Search Read Processor.


.. figure:: ../../_assets/tutorials/dataset/22_a.PNG
   :alt: Dataset
   :width: 60%  
 
 
In the dialog above, 'Refresh Schema' button infers the schema of the index. Thus, it is able to pass down the output schema to the next processor making it easy to build workflows.


The SQL field specifies the SQL to be used for reading from Elastic Search. It allows you to limit the columns of interest, and apply clauses etc.


The Elastic Search Processor understands the SQL and translates it into the appropriate QueryDSL. The connector pushes down the operations directly to the source, where the data is efficiently filtered out so that only the required data is streamed back to Spark. This significantly increases the query performance and minimizes the CPU, memory and I/O operations on both Spark and Elastic Search Clusters.


The sample workflow below reads the data from the sparkflows/housing index in Elastic Search and prints out the first few lines.


.. figure:: ../../_assets/tutorials/dataset/read-elastic-wf.png
   :alt: Dataset
   :width: 60%


Workflow Execution
------------------


When the sample workflow above is executed, it reads in the index from Elastic Search and displays the first few lines.


.. figure:: ../../_assets/tutorials/dataset/23.PNG
   :alt: Dataset
   :width: 60%


   
   
   
   
