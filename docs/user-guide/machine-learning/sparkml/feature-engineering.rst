Feature Engineering
==================

Feature engineering is the process of creating new features from one or multiple existing features, potentially for use in statistical analysis. This process adds new information to be accessible during the model construction and therefore hopefully result in a more accurate model.

Sparkflows provides several processors for feature engineering.

.. list-table:: Feature Engineering Processors in Sparkflows
   :widths:  20 80
   :header-rows: 1

   * - Title
     - Description
   * - DateToAge
     - Convert Date to Age.
   * - CaseWhen 
     - Based on the value, convert it to another value.
   * - Scala
     - Write Scala code in Spark for generating new Features.
   * - SQL
     - Write SQL code for generating new features.
   * - StopWordRemover
     - Removes Stop Words.
   * - Tokenizer
     - Tokenizes a string into Tokens.
   * - OneHotEncoder
     - Applies one hot encoding.
   * - TF/IDF
     - Finds the TF and IDF.
   * - IndexString
     - Converts a column containing string to numeric values.
     

Tokenizer
---------

Tokenization is the process of taking text (such as a sentence) and breaking it into individual terms (usually words). 

More details are available at the Spark MLlib/ML docs page: https://spark.apache.org/docs/latest/ml-features#tokenizer


Stop Word Remover
-----------------

Stop words filters out stop words from input. Null values from input array are preserved unless adding null to stopWords explicitly.

More details are available at the Spark MLlib/ML docs page: https://spark.apache.org/docs/latest/ml-features#stopwordsremover


OneHotEncoder
-------------

One-hot encoding maps a categorical feature, represented as a label index, to a binary vector with at most a single one-value indicating the presence of a specific feature value from among the set of all feature values. This encoding allows algorithms which expect continuous features, such as Logistic Regression, to use categorical features. For string type input data, it is common to encode categorical features using StringIndexer first.

More details are available at the Spark MLlib/ML docs page: https://spark.apache.org/docs/latest/ml-features#onehotencoder
