
ChiSqSelector
========== 

Chi-Squared feature selection, which selects categorical features to use for predicting a categorical label.

Type
---------- 

ml-transformer

Class
---------- 

fire.nodes.ml.NodeChiSqSelector

Fields
---------- 

+----------------+------------------+---------------------------------------------------------------------------------------+
| Name           | Title            | Description                                                                           |
+================+==================+=======================================================================================+
| featuresCol    | Features Column  | The features column name                                                              |
+----------------+------------------+---------------------------------------------------------------------------------------+
| outputCol      | Output Column    | The output column name                                                                |
+----------------+------------------+---------------------------------------------------------------------------------------+
| labelCol       | Label Column     | The label column name                                                                 |
+----------------+------------------+---------------------------------------------------------------------------------------+
| numTopFeatures | NumTopFeatures   | Number of features that selector will select (ordered by statistic value descending). |
+----------------+------------------+---------------------------------------------------------------------------------------+