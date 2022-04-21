Split By Multiple Expressions
=========== 

Splits the incoming DataFrame into multiple output DataFrames by applying the conditional logic

Input
--------------
It accepts a DataFrame as input from the previous Node

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeSplitByMultipleExpressions

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - conditionExpr1
        - Conditional Expression 1 to split the Data on
        - Conditional Expression 1 to be used for Splitting the Dataset
      * - conditionExpr2
        - Conditional Expression 2 to split the Data on
        - Conditional Expression 2 to be used for Splitting the Dataset
      * - conditionExpr3
        - Conditional Expression 3 to split the Data on
        - Conditional Expression 3 to be used for Splitting the Dataset
      * - conditionExpr4
        - Conditional Expression 4 to split the Data on
        - Conditional Expression 4 to be used for Splitting the Dataset
      * - conditionExpr5
        - Conditional Expression 5 to split the Data on
        - Conditional Expression 5 to be used for Splitting the Dataset


Details
-------


This node splits the incoming DataFrame into multiple output DataFrames by applying the provided conditional logic.


Examples
-------


Incoming Dataframe has following rows:

CUST_CD    |    CUST_NAME    |    AGE    |    SALARY    
--------------------------------------------------------
C01        |    MATT         |    50     |    50000     
C02        |    LISA         |    45     |    40000
C03        |    ROBIN        |    30     |    40000
C04        |    MARCUS       |    35     |    50000

If SplitByMultipleExpressions node is configured to split the incoming Dataframe into multiple Dataframes based on following conditional Expressions 
then outgoing Dataframes would be created as below:

 First outgoing Dataframe for the conditional Expression [AGE > 40]
+++++++++++++++

CUST_CD    |    CUST_NAME    |    AGE    |    SALARY    
--------------------------------------------------------
C01        |    MATT         |    50     |    50000     
C02        |    LISA         |    45     |    40000

 Second outgoing Dataframe for the conditional Expression [SALARY = 40000]
+++++++++++++++

CUST_CD    |    CUST_NAME    |    AGE    |    SALARY    
--------------------------------------------------------
C02        |    LISA         |    45     |    40000
C03        |    ROBIN        |    30     |    40000

 Third outgoing Dataframe for the conditional Expression [AGE > 40 AND AGE < 50]
+++++++++++++++

CUST_CD    |    CUST_NAME    |    AGE    |    SALARY    
--------------------------------------------------------
C02        |    LISA         |    45     |    40000
