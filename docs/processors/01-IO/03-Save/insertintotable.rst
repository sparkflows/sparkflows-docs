InsertIntoHIVETable
=========== 

Saves the DataFrame into an Apache HIVE Table

Type
--------- 

transform

Class
--------- 

fire.nodes.save.NodeInsertIntoTable

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - database
        - HIVE Database
        - Name of the HIVE Database
      * - table
        - HIVE Table
        - Name of the HIVE table
      * - saveMode
        - Save Mode
        - Whether to Append, Overwrite or Error if the path Exists
      * - partitionBy
        - Partition By
        - Partition By Column (can be empty)
      * - bucketBy
        - Bucket By
        - Bucket By Column (can be empty)


Details
-------


When using Insert Into Table, the HIVE table has to already exist.

Otherwise it throws the following exception:

org.apache.spark.sql.catalyst.analysis.NoSuchTableException: Table or view 'xyz' not found in database 'abc';


