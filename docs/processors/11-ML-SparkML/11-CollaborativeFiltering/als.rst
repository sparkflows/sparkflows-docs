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
        - Checkpoint Interval
        - The checkpoint interval.
      * - nonnegative
        - Non negative
        - Whether to apply nonnegativity constraints.
      * - numItemBlocks
        - Num Item Blocks
        - The number of item blocks.
      * - numUserBlocks
        - Num User Blocks
        - The number of user blocks.
      * - rank
        - Rank
        - The rank of the matrix factorization.
      * - seed
        - Seed
        - Random Seed.
      * - implicitPrefs
        - Implicit Prefs
        - whether to use implicit preference


Details
-------


Collaborative filtering is commonly used for recommender systems. These techniques aim to fill in the missing entries of a user-item association matrix. spark.ml currently supports model-based collaborative filtering, in which users and products are described by a small set of latent factors that can be used to predict missing entries. spark.ml uses the alternating least squares (ALS) algorithm to learn these latent factors. The implementation in spark.ml has the following parameters:


*  numBlocks is the number of blocks the users and items will be partitioned into in order to parallelize computation (defaults to 10).
*  rank is the number of latent factors in the model (defaults to 10).
*  maxIter is the maximum number of iterations to run (defaults to 10).
*  regParam specifies the regularization parameter in ALS (defaults to 1.0).
*  implicitPrefs specifies whether to use the explicit feedback ALS variant or one adapted for implicit feedback data (defaults to false which means using explicit feedback).
*  alpha is a parameter applicable to the implicit feedback variant of ALS that governs the baseline confidence in preference observations (defaults to 1.0).
*  nonnegative specifies whether or not to use nonnegative constraints for least squares (defaults to false).


More details are available at Apache Spark ML docs page:

http://spark.apache.org/docs/latest/ml-collaborative-filtering.html


Examples
-------

Below example is available at : https://spark.apache.org/docs/latest/mllib-collaborative-filtering.html#examples
+++++++++++++++

import org.apache.spark.mllib.recommendation.ALS
import org.apache.spark.mllib.recommendation.MatrixFactorizationModel
import org.apache.spark.mllib.recommendation.Rating

// Load and parse the data
val data = sc.textFile("data/mllib/als/test.data")
val ratings = data.map(_.split(',') match { case Array(user, item, rate) =>
  Rating(user.toInt, item.toInt, rate.toDouble)
})

// Build the recommendation model using ALS
val rank = 10
val numIterations = 10
val model = ALS.train(ratings, rank, numIterations, 0.01)

// Evaluate the model on rating data
val usersProducts = ratings.map { case Rating(user, product, rate) =>
  (user, product)
}
val predictions =
  model.predict(usersProducts).map { case Rating(user, product, rate) =>
    ((user, product), rate)
  }
val ratesAndPreds = ratings.map { case Rating(user, product, rate) =>
  ((user, product), rate)
}.join(predictions)
val MSE = ratesAndPreds.map { case ((user, product), (r1, r2)) =>
  val err = (r1 - r2)
  err * err
}.mean()
println(s"Mean Squared Error = $MSE")

// Save and load model
model.save(sc, "target/tmp/myCollaborativeFilter")
val sameModel = MatrixFactorizationModel.load(sc, "target/tmp/myCollaborativeFilter")
