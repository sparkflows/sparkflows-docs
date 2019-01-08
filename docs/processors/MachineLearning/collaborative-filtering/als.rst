ALS
=========== 

Alternating Least Squares (ALS) matrix factorization.

Input
--------------
It takes in a DataFrame as input and performs ALS

Output
--------------
It generates the ALSModel and passes it to the next Predict and ModelSave Nodes. It also passes the incoming DataFrame to the next Nodes

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


Details
======


Collaborative filtering is commonly used for recommender systems. These techniques aim to fill in the missing entries of a user-item association matrix. spark.mllib currently supports model-based collaborative filtering, in which users and products are described by a small set of latent factors that can be used to predict missing entries. spark.mllib uses the alternating least squares (ALS) algorithm to learn these latent factors.

More at Spark MLlib/ML docs page : http://spark.apache.org/docs/latest/mllib-collaborative-filtering.html


