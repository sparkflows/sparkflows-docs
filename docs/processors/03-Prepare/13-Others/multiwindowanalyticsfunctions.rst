Multi Window Analytics
=========== 



Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeMultiWindowAnalytics

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - analyticsCols
        - AnalyticsColumn
        - 
      * - windowFunctions
        - Window Function
        - Window Function Name
      * - partitionByCols
        - PartitionBy
        - partition column names separated by comma(,) 
      * - orderByCols
        - OrderBy
        - order by column names separated by comma(,)
      * - outPutColumns
        - OutPutColumn
        - Enter output field(column) name


Details
-------


It creates a new Dataframe with new ouuput columns appended to the incoming Dataframe which are computed based on application of Window Function on Analytics Columns.

This node facilitates computation of multiple Analytics Columns.


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

 If MultiWindowAnalytics node is configured as below:
+++++++++++++++

ANALYTICSCOLUMN    |    WINDOW FUNCTION    |    PARTITIONBY    |    ORDERBY    |    OUTPUTCOLUMN 	
-----------------------------------------------------------------------------------------------------------
SALARY             |    first_value        |    DEPT           |    AGE        |    SALARY_OF_YOUNGEST
AGE                |    lag                |    DEPT           |    SALARY     |    AGE_OF_PREVRANKSALARY

then outgoing Dataframe would be created as below 
where incoming Dataframe is partitioned by [DEPT] and data is sorted by [AGE] and [FIRST VALUE] of Analytics Column [SALARY] 
within a partition is appended as new column [SALARY_OF_YOUNGEST]
for second Analytics Column, incoming Dataframe is partitioned by [DEPT] and data is sorted by [SALARY] and [AGE_OF_PREVRANKSALARY] is populated with the 
Analytics Column [AGE] of row which is just 1 rank above the current row in the order of [SALARY]:

EMP_CD    |    EMP_NAME    |    DEPT    |    SALARY    |    AGE    |    SALARY_OF_YOUNGEST    |    AGE_OF_PREVRANKSALARY
------------------------------------------------------------------------------------------------------------------------------
E03       |    MARTIN      |    HR      |    20000     |    25     |    60000                 |    	
E02       |    LISA        |    HR      |    45000     |    35     |    60000                 |    25
E01       |    ANTHONY     |    HR      |    50000     |    40     |    60000                 |    35
E07       |    BELLA       |    HR      |    60000     |    24     |    60000                 |    40
E06       |    JOE         |    SALES   |    40000     |    25     |    40000                 |    
E04       |    DAVID       |    SALES   |    55000     |    40     |    40000                 |    25
E05       |    MARK        |    SALES   |    60000     |    45     |    40000                 |    40
