Window Analytics
=========== 



Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeWindowAnalytics

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
      * - analyticsCol
        - Analytics Column
        - 
      * - window_offset
        - Window Offset
        - It's used in lead and lag functions.


Details
-------


This node Generates a new Dataframe with Analytics Column appended to the incoming Dataframe.

Analytics Column is populated with value based on the Window Function selected.


Examples
-------


Incoming Dataframe has following rows:

EMP_CD    |    EMP_NAME    |    DEPT    |    SALARY    |    AGE    
------------------------------------------------------------------------
E01       |    ANTHONY     |    HR      |    50000     |    40
E02       |    LISA        |    HR      |    45000     |    35
E03       |    MARTIN      |    HR      |    20000     |    25
E04       |    DAVID       |    SALES   |    55000     |    40
E05       |    MARK        |    SALES   |    60000     |    45
E06       |    JOE         |    SALES   |    40000     |    25
E07       |    BELLA       |    HR      |    60000     |    24

 If WindowAnalytics node is configured as below:
+++++++++++++++

PARTITIONBY      :     DEPT
ORDERBY          :     AGE
WINDOW FUNCTION  :     first_value
ANALYTICS COLUMN :     SALARY : integer
WINDOW OFFSET    :     1

then outgoing Dataframe would be created as below 
where incoming Dataframe is partitioned by [DEPT] and data is sorted by [AGE] and [FIRST VALUE] of Analytics Column [SALARY] within a partition is appended as new column:

EMP_CD    |    EMP_NAME    |    DEPT    |    SALARY    |    AGE    |    first_value
---------------------------------------------------------------------------------------
E07       |    BELLA       |    HR      |    60000     |    24     |    60000
E03       |    MARTIN      |    HR      |    20000     |    25     |    60000
E02       |    LISA        |    HR      |    45000     |    35     |    60000
E01       |    ANTHONY     |    HR      |    50000     |    40     |    60000
E06       |    JOE         |    SALES   |    40000     |    25     |    40000
E04       |    DAVID       |    SALES   |    55000     |    40     |    40000
E05       |    MARK        |    SALES   |    60000     |    45     |    40000

 If WindowAnalytics node is configured as below:
+++++++++++++++

PARTITIONBY      :     DEPT
ORDERBY          :     AGE
WINDOW FUNCTION  :     lead
ANALYTICS COLUMN :     SALARY : integer
WINDOW OFFSET    :     2

then outgoing Dataframe would be created as below 
where incoming Dataframe is partitioned by [DEPT] and data is sorted by [AGE] and 
Analytics Column [SALARY] value of leading 2 or [WINDOW OFFSET] rows within a partition is appended as new column:

EMP_CD    |    EMP_NAME    |    DEPT    |    SALARY    |    AGE    |    first_value
---------------------------------------------------------------------------------------
E07       |    BELLA       |    HR      |    60000     |    24     |    45000
E03       |    MARTIN      |    HR      |    20000     |    25     |    50000
E02       |    LISA        |    HR      |    45000     |    35     |    
E01       |    ANTHONY     |    HR      |    50000     |    40     |    
E06       |    JOE         |    SALES   |    40000     |    25     |    60000
E04       |    DAVID       |    SALES   |    55000     |    40     |    
E05       |    MARK        |    SALES   |    60000     |    45     |    
