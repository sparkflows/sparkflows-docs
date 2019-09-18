FilterByStringLength
=========== 

This node filters the Rows within the given string length. The column to be used for determining the string length is specified

Input
--------------
It accepts a DataFrame as input from the previous Node

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeFilterByStringLength

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
      * - minLength
        - Minimum length
        - Minimum length of String
      * - maxLength
        - Maximum length
        - Maximum length of String


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
     
   * - Stefan
     - 7
     - 80  

Parameters
----------


.. list-table:: 
   :widths: 10 10
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Input Column Name
     - name
     
   * - Minimum length
     - 6
     
   * - Maximum length
     - 10


Output
------

.. list-table:: 
   :widths: 10 20 10
   :header-rows: 1

   * - Stefan
     - 7
     - 80 
