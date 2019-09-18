DropColumns
=========== 

This node creates a new DataFrame by deleting columns specified as an input

Input
--------------
It takes in a DataFrame as input

Output
--------------
The specified columns are dropped from the incoming DataFrame to generate the output DataFrame

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeDropColumns

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - dropCols
        - Columns
        - The columns to be excluded from the output DataFrame

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

Parameters
----------


.. list-table:: 
   :widths: 10 20
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Columns
     - age


Output
--------------

.. list-table::
   :widths: 10 10
   :header-rows: 1
   
   * - name
     - height
   
   * - Alice
     - 80
     
   * - Alice
     - 80
     
   * - Alice
     - 80



