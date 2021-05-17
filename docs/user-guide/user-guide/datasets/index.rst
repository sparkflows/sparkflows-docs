
Datasets
====

Fire Insights allows you to define your datasets. These datasets are then used in workflows as data sources. Dataset sources can be local file systems when running in local mode, or HDFS & HIVE when running on a Spark cluster.

**Schema**
 
  * Datasets have schema defined for them. This allows Fire Insights to read and create a DataFrame out of it. The DataFrame is then used for transforms, machine learning, etc.
 
**File formats**
 
  * Fire Insights supports various File formats and is able to infer the schema. These include ``CSV/TSV, Parquet, Avro, JSON, XML`` files.
  * Fire Insights also supports creating datasets from ``HIVE`` tables. This is not necessary because the Workflows HIVE Processors can be directly connected to specific HIVE tables (instead of creating a Dataset in Fire for them).


**Dataset Listing Page**

When you open any application, all existing Datasets specific to the application are displayed in the Datasets tab.

 .. figure:: ../../../_assets/tutorials/dataset/1.PNG
   :alt: Dataset
   :width: 90%
  

 
 
.. toctree::
   :maxdepth: 2

   creating-datasets.rst
   
   
