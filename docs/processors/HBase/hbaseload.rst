
HBaseLoad
========== 

Loads all the rows in the incoming DataFrame onto HBase using the specific field mapping

Type
---------- 

transform

Class
---------- 

fire.nodes.hbase.NodeHBaseLoad

Fields
---------- 

+----------------+---------------------+---------------------------------------------------------+
| Name           | Title               | Description                                             |
+================+=====================+=========================================================+
| hbaseTableName | HBase Table Name    | HBase Table into which data gets loaded                 |
+----------------+---------------------+---------------------------------------------------------+
| rowKeyCol      | Row Key Column      | DataFrame column which is used as the row keys of HBase |
+----------------+---------------------+---------------------------------------------------------+
| inputCols      | Variable            | None                                                    |
+----------------+---------------------+---------------------------------------------------------+
| hbaseColFamily | HBase Column Family | HBase Column Family for the variable                    |
+----------------+---------------------+---------------------------------------------------------+
| hbaseCols      | HBase Columns       | HBase Column Name into which the variable is loaded     |
+----------------+---------------------+---------------------------------------------------------+