
BinaryClassificationEvaluator
^^^^^^ 

Evaluator for binary classification, which expects two input columns: rawPrediction and label.

type

ml-evaluator

nodeClass

fire.nodes.ml.NodeBinaryClassificationEvaluator

Fields

+----------------+------------------+------------------------------------+
|      Name      |       Title      |             Description            |
+----------------+------------------+------------------------------------+
| labelCol | Label Column | The label column for model fitting. | 
+----------------+------------------+------------------------------------+
| rawPredictionCol | RawPrediction Column | The raw prediction (confidence) column. | 
+----------------+------------------+------------------------------------+
| metricName | Metric Name | The metric used in evaluation. | 
+----------------+------------------+------------------------------------+
