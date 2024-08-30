PDF Image OCR
===================
This node reads the content of OCR image embedded in a PDF file and converts it to Text.

Below is a sample workflow which contains the PDF Image OCR processor in Fire Insights. It demonstrates the usage of the PDF Image OCR node to read content of OCR image embedded in a PDF file and converts it to Text.

It does the following processing of data:

*	Reads the content of OCR image embedded in a PDF file and converts it to Text using the PDF Image OCR node.
*	Prints the content of OCR image embedded in a PDF file in text format.

.. figure:: ../../../_assets/user-guide/read-write/read-unstructured/PDF-Image-WF.png
   :alt: readwrite_userguide
   :width: 50%
   
**PDF Image OCR node configuration**

PDF Image OCR node is configured as below.

*	Path of the PDF file needs to be entered in the ``Path Of The PDF Files`` box.
*	Column in the output to display file name is to be entered in the ``File Name Column`` box.
*	Column in the output to display content of the file is to be entered in the ``Column Name Which Contains Result of OCR`` box.
*	Output prints the content of OCR image embedded in a PDF file in text format.

.. figure:: ../../../_assets/user-guide/read-write/read-unstructured/PDFImageConfig.png
   :alt: readwrite_userguide
   :width: 70%
   
**PDF Image OCR node output**

Output of the PDF Image OCR node prints the content of OCR image embedded in a PDF file in text format.

.. figure:: ../../../_assets/user-guide/read-write/read-unstructured/pdfocr-printnode-output.png
   :alt: readwrite_userguide
   :width: 70%       	    
