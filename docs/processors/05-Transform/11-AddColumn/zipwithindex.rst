ZipWithIndex
=========== 

This node Generates a new column with unique Index/Value for each row in the Dataset

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeZipWithIndex

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - indexColName
        - Index Column Name
        - Index column name


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
     
   * - Index Column Name
     - row_id

Output
--------

.. list-table:: 
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - id
     - label
     - f1
     - f2
     - row_id
     
   * - 6
     - 1.0
     - 2.1
     - 2.0
     - 0
   
   * - 4
     - 0.0
     - 4.1
     - 5.0
     - 1
     
   * - 5
     - 0.0
     - 3.1
     - 6.0
     - 2
      
   * - 66
     - 1.0
     - 2.1
     - 2.0
     - 3
     
     
     
