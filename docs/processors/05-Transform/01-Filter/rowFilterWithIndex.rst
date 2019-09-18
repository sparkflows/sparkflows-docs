NodeRowFilterByIndex
=========== 

This node creates a new DataFrame containing only rows satisfying given condition

Input
--------------
It accepts DataFrame as input from the previous Node

Output
--------------
This node filters the rows based on the conditional expression to generate the output DataFrame

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeRowFilterByIndex

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - indexes
        - Indexes
        - Comma separated index values starts from 0. ex: 0, 1, 2, 5
      * - indexesRange
        - IndexesRange
        - Index ranges example like 10-14 i.e 10, 11, 12, 13, 14.


Examples
---------

Input
--------------

.. list-table:: 
   :widths: 10 20 10
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
----------


.. list-table:: 
   :widths: 10 10
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Indexes
     - 0,2
     
   * - IndexesRange
     - 


Output1
--------------

.. list-table:: 
   :widths: 10 20 10
   :header-rows: 1

   * - name
     - age
     - height
   
   * - Alice
     - 5
     - 80
     
   * - Alice
     - 10
     - 80



Parameters2
----------


.. list-table:: 
   :widths: 10 10
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Indexes
     - 0,2
     
   * - IndexesRange
     - 4-5


Output2
--------------

.. list-table:: 
   :widths: 10 20 10
   :header-rows: 1

   * - name
     - age
     - height
   
   * - Alice
     - 5
     - 80
      
   * - Alice
     - 10
     - 80
          
   * - James
     - 10
     - 60
    
   * - James
     - 7
     - 80
