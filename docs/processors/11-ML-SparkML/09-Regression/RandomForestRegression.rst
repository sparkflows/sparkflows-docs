Random Forest Regression
=========== 

It supports both continuous and categorical features.

Input
--------------
This takes in a DataFrame and performs Random Forest Regression

Output
--------------
It generates the Random Forest Regression Model and passes it to the next Predict and ModelSave Nodes. The input DataFrame is also passed along to the next nodes.

Type
--------- 

ml-estimator

Class
--------- 

fire.nodes.ml.NodeRandomForestRegression

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
      * - featureSubsetStrategy
        - Feature Subset Strategy
        - The number of features to consider for splits at each tree node.
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
      * - numTrees
        - Num Trees
        - The number of trees to train
      * - subsamplingRate
        - Subsampling Rate
        - The fraction of the training data used for learning each decision tree.
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
        - Min Info Gain Grid Search
        - Min Info Gain Grid Search
      * - maxBinsGrid
        - Max Bins Grid Search
        - Max Bins for Grid Search
      * - maxDepthGrid
        - Max Depth Grid Search
        - Regularization Parameters for Grid Search
      * - numTreesGrid
        - Num Trees Grid Search
        - Number of trees for Grid Search


Details
-------


Random forests are a popular family of classification and regression methods.
The DataFrame API supports two major tree ensemble algorithms: Random Forests and Gradient-Boosted Trees (GBTs). Both use spark.ml decision trees as their base models.

More details are available at Apache Spark ML docs page :

http://spark.apache.org/docs/latest/ml-classification-regression.html#random-forest-regression


Examples
-------

Below example is available at : https://spark.apache.org/docs/latest/ml-classification-regression.html#random-forest-regression

import org.apache.spark.ml.Pipeline
import org.apache.spark.ml.evaluation.RegressionEvaluator
import org.apache.spark.ml.feature.VectorIndexer
import org.apache.spark.ml.regression.{RandomForestRegressionModel, RandomForestRegressor}

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

// Train a RandomForest model.
val rf = new RandomForestRegressor()
  .setLabelCol("label")
  .setFeaturesCol("indexedFeatures")

// Chain indexer and forest in a Pipeline.
val pipeline = new Pipeline()
  .setStages(Array(featureIndexer, rf))

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

val rfModel = model.stages(1).asInstanceOf[RandomForestRegressionModel]
println(s"Learned regression forest model:\n ${rfModel.toDebugString}")
