
SaveParquet
========== 

Saves the DataFrame into the specified location in Parquet Format. When running on Hadoop, it is saved onto HDFS.

Type
---------- 

transform

Class
---------- 

fire.nodes.save.NodeSaveParquet

Fields
---------- 

+----------+-----------+----------------------------------------------------------+
| Name     | Title     | Description                                              |
+==========+===========+==========================================================+
| path     | Path      | Path where to save the Parquet files                     |
+----------+-----------+----------------------------------------------------------+
| saveMode | Save Mode | Whether to Append, Overwrite or Error if the path Exists |
+----------+-----------+----------------------------------------------------------+