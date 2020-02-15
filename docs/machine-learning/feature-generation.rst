Feature Generation
==================

Feature generation is the process of creating new features from one or multiple existing features, potentially for using in statistical analysis. This process adds new information to be accessible during the model construction and therefore hopefully result in more accurate model.

Fire Insights provides a number of processors for Feature Generation. These include:

.. list-table:: Below are the Relevant Files
   :widths: 10 20 40
   :header-rows: 1

   * - Title
     - Description
     - File
   * - emr-file-mysql.json
     - CloudFormation Template
     - https://s3.amazonaws.com/sparkflows-cft/mysql-db/emr-fire-mysql.json
   * - deploy-fire-mysql.sh
     - Script for deploying Fire with MySQL
     - https://s3.amazonaws.com/sparkflows-cft/mysql-db/deploy-fire-mysql.sh
   * - script-runner.jar
     - Script Runner
     - https://s3.amazonaws.com/sparkflows-cft/mysql-db/script-runner.jar

- DateToAge : Convert Date to Age
- CaseWhen : Based on the value, convert it to another value
- Scala : Write Scala code in Spark for generating new Features
- SQL : Write SQL code for generating new Features
- StopWordRemover : Removes Stop Words
- Tokenizer : Tokenizes a string into Tokens
- OneHotEncoder : Applies one hot encoding
- TF/IDF : Finds the TF and IDF
- IndexString : Converts a column containing String to numeric values

