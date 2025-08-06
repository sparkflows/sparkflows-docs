PDF
=====
This node reads the content of single PDF file or multiple PDF files from a directory.

Below is a sample workflow which contains the PDF processor in Fire Insights. It demonstrates the usage of PDF node to read the content of PDF files from a given path.

It does the following processing of data:

*	Reads incoming dataset using the PDF node.
* 	Print PDF files along with their content using the Print Node. Output is displayed in file name and its content pair.

.. figure:: ../../../_assets/user-guide/read-write/read-unstructured/read-pdf-WF.png
   :alt: readpdf_node_userguide
   :width: 50%
   

**PDF Node Configuration**

The PDF node is configured as below.

*	``Path``: Select a PDF file or path of a directory containing PDF files. The ``Browse FileSystem`` option can be used to browse and select a PDF file or a directory from HDFS.
*	``FILE NAME``: Enter the column name to list file name in the output.
*	``FILE CONTENT``: Enter the column name to list file content in the output.
*	``Okay`` button needs to be clicked to complete the configuration.

.. figure:: ../../../_assets/user-guide/read-write/read-unstructured/PDF-Config.png
   :alt: readpdf_node_userguide
   :width: 70%

**PDF Node Output**

Data read from PDF files is printed as below using the Print node. Output is displayed in the file name and its content pair.

.. figure:: ../../../_assets/user-guide/read-write/read-unstructured/PDF-Output.png
   :alt: readpdf_node_userguide
   :width: 70%
