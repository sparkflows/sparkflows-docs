CountVectorizer
=========== 

Extracts the vocabulary from a given collection of documents and generates a vector of token counts for each document.

Input
--------------
It takes in a DataFrame as input and transforms it to another DataFrame

Output
--------------
It adds a new column to the incoming DataFrame containing the vector of token counts in the input column, to generate the output DataFrame

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodeCountVectorizer

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
        - Input column name
      * - outputCol
        - Output Column
        - Output column name
      * - vocabularySize
        - Vocabulary Size
        - Max size of the vocabulary.


Details
-------


CountVectorizer and CountVectorizerModel aim to help convert a collection of text documents to vectors of token counts. When an a-priori dictionary is not available, CountVectorizer can be used as an Estimator to extract the vocabulary and generates a CountVectorizerModel. The model produces sparse representations for the documents over the vocabulary, which can then be passed to other algorithms like LDA.

More at Spark MLlib/ML docs page : https://spark.apache.org/docs/latest/ml-features.html#countvectorizer


