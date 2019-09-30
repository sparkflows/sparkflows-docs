TextCaseTransformer
=========== 

This node converts text to upper or lower case

Input
--------------
It accepts a DataFrame as input from the previous Node

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeTextCaseTransformer

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
      * - mode
        - Text Case Type
        - input to convert text to upper or lower case
      * - outputCol
        - Output Column
        - Output Column


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

Parameters1
----------


.. list-table:: 
   :widths: 10 20
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Input Column Name
     - name
    
   * - Text Case Type
     - upper
     
   * - Output Column
     - name_upper


Output1
--------------

.. list-table:: 
   :widths: 10 20 10 10
   :header-rows: 1

   * - name
     - age
     - height
     - name_upper
   
   * - Alice
     - 5
     - 80
     - ALICE
     
   * - Alice
     - 5
     - 80
     - ALICE
     
   * - Alice
     - 10
     - 80
     - ALICE


-------------------------------------------------------------------------------


Parameters2
------------


.. list-table:: 
   :widths: 10 20
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Input Column Name
     - name
    
   * - Text Case Type
     - lower
     
   * - Output Column
     - name_lower


Output2
--------------

.. list-table:: 
   :widths: 10 20 10 10
   :header-rows: 1

   * - name
     - age
     - height
     - name_lower
   
   * - Alice
     - 5
     - 80
     - alice
     
   * - Alice
     - 5
     - 80
     - alice
     
   * - Alice
     - 10
     - 80
     - alice
     
     
