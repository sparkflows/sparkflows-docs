FindAndReplaceUsingRegexMultiple
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

fire.nodes.etl.NodeFindAndReplaceUsingRegexMultiple

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
      * - searchPatterns
        - Find
        - Enter Search Pattern
      * - replacePatterns
        - Replace
        - Enter replacement Value


Examples
----------

Input
---------

.. list-table:: 
   :widths: 20 20 20
   :header-rows: 2

   * - name
     - age
     - height
     
   * - StringType
     - IntegerType
     - StringType
     
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
   :widths: 10 30 20 20
   :header-rows: 1
   
   * - Id
     - Input Columns
     - Find
     - Replace
     
   * - 1
     - name
     - Al*
     - Jim
     
   * - 2
     - height
     - 80
     - 60 


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
     - 60
     
   * - Jimice
     - 5
     - 60
     
   * - Jimice
     - 10
     - 60
     
   * - James
     - 5
     - 50
     
   * - James
     - 10
     - 60
    
   * - James
     - 7
     - 60



