
StandardScaler
^^^^^^ 

StandardScaler transforms a dataset of Vector rows, normalizing each feature to have unit standard deviation and/or zero mean.

type

ml-transformer

nodeClass

fire.nodes.ml.NodeStandardScaler

Fields

+-----------+-------------------+--------------------------------------------+
|    Name   |       Title       |                Description                 |
+-----------+-------------------+--------------------------------------------+
|  inputCol |    Input Column   |           The input column name            |
| outputCol |   Output Column   |           The output column name           |
|  withMean |     With Mean     | Centers the data with mean before scaling. |
|  withStd  | With Standard Dev | Scales the data to unit standard deviation |
+-----------+-------------------+--------------------------------------------+