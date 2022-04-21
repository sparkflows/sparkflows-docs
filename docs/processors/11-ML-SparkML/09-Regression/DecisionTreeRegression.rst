Decision Tree Regression
=========== 

It supports both continuous and categorical features.

Input
--------------
This takes in a DataFrame and performs Decision Tree Regression

Output
--------------
The Decision Tree Regression Model generated is passed along to the next nodes. The input DataFrame is also passed along to the next nodes

Type
--------- 

ml-estimator

Class
--------- 

fire.nodes.ml.NodeDecisionTreeRegression

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
      * - maxBins
        - Max Bins
        - The maximum number of bins used for discretizing continuous features.Must be >= 2 and >= number of categories in any categorical feature.
      * - maxDepth
        - Max Depth
        - The Maximum depth of a tree
      * - minInfoGain
        - Min Information Gain
        - The Minimum information gain for a split to be considered at a tree node
      * - minInstancesPerNode
        - Min Instances Per Node
        - The Minimum number of instances each child must have after split
      * - seed
        - Seed
        - The random seed
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
        - Min Information Gain Param Grid Search
        - Min Information Gain Parameters for Grid Search
      * - maxBinsGrid
        - Max Bins Param Grid Search
        - Max Bins Parameters for Grid Search
      * - maxDepthGrid
        - Max Depth Param Grid Search
        - Max Depth Parameters for Grid Search


Details
-------


Decision tree supports both continuous and categorical features.

More details are available at Apache Spark ML docs page : https://spark.apache.org/docs/1.6.0/ml-classification-regression.html#decision-tree-regression


Examples
-------

Below example is available at : https://spark.apache.org/docs/latest/ml-classification-regression.html#decision-tree-regression

import org.apache.spark.ml.Pipeline
import org.apache.spark.ml.evaluation.RegressionEvaluator
import org.apache.spark.ml.feature.VectorIndexer
import org.apache.spark.ml.regression.DecisionTreeRegressionModel
import org.apache.spark.ml.regression.DecisionTreeRegressor

// Load the data stored in LIBSVM format as a DataFrame.
val data = spark.read.format("libsvm").load("data/mllib/sample_libsvm_data.txt")

// Automatically identify categorical features, and index them.
// Here, we treat features with > 4 distinct values as continuous.
val featureIndexer = new VectorIndexer()
  .setInputCol("features")
  .setOutputCol("indexedFeatures")
  .setMaxCategories(4)
  .fit(data)

// Split the data into training and test sets (30% held out for testing).
val Array(trainingData, testData) = data.randomSplit(Array(0.7, 0.3))

// Train a DecisionTree model.
val dt = new DecisionTreeRegressor()
  .setLabelCol("label")
  .setFeaturesCol("indexedFeatures")

// Chain indexer and tree in a Pipeline.
val pipeline = new Pipeline()
  .setStages(Array(featureIndexer, dt))

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

val treeModel = model.stages(1).asInstanceOf[DecisionTreeRegressionModel]
println(s"Learned regression tree model:\n ${treeModel.toDebugString}")
