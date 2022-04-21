Multi Window Ranking
=========== 



Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeMultiWindowRanking

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - windowFunctions
        - WindowFunction
        - Window Function Name
      * - partitionByCols
        - PartitionBy
        - partition column names separated by comma(,) 
      * - orderByCols
        - OrderBy
        - order by column names separated by comma(,)
      * - outPutColumns
        - OutputColumn
        - Enter output field(column) name


Details
-------


This node Generates a new Dataframe with Rank Columns appended to the incoming Dataframe.

Rank Columns are populated with value based on the Window Function selected.

This node facilitates computation of multiple Rank Columns.


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

 If MultiWindowRanking node is configured as below:
+++++++++++++++

WINDOW FUNCTION    |    PARTITIONBY    |    ORDERBY                |    OUTPUTCOLUMN 	
----------------------------------------------------------------------------------------------
RANK               |    DEPT           |    AGE DESC, EMP_NAME     |    ORDERED_BY_AGEDESC
ROW_NUMBER         |                   |    EMP_CD                 |    ROW_NUM_EMPCD

then outgoing Dataframe would be created as below 
where incoming Dataframe is partitioned by [DEPT] and data is sorted by [AGE DESC, EMP_NAME] and [RANK] value or the order value
within a partition is appended as new column [ORDERED_BY_AGEDESC]
for second Ranking Column, entire incoming Dataframe is sorted by [EMP_CD] and [ROW_NUM_EMPCD] is populated with the 
[ROW_NUMBER] value or the order value after sorting of the Dataframe:

EMP_CD    |    EMP_NAME    |    DEPT    |    SALARY    |    AGE    |    ORDERED_BY_AGEDESC    |    ROW_NUM_EMPCD
------------------------------------------------------------------------------------------------------------------------------
E01       |    ANTHONY     |    HR      |    50000     |    40     |    1                     |    1
E02       |    LISA        |    HR      |    45000     |    35     |    2                     |    2
E03       |    MARTIN      |    HR      |    20000     |    25     |    3                     |    3	
E07       |    BELLA       |    HR      |    60000     |    24     |    4                     |    7
E04       |    DAVID       |    SALES   |    55000     |    40     |    1                     |    4
E05       |    MARK        |    SALES   |    60000     |    45     |    2                     |    5
E06       |    JOE         |    SALES   |    40000     |    25     |    3                     |    6
