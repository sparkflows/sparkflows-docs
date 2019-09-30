WindowAnalytics
=========== 



Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeWindowAnalytics

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - partitionByCols
        - PartitionBy
        - partition column names separated by comma(,) 
      * - orderByCols
        - OrderBy
        - order by column names separated by comma(,)
      * - windowFunction
        - Window Function
        - Window Function Name
      * - analyticsCol
        - Analytics Column
        - 

Examples
---------

Input
--------

.. list-table:: 
   :widths: 20 20 20 20 20 20
   :header-rows: 1

   * - id
     - price
     - bedrooms
     - bathrms
     - stories
     
   * - 1
     - 42000
     - 3
     - 1
     - 2
   
   * - 2
     - 38500
     - 2
     - 1
     - 1
  
   * - 3
     - 49500
     - 3
     - 1
     - 1
  
   * - 4
     - 60500
     - 3
     - 1
     - 2
     
   * - 5
     - 61000
     - 2
     - 1
     - 1
  
   * - 6
     - 66000
     - 3
     - 1
     - 1

   * - 7
     - 66000
     - 3
     - 2
     - 2
     
Parameters
------------

.. list-table:: 
   :widths: 20 30
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Current Column Names
     - f1 f2
     
   * - Columns New Name
     - new_f1 new_f2




