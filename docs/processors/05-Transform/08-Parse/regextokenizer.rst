RegexTokenizer
=========== 

This node creates a new DataFrame by the process of taking text (such as a sentence) and breaking it into individual terms (usually words) based on regular express

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeRegexTokenizer

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCol
        - Column
        - input column for tokenizing
      * - outputCol
        - Tokenized Column
        - New output column after tokenization
      * - pattern
        - Pattern
        - The regex pattern used to match delimiters
      * - gaps
        - Gaps
        - Indicates whether the regex splits on gaps



Examples
---------

Input
--------------

.. list-table:: 
   :widths: 10 40 10
   :header-rows: 2

   * - label
     - message
     - id
   
   * - DoubleType
     - StringType
     - DoubleType
     
   * - 1.0
     - this is a spam
     - 2.0
     
   * - 0.0
     - i am going to work
     - 1.0
     
   
Parameters
----------


.. list-table:: 
   :widths: 10 10
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Column
     - message
     
   * - Tokenized Column
     - token_output 
     
   * - Pattern
     - \\s+
     
   * - Gaps
     - false
     
     
Output
--------------

.. list-table:: 
   :widths: 10 40 10 50
   :header-rows: 2

   * - label
     - message
     - id
     - token_output
   
   * - DoubleType
     - StringType
     - DoubleType
     - ArrayType(StringType,true)
     
   * - 1.0
     - this is a spam
     - 2.0
     - WrappedArray(this, is, a, spam)
     
   * - 0.0
     - i am going to work
     - 1.0
     - WrappedArray(i, am, going, to, work)



