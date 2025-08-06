Binary Files
============
This node reads content of a Binary File and converts it to Text.

Below is a sample workflow which contains the Binary Files processor in Fire Insights. It demonstrates the usage of the Binary Files node to read content of a Binary file.

It does the following processing of data:

*	Reads the content of a Binary File using the Binary Files node. In this example it reads a PNG image file having an OCR image.
*	Parses the content using the OCR node and converts it to text.
*	Prints the content of Binary file in text format.

.. figure:: ../../../_assets/user-guide/read-write/read-unstructured/read-binary-WF.png
   :alt: readwrite_userguide
   :width: 50%
   
**Binary Files Node Configuration**

The Binary Files node is configured as below.

*	``PATH``: Select path of the Binary file in the box.
*	``FILE NAME COLUMN``: Enter the column name to display the file name in the output.
*	``BINARY FILE CONTENT COLUMN``:  Enter the column name to display the file content in the output.
*	Output prints the content of the Binary file in text format.

.. figure:: ../../../_assets/user-guide/read-write/read-unstructured/binaryfiles-config.png
   :alt: readwrite_userguide
   :width: 70%
   
**Binary Files Node Output**

Output of Binary Files node prints content of Binary Image file in text format.

.. figure:: ../../../_assets/user-guide/read-write/read-unstructured/binaryfiles-printnode-output.png
   :alt: readwrite_userguide
   :width: 70%     
