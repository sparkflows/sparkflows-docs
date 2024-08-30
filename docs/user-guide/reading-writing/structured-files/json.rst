JSON
========
Below is a sample workflow which contains the Read JSON processor in Fire Insights. It demonstrates the usage of the Read JSON node to read a JSON file.

It does the following processing of data:

*	Reads incoming dataset in JSON File format using the Read JSON node.
* 	Prints the content of JSON file using the Print node.

.. figure:: ../../_assets/user-guide/read-write/read-structured/read-JSON-WF.png
   :alt: readjson_node_userguide
   :width: 50%
   

**Read JSON node configuration**

The Read JSON node is configured as below.

*	A ``JSON Data File`` needs to be selected in the ``Path``. The ``Browse HDFS`` option can be used to browse and select a JSON file from HDFS.
*	If a record data in the JSON file is present in multiple lines then ``Multiline`` needs to be selected as ``True``.
*	Once a JSON file is selected the ``Refresh Schema`` button needs to be clicked to list Schema defined in the ``JSON Data File``. 
*	``OK`` button needs to be clicked to complete the configuration.

.. figure:: ../../_assets/user-guide/read-write/read-structured/json_config.PNG
   :alt: readjson_node_userguide
   :width: 70%

**Read JSON node output**

Data read from JSON File is printed as below using the Print node.

.. figure:: ../../_assets/user-guide/read-write/read-structured/json_output.PNG
   :alt: readjson_node_userguide
   :width: 70%
