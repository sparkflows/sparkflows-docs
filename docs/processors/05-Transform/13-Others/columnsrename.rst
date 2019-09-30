ColumnsRename
=========== 

This node creates a new DataFrame by renaming existing columns with new name

Input
--------------
This type of node takes in a DataFrame and transforms it to another DataFrame.

Output
--------------
The specified columns are renamed to have the new names.

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeColumnsRename

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - currentColNames
        - Current Column Names
        - Current Column Names
      * - newColNames
        - Columns New Name
        - New name for existing columns

Examples
---------

Input
--------

.. list-table:: 
   :widths: 20 20 20 20
   :header-rows: 1

   * - id
     - label
     - f1
     - f2
     
   * - 6
     - 1.0
     - 2.1
     - 2.0
   
   * - 4
     - 0.0
     - 4.1
     - 5.0
     
   * - 5
     - 0.0
     - 3.1
     - 6.0
      
   * - 66
     - 1.0
     - 2.1
     - 2.0


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

Output
--------

.. list-table:: 
   :widths: 20 20 20 20
   :header-rows: 1

   * - id
     - label
     - new_f1
     - new_f2
     
   * - 6
     - 1.0
     - 2.1
     - 2.0
   
   * - 4
     - 0.0
     - 4.1
     - 5.0
     
   * - 5
     - 0.0
     - 3.1
     - 6.0
 
   * - 66
     - 1.0
     - 2.1
     - 2.0



