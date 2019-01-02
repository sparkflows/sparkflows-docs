NGramTransformer
=========== 

Converts the input array of strings into an array of n-grams. Null values in the input array are ignored. It returns an array of n-grams where each n-gram is represented by a space-separated string of words.When the input is empty, an empty array is returned. When the input array length is less than n (number of elements per n-gram), no n-grams are returned

Input
--------------
It takes in a DataFrame as input and transforms it to another DataFrame

Output
--------------
It adds a new column consisting of a sequence of nn-grams where each nn-gram is represented by a space-delimited string of nn consecutive words, to the incoming DataFrame

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodeNGramTransformer

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
        - Contains sequence of strings
      * - inputColStringArrCol
        - List of Words
        - Sequence of words
      * - outputCol
        - Output Column
        - Consist of a sequence of n-grams where each n-gram is represented by a space-delimited string of n consecutive words
      * - numberOfGrams
        - Number of Grams
        - Sequence of 'string array' for integer 'Number of Grams'


Details
======


This node converts the input array of strings into an array of n-grams. Null values in the input array are ignored. It returns an array of n-grams where each n-gram is represented by a space-separated string of words.When the input is empty, an empty array is returned. When the input array length is less than n (number of elements per n-gram), no n-grams are returned"

More at Spark MLlib/ML docs page : http://spark.apache.org/docs/latest/ml-features.html#n-gram


