
FieldSplitter
^^^^^^ 

This node splits the string at specified delimiter

type

transform

nodeClass

fire.nodes.etl.NodeFieldSplitter

Fields

+------------+----------------+-----------------------------------------------------------+
|    Name    |     Title      |                        Description                        |
+------------+----------------+-----------------------------------------------------------+
|  inputCol  |  Input Column  |                     input column name                     |
| outputCols | Output Columns |  new column names separed by comma','.(eg: col1,co2,col3) |
|    sep     |   Separator    | separator to split the input column value(default: space) |
|  onError   |    On Error    |                                                           |
+------------+----------------+-----------------------------------------------------------+