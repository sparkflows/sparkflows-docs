
NGramTransformer
^^^^^^ 

Converts the input array of strings into an array of n-grams. Null values in the input array are ignored. It returns an array of n-grams where each n-gram is represented by a space-separated string of words.When the input is empty, an empty array is returned. When the input array length is less than n (number of elements per n-gram), no n-grams are returned

type

ml-transformer

nodeClass

fire.nodes.ml.NodeNGramTransformer

Fields

+----------------------+-----------------+----------------------------------------------------------------------------------------------------------------------+
| numberOfGrams        | Number of Grams | Sequence of 'string array' for integer 'Number of Grams'                                                             |
+======================+=================+======================================================================================================================+
| inputCol             | Input Column    | Contains sequence of strings                                                                                         |
+----------------------+-----------------+----------------------------------------------------------------------------------------------------------------------+
| inputColStringArrCol | List of Words   | Sequence of words                                                                                                    |
+----------------------+-----------------+----------------------------------------------------------------------------------------------------------------------+
| outputCol            | Output Column   | Consist of a sequence of n-grams where each n-gram is represented by a space-delimited string of n consecutive words |
+----------------------+-----------------+----------------------------------------------------------------------------------------------------------------------+
| numberOfGrams        | Number of Grams | Sequence of 'string array' for integer 'Number of Grams'                                                             |
+----------------------+-----------------+----------------------------------------------------------------------------------------------------------------------+