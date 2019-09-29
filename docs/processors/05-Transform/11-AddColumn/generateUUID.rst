GenerateUUID
=========== 

This node Generates a Universally Unique ID

Input
--------------
It accepts a dataframe as input

Output
--------------
It adds a new column for UUID to the input DataFrame. This new DataFrame is sent to the output

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeGenerateUUID

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
        
      * - outputCol
        - Output Column
        - Output Column Name

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
     
   * - Output Column
     - UUID


Output
--------

.. list-table:: 
   :widths: 20 20 20 20 70
   :header-rows: 1

   * - id
     - label
     - f1
     - f2
     - UUID
     
   * - 6
     - 1.0
     - 2.1
     - 2.0
     - 4a3fb350-d18c-4984-9ed6-799ef15cf4a3
   
   * - 4
     - 0.0
     - 4.1
     - 5.0
     - 5de0c6c7-1787-436e-a0fc-9220ff6147ad
     
   * - 5
     - 0.0
     - 3.1
     - 6.0
     - 1542c223-c8ba-456a-af4f-e3c09aca357c
      
   * - 66
     - 1.0
     - 2.1
     - 2.0
     - 91cbe234-7bf8-4e7d-9b2f-10f276c80f51
     
     
