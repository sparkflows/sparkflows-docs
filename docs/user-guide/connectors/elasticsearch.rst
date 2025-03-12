Elasticsearch
==========

Elasticsearch is a powerful, distributed search and analytics engine. Fire Insights offers a set of processors that enable reading and writing data using Elasticsearch. 

Follow the steps below to configure and use these connectors effectively.

Read Elastic Search
---------------------------------------

* Read Elastic Search connector can be used to **read data using Elasticsearch**. 
* It reads a collection of documents hosted on a server and assigns index to them to facilitate search capability. 
* It reads the index from Elasticsearch.

**Configure Read Elasticsearch connector** 
+++++++++++++++++++++++++++++++++++++++++++++++
To configure it, define the following connection details, as shown below:

 .. figure:: ../../_assets/tutorials/elasticsearch/elasticsearch-read.png
    :alt: Connectors
    :width: 65%

* **Index Name:** Enter a name for the collection of documents. It is a logical namespace that maps to a collection of documents having similar characteristics. Each document within an index is stored as a JSON object.  
* **Elastic Search Host:** Enter network address of the machine or server where Elasticsearch is running.
* **Elastic Search Port:** Enter the network port detail used by the Elasticsearch to listen to the incoming connection requests.
* **Spark Temporary Table For Reading From ES:** Enter name of the Spark Temporary Table to be used to fetch ES data from.
* **SQL For Reading From Elastic Search:** Enter the SQL Statement to be used to read data from the Spark Temp Table.
* Click on **Refresh Schema** button to fetch the selected table schema. It infers the schema and pass it on to the next processor for further processing.
* Then click on **Okay** button.

.. note:: The SQL field specifies the SQL to be used for reading from Elastic Search. It allows you to limit the columns of interest, and apply clauses etc. 
 
The Elasticsearch Processor understands the SQL and translates it into the appropriate QueryDSL. The connector pushes down the operations directly to the source, where the data is efficiently filtered out so that only the required data is streamed back to Spark. This significantly increases the query performance and minimizes the CPU, memory and I/O operations on both the Spark and Elastic Search Clusters.

Save Elastic Search
------------------

* Save Elastic Search connector can be used to **save data using Elasticsearch**.
* Elasticsearch is often used for indexing, searching and analyzing datasets. 
* Fire Insights makes it easy to write data to Elasticsearch. 
* **Elasticsearch-hadoop** provides native integration between Elasticsearch and Apache Spark.

**Configure Save Elastic Search connector**
+++++++++++++++++++++++++++++++++++++++++++++
To configure it, define the following connection details, as shown below:

 .. figure:: ../../_assets/tutorials/elasticsearch/elasticsearch-save.png
    :alt: Connectors
    :width: 65%

* **Index Name:** Enter a name for the collection of documents where data will be saved. It is a logical namespace that maps to a collection of documents having similar characteristics. Each document within an index is stored as a JSON object.  
* **Elastic Search Host:** Enter network address of the machine or server where Elasticsearch is running.
* **Elastic Search Port:** Enter the network port detail used by the Elasticsearch to listen to the incoming connection requests.
* **ES Index Auto Create:** Enter **True** or **False**. It indicates whether indices can be automatically created when you index documents if the index does not already exist.
* **ES Nodes WAN Only:** Enter **True** or **False**. It indicates whether it is for WAN-only node. WAN-only node typically refers to a node that is part of a cluster but is only intended to handle external (WAN) traffic, as opposed to local (LAN) traffic within the cluster.
* **ES Nodes Ingest Only:** Enter **True** or **False**. It indicates whether it is for Ingest-only node. Ingest nodes are responsible for preprocessing and transforming documents before they are indexed. 
* **ES Nodes Data Only:**  Enter **True** or **False**. It indicates whether it is for Data-only node. Data nodes are responsible for storing and managing data. They handle data indexing and search operations.
* **ES Net Http Auth User:** Enter **username** to access the host.
* **ES Net Http Auth Pass:** Enter **password** to access the host.
* **Key-Value Pairs:** Enter key-value pair refering to the way data is structured and stored in documents within an index.

Workflow
------------------

* A sample workflow to read and save data using Elasticsearch can be created as shown below. It uses the **Elasticsearch nodes** to read and write data.
* This workflow transforms data before saving the data using Elasticsearch.

 .. figure:: ../../_assets/tutorials/elasticsearch/elasticsearch-workflow.png
    :alt: Connectors
    :width: 65%
   
