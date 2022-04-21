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


Details
-------


Tokenization is the process of taking text (such as a sentence) and breaking it into individual terms (usually words). 
                                                                                                  
More at Spark MLlib/ML docs page : https://spark.apache.org/docs/2.0.0/ml-features.html#tokenizer


Examples
-------


The below example is available at : https://spark.apache.org/docs/2.0.0/ml-features.html#tokenizer
+++++++++++++++

import org.apache.spark.ml.feature.{RegexTokenizer, Tokenizer}

val sentenceDataFrame = spark.createDataFrame(Seq(
  (0, "Hi I heard about Spark"),
  (1, "I wish Java could use case classes"),
  (2, "Logistic,regression,models,are,neat")
)).toDF("label", "sentence")

val tokenizer = new Tokenizer().setInputCol("sentence").setOutputCol("words")
val regexTokenizer = new RegexTokenizer()
  .setInputCol("sentence")
  .setOutputCol("words")
  .setPattern("\\W") // alternatively .setPattern("\\w+").setGaps(false)

val tokenized = tokenizer.transform(sentenceDataFrame)
tokenized.select("words", "label").take(3).foreach(println)
val regexTokenized = regexTokenizer.transform(sentenceDataFrame)
regexTokenized.select("words", "label").take(3).foreach(println)
