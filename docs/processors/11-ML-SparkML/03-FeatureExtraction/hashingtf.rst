HashingTF
=========== 

Maps a sequence of terms to term frequencies using the hashing trick.

Input
--------------
It takes in a DataFrame as input and transforms it to another DataFrame

Output
--------------
A new column is added to the input DataFrame containing hashing of the bag of words into a feature vector

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodeHashingTF

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
        - Contains sets of terms. In text processing, a 'set of terms' might be a bag of words
      * - outputCol
        - Output Column
        - Output column name




