Group By
=========== 

Grouper Node

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeGroupBy

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - Aggregation Setting
        - Aggregation Setting
      * - groupingCols
        - Grouping Columns
        - Grouping Columns
      * - aggregateCols
        - Aggregate Columns
        - Aggregate Columns
      * - aggregateOperations
        - Aggregate Operation to use
        - Aggregate Operation
      * - Filter Setting
        - Filter Setting
      * - whereClause
        - Where Clause
        - where condition before group by function
      * - havingClause
        - Having Clause
        - having condition after group by function


Details
-------


This node computes aggregations of a group of rows against selected grouping column by applying selected aggregate functions on specified aggregate columns.

Outgoing Dataframe can be filtered based on the Where Clause and Having Clause provided.


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

if GroupBy node is configured as below:

GROUPING COLUMNS      :    DEPT

AGGREGATE COLUMNS    |    AGGREGATE OPERATION
-------------------------------------------------
EMP_CD               |    COUNT
SALARY               |    SUM

then outgoing Dataframe would be created as below after performing specified aggregation
Count of Employees and Summation of Salary all Employees is computed for each [DEPT]:

DEPT           |    count_emp_cd    |    sum_salary
----------------------------------------------------------
FRONT DESK     |    2               |    21000
MARKETING      |    2               |    25000
HR             |    1               |    10000
SALES          |    1               |    11000
MAINTENANCE    |    2               |    25000

if [WHERE CLAUSE] is entered as [DEPT = 'HR'] then outgoing Dataframe would consists of data only from HR department.

if [HAVING CLAUSE] is entered as [COUNT(*) > 1] then outgoing Dataframe would consists of data for Department where count of Employees is more than 1.
