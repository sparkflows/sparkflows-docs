Word2Vec
=========== 

Transforms vectors of words into vectors of numeric codes for the purpose of further processing by NLP or machine learning algorithms.

Input
--------------
It takes in a DataFrame as input and transforms it to another DataFrame

Output
--------------
A new column containing feature vector is added to the incoming DataFrame

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodeWord2Vec

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
        - Contains sequences of words
      * - inputColStringArrCol
        - Text Array Column
        - The text array column which is produced
      * - outputCol
        - Output Column
        - Output column name
      * - vectorSize
        - Vector Size
        - Vector Size
      * - minCount
        - Min Count
        - Min Count


Details
======


Word2Vec is an Estimator which takes sequences of words representing documents and trains a Word2VecModel. The model maps each word to a unique fixed-size vector. The Word2VecModel transforms each document into a vector using the average of all words in the document; this vector can then be used for as features for prediction, document similarity calculations, etc.

More at Spark MLlib/ML docs page : http://spark.apache.org/docs/latest/ml-features.html#word2vec


