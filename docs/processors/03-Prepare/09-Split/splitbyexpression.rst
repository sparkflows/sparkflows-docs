Split By Expression
=========== 

This node splits the incoming DataFrame into two output DataFrames by applying the conditional logic

Input
--------------
It accepts a DataFrame as input from the previous Node

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeSplitByExpression

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - conditionExpr
        - Conditional Expression to split the Data on
        - Conditional Expression to be used for Splitting the DataFrame into two. DataFrame which matches the condition will go to the lower edge output. The other would go to the higher edge output.


Details
-------


This node splits the incoming DataFrame into two output DataFrames by applying the conditional logic.


Examples
-------


Incoming Dataframe has following rows:

CUST_CD   |   CUST_NAME   |   AGE   
------------------------------------
C01       |   MATT        |   50    
C02       |   LISA        |   45
C03       |   ROBIN       |   35
C04       |   MARCUS      |   30 

If SplitByExpression node is configured to split the incoming Dataframe into two Dataframes based on Expression [AGE > 40] 
then two outgoing Dataframes would be created as below:

First Dataframe where [AGE] is greater than 40
+++++++++++++++

CUST_CD   |   CUST_NAME   |   AGE   
------------------------------------
C01       |   MATT        |   50    
C02       |   LISA        |   45

Second Dataframe where [AGE] is less than 40
+++++++++++++++

CUST_CD   |   CUST_NAME   |   AGE   
------------------------------------
C03       |   ROBIN       |   35
C04       |   MARCUS      |   30 
