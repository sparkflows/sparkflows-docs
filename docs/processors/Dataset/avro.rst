
ReadAvro
========== 

Dataset Node for reading Avro files

Input
---------- 

It reads in Avro files

Output
---------- 

It creates a DataFrame from the data read and sends it to its output

Type
---------- 

dataset

Class
---------- 

fire.nodes.dataset.NodeDatasetAvro

Fields
---------- 

+------------------+----------------------------+---------------------------------+
| Name             | Title                      | Description                     |
+==================+============================+=================================+
| path             | Path                       | Path of the Avro file/directory |
+------------------+----------------------------+---------------------------------+
| outputColNames   | Column Names for the CSV   | New Output Columns of the SQL   |
+------------------+----------------------------+---------------------------------+
| outputColTypes   | Column Types for the CSV   | Data Type of the Output Columns |
+------------------+----------------------------+---------------------------------+
| outputColFormats | Column Formats for the CSV | Format of the Output Columns    |
+------------------+----------------------------+---------------------------------+