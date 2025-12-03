JSON
========

Read JSON
-------------
This node reads JSON files.

Below is a sample workflow which contains the Read JSON processor in Sparkflows. It demonstrates the usage of the Read JSON node to read a JSON file.

.. figure:: ../../../_assets/user-guide/read-write/read-structured/read-JSON-WF.png
   :alt: readjson_node_userguide
   :width: 50%
   
It does the following processing of data:

*	Reads incoming dataset in JSON File format using the Read JSON node.
* 	Prints the content of JSON file using the Print node.



**Read JSON Node Configuration**

The Read JSON node is configured as below.

*	``Path``: Select a **JSON Data File**. The **Browse HDFS** option can be used to browse and select a JSON file from HDFS.
*	``Multiline``: Select it as **True** if a record data in the JSON file is present in multiple lines.
*	``Refresh Schema``: Once a JSON file is selected click on **Refresh Schema** button to list Schema defined in the **JSON Data File**. 
*	``Okay``: To complete the configuration click this button.

.. figure:: ../../../_assets/user-guide/read-write/read-structured/json_config.PNG
   :alt: readjson_node_userguide
   :width: 70%

**Read JSON Node Output**

Data read from JSON File is printed as below using the Print node.

.. figure:: ../../../_assets/user-guide/read-write/read-structured/json_output.PNG
   :alt: readjson_node_userguide
   :width: 70%


Save JSON
----------------------------------------
This node saves the incoming dataset as JSON File.

Below is a sample workflow which contains the Save JSON processor in Sparkflows. It demonstrates the usage of Save JSON node to save the incoming dataset in JSON format.

.. figure:: ../../../_assets/user-guide/read-write/save-files/save-json-wf.png
   :alt: savefiles_userguide
   :width: 50%
   
It does the following processing of data:

*	Reads the incoming dataset.
*	Coalesce node is used to define the number of partitions to be created while saving.
*	Saves the incoming dataset in JSON format using the Save JSON node.


**Incoming Dataset**

.. figure:: ../../../_assets/user-guide/read-write/save-files/InputData.png
   :alt: savefiles_userguide
   :width: 75%
   
**Save JSON Node Configuration**

Save JSON node is configured as below.

General Tab

* ``Path``: Select the HDFS location where created file needs to be saved. 
* ``Save Mode``: Select a save mode from the dropdown list. It states whether to *Append*, *Overwrite*, *Error out if file exists* or *Ignore* while saving file.

  .. figure:: ../../../_assets/user-guide/read-write/save-files/JsonGenConfig.png
     :alt: savefiles_userguide
     :width: 75%
   
Advance Tab

* ``PARTITION COLUMN NAMES``: Select the set of columns that need to be used to partition data. One file would be created for each partition.
* Saves the incoming dataset in JSON format.


  .. figure:: ../../../_assets/user-guide/read-write/save-files/JsonAdvConfig.png
     :alt: savefiles_userguide
     :width: 75%
   
