Read Hana Csv
=========== 

It reads in Hana CSV files and creates a DataFrame from it

Input
--------------
It reads in CSV text files and sql file to create schema from it

Output
--------------
It creates a DataFrame from the data read and sends it to its output

Type
--------- 

dataset

Class
--------- 

fire.nodes.dataset.NodeReadHANACSVDump

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - path
        - Path
        - Path of the Text file/directory
      * - hdfsSqlFile
        - SQL File
        - Path of the sql file that contains create table script.
      * - outputColNames
        - Column Names for the CSV
        - New Output Columns of the SQL
      * - outputColTypes
        - Column Types for the CSV
        - Data Type of the Output Columns
      * - outputColFormats
        - Column Formats for the CSV
        - Format of the Output Columns


Details
-------


This node reads data from Hana CSV files and creates a DataFrame from it.


