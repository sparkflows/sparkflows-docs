
RemoveDuplicateRows
^^^^^^ 

This node take an array of fields, compare rows on those fields. If they full match then its a match. From the matches it would randomly take one row and drop the rest.

type

transform

nodeClass

fire.nodes.etl.NodeRemoveDuplicateRows

Fields

+-----------+---------+--------------------------------------+
| Name      | Title   | Description                          |
+===========+=========+======================================+
| inputCols | Columns | The columns to be selected for match |
+-----------+---------+--------------------------------------+