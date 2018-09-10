ALS
=========== 

Alternating Least Squares (ALS) matrix factorization.

Type
--------- 

ml-estimator

Class
--------- 

fire.nodes.ml.NodeALS

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - userCol
        - User Column
        - The column name for user ids.
      * - itemCol
        - Item Column
        - The column name for item ids.
      * - ratingCol
        - Rating Column
        - The column name for ratings.
      * - predictionCol
        - Prediction Column
        - The prediction column created during model scoring
      * - maxIter
        - Max iterations
        - The maximum number of iterations.
      * - regParam
        - Regularization Param
        - The regularization parameter.(>=0)
      * - alpha
        - Alpha
        - The alpha parameter in the implicit preference formulation.(>=0)
      * - checkpointInterval
        - CheckpointInterval
        - The checkpoint interval.
      * - nonnegative
        - Nonnegative
        - Whether to apply nonnegativity constraints.
      * - numItemBlocks
        - numItemBlocks
        - The number of item blocks.
      * - numUserBlocks
        - numUserBlocks
        - The number of user blocks.
      * - rank
        - Rank
        - The rank of the matrix factorization.
      * - seed
        - Seed
        - Random Seed.
      * - implicitPrefs
        - ImplicitPrefs
        - whether to use implicit preference




