Split
=========== 

This node splits the incoming DataFrame into 2. It takes in the fraction to use in splitting the data. For example, if the fraction is .7, it would split the data into 2 DataFrames, one containing 70% of the rows and the other containing the remaining 30%.

Input
--------------
It takes in a DataFrame as input

Output
--------------
The input DataFrame is split into 2 DataFrames and output

Type
--------- 

transform

Class
--------- 

fire.nodes.ml.NodeSplit

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - fraction1
        - Fraction 1
        - Fraction to be used for Splitting the DataFrame into two. The first DataFrame would go to the lower edge output. The other would go to the higher edge output.
        
 
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
     
   * - Fraction 1
     - 0.8


Output1
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
      
     
 Output2
--------

.. list-table:: 
   :widths: 20 20 20 20
   :header-rows: 1

   * - id
     - label
     - f1
     - f2
     
   * - 66
     - 1.0
     - 2.1
     - 2.0    


