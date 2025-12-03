PDF Image OCR
===================
This node reads the content of OCR image embedded in a PDF file and converts it to Text.

Below is a sample workflow which contains the PDF Image OCR processor in Sparkflows. It demonstrates the usage of the PDF Image OCR node to read content of OCR image embedded in a PDF file and converts it to Text.

It does the following processing of data:

*	Reads the content of OCR image embedded in a PDF file and converts it to Text using the PDF Image OCR node.
*	Prints the content of OCR image embedded in a PDF file in text format.

.. figure:: ../../../_assets/user-guide/read-write/read-unstructured/PDF-Image-WF.png
   :alt: readwrite_userguide
   :width: 50%
   
**PDF Image OCR Node Configuration**

PDF Image OCR node is configured as below.

*	``PATH OF THE PDF FILES``: Enter the path of the PDF file in the box.
*	``FILE NAME COLUMN``: Enter the column name to display the file name in the output.
*	``COLUMN NAME WHICH CONTAINS THE RESULT OF OCR``: Enter the column name to display the file content in the output.
*	Output prints the content of OCR image embedded in a PDF file in text format.

.. figure:: ../../../_assets/user-guide/read-write/read-unstructured/PDFImageConfig.png
   :alt: readwrite_userguide
   :width: 70%
   
**PDF Image OCR Node Output**

Output of the PDF Image OCR node prints the content of OCR image embedded in a PDF file in text format.

.. figure:: ../../../_assets/user-guide/read-write/read-unstructured/pdfocr-printnode-output.png
   :alt: readwrite_userguide
   :width: 70%       	    
