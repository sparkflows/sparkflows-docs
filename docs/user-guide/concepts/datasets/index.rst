
Datasets
====

Fire Insights allows you to define your datasets. These datasets are then used in workflows as data sources. Dataset sources can be local file systems when running in local mode, HDFS & HIVE when running on a Apache Spark cluster, or Snowflake among other external connections.

**Schema**
 
  * Datasets have schema defined for them. This allows Fire Insights to read and create a DataFrame out of it. The DataFrame can then undergo multiple transforms, machine learning models can be built on it, etc.


 
**File Formats**
 
  * Fire Insights supports various file formats and is able to infer the schema. These include ``CSV/TSV, Parquet, Avro, JSON, XML`` files.
  * Fire Insights also supports creating datasets from ``HIVE`` tables. This is not necessary because the Workflows HIVE Processors can be directly connected to specific HIVE tables (instead of creating a dataset in Fire for them).


**Dataset Listing Page**

When you open any application, all existing datasets specific to the application are displayed in the 'Datasets' tab.

 .. figure:: ../../../_assets/tutorials/dataset/DatasetListing.png
   :alt: Dataset
   :width: 75%
  

 
 
.. toctree::
   :maxdepth: 2

   creating-datasets.rst
   
   
