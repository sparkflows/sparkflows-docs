MulticlassClassificationEvaluator
=========== 

Evaluator for multiclass classification, which expects two input columns: score and label.

Type
--------- 

ml-evaluator

Class
--------- 

fire.nodes.ml.NodeMulticlassClassificationEvaluator

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
      * - predictionCol
        - Prediction Column
        - The prediction column.
      * - metricName
        - Metric Name
        - The metric used in evaluation.


Details
-------


Evaluator for multiclass classification, which expects two input columns: score and label.

More at Spark MLlib/ML docs page :https://spark.apache.org/docs/1.6.0/mllib-evaluation-metrics.html#multiclass-classification


