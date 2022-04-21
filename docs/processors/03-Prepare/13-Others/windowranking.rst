Window Ranking
=========== 



Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeWindowRanking

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - partitionByCols
        - PartitionBy
        - partition column names separated by comma(,) 
      * - orderByCols
        - OrderBy
        - order by column names separated by comma(,)
      * - windowFunction
        - Window Function
        - Window Function Name


Details
-------


This node Generates a new Dataframe with Rank Column appended to the incoming Dataframe.

Rank Column is populated with value based on the Window Function selected.


Examples
-------


Incoming Dataframe has following rows:

EMP_CD    |    EMP_NAME    |    DEPT    |    SALARY    |    AGE    
------------------------------------------------------------------------
E01       |    ANTHONY     |    HR      |    50000     |    40
E02       |    LISA        |    HR      |    50000     |    35
E03       |    MARTIN      |    HR      |    20000     |    25
E04       |    DAVID       |    SALES   |    55000     |    40
E05       |    MARK        |    SALES   |    60000     |    45
E06       |    JOE         |    SALES   |    40000     |    25
E07       |    BELLA       |    HR      |    60000     |    24

 If WindowRanking node is configured as below:
+++++++++++++++

PARTITIONBY      :     DEPT
ORDERBY          :     SALARY
WINDOW FUNCTION  :     RANK

then outgoing Dataframe would be created as below 
where incoming Dataframe is partitioned by [DEPT] and data is sorted by [SALARY] and [rank] column would be populated with rank value within a partition
if two or more rows have same [SALARY] value then they would be assigned same rank value and next row would be assigned with value as per the order within a partition:

EMP_CD    |    EMP_NAME    |    DEPT    |    SALARY    |    AGE    |    rank
---------------------------------------------------------------------------------------
E03       |    MARTIN      |    HR      |    20000     |    25     |    1
E01       |    ANTHONY     |    HR      |    50000     |    40     |    2
E02       |    LISA        |    HR      |    50000     |    35     |    2
E07       |    BELLA       |    HR      |    60000     |    24     |    4
E06       |    JOE         |    SALES   |    40000     |    25     |    1
E04       |    DAVID       |    SALES   |    55000     |    40     |    2
E05       |    MARK        |    SALES   |    60000     |    45     |    3

 If WindowRanking node is configured as below:
+++++++++++++++

PARTITIONBY      :     DEPT
ORDERBY          :     SALARY
WINDOW FUNCTION  :     DENSE_RANK

then outgoing Dataframe would be created as below 
where incoming Dataframe is partitioned by [DEPT] and data is sorted by [SALARY] and [rank] column would be populated with rank value within a partition
if two or more rows have same [SALARY] value then they would be assigned same rank value and next row would be assigned with next rank value:

EMP_CD    |    EMP_NAME    |    DEPT    |    SALARY    |    AGE    |    rank
---------------------------------------------------------------------------------------
E03       |    MARTIN      |    HR      |    20000     |    25     |    1
E01       |    ANTHONY     |    HR      |    50000     |    40     |    2
E02       |    LISA        |    HR      |    50000     |    35     |    2
E07       |    BELLA       |    HR      |    60000     |    24     |    3
E06       |    JOE         |    SALES   |    40000     |    25     |    1
E04       |    DAVID       |    SALES   |    55000     |    40     |    2
E05       |    MARK        |    SALES   |    60000     |    45     |    3
