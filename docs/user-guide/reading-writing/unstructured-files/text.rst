Text Files
==========
This node reads the content of a single text file or multiple text files from a directory.

Below is a sample workflow which contains the Text Files processor in Fire Insights. It demonstrates the usage of Text Files node to read the content of Text files from a given path. Data from all the files would be displayed together in a single column. Each line of data in the files would represent one record in the output.

It does the following processing of data:

*	Reads incoming dataset using the Text Files node. Dataset can belong to a single file or a set of files from a directory.
* 	Print the contents of all Text Files in a single outgoing dataset using the Print Node. Each line of data in the Text Files would be listed as a record in output.

.. figure:: ../../../_assets/user-guide/read-write/read-unstructured/read-text-WF.png
   :alt: readtextfiles_node_userguide
   :width: 50%
   

**Text Files Node Configuration**

The Text Files node is configured as below.

*	``Path``: Select a Text file or path of a directory containing multiple Text files. The ``Browse HDFS`` option can be used to browse and select a Text file or a directory from HDFS.
*	``OUTPUT COLUMN NAME``: Enter column name to list Text files' content in the output.
*	``OK`` button needs to be clicked to complete the configuration.

.. figure:: ../../../_assets/user-guide/read-write/read-unstructured/readtextfiles-configuration.png
   :alt: readtextfiles_node_userguide
   :width: 70%

**Text Files Node Output**

Data read from Text files is printed as below using the Print node. Data from all files will be displayed together in a single column. Each line of data in the files would represent one record in the output.

.. figure:: ../../../_assets/user-guide/read-write/read-unstructured/readtextfiles-printnode-output.png
   :alt: readtextfiles_node_userguide
   :width: 70%
