CSV
======

Below is a sample workflow which contains the Read CSV processor in Fire Insights. It demonstrates the usage of Read CSV File node to read a CSV file.

It does the following processing of data:

*	Reads incoming dataset in CSV Data format using the Read CSV node.
* 	Prints the content of the CSV file using the Print node.

.. figure:: ../../_assets/user-guide/read-write/read-structured/CSV_WF.png
   :alt: readcsv_node_userguide
   :width: 50%
   

**Read CSV Node configuration**

The Read CSV node is configured as below.

*	A ``CSV Data File`` needs to be selected in the ``Path``. The ``Browse HDFS`` option can be used to browse and select a CSV file from HDFS.
*	A Delimiter or Character used to separate two columns' data needs to be selected in the ``Separator``. In most of the cases ``,`` / comma is used to separate two columns.
*	``Header`` needs to be selected as ``True`` or ``False`` based on whether data file contains header row that can be used in the imported dataset.
*	Once a CSV file is selected the ``Refresh Schema`` button needs to be clicked to list Schema defined in the ``CSV Data File``. 
*	``OK`` button needs to be clicked to complete the configuration.

.. figure:: ../../_assets/user-guide/read-write/read-structured/CSVConfig.png
   :alt: readcsv_node_userguide
   :width: 70%

**Read CSV node output**

Data read from a CSV Data File is printed as below using the Print node.

.. figure:: ../../_assets/user-guide/read-write/read-structured/CSVOutput.png
   :alt: readcsv_node_userguide
   :width: 70%
   
