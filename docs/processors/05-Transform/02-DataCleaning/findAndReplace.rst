FindAndReplaceUsingRegex
=========== 

This node finds and replaces text in a column containing string

Input
--------------
It accepts a DataFrame as input from the previous Node

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeFindAndReplaceUsingRegex

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCols
        - Input Columns
        - Columns on which to apply Regex
      * - searchPattern
        - Find
        - Enter Search Pattern
      * - replacePattern
        - Replace
        - Enter replacement Value

Examples
---------

Input1
---------

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
-------------


.. list-table:: 
   :widths: 10 10
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Input Columns
     - name
   
   * - Find
     - Al*
   
   * - Replace
     - Jim


Output1
---------

.. list-table:: 
   :widths: 10 20 10
   :header-rows: 1

   * - name
     - age
     - height
   
   * - Jimice
     - 5
     - 80
     
   * - Jimice
     - 5
     - 80
     
   * - Jimice
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


Input2
---------

.. list-table:: 
   :widths: 10 20 10
   :header-rows: 1

   * - id
     - prodId
     - message
   
   * - 1.0
     - 2.0
     - this is a spam
     
   * - 0.0
     - 1.0
     - i am going to work
     

Parameters2
-------------


.. list-table:: 
   :widths: 10 10
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Input Columns
     - name
   
   * - Find
     - \\s
   
   * - Replace
     - `*`



Output2
---------

.. list-table:: 
   :widths: 10 20 10
   :header-rows: 1

   * - id
     - prodId
     - message
   
   * - 1.0
     - 2.0
     - this*is*a*spam
     
   * - 0.0
     - 1.0
     - i*am*going*to*work
