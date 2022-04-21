Pivot By
=========== 

Pivot Node

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodePivotBy

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - groupingCols
        - Grouping Columns
        - Grouping Columns
      * - pivotCols
        - Pivot Columns
        - Pivoting Columns
      * - aggregateCols
        - Aggregate Columns
        - Aggregate Columns
      * - aggregateOperations
        - Aggregate Operation to use
        - Aggregate Operation
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


This node creates a Dataframe based on the Pivot table created out of the incoming Dataframe.

Pivot table is created by Aggregation of rows by applying the Aggregate functions on the Aggregate Columns against the Grouping and Pivot Columns selected.


Examples
-------


Incoming Dataframe has following rows:

EMP_CD    |    EMP_NAME    |    LOCATION    |    DEPT         |    SALARY
-----------------------------------------------------------------------------
E01       |    DAVID       |    NEW YORK    |    HR           |    10000
E02       |    JOHN        |    NEW JERSEY  |    SALES        |    11000
E03       |    MARTIN      |    NEW YORK    |    MARKETING    |    12000
E04       |    TONY        |    NEW JERSEY  |    MARKETING    |    13000
E05       |    ROSS        |    NEW YORK    |    FRONT DESK   |    10000
E06       |    LISA        |    NEW JERSEY  |    FRONT DESK   |    11000
E07       |    PAUL        |    NEW YORK    |    MAINTENANCE  |    12000
E08       |    MARK        |    NEW JERSEY  |    MAINTENANCE  |    13000

if PivotBy node is configured as below:

GROUPING COLUMNS      :    DEPT
PIVOT COLUMNS         :    LOCATION

AGGREGATE COLUMNS    |    AGGREGATE OPERATION
-------------------------------------------------
EMP_CD               |    COUNT

then outgoing Dataframe would be created as below after performing specified aggregation
Count of Employees for each combination of [DEPT] and [LOCATION] would be listed as below:

DEPT         |    NEW JERSEY       |    NEW YORK
---------------------------------------------------
FRONT DESK   |    1                |    1
MARKETING    |    1                |    1
HR           |                     |    1
SALES        |    1                |
MAINTENANCE  |    1                |    1
