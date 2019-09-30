SortBy
=========== 

It sorts the incoming DataFrame on the fields specified.

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeSortBy

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - description
        - Description
        - Description
      * - sortByColNames
        - Columns
        - Columns on which to Sort By
      * - ascDesc
        - Sorting Order
        - Whether to sort in ascending or descending order


Examples
---------

Input
--------

.. list-table:: 
   :widths: 20 20 20 20
   :header-rows: 1

   * - id
     - label
     - f1
     - f2
     
   * - 6
     - 1.0
     - 2.1
     - 2.0
   
   * - 4
     - 0.0
     - 4.1
     - 5.0
     
   * - 5
     - 0.0
     - 3.1
     - 6.0
      
   * - 66
     - 1.0
     - 2.1
     - 2.0


Parameters
------------

.. list-table:: 
   :widths: 20 30
   :header-rows: 1
   
   * - Columns
     - Sorting Order
     
   * - id
     - desc
     
   * - label
     - asc

Output
--------

.. list-table:: 
   :widths: 20 20 20 20
   :header-rows: 1

   * - id
     - label
     - f1
     - f2
   
   * - 66
     - 1.0
     - 2.1
     - 2.0
   
   * - 6
     - 1.0
     - 2.1
     - 2.0
 
   * - 5
     - 0.0
     - 3.1
     - 6.0
              
   * - 4
     - 0.0
     - 4.1
     - 5.0  
