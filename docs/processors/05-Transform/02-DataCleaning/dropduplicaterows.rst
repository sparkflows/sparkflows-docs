DropDuplicateRows
=========== 

This node creates a new DataFrame by dropping duplicate rows

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeDropDuplicateRows

Input
--------
A DataFrame to filter rows on duplicate.

Output
--------
A DataFrame containing no duplicate row on the selected coulmns.

Fields
---------- 

.. list-table:: 
   :widths: 10 30 40
   :header-rows: 1

   * - Name
     - Type
     - Description
   
   * - COLUMNS
     - Seq of Coulmns
     - Seq of Coulmns to check the duplicate condition.(By default duplication checked on all the columns)
   
Examples
--------

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
     
   * - COLUMNS
     - name,height


Output1
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
   
Parameters2
----------


.. list-table:: 
   :widths: 10 20
   :header-rows: 1
   
   * - Name
     - Value
     
   * - COLUMNS
     - 


Output2
-------

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
     - 10
     - 80
   
