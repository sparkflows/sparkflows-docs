
Dedup
========== 

Performs Dedup

Input
---------- 

It takes in a DataFrame as input

Output
---------- 

Dataframe with confidence score field and other selected scores for entities

Type
---------- 

transform

Class
---------- 

fire.nodes.ml.NodeDedup

Fields
---------- 

+--------------------+---------------------+-------------------------------+
| Name               | Title               | Description                   |
+====================+=====================+===============================+
| confidenceScore    | Confidence Score    | Confidence Score              |
+--------------------+---------------------+-------------------------------+
| lhsCols            | LHS Variables       | LHS columns for matching      |
+--------------------+---------------------+-------------------------------+
| rhsCols            | RHS Variables       | RHS columns for matching      |
+--------------------+---------------------+-------------------------------+
| matchingAlgorithms | Algorithm to use    | Algorithm to use for matching |
+--------------------+---------------------+-------------------------------+
| matchingWeights    | Weights for matches | Weights for matches           |
+--------------------+---------------------+-------------------------------+
| outputCols         | Output Column       | Output Column                 |
+--------------------+---------------------+-------------------------------+