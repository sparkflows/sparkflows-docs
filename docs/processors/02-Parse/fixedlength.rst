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


Examples
-------


Incoming Dataframe has following rows:

DATA_COLS
-------------------------------------------
CUST001INV00120200101PRD0011200
CUST001INV00220200202PRD0022200

Data in each row contains data of multiple columns having fixed length.

if FixedLength node is configured as below then multiple columns of fixed length would be created in the outgoing Dataframe:

COLUMN NAMES FOR THE CSV    |    COLUMN TYPES FOR THE CSV    |    LENGTH OF EACH COLUMN 	
--------------------------------------------------------------------------------------------
CUST_CD                     |    STRING                      |    7
INV_NO                      |    STRING                      |    6
INV_DATE                    |    STRING                      |    8
PRODUCT_CD                  |    STRING                      |    6
INV_AMT                     |    STRING                      |    4

after execution of FixedLength node following outgoing Dataframe would be created containing fixed length columns:

DATA_COL                          |    CUST_CD    |    INV_NO    |    INV_DATE    |    PRODUCT_CD    |    INV_AMT
----------------------------------------------------------------------------------------------------------------------
CUST001INV00120200101PRD0011200   |    CUST001    |    INV001    |    20200101    |    PRD001        |    1200
CUST001INV00220200202PRD0022200   |    CUST001    |    INV002    |    20200202    |    PRD002        |    2200
