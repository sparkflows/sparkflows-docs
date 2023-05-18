Clustering Houses
=================

Here, we have a housing dataset available to us. We need to cluster the houses in the best possible way.

We will perform the clustering using K-means algorithm availabe in Apache Spark ML.

Dataset
-------

The dataset is a Housing dataset containing column like price, number of bedrooms, number of bathrooms, etc.

* Bedrooms : Number of bedrooms in the house.
* Price : The price at which the house was sold.


Workflow
-------

Below is the workflow for creating a K-means model for clustering the houses. It does the following:

* Reads data from a sample dataset.
* Prints the result.
* Assembles the features for prediction.
* Splits it.
* Perform K-means Clustering.
* Prediction.
* Prints the prediction result.

.. figure:: ../../../_assets/tutorials/machine-learning/clustering-houses/k-means-cluster-wf.png
   :alt: Clustering Houses
   :width: 65%

Reading from Dataset
---------------------

First we read in the Housing Dataset using the ``Read CSV`` node.

Below are the parameters which we use:

.. figure:: ../../../_assets/tutorials/machine-learning/clustering-houses/read-config.png
   :alt: Clustering Houses
   :width: 65%
   
After reading, the ``Read CSV`` node, output looks like below:

.. figure:: ../../../_assets/tutorials/machine-learning/clustering-houses/read-output.png
   :alt: Clustering Houses
   :width: 65%
   
Assemble the features for predictions
-------------------------------------

Next, we assemble the features we want to use in the KMeans Clustering. We use the ``Vector Assembler`` node for it.

More details for Vector Assembler in Apache Spark ML can be found here : https://spark.apache.org/docs/latest/ml-features.html#vectorassembler


.. figure:: ../../../_assets/tutorials/machine-learning/clustering-houses/vector-assembler-config.png
   :alt: Clustering Houses
   :width: 65%
   
The output of the Vector Assembler node looks like below:

.. figure:: ../../../_assets/tutorials/machine-learning/clustering-houses/vector-assembler-output.png
   :alt: Clustering Houses
   :width: 65%
   
Split it
---------

It splits features of prediction using Split Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../../_assets/tutorials/machine-learning/clustering-houses/split-config.png
   :alt: Clustering Houses
   :width: 65%
   
Perform KMeans Clustering
-------------------------

It performs K-means Clustering on the Housing Dataset using K-means Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../../_assets/tutorials/machine-learning/clustering-houses/k-means-config.png
   :alt: Clustering Houses
   :width: 65%
   
   
Prediction
-----------

It predicts features updated using Predict Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../../_assets/tutorials/machine-learning/clustering-houses/predict-config.png
   :alt: Clustering Houses
   :width: 65%
   
   
Print the prediction results
-----------------------------

It prints the prediction results.

.. figure:: ../../../_assets/tutorials/machine-learning/clustering-houses/result.png
   :alt: Clustering Houses
   :width: 65%
