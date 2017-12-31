
Join Using SQL
^^^^^^ 

This node registers the incoming DataFrames as temporary tables and executes the SQL provided

type

join

nodeClass

fire.nodes.etl.NodeJoinUsingSQL

Fields

+------------------+----------------------------+---------------------------------+
| Name             | Title                      | Description                     |
+==================+============================+=================================+
| tempTable1       | Temp Table1                | Temp Table Name to be used      |
+------------------+----------------------------+---------------------------------+
| tempTable2       | Temp Table2                | Temp Table Name to be used      |
+------------------+----------------------------+---------------------------------+
| sql              | SQL                        | SQL to be run                   |
+------------------+----------------------------+---------------------------------+
| outputColNames   | Column Names for the CSV   | New Output Columns of the SQL   |
+------------------+----------------------------+---------------------------------+
| outputColTypes   | Column Types for the CSV   | Data Type of the Output Columns |
+------------------+----------------------------+---------------------------------+
| outputColFormats | Column Formats for the CSV | Format of the Output Columns    |
+------------------+----------------------------+---------------------------------+