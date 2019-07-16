VectorAssembler
=========== 

Merges multiple columns into a vector column

Input
--------------
It takes in a DataFrame and transforms it to another DataFrame

Output
--------------
It adds a new column to the incoming DataFrame. The new column contains the values of the input columns concatenated into a vector in the specified order.

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodeVectorAssembler

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCols
        - Input Columns
        - Input column of type - all numeric, boolean and vector
      * - outputCol
        - Output Column
        - Output column name




