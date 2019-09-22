Math Expression
=========== 



Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeMathExpression

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - outputCols
        - OutPut Column
        - Output Column Name
      * - expressions
        - Math Expression
        - Define math expression.


Examples
----------

Input
---------

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
   :widths: 10 25 25
   :header-rows: 1

   * - Id
     - OutPut Column
     - Math Expression
   
   * - 1
     - squre_of_age
     - age * age
     
   * - 2
     - add_height
     - height + 10

   * - 3
     - minus_height
     - height - 10
    
Output
---------

.. list-table:: 
   :widths: 20 20 20 40 40 40
   :header-rows: 1

   * - name
     - age
     - height
     - squre_of_age
     - add_height
     - minus_height
     
   * - Alice
     - 5
     - 80
     - 25
     - 90
     - 70 
     
   * - Alice
     - 5
     - 80
     - 25
     - 90
     - 70
     
   * - Alice
     - 10
     - 80
     - 100
     - 90
     - 70
     
   * - James
     - 5
     - 50
     - 25
     - 60
     - 40
     
   * - James
     - 10
     - 60
     - 100
     - 70
     - 50
    
   * - James
     - 7
     - 80
     - 49
     - 90
     - 70
