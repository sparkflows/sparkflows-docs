GBT Classifier
=========== 

Gradient-Boosted Trees (GBTs) is a learning algorithm for classification. It supports binary labels, as well as both continuous and categorical features. Note: Multiclass labels are not currently supported.

Input
--------------
It takes in a DataFrame as input and performs GBT Classification

Output
--------------
The GBT Model generated is passed along to the next nodes. The input DataFrame is also passed along to the next nodes

Type
--------- 

ml-estimator

Class
--------- 

fire.nodes.ml.NodeGBTClassifier

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
        - Min Information Gain Param Grid Search
        - Min Information Gain Parameters for Grid Search
      * - maxBinsGrid
        - Max Bins Param Grid Search
        - Max Bins Parameters for Grid Search
      * - maxDepthGrid
        - Max Depth Param Grid Search
        - Max Depth Parameters for Grid Search
      * - maxIterGrid
        - Max Iteration Param Grid Search
        - Max Iteration Parameters for Grid Search


Details
-------


Gradient-boosted trees (GBTs) are a popular classification and regression method using ensembles of decision trees. 

More details are available at : http://spark.apache.org/docs/latest/ml-classification-regression.html#gradient-boosted-tree-classifier


Examples
-------

Below example is available at :https://spark.apache.org/docs/latest/ml-classification-regression.html#gradient-boosted-tree-classifier

import org.apache.spark.ml.Pipeline
import org.apache.spark.ml.classification.{GBTClassificationModel, GBTClassifier}
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator
import org.apache.spark.ml.feature.{IndexToString, StringIndexer, VectorIndexer}

// Load and parse the data file, converting it to a DataFrame.
val data = spark.read.format("libsvm").load("data/mllib/sample_libsvm_data.txt")

// Index labels, adding metadata to the label column.
// Fit on whole dataset to include all labels in index.
val labelIndexer = new StringIndexer()
  .setInputCol("label")
  .setOutputCol("indexedLabel")
  .fit(data)
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
val gbt = new GBTClassifier()
  .setLabelCol("indexedLabel")
  .setFeaturesCol("indexedFeatures")
  .setMaxIter(10)
  .setFeatureSubsetStrategy("auto")

// Convert indexed labels back to original labels.
val labelConverter = new IndexToString()
  .setInputCol("prediction")
  .setOutputCol("predictedLabel")
  .setLabels(labelIndexer.labelsArray(0))

// Chain indexers and GBT in a Pipeline.
val pipeline = new Pipeline()
  .setStages(Array(labelIndexer, featureIndexer, gbt, labelConverter))

// Train model. This also runs the indexers.
val model = pipeline.fit(trainingData)

// Make predictions.
val predictions = model.transform(testData)

// Select example rows to display.
predictions.select("predictedLabel", "label", "features").show(5)

// Select (prediction, true label) and compute test error.
val evaluator = new MulticlassClassificationEvaluator()
  .setLabelCol("indexedLabel")
  .setPredictionCol("prediction")
  .setMetricName("accuracy")
val accuracy = evaluator.evaluate(predictions)
println(s"Test Error = ${1.0 - accuracy}")

val gbtModel = model.stages(2).asInstanceOf[GBTClassificationModel]
println(s"Learned classification GBT model:\n ${gbtModel.toDebugString}")
