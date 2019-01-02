SaveHBase
=========== 

Saves all the rows in the incoming DataFrame onto Apache HBase using the specific field mapping

Input
--------------
It takes in a DataFrame as input

Output
--------------
Incoming dataFrame is passed along to the next nodes.

Type
--------- 

transform

Class
--------- 

fire.nodes.hbase.NodeSaveHBase

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - hbaseTableName
        - HBase Table Name
        - HBase Table into which data gets loaded
      * - rowKeyCol
        - Row Key Column
        - DataFrame column which is used as the row keys of HBase
      * - inputCols
        - Variable
      * - hbaseColFamily
        - HBase Column Family
        - HBase Column Family for the variable
      * - hbaseCols
        - HBase Columns
        - HBase Column Name into which the variable is loaded


Details
======


SaveHBase node saves all the rows in the incoming DataFrame onto HBase using the specific field mapping.

The DataFrame columns which do not have to be loaded into HBase are left empty.


