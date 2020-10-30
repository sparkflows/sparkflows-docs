RegressionEvaluator
=========== 

Evaluator for regression, which expects two input columns: prediction and label.

Input
--------------
It takes in a DataFrame as input

Output
--------------
The incoming DataFrame is passed to the output

Type
--------- 

ml-evaluator

Class
--------- 

fire.nodes.ml.NodeRegressionEvaluator

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


Evaluator for regression, which expects two input columns: prediction and label.

More at Spark MLlib/ML docs page:

http://spark.apache.org/docs/1.6.0/api/scala/index.html#org.apache.spark.ml.evaluation.RegressionEvaluator


