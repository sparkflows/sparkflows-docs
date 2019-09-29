Hash
=========== 

This node adds a new Columns which contains the Hash of the specified columns

Input
--------------
It accepts a DataFrame as input from the previous Node

Output
--------------
A new column is added to the incoming DataFrame by creating a Hash of the specified input columns.

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeHash

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
        - Columns to be concatenated
      * - hashingAlgorithm
        - Hashing Algorithm
        - Hashing Algorithm SHA2 & MD5, by default MD5)
      * - outputCol
        - Output Column Name
        - Column name for Hash
      * - bitLength
        - Bit Length
        - Bit Length(used in SHA2) and Hashing node bitLength-(0, 224, 256, 384, 512)
      * - sep
        - Separator
        - Separator to be used when concatenating the columns


Examples
---------

Input
--------------

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

Parameters1
------------

.. list-table:: 
   :widths: 20 30
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Columns
     - f1 f2
     
   * - Hashing Algorithm
     - SH2
     
   * - Output Column Name
     - sh2_hash
     
   * - Bit Length
     - 0
     
   * - separator
     - 

Output1
--------------

.. list-table:: 
   :widths: 20 20 20 20 60
   :header-rows: 1

   * - id
     - label
     - f1
     - f2
     - sh2_hash
     
   * - 6
     - 1.0
     - 2.1
     - 2.0
     - 1476beec9dd8dc61bb617ba15e068e43ad918c83cc543d290f45a219d603e75c
   
   * - 4
     - 0.0
     - 4.1
     - 5.0
     - fcfeacf3a36da93855bf43bca5b6942e09f76330692d8a666a0215d3ce05889f
     
   * - 5
     - 0.0
     - 3.1
     - 6.0
     - a7c8371a5a7b55d0f4e5dff4e083b5d3c82f83b025ff26f4123bd4c348a8bbb2
      
   * - 66
     - 1.0
     - 2.1
     - 2.0
     - 1476beec9dd8dc61bb617ba15e068e43ad918c83cc543d290f45a219d603e75c
     
------------------------------------------------------------------------------------- 
 
 Parameters2
------------

.. list-table:: 
   :widths: 20 30
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Columns
     - f1 f2
     
   * - Hashing Algorithm
     - MD5
     
   * - Output Column Name
     - md5_hash
     
   * - Bit Length
     - 
     
   * - separator
     - 

Output2
--------------

.. list-table:: 
   :widths: 20 20 20 20 60
   :header-rows: 1

   * - id
     - label
     - f1
     - f2
     - md5_hash
     
   * - 6
     - 1.0
     - 2.1
     - 2.0
     - 32d7edaf74fd94509361bcd1f0c56763
   
   * - 4
     - 0.0
     - 4.1
     - 5.0
     - f2880da79c8d1c255c1afdba28a9001e
     
   * - 5
     - 0.0
     - 3.1
     - 6.0
     - c5c2c80d0b26cecafe376dc4cdc91e6f
      
   * - 66
     - 1.0
     - 2.1
     - 2.0
     - 32d7edaf74fd94509361bcd1f0c56763
     
