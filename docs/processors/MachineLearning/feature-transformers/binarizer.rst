Binarizer
=========== 

Binarize a column of continuous features given a threshold.

Input
--------------
This type of node takes in a DataFrame and transforms it to another DataFrame

Output
--------------
A new column containing the binarized values is added to the incoming DataFrame

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodeBinarizer

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
        - The input column name
      * - outputCol
        - Output Column
        - The output column name
      * - threshold
        - Threshold
        - The features greater than the threshold, will be binarized to 1.0.The features equal to or less than the threshold, will be binarized to 0.0.


Details
======


This node binarizes a column of continuous features given a threshold.

More at Spark MLlib/ML docs page : https://spark.apache.org/docs/latest/ml-features.html#binarizer


