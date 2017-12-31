
Normalizer
^^^^^^ 

Normalizer is a Transformer which transforms a dataset of Vector rows, normalizing each Vector to have unit norm.

type

ml-transformer

nodeClass

fire.nodes.ml.NodeNormalizer

Fields

+-----------+---------------+------------------------------------------------------------+
| p         | P             | Normalization in L^p space. Must be >= 1. (default: p = 2) |
+===========+===============+============================================================+
| inputCol  | Input Column  | The input column name                                      |
+-----------+---------------+------------------------------------------------------------+
| outputCol | Output Column | The output column name                                     |
+-----------+---------------+------------------------------------------------------------+
| p         | P             | Normalization in L^p space. Must be >= 1. (default: p = 2) |
+-----------+---------------+------------------------------------------------------------+