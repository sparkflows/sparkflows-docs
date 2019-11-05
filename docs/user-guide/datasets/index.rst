
Datasets
====

Fire Insights allows you to define your DataSets. These DataSets are then used in Workflows as data sources. DataSet sources can be local file system when running in local mode, or HDFS & HIVE when running on a Spark cluster.

**Schema**
 
  * DataSets have Schema defined for them. This allows Fire Insights to read and create a DataFrame out of it. The DataFrame is then used for transforms, machine learning etc.
 
**File formats**
 
  * Sparkflows supports various File formats and is able to infer the schema. These include ``CSV/TSV, Parquet, Avro, JSON, XML`` files.
  * Sparkflows also supports creating datasets from ``HIVE`` tables. This is not necessary as in the Workflows HIVE Processors it can be directly connected to specific HIVE tables (instead of creating a Dataset in Fire for them).


**Dataset Listing Page**

When you open any application, all existing Datasets specific to the application are displayed in the Datasets tab.

 .. figure:: ../../_assets/tutorials/dataset/1.PNG
   :alt: Dataset
   :align: center
   :width: 60%
  

 
 
.. toctree::
   :maxdepth: 2

   creating-datasets.rst
   
   
