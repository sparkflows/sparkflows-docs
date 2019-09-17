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
.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - name
     - Alice
     - Alice
     - Alice
     
   * - age
     - 5
     - 5
     - 10
     
   * - height 
     - 80
     - 80
     - 80

Parameters
----------
COLUMNS        name,height

Output
--------------
name,age,height
Alice,5,80





