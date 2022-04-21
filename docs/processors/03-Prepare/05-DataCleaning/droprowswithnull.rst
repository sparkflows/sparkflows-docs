Drop Rows With Null
=========== 

This node creates a new DataFrame by dropping rows containing null values

Input
--------------
It accepts DataFrame as input from the previous Node

Output
--------------
This node drops rows containing null values

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeDropRowsWithNull

Fields
--------- 



Details
-------


This node creates a new DataFrame by dropping rows containing NULL values in any of the columns.


Examples
-------


Incoming Dataframe has following rows:

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE
-------------------------------------------------------
E01       |    DAVID       |    HR         |    25
E05       |    MARK        |               |    25
E02       |    JOHN        |    SALES      |    35
E03       |    TONY        |    MARKETING  |    
E04       |    MARTIN      |    MARKETING  |    45

Incoming Dataframe has NULL values for two rows. 
Using DropRowsWithNull node would result in below outgoing Dataframe created by dropping rows having NULL values in any of the columns:

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE
-------------------------------------------------------
E01       |    DAVID       |    HR         |    25
E02       |    JOHN        |    SALES      |    35
E04       |    MARTIN      |    MARKETING  |    45
