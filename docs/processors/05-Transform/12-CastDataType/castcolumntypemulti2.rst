MultiCastColumnType2
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

fire.nodes.etl.NodeMultiCastColumnType2

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputColNames
        - Columns
        - Columns
      * - outputColTypes
        - New Data Type
        - New data type(INTEGER, DOUBLE, STRING, LONG, SHORT)
      * - replaceExistingCols
        - Replace Existing Cols
        - Whether to replace existing Columns or create New Ones
      * - formats
        - Formats
        - Formats like yyy-MM-dd used in input & output

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

Parameters
----------


.. list-table:: 
   :widths: 10 10 20 20 20
   :header-rows: 1
   
   * - RowID
     - Columns
     - New Data Type
     - Replace Existing Cols
     - Formats
     
   * - 1
     - age
     - DOUBLE
     - true
     - 
     
   * - 2
     - height
     - DOUBLE
     - false
     - 

Output
--------

.. list-table:: 
   :widths: 10 10 10 10
   :header-rows: 2

   * - name
     - height
     - age
     - height-new
 
   * - DoubleType
     - StringType
     - DoubleType
     - DoubleType
     
   * - Alice
     - 80
     - 5.0
     - 80.0
   
   * - Alice
     - 80
     - 5.0
     - 80.0
     
   * - Alice
     - 80
     - 10.0
     - 80.0


