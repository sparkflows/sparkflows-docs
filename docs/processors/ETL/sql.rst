
SQL
^^^^^^ 

This node runs the given SQL on the incoming DataFrame

type

transform

nodeClass

fire.nodes.etl.NodeSQL

Fields

+------------------+-----------------------+---------------------------------+
| Name             | Title                 | Description                     |
+==================+=======================+=================================+
| tempTable        | Temp Table            | Temp Table Name to be used      |
+------------------+-----------------------+---------------------------------+
| sql              | SQL                   | SQL to be run                   |
+------------------+-----------------------+---------------------------------+
| outputColNames   | Output Column Names   | Name of the Output Columns      |
+------------------+-----------------------+---------------------------------+
| outputColTypes   | Output Column Types   | Data Type of the Output Columns |
+------------------+-----------------------+---------------------------------+
| outputColFormats | Output Column Formats | Format of the Output Columns    |
+------------------+-----------------------+---------------------------------+