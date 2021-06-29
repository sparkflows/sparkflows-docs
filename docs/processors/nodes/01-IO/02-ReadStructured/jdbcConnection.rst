JDBC Connection
=========== 

This node reads data from Relational Databases using JDBC and creates a DataFrame from it

Input
--------------
It reads data from Relational Databases

Output
--------------
It creates a DataFrame from the data read and sends it to its output

Type
--------- 

dataset

Class
--------- 

fire.nodes.dataset.NodeDatasetJDBCUsingConnection

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - connection
        - Connection
        - The JDBC connection to connect
      * - dbtable
        - DB Table
        - The JDBC table that should be read. Note that anything that is valid in a FROM clause of a SQL query can be used. For example, instead of a full table you could also use a subquery in parentheses.
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


This node reads data from Relational Databases using JDBC and creates a DataFrame from it.


