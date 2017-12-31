
PDFImageOCR
========== 

Reads in PDF Files from a given path, extracts the images from them and converts them to text with Tesseract

Type
---------- 

dataset

Class
---------- 

fire.nodes.dataset.NodeDatasetPDFImageOCR

Fields
---------- 

+-------------+----------------------------------------------+-------------------------------------------+
| Name        | Title                                        | Description                               |
+=============+==============================================+===========================================+
| path        | Path of the PDF files                        | Path of the PDF file/directory            |
+-------------+----------------------------------------------+-------------------------------------------+
| fileNameCol | File Name Column                             | File Name Column in the Output DataFrame  |
+-------------+----------------------------------------------+-------------------------------------------+
| outputCol   | Column Name which contains the result of OCR | OCR output Column in the Output DataFrame |
+-------------+----------------------------------------------+-------------------------------------------+