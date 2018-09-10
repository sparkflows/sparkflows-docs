Dedup
=========== 

This node is used for problems like entity resolution or data matching. Entity resolution or Data matching is the problem of finding and linking different mentions of the same entity in a single data source or across multiple data sources.

Input
--------------
It takes in a DataFrame as input

Output
--------------
Dataframe with confidence score field and other selected scores for entities

Type
--------- 

transform

Class
--------- 

fire.nodes.ml.NodeDedup

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1
      * - Name
        - Title
        - Description
      * - confidenceScore
        - Confidence Score
        - Confidence Score
      * - lhsCols
        - LHS Variables
        - LHS columns for matching
      * - rhsCols
        - RHS Variables
        - RHS columns for matching
      * - matchingAlgorithms
        - Algorithm to use
        - Algorithm to use for matching
      * - matchingWeights
        - Weights
        - Weights for matches
      * - outputCols
        - Output Column
        - Output Column




