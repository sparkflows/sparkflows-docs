ConcatColumns
=========== 

This node creates a new DataFrame by concatenating the specified columns of the input DataFrame

Input
--------------
It accepts a DataFrame as input from the previous Node

Output
--------------
A new column is added to the incoming DataFrame by concatenating the specified columns. The new DataFrame is sent to the output of this Node.

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeConcatColumns

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
      * - outputCol
        - Concatenated Column Name
        - Column name for the concatenated columns
      * - sep
        - Separator
        - Separator to be used when concatenating the columns


Examples
---------

Input
--------

.. list-table:: 
   :widths: 20 20 20 20
   :header-rows: 1

   * - site_id
     - app_id
     - site_domain
     - site_category
     
   * - 1fbe01fe
     - ecad2386 
     - f3845767 
     - 28905ebd
     
   * - 1fbe01fe
     - ecad2386
     - f3845767
     - 28905ebd 
   
   * - fe8cc448
     - ecad2386
     - 9166c161
     - 0569f928
     
   * - d6137915
     - ecad2386
     - bb1ef334
     - f028772b
     
Parameters
------------

.. list-table:: 
   :widths: 20 30
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Columns
     - site_id app_id

   * - Concatenated Column Name
     - site_id_app_id
     
   * - Separator
     - |
     
Output
---------
 
.. list-table:: 
   :widths: 20 20 20 20
   :header-rows: 1

   * - site_id
     - app_id
     - site_domain
     - site_category
     
   * - 1fbe01fe
     - ecad2386 
     - f3845767 
     - 28905ebd
     - 1fbe01fe|ecad2386 
     
   * - 1fbe01fe
     - ecad2386
     - f3845767
     - 28905ebd 
     - 1fbe01fe|ecad2386
   
   * - fe8cc448
     - ecad2386
     - 9166c161
     - 0569f928
     - fe8cc448|ecad2386
     
   * - d6137915
     - ecad2386
     - bb1ef334
     - f028772b
     - d6137915|ecad2386 
 
