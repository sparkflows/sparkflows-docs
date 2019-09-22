Cube
=========== 

Cube Node generates a result set that shows aggregates for all combinations of values in the selected columns.

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeCube

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - cubeCols
        - Cube Columns
        - 
      * - aggregateCols
        - Aggregate Columns
        - Aggregate Columns
      * - aggregateOperations
        - Aggregate Operation to Use
        - Aggregate Operation


Examples
----------

Input
------

.. list-table:: 
   :widths: 20 20 20
   :header-rows: 1

   * - name
     - age
     - height
     
   * - Alice
     - 5
     - 80
     
   * - Alice
     - 5
     - 80
     
   * - Alice
     - 10
     - 80
     
   * - James
     - 5
     - 50
     
   * - James
     - 10
     - 60
    
   * - James
     - 7
     - 80
     
 
Parameters1
-------------

.. list-table:: 
   :widths: 10 25
   :header-rows: 1

   * - Name
     - Value
   
   * - Cube Columns
     - name

.. list-table:: 
   :widths: 10 25 40
   :header-rows: 1
   
   * - Id
     - Aggregate Columns
     - Aggregate Operation to Use
   
   * - 1
     - age
     - max
   
   * - 2
     - height
     - min
   

Output1
---------

.. list-table:: 
   :widths: 20 20 20
   :header-rows: 1

   * - name
     - max_age
     - min_height
     
   * - Alice
     - 10
     - 80
     
   * -
     - 10
     - 50
     
   * - James
     - 10
     - 50
     
-------------------------------------------------------------------    
 
 Parameters2
-------------

.. list-table:: 
   :widths: 10 25
   :header-rows: 1

   * - Name
     - Value
   
   * - Cube Columns
     - age

.. list-table:: 
   :widths: 10 25 40
   :header-rows: 1
   
   * - Id
     - Aggregate Columns
     - Aggregate Operation to Use
   
   * - 1
     - height
     - max
   
   * - 2
     - height
     - min
   

Output2
---------

.. list-table:: 
   :widths: 20 20 20
   :header-rows: 1

   * - age
     - max_height
     - min_height
     
   * - 
     - 80
     - 50
     
   * - 5
     - 80
     - 50
     
   * - 10
     - 80
     - 60
 
   * - 7
     - 80
     - 80
 
