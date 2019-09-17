DropDuplicateRows
=========== 

This node creates a new DataFrame by dropping duplicate rows

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeDropDuplicateRows

Input
--------
A DataFrame to filter rows on duplicate.

Output
--------
A DataFrame containing no duplicate row on the selected coulmns.

Parameters
---------- 
COLUMNS           Seq of Coulmns to check the duplicate condition.(By default duplication checked on all the columns)

Examples
--------

Input
--------------
name,age,height \n
Alice,5,80 \n
Alice,5,80 \n
Alice,10,80 \n

Parameters
----------
COLUMNS        name,height

Output
--------------
name,age,height
Alice,5,80





