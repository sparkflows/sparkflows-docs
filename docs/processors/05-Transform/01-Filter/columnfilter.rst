ColumnFilter
=========== 

This node creates a new DataFrame that contains only the selected columns

Input
--------------
This type of node takes in a DataFrame and transforms it to another DataFrame.

Output
--------------
This node filters the specified columns from the incoming DataFrame

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeColumnFilter

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - outputCols
        - Columns
        - Columns to be included in the output DataFrame

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
     - name,height


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


