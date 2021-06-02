Feature Generation
==================

Feature generation is the process of creating new features from one or multiple existing features, potentially for use in statistical analysis. This process adds new information to be accessible during the model construction and therefore hopefully result in a more accurate model.

Fire  Insights provides several processors for Feature Generation

.. list-table:: Feature Generation Processors in Fire Insights
   :widths:  20 80
   :header-rows: 1

   * - Title
     - Description
   * - DateToAge
     - Convert Date to Age
   * - CaseWhen 
     - Based on the value, convert it to another value
   * - Scala
     - Write Scala code in Spark for generating new Features
   * - SQL
     - Write SQL code for generating new features
   * - StopWordRemover
     - Removes Stop Words
   * - Tokenizer
     - Tokenizes a string into Tokens
   * - OneHotEncoder
     - Applies one hot encoding
   * - TF/IDF
     - Finds the TF and IDF
   * - IndexString
     - Converts a column containg String to numeric values
     
