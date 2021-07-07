IDF
=========== 

Compute the Inverse Document Frequency (IDF) given a collection of documents.

Input
--------------
It takes in a DataFrame and transforms it to another DataFrame

Output
--------------
The output DataFrame contains a new column of type vector, It takes feature vectors (generally created from HashingTF) as input and scales each column. Intuitively, it down-weights columns which appear frequently in a corpus.

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodeIDF

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
        - Input Column Name
      * - outputCol
        - Output Column
        - Output column name
      * - minDocFreq
        - MinDocFreq
        - The minimum of documents in which a term should appear.




