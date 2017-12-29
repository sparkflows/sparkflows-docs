
Binarizer
^^^^^^ 

Binarize a column of continuous features given a threshold.

type

ml-transformer

nodeClass

fire.nodes.ml.NodeBinarizer

Fields

+-----------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
|    Name   |     Title     |                                                                  Description                                                                  |
+-----------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
|  inputCol |  Input Column |                                                             The input column name                                                             |
| outputCol | Output Column |                                                             The output column name                                                            |
| threshold |   Threshold   | The features greater than the threshold, will be binarized to 1.0.The features equal to or less than the threshold, will be binarized to 0.0. |
+-----------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------+