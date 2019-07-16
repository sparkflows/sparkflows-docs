StringIndexer
=========== 

StringIndexer encodes a string column of labels to a column of label indices

Input
--------------
It takes in a DataFrame and transforms it to another DataFrame

Output
--------------
It adds a new column containing the encoding of the string column of labels to a column of label indices, to the incoming DataFrame.

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodeStringIndexer

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - handleInvalid
        - Handle Invalid
        - Invalid entries to be skipped or thrown error
      * - inputCols
        - Input Columns
        - Column containing labels
      * - outputCols
        - Output Columns
        - Output  columns




