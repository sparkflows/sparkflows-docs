
Jython
^^^^^^ 

This node runs any given Python code. The input dataframe is passed in the variable inDF. The output dataframe should be placed in the variable outDF

type

transform

nodeClass

fire.nodes.etl.NodeJython

Fields

+------------------+----------------------------+----------------------------------------------------------------------------------+
| outputColFormats | Column Formats for the CSV | Format of the Output Columns                                                     |
+==================+============================+==================================================================================+
| code             | Jython                     | Python code to be run. Input dataframe is in inDF. Output dataframe is in outDF. |
+------------------+----------------------------+----------------------------------------------------------------------------------+
| outputColNames   | Column Names for the CSV   | New Output Columns of the SQL                                                    |
+------------------+----------------------------+----------------------------------------------------------------------------------+
| outputColTypes   | Column Types for the CSV   | Data Type of the Output Columns                                                  |
+------------------+----------------------------+----------------------------------------------------------------------------------+
| outputColFormats | Column Formats for the CSV | Format of the Output Columns                                                     |
+------------------+----------------------------+----------------------------------------------------------------------------------+