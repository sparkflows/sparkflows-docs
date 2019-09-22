GroupBy
=========== 

Grouper Node

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeGroupBy

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
      * - aggregateCols
        - Aggregate Columns
        - Aggregate Columns
      * - aggregateOperations
        - Aggregate Operation to Use
        - Aggregate Operation
      * - havingClause
        - Having Clause
        - having condition after group by function
      * - whereClause
        - Where Clause
        - where condition before group by function


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
   
   * - Grouping Columns
     - name
     
   * - Having Clause
     -
     
   * - Where Clause
     -

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
   
   * - 3
     - name
     - count 
   

Output1
---------

.. list-table:: 
   :widths: 20 20 20 20
   :header-rows: 1

   * - name
     - max_age
     - min_height
     - count_name
     
   * - James
     - 10
     - 50
     - 3
     
   * - Alice
     - 10
     - 80
     - 3
     
     
-------------------------------------------------------------------


Parameters2
-------------

.. list-table:: 
   :widths: 10 25
   :header-rows: 1

   * - Name
     - Value
   
   * - Grouping Columns
     - name
     
   * - Having Clause
     -
     
   * - Where Clause
     - (age = 5 or age = 7) and height != 50

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
   
   * - 3
     - name
     - count 
   

Output2
---------

.. list-table:: 
   :widths: 20 20 20 20
   :header-rows: 1

   * - name
     - max_age
     - min_height
     - count_name
     
   * - James
     - 7
     - 80
     - 1
     
   * - Alice
     - 5
     - 80
     - 2
 
-----------------------------------------------------------------------------

