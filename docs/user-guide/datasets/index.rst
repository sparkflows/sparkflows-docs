
Datasets
====

Fire Insights allows you to define your DataSets. These DataSets are then used in Workflows as data sources. DataSet sources can be local file system when running in local mode, or HDFS & HIVE when running on a Spark cluster.

**Schema**
 
  * DataSets have Schema defined for them. This allows Sparkflows to create a Spark DataFrame from them in the workflows.
 
**File formats**
 
  * Sparkflows support various File formats and is able to infer the schema. These include ``CSV/TSV, Parquet, Avro, JSON, XML`` files.
  * Sparkflows also supports creating datasets from ``HIVE`` tables. This is not necessary as in the Workflows HIVE Processors can be directly connected to specific HIVE tables (instead of creating a Dataset in Fire for them).


**Dataset Listing Page**

The Dataset Listing Page displays all the Datasets created in Fire.

 .. figure:: ../_assets/tutorials/01/dataset-listings.png
   :alt: Dataset Listings
   :align: center
  

 
 
.. toctree::
   :maxdepth: 2

   creating-datasets.rst
   reading-from-rdbms.rst
   
   
