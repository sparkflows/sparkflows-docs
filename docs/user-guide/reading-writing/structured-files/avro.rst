Avro 
======

Below is a sample workflow which contains the Read Avro processor in Fire Insights. It demonstrates the usage of the Read Avro node to read an Avro Data file.

It does the following processing of data:

*	Reads incoming dataset in the Avro Data File format using the Read Avro node.
* 	Prints the content of Avro file using the Print node.


.. figure:: ../../_assets/user-guide/read-write/read-structured/Avro-WF.png
   :alt: readavro_node_userguide
   :width: 50%
   

**Read Avro node configuration**

The Read Avro node is configured as below.

*	An ``Avro Data File`` needs to be selected in the ``Path``. The ``Browse HDFS`` option can be used to browse and select an Avro file from HDFS.
*	Once an Avro file is selected the ``Refresh Schema`` button needs to be clicked to list Schema defined in the ``Avro Data File``.
*	``OK`` button needs to be clicked to complete configuration.

.. figure:: ../../_assets/user-guide/read-write/read-structured/AvroConfig.png
   :alt: readavro_node_userguide
   :width: 70%

**Read Avro node output**

Data read from an ``Avro Data File`` is printed as below using the Print node.

.. figure:: ../../_assets/user-guide/read-write/read-structured/AvroOutput.png
   :alt: readavro_node_userguide
   :width: 70%
