GBT Regression
=========== 

It supports both continuous and categorical features.

Input
--------------
This takes in a DataFrame and performs Logistic Regression

Output
--------------
It generates the GBTRegression and passes it to the next Predict and ModelSave Nodes. The input DataFrame is also passed along to the next nodes.

Type
--------- 

ml-estimator

Class
--------- 

fire.nodes.ml.NodeGBTRegression

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - featuresCol
        - Features Column
        - Features column of type vectorUDT for model fitting
      * - labelCol
        - Label Column
        - The label column for model fitting
      * - predictionCol
        - Prediction Column
        - The prediction column created during model scoring.
      * - impurity
        - Impurity
        - The Criterion used for information gain calculation
      * - lossType
        - Loss Function
        - The Loss function which GBT tries to minimize
      * - maxBins
        - Max Bins
        - The maximum number of bins used for discretizing continuous features.Must be >= 2 and >= number of categories in any categorical feature.
      * - maxDepth
        - Max Depth
        - The Maximum depth of a tree
      * - maxIter
        - Max Iterations
        - The maximum number of iterations(>=0)(a.k.a numtrees)
      * - minInfoGain
        - Min Information Gain
        - The Minimum information gain for a split to be considered at a tree node
      * - minInstancesPerNode
        - Min Instances Per Node
        - The Minimum number of instances each child must have after split
      * - subsamplingRate
        - Subsampling Rate
        - The fraction of the training data used for learning each decision tree.
      * - seed
        - Seed
        - The random seed
      * - stepSize
        - Step Size
        - Step size (a.k.a. learning rate), The step size to be used for each iteration of optimization.
      * - cacheNodeIds
        - Cache Node Ids
        - The caching nodes IDs. Can speed up training of deeper trees.
      * - checkpointInterval
        - Checkpoint Interval
        - The checkpoint interval. E.g. 10 means that the cache will get checkpointed every 10 iterations.Set checkpoint interval (>= 1) or disable checkpoint (-1)
      * - maxMemoryInMB
        - Max memory
        - Maximum memory in MB allocated to histogram aggregation.
      * - gridSearch
        - Grid Search
      * - minInfoGainGrid
        - Min Info Gain Grid Search
        - Min Info Gain Grid Search
      * - maxBinsGrid
        - Max Bins Grid Search
        - Max Bins for Grid Search
      * - maxDepthGrid
        - Max Depth Grid Search
        - Regularization Parameters for Grid Search
      * - maxIterGrid
        - Max Iterations Grid Search
        - Max Iterations for Grid Search


Details
-------


Gradient-Boosted Trees (GBTs) are ensembles of decision trees. GBTs iteratively train decision trees in order to minimize a loss function. 
The spark.ml implementation supports GBTs for binary classification and for regression, using both continuous and categorical features.

More details are available at Apache Spark ML docs page:

http://spark.apache.org/docs/latest/ml-classification-regression.html#gradient-boosted-tree-regression


Examples
-------

Below example is available at : https://spark.apache.org/docs/latest/ml-classification-regression.html#gradient-boosted-tree-regression


import org.apache.spark.ml.Pipeline
import org.apache.spark.ml.evaluation.RegressionEvaluator
import org.apache.spark.ml.feature.VectorIndexer
import org.apache.spark.ml.regression.{GBTRegressionModel, GBTRegressor}

// Load and parse the data file, converting it to a DataFrame.
val data = spark.read.format("libsvm").load("data/mllib/sample_libsvm_data.txt")

// Automatically identify categorical features, and index them.
// Set maxCategories so features with > 4 distinct values are treated as continuous.
val featureIndexer = new VectorIndexer()
  .setInputCol("features")
  .setOutputCol("indexedFeatures")
  .setMaxCategories(4)
  .fit(data)

// Split the data into training and test sets (30% held out for testing).
val Array(trainingData, testData) = data.randomSplit(Array(0.7, 0.3))

// Train a GBT model.
val gbt = new GBTRegressor()
  .setLabelCol("label")
  .setFeaturesCol("indexedFeatures")
  .setMaxIter(10)

// Chain indexer and GBT in a Pipeline.
val pipeline = new Pipeline()
  .setStages(Array(featureIndexer, gbt))

// Train model. This also runs the indexer.
val model = pipeline.fit(trainingData)

// Make predictions.
val predictions = model.transform(testData)

// Select example rows to display.
predictions.select("prediction", "label", "features").show(5)

// Select (prediction, true label) and compute test error.
val evaluator = new RegressionEvaluator()
  .setLabelCol("label")
  .setPredictionCol("prediction")
  .setMetricName("rmse")
val rmse = evaluator.evaluate(predictions)
println(s"Root Mean Squared Error (RMSE) on test data = $rmse")

val gbtModel = model.stages(1).asInstanceOf[GBTRegressionModel]
println(s"Learned regression GBT model:\n ${gbtModel.toDebugString}")
