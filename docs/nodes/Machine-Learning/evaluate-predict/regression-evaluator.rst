
RegressionEvaluator
========== 

Evaluator for regression, which expects two input columns: prediction and label.

Type
---------- 

ml-evaluator

Class
---------- 

fire.nodes.ml.NodeRegressionEvaluator

Fields
---------- 

+---------------+-------------------+-------------------------------------+
| Name          | Title             | Description                         |
+===============+===================+=====================================+
| labelCol      | Label Column      | The label column for model fitting. |
+---------------+-------------------+-------------------------------------+
| predictionCol | Prediction Column | The prediction column.              |
+---------------+-------------------+-------------------------------------+
| metricName    | Metric Name       | The metric used in evaluation.      |
+---------------+-------------------+-------------------------------------+