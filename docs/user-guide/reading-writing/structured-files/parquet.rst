Parquet
========
Below is a sample workflow which contains Read Parquet processor in Fire Insights. It demonstrates usage of Read Parquet node to read a Parquet file.

It does following processing of data:

*	Reads incoming Dataset in Parquet Data File format using Read Parquet node.
* 	Prints the content of Parquet file using Print node.

.. figure:: ../../_assets/user-guide/read-write/read-structured/Parquet-WF.png
   :alt: readparquet_node_userguide
   :width: 50%
   

**Read Parquet node configuration**

The Read Parquet node is configured as below.

*	A ``Parquet Data File`` needs to be selected in the ``Path``. The ``Browse HDFS`` option can be used to browse and select a Parquet file from HDFS.
*	Once a Parquet file is selected the ``Refresh Schema`` button needs to be clicked to list Schema defined in the ``Parquet Data File``. 
*	``OK`` button needs to be clicked to complete the configuration.

.. figure:: ../../_assets/user-guide/read-write/read-structured/ParquetConfig.png
   :alt: readparquet_node_userguide
   :width: 70%

**Read Parquet node output**

Data read from a Parquet Data File is printed as below using the Print node.

.. figure:: ../../_assets/user-guide/read-write/read-structured/ParquetOutput.png
   :alt: readparquet_node_userguide
   :width: 70%
