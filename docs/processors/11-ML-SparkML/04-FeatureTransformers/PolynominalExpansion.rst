PolynominalExpansion
=========== 

Perform feature expansion in a polynomial space

Input
--------------
It takes in a DataFrame and transforms it to another DataFrame

Output
--------------
The output DataFrame contains a new column of type vector, Expanding your features into a polynomial space, which is formulated by an n-degree combination of original dimensions.

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodePolynominalExpansion

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCol
        - Input Column
        - The input column name
      * - outputCol
        - Output Column
        - The output column name
      * - degree
        - Degree
        - The polynomial degree to expand, which should be >= 1. A value of 1 means no expansion.




