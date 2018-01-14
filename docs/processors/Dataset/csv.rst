
ReadCSV
========== 

It reads in CSV files and creates a DataFrame from it

Input
---------- 

It reads in CSV text files

Output
---------- 

It creates a DataFrame from the data read and sends it to its output

Type
---------- 

dataset

Class
---------- 

fire.nodes.dataset.NodeDatasetCSV

Fields
---------- 

+------------------+----------------------------+---------------------------------+
| Name             | Title                      | Description                     |
+==================+============================+=================================+
| path             | Path                       | Path of the Text file/directory |
+------------------+----------------------------+---------------------------------+
| separator        | Separator                  | CSV Separator                   |
+------------------+----------------------------+---------------------------------+
| header           | Header                     | Does the file have a header row |
+------------------+----------------------------+---------------------------------+
| outputColNames   | Column Names for the CSV   | New Output Columns of the SQL   |
+------------------+----------------------------+---------------------------------+
| outputColTypes   | Column Types for the CSV   | Data Type of the Output Columns |
+------------------+----------------------------+---------------------------------+
| outputColFormats | Column Formats for the CSV | Format of the Output Columns    |
+------------------+----------------------------+---------------------------------+