CastColumnType
=========== 

This node creates a new DataFrame by casting input columns with a new data type

Input
--------------
This type of node takes in a DataFrame and transforms it to another DataFrame

Output
--------------
This node casts the data type of columns as specified

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeCastColumnType

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCols
        - Columns
        - Columns to be cast to new data type
      * - outputColType
        - New Data Type
        - New data type(INTEGER, DOUBLE, STRING, LONG, SHORT)
      * - replaceExistingCols
        - Replace Existing Cols
        - Whether to replace existing columns or create new ones

Examples
---------

Input
--------------

.. list-table:: 
   :widths: 10 20 10
   :header-rows: 2

   * - name
     - age
     - height
   
   * - StringType
     - StringType
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

Parameters1
----------


.. list-table:: 
   :widths: 10 10
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Columns
     - age,height
     
   * - New Data Type
     - DOUBLE

   * - Replace Existing Cols
     - true

Output1
--------------

.. list-table:: 
   :widths: 10 20 10
   :header-rows: 2

   * - name
     - age
     - height
 
   * - DoubleType
     - DoubleType
     - DoubleType
     
   * - Alice
     - 5.0
     - 80.0
   
   * - Alice
     - 5.0
     - 80.0
     
   * - Alice
     - 10.0
     - 80.0


Parameters2
----------


.. list-table:: 
   :widths: 10 10
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Columns
     - age,height
     
   * - New Data Type
     - DOUBLE

   * - Replace Existing Cols
     - false

Output2
--------------

.. list-table:: 
   :widths: 10 10 10 10 10
   :header-rows: 2

   * - name
     - age
     - height
 
   * - DoubleType
     - StringType
     - StringType
     - DoubleType
     - DoubleType
     
   * - Alice
     - 5
     - 80
     - 5.0
     - 80.0
   
   * - Alice
     - 5
     - 80
     - 5.0
     - 80.0
     
   * - Alice
     - 10
     - 80
     - 10.0
     - 80.0


