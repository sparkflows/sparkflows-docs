
Save JDBC
^^^^^^ 

This node writes data to databases using JDBC.

type

transform

nodeClass

fire.nodes.save.NodeSaveJDBC

Fields

+----------+-----------+----------------------------------------------------------------+
| Name     | Title     | Description                                                    |
+==========+===========+================================================================+
| url      | URL       | The JDBC URL to connect to                                     |
+----------+-----------+----------------------------------------------------------------+
| table    | DB Table  | The JDBC table to write to                                     |
+----------+-----------+----------------------------------------------------------------+
| driver   | Driver    | The class name of the JDBC driver needed to connect to the URL |
+----------+-----------+----------------------------------------------------------------+
| user     | User      | Username with which to connect to the DB                       |
+----------+-----------+----------------------------------------------------------------+
| password | Password  | Password with which to connect to the DB                       |
+----------+-----------+----------------------------------------------------------------+
| saveMode | Save Mode | Whether to Append, Overwrite or Error if the table Exists      |
+----------+-----------+----------------------------------------------------------------+