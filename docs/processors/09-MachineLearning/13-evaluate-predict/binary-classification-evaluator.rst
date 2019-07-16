BinaryClassificationEvaluator
=========== 

Evaluator for binary classification, which expects two input columns: rawPrediction and label.

Output
--------------
It outputs the Probability for each class

Type
--------- 

ml-evaluator

Class
--------- 

fire.nodes.ml.NodeBinaryClassificationEvaluator

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - labelCol
        - Label Column
        - The label column for model fitting.
      * - rawPredictionCol
        - RawPrediction Column
        - The raw prediction (confidence) column.
      * - metricName
        - Metric Name
        - The metric used in evaluation.


Details
-------


Evaluator for binary classification, which expects two input columns: rawPrediction and label.


More at Spark MLlib/ML docs page : http://spark.apache.org/docs/latest/mllib-evaluation-metrics.html#binary-classification


