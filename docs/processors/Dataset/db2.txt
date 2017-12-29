
DB2 JDBC
^^^^^^ 

This node reads data from other databases using JDBC.

type

dataset

nodeClass

fire.nodes.dataset.NodeDatasetJDBC

Fields

+------------------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|       Name       |           Title           |                                                                                             Description                                                                                              |
+------------------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|       url        |          DB2 URL          |                                                                                      The JDBC URL to connect to                                                                                      |
|       user       |            User           |                                                                                    User for connecting to the DB                                                                                     |
|     password     |          Password         |                                                                                  Password for connecting to the DB                                                                                   |
|     dbtable      |         DB2 Table         | The JDBC table that should be read. Note that anything that is valid in a FROM clause of a SQL query can be used. For example, instead of a full table you could also use a subquery in parentheses. |
|      driver      |         DB2 Driver        |                                                                   The class name of the JDBC driver needed to connect to this URL                                                                    |
|  outputColNames  | Column Names of the Table |                                                                                  Output Columns Names of the Table                                                                                   |
|  outputColTypes  | Column Types of the Table |                                                                                   Output Column Types of the Table                                                                                   |
| outputColFormats |       Column Formats      |                                                                                        Output Column Formats                                                                                         |
+------------------+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+