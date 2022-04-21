Count Vectorizer
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


CountVectorizer and CountVectorizerModel aim to help convert a collection of text documents to vectors of token counts. When an a-priori dictionary is not available, CountVectorizer can be used as an Estimator to extract the vocabulary and generates a CountVectorizerModel. 
The model produces sparse representations for the documents over the vocabulary, which can then be passed to other algorithms like LDA.

More at Spark MLlib/ML docs page : https://spark.apache.org/docs/latest/ml-features.html#countvectorizer


Examples
-------


The below example is available at : https://spark.apache.org/docs/latest/ml-features.html#countvectorizer
+++++++++++++++


import org.apache.spark.ml.feature.{CountVectorizer, CountVectorizerModel}

val df = spark.createDataFrame(Seq(
  (0, Array("a", "b", "c")),
  (1, Array("a", "b", "b", "c", "a"))
)).toDF("id", "words")

// fit a CountVectorizerModel from the corpus
val cvModel: CountVectorizerModel = new CountVectorizer()
  .setInputCol("words")
  .setOutputCol("features")
  .setVocabSize(3)
  .setMinDF(2)
  .fit(df)

// alternatively, define CountVectorizerModel with a-priori vocabulary
val cvm = new CountVectorizerModel(Array("a", "b", "c"))
  .setInputCol("words")
  .setOutputCol("features")

cvModel.transform(df).show(false)
