Normalizer
=========== 

Normalizer is a Transformer which transforms a dataset of Vector rows, normalizing each Vector to have unit norm.

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodeNormalizer

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCol
        - Input Column
        - The input column name
      * - outputCol
        - Output Column
        - The output column name
      * - p
        - P
        - Normalization in L^p space. Must be >= 1. (default: p = 2)




