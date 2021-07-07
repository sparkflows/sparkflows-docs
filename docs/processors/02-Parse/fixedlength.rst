Fixed Length Fields
=========== 

Reads in files with fixed length fields

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeFixedLength

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCol
        - Input Column
        - input column name
      * - outputColNames
        - Column Names for the CSV
        - New Output Columns of the SQL
      * - outputColTypes
        - Column Types for the CSV
        - Data Type of the Output Columns
      * - colLengths
        - Length of each column
        - Length of the columns in characters
      * - outputColFormats
        - Column Formats for the CSV
        - Format of the Output Columns


Details
-------


Reads in files with fixed length fields. The output column names and their data types are specified. Also the length of each column is specified.


