Union All
=========== 

This node creates a new DataFrame by merging all the rows without removing the duplicates

Input
--------------
It accepts a DataFrame as input from the previous Node

Output
--------------
This node does union of all the rows without removing the duplicates

Type
--------- 

join

Class
--------- 

fire.nodes.etl.NodeUnionAll

Fields
--------- 



Details
-------



*  This node creates a new DataFrame by merging all the rows without removing the duplicates.
*  It accepts two or more DataFrames as input from the previous Nodes.
*  The resulting Dataframe is union of all the rows without removing the duplicates.


Examples
-------


1st Incoming Dataframe has following rows:

EMP_CD    |    EMP_NAME    |    DEPT       
-------------------------------------------
E01       |    DAVID       |    HR         
E02       |    JOHN        |    SALES      
E03       |    MARTIN      |    MARKETING  
E04       |    TONY        |    MARKETING  

2nd Incoming Dataframe has following rows:

EMP_CD    |    EMP_NAME    |    DEPT       
-------------------------------------------
E03       |    MARTIN      |    MARKETING  
E04       |    TONY        |    MARKETING  
E05       |    MARK        |    HR         
E06       |    ROSS        |    SALES      

after execution of UnionAll node following outgoing Dataframe would be created after combining all rows from all input Dataframes without removing duplicate rows:

EMP_CD    |    EMP_NAME    |    DEPT       
-------------------------------------------
E01       |    DAVID       |    HR         
E02       |    JOHN        |    SALES      
E03       |    MARTIN      |    MARKETING  
E04       |    TONY        |    MARKETING  
E03       |    MARTIN      |    MARKETING  
E04       |    TONY        |    MARKETING  
E05       |    MARK        |    HR         
E06       |    ROSS        |    SALES      
