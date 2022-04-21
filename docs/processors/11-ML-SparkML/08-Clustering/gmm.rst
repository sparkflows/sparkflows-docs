Gaussian Mixture
=========== 

This class performs expectation maximization for multivariate Gaussian Mixture Models (GMMs). A GMM represents a composite distribution of independent Gaussian distributions with associated mixing weights specifying each's contribution to the composite.

Input
--------------
It takes in a DataFrame as input and performs GaussianMixture clustering

Output
--------------
The input DataFrame is passed along to the next Processors

Type
--------- 

ml-estimator

Class
--------- 

fire.nodes.ml.NodeGaussianMixture

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


Details
-------


A Gaussian Mixture Model represents a composite distribution whereby points are drawn from one of k Gaussian sub-distributions, each with its own probability. The spark.ml implementation uses the expectation-maximization algorithm to induce the maximum-likelihood model given a set of samples.

GaussianMixture is implemented as an Estimator and generates a GaussianMixtureModel as the base model.

More details are available at Apache Spark ML docs page:

https://spark.apache.org/docs/latest/ml-clustering.html#gaussian-mixture-model-gmm


Examples
-------


Below example is available at : https://spark.apache.org/docs/latest/ml-clustering.html#gaussian-mixture-model-gmm

import org.apache.spark.ml.clustering.GaussianMixture

// Loads data
val dataset = spark.read.format("libsvm").load("data/mllib/sample_kmeans_data.txt")

// Trains Gaussian Mixture Model
val gmm = new GaussianMixture()
  .setK(2)
val model = gmm.fit(dataset)

// output parameters of mixture model model
for (i <- 0 until model.getK) {
  println(s"Gaussian $i:\nweight=${model.weights(i)}\n" +
      s"mu=${model.gaussians(i).mean}\nsigma=\n${model.gaussians(i).cov}\n")
}
