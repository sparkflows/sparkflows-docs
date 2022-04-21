Cube
=========== 

Cube Node generates a result set that shows aggregates for all combinations of values in the selected columns.

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeCube

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - cubeCols
        - Cube Columns
        - 
      * - aggregateCols
        - Aggregate Columns
        - Aggregate Columns
      * - aggregateOperations
        - Aggregate Operation to use
        - Aggregate Operation


Details
-------


Cube Node generates a result set that shows aggregates for all combinations of values in the selected columns.

Outgoing Dataframe is created by applying aggregated functions on aggregate columns for all combinations of values present in the selected cube columns.

More than one aggregations can be selected.


Examples
-------


Incoming Dataframe has following rows:

EMP_CD    |    EMP_NAME    |    LOCATION    |    DEPT         |    SALARY
-----------------------------------------------------------------------------
E05       |    ROSS        |    NEW YORK    |    FRONT DESK   |    10000
E06       |    LISA        |    NEW JERSEY  |    FRONT DESK   |    11000
E07       |    PAUL        |    NEW YORK    |    MAINTENANCE  |    12000
E08       |    MARK        |    NEW JERSEY  |    MAINTENANCE  |    13000

if Cube node is configured as below:

CUBE COLUMNS      :    LOCATION, DEPT

AGGREGATE COLUMNS    |    AGGREGATE OPERATION
-------------------------------------------------
SALARY               |    SUM

then outgoing Dataframe would be created as below after performing specified aggregation
Summation of Salary all Employees is computed for all combinations of values present in [LOCATION] and [DEPT] columns:

LOCATION           |    DEPT           |    sum_SALARY
----------------------------------------------------------------
                   |                   |    46000               <=    Summation for all values
NEW YORK           |                   |    22000               <=    Summation of Salary of Employees at NEW YORK location											
NEW JERSEY         |                   |    24000               <=    Summation of Salary of Employees at NEW JERSEY location
                   |    FRONT DESK     |    21000               <=    Summation of Salary of Employees in FRONT DESK department
                   |    MAINTENANCE    |    25000               <=    Summation of Salary of Employees in MAINTENANCE department
NEW JERSEY         |    MAINTENANCE    |    13000               <=    Summation of Salary of Employees at NEW JERSEY in MAINTENANCE department
NEW YORK           |    FRONT DESK     |    10000               <=    Summation of Salary of Employees at NEW YORK in FRONT DESK department
NEW JERSEY         |    FRONT DESK     |    11000               <=    Summation of Salary of Employees at NEW JERSEY in FRONT DESK department
NEW YORK           |    MAINTENANCE    |    12000               <=    Summation of Salary of Employees at NEW YORK in MAINTENANCE department
