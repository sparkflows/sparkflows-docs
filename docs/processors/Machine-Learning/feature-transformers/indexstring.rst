
IndexString
^^^^^^ 

Maps a column of indices back to a new column of corresponding string values. The index-string mapping is either from the ML attributes of the input column, or from user-supplied labels

type

ml-transformer

nodeClass

fire.nodes.ml.NodeIndexString

Fields

+-----------+---------------+---------------------------------+
| outputCol | Output Column | Output column name              |
+===========+===============+=================================+
| inputCol  | Input Column  | Column containing label indices |
+-----------+---------------+---------------------------------+
| outputCol | Output Column | Output column name              |
+-----------+---------------+---------------------------------+