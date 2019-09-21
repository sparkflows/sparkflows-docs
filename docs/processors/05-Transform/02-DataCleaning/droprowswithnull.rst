DropRowsWithNull
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
This node has no fields. By default it check the all columns.

Examples
---------

Input
--------------

.. list-table:: 
   :widths: 10 10
   :header-rows: 1

   * - id
     - amount
   
   * - 1
     - 100
     
   * - 2
     - 200
     
   * - 3
     - 
     
   * - 4
     - 400
     
   * - 5
     - 400
    
   * - 6
     - 400
   
   * - 7
     - 600
    
   * - 8
     - 700

Output
-------

.. list-table:: 
   :widths: 10 10
   :header-rows: 1

   * - id
     - amount
   
   * - 1
     - 100
     
   * - 2
     - 200
     
   * - 4
     - 400
     
   * - 5
     - 400
    
   * - 6
     - 400
   
   * - 7
     - 600
    
   * - 8
     - 700









