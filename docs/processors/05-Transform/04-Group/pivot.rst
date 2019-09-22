PivotBy
=========== 

Pivot Node

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodePivotBy

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - groupingCols
        - Grouping Columns
        - Grouping Columns
      * - pivotCols
        - Pivot Columns
        - Pivoting Columns
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
     
 
Parameters
-------------

.. list-table:: 
   :widths: 10 25
   :header-rows: 1

   * - Name
     - Value
   
   * - Grouping Columns
     - name
     
   * - Pivot Columns
     - age
    
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
   

Output
---------

.. list-table:: 
   :widths: 20 10 10 10
   :header-rows: 1

   * - name
     - 5
     - 7
     - 10
     
   * - James
     - 50
     - 80
     - 60
     
   * - Alice
     - 80
     - 
     - 50
     
