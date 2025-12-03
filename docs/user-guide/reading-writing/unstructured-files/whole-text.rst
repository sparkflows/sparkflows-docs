Whole Text Files
==================
This node reads the list of Text Files and their content from a directory and lists them in File Name and File Content pair.

Below is a sample workflow which contains the Whole Text Files processor in Sparkflows. It demonstrates the usage of the Whole Text Files node to read list of Text Files and their contents from a given path and list them in the File Name and File Content pair.

It does following processing of data:

*	Reads incoming Dataset using the Whole Text Files node.
* 	Prints output in the file name and its content pair using the Print Node.

.. figure:: ../../../_assets/user-guide/read-write/read-unstructured/whole-text-WF.png
   :alt: readwholetext_node_userguide
   :width: 50%
   

**Whole Text Files Node Configuration**

The Whole Text Files node is configured as below.

*	``PATH``: Select the path of a directory containing the Text files. The ``Browse HDFS`` option can be used to browse and select a directory from HDFS.
*	``OK`` button needs to be clicked to complete the configuration.

.. figure:: ../../../_assets/user-guide/read-write/read-unstructured/readwholetext-configuration.png
   :alt: readwholetext_node_userguide
   :width: 70%

**Whole Text Files Node Output**

List of Text Files along with their contents is printed as below using the Print node. Output is printed in the File Name and File Content pair.

.. figure:: ../../../_assets/user-guide/read-write/read-unstructured/readwholetext-printnode-output.png
   :alt: readwholetext_node_userguide
   :width: 70%
