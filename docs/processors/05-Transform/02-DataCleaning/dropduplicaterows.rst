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
   :widths: 10 20 10
   :header-rows: 1

   * - name
     - age
     - height
   
   * - Alice
     - Alice
     - Alice
     
   * - 5
     - 5
     - 10
     
   * - 80
     - 80
     - 80

Parameters
----------
COLUMNS        name,height

Output
--------------
name,age,height
Alice,5,80





