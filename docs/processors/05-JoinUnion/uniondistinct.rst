Union Distinct
=========== 

This node creates a new DataFrame by performing a DISTINCT on the result set, eliminating any duplicate rows

Input
--------------
It takes in multiple DataFrames as input

Output
--------------
This node does union of all the rows from the incoming DataFrames to generate the output DataFrame

Type
--------- 

join

Class
--------- 

fire.nodes.etl.NodeUnionDistinct

Fields
--------- 



Details
-------



*  This node creates a new DataFrame by performing a DISTINCT on the result set, eliminating any duplicate rows.
*  It takes in multiple DataFrames as input.
*  This node does union of all the rows from the incoming DataFrames to generate the output DataFrame after removing duplicate rows.


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

after execution of UnionDistinct node following outgoing Dataframe would be created after combining all rows from all input Dataframes and removing duplicate rows.
Outgoing Dataframe contains only distinct rows:

EMP_CD    |    EMP_NAME    |    DEPT       
-------------------------------------------
E01       |    DAVID       |    HR         
E02       |    JOHN        |    SALES      
E03       |    MARTIN      |    MARKETING  
E04       |    TONY        |    MARKETING  
E05       |    MARK        |    HR         
E06       |    ROSS        |    SALES      
