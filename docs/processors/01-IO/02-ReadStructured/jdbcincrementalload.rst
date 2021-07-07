JDBC Incremental Load
=========== 

This node is used to load incremental data from RDBMS to Hive.

Input
--------------
RDBMS detail like url, username , password, hivedb , hive table name

Type
--------- 

dataset

Class
--------- 

fire.nodes.dataset.NodeDatasetJDBCIncrementalLoad

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - sqldb
        - SqlDB
        - 
      * - sqlServer
        - SqlServer
        - 
      * - sqlUser
        - SqlUser
        - 
      * - password
        - password
        - 
      * - sqltable
        - SqlTable
        - 
      * - sqlkeycolumn
        - SqlKeyColumn
        - 
      * - homeDirectory
        - Config Path
        - 
      * - performance
        - Performance
      * - partitionColumn
        - PartitionColumn
        - PartitionColumn must be a numeric, date, or timestamp column from the table
      * - lowerBound
        - LowerBound
        -  lowerBound and upperBound are just used to decide the partition stride, not for filtering the rows in table. So all rows in the table will be partitioned and returned. This option applies only to reading.
      * - upperBound
        - UpperBound
        -  lowerBound and upperBound are just used to decide the partition stride, not for filtering the rows in table. So all rows in the table will be partitioned and returned. This option applies only to reading.
      * - numPartitions
        - NumPartitions
        - The maximum number of partitions that can be used for parallelism in table reading
      * - fetchsize
        - FetchSize
        - The JDBC fetch size, which determines how many rows to fetch per round trip.
      * - schema
        - Schema
      * - outputColNames
        - Column Names of the Table
        - Output Columns Names of the Table
      * - outputColTypes
        - Column Types of the Table
        - Output Column Types of the Table
      * - outputColFormats
        - Column Formats
        - Output Column Formats


Details
-------


This node is used to load incremental data from RDBMS to Hive.


