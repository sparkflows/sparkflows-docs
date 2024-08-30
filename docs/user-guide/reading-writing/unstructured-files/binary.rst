Binary Files
============
This node reads content of a Binary File and converts it to Text.

Below is a sample workflow which contains the Binary Files processor in Fire Insights. It demonstrates the usage of the Binary Files node to read content of a Binary file.

It does the following processing of data:

*	Reads the content of a Binary File using the Binary Files node. In this example it reads a png image file having an OCR image.
*	Parses the content using the OCR node and converts it to text.
*	Prints the content of Binary file in text format.

.. figure:: ../../../_assets/user-guide/read-write/read-unstructured/read-binary-WF.png
   :alt: readwrite_userguide
   :width: 50%
   
**Binary Files node configuration**

The Binary Files node is configured as below.

*	Path of the Binary file needs to be selected in the ``Path`` box.
*	Column in the output to display the file name is to be entered in the ``File Name Column`` box.
*	Column in the output to display the content of the file is to be entered in the ``Binary File Content Column`` box.
*	Output prints the content of the Binary file in text format.

.. figure:: ../../../_assets/user-guide/read-write/read-unstructured/binaryfiles-config.png
   :alt: readwrite_userguide
   :width: 70%
   
**Binary Files node output**

Output of Binary Files node prints content of Binary Image file in text format.

.. figure:: ../../../_assets/user-guide/read-write/read-unstructured/binaryfiles-printnode-output.png
   :alt: readwrite_userguide
   :width: 70%     
