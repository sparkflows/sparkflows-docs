PDF
=====

Below is a sample workflow which contains the PDF processor in Fire Insights. It demonstrates the usage of PDF node to read the content of PDF files from a given path.

It does the following processing of data:

*	Reads incoming dataset using the PDF node.
* 	Print PDF files along with their content using the Print Node. Output is displayed in file name and its content pair.

.. figure:: ../../../_assets/user-guide/read-write/read-unstructured/read-pdf-WF.png
   :alt: readpdf_node_userguide
   :width: 50%
   

**PDF node configuration**

The PDF node is configured as below.

*	A PDF file or path of a directory containing PDF files needs to be selected in the ``Path``. The ``Browse HDFS`` option can be used to browse and select a PDF file or a directory from HDFS.
*	Column name to list file name in output needs to be entered in the ``File Name``.
*	Column name to list file content in output needs to be entered in the ``File Content``.
*	``OK`` button needs to be clicked to complete the configuration.

.. figure:: ../../../_assets/user-guide/read-write/read-unstructured/PDF-Config.png
   :alt: readpdf_node_userguide
   :width: 70%

**PDF node output**

Data read from PDF files is printed as below using the Print node. Output is displayed in the file name and its content pair.

.. figure:: ../../../_assets/user-guide/read-write/read-unstructured/PDF-Output.png
   :alt: readpdf_node_userguide
   :width: 70%
