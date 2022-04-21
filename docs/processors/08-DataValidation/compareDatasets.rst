Compare Datasets
=========== 

Validate the input datasets

Type
--------- 

join

Class
--------- 

fire.nodes.validation.NodeCompareDatasets

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description


Details
-------


This node compares two incoming Dataframes and if set of fields of both Dataframes matches 
then creates three outgoing Dataframe 
one having rows present in 1st but not in 2nd, second one having rows present in 2nd but not in 1st and third one with common rows. 

It doesn't result in any output if set of fields of incoming Dataframes are different.


Examples
-------


1st Incoming Dataframe has following rows:

EMP_CD    |    EMP_NAME    |    DEPT
----------------------------------------------
E01       |    DAVID       |    HR
E02       |    JOHN        |    SALES
E03       |    MARTIN      |    MARKETING

2nd Incoming Dataframe has following rows:

EMP_CD    |    EMP_NAME    |    DEPT
----------------------------------------------
E03       |    MARTIN      |    MARKETING
E04       |    TONY        |    MARKETING
E05       |    MARK        |    HR

execution of CompareDatasets node would result in below three outgoing Dataframes:

 Outgoing Dataframe with rows present in 1st but not in 2nd
+++++++++++++++

EMP_CD    |    EMP_NAME    |    DEPT
----------------------------------------------
E01       |    DAVID       |    HR
E02       |    JOHN        |    SALES

 Outgoing Dataframe with rows present in 2nd but not in 1st
+++++++++++++++

EMP_CD    |    EMP_NAME    |    DEPT
----------------------------------------------
E04       |    TONY        |    MARKETING
E05       |    MARK        |    HR

 Outgoing Dataframe with rows present in both
+++++++++++++++

EMP_CD    |    EMP_NAME    |    DEPT
----------------------------------------------
E03       |    MARTIN      |    MARKETING

if incoming Dataframes have different fields either having different Column Names or different count of columns then outgoing Dataframe won't be created.
