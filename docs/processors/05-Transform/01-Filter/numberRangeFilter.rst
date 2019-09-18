FilterByNumberRange
=========== 

This node filter Rows in the given Number Range

Input
--------------
It accepts a DataFrame as input from the previous Node

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeFilterByNumberRange

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCol
        - Input Column Name
        - input column name
      * - lowestValue
        - Lowest Value
        - input lowest value
      * - highestValue
        - Highest Value
        - input highest value


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

Parameters
----------


.. list-table:: 
   :widths: 10 10 10 10
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Input Column Name
     - age
     
   * - Lowest Value
     - 7
     
   * - Highest Value
     - 10


Output
------

.. list-table:: 
   :widths: 10 20 10
   :header-rows: 1

   * - name
     - age
     - height
   
   * - Alice
     - 10
     - 80
     
   * - James
     - 10
     - 60
    
   * - James
     - 7
     - 80




