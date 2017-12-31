
QuantileDiscretizer
^^^^^^ 

QuantileDiscretizer takes a column with continuous features and outputs a column with binned categorical features.

type

ml-transformer

nodeClass

fire.nodes.ml.NodeQuantileDiscretizer

Fields

+----------------+------------------+------------------------------------+
|      Name      |       Title      |             Description            |
+----------------+------------------+------------------------------------+
| inputCol | Input Column | The Input column name | 
+----------------+------------------+------------------------------------+
| outputCol | Output Column | Output column name | 
+----------------+------------------+------------------------------------+
| numBuckets | NumBuckets | Maximum number of buckets (quantiles or categories) into which the data points are grouped. Must be >= 2. | 
+----------------+------------------+------------------------------------+
