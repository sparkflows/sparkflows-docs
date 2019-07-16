PDFImageOCR
=========== 

Reads in PDF Files from a given path, extracts the images from them and converts them to text with Tesseract

Input
--------------
It reads in a PDF file or a directory containing PDF files

Output
--------------
It creates a DataFrame from the data read and sends it to its output

Type
--------- 

dataset

Class
--------- 

fire.nodes.dataset.NodeDatasetPDFImageOCR

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - path
        - Path of the PDF files
        - Path of the PDF file/directory
      * - fileNameCol
        - File Name Column
        - File Name Column in the Output DataFrame
      * - outputCol
        - Column Name which contains the result of OCR
        - OCR output Column in the Output DataFrame




