Tokenizer
=========== 

A tokenizer that converts the input string to lowercase and then splits it by white spaces.

Input
--------------
It takes in a DataFrame and transforms it to another DataFrame

Output
--------------
It adds a new column containing the results of tokenization of the input column, to the incoming DataFrame.

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodeTokenizer

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
        - Column containing text (such as sentence)
      * - outputCol
        - Output Column
        - Output column name




