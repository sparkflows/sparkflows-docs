K-Means
=========== 

K-means clustering with support for k-means|| initialization proposed by Bahmani et al

Input
--------------
It takes in a DataFrame as input and performs K-Means clustering

Output
--------------
The input DataFrame is passed along to the next Processors

Type
--------- 

ml-estimator

Class
--------- 

fire.nodes.ml.NodeKMeans

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
        - Features column of type vectorUDT for model fitting.
      * - k
        - K
        - The number of clusters to create.
      * - maxIter
        - Max Iterations
        - The maximum number of iterations.
      * - predictionCol
        - Prediction Column
        - The prediction column created during model scoring.
      * - seed
        - Seed
        - Random Seed.
      * - tol
        - Tolerence
        - The convergence tolerance for iterative algorithms.
      * - initMode
        - initMode
        - The initialization algorithm mode.
      * - initSteps
        - initSteps
        - The number of steps for the k-means|| initialization mode. It will be ignored when other initialization modes are chosen.


Details
-------


k-means is one of the most commonly used clustering algorithms that clusters the data points into a predefined number of clusters. The MLlib implementation includes a parallelized variant of the k-means++ method called kmeans||.

KMeans is implemented as an Estimator and generates a KMeansModel as the base model.

More details are available at Apache Spark ML docs page:

https://spark.apache.org/docs/latest/ml-clustering.html#k-means


Examples
-------


Below example is available at : https://spark.apache.org/docs/latest/ml-clustering.html#k-means

import org.apache.spark.ml.clustering.KMeans
import org.apache.spark.ml.evaluation.ClusteringEvaluator

// Loads data.
val dataset = spark.read.format("libsvm").load("data/mllib/sample_kmeans_data.txt")

// Trains a k-means model.
val kmeans = new KMeans().setK(2).setSeed(1L)
val model = kmeans.fit(dataset)

// Make predictions
val predictions = model.transform(dataset)

// Evaluate clustering by computing Silhouette score
val evaluator = new ClusteringEvaluator()

val silhouette = evaluator.evaluate(predictions)
println(s"Silhouette with squared euclidean distance = $silhouette")

// Shows the result.
println("Cluster Centers: ")
model.clusterCenters.foreach(println)
