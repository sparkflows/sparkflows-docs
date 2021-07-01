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


   
   
   
   
