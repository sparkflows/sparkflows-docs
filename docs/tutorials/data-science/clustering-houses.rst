Clustering Houses
=================

Here we have a housing dataset available to us. We need to cluster the houses in the best possible way.

We will perform the clustering using KMeans algorithm availabe in Apache Spark ML.

Dataset
-------

We have taken the Housing dataset from .....

It looks like below:

IMAGE

The columns in the dataset are pretty self-explanatory.

* bedrooms : number of bedrooms in the house
* price : the price at which the house was sold


Workflow
-------

Below is the workflow for creating a KMeans model for clustering the houses. It does the following:

* Reads data from a sample dataset.
* Prints the result.
* Assembles the features for prediction.
* Splits it.
* Perform KMeans Clustering.
* Prediction.
* Print the prediction result.

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/1.png
   :alt: Clustering Houses
   :width: 100%

Reading from Dataset
---------------------

First we read in the Housing Dataset using the ``Read CSV`` node.

Below are the parameters which we use:

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/2.png
   :alt: Clustering Houses
   :width: 80%
   
After reading, the ``Read CSV`` node, output looks like below:

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/2a.png
   :alt: Clustering Houses
   :width: 80%
   
Assemble the features for predictions
-------------------------------------

Next we assemble the features we want to use in the KMeans Clustering. We use the ``Vector Assembler`` node for it.
More details for Vector Assembler in Apache Spark ML can be found here : https://spark.apache.org/docs/latest/ml-features.html#vectorassembler


.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/4.png
   :alt: Clustering Houses
   :width: 80%
   
The output of the Vector Assembler node looks like below:

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/4a.png
   :alt: Clustering Houses
   :width: 80%
   
Split it
---------

It splits features of prediction using Split Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/5.png
   :alt: Clustering Houses
   :width: 80%
   
Perform KMeans Clustering
-------------------------

It performs KMeans Clustering on the Housing Dataset using KMeans Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/6.png
   :alt: Clustering Houses
   :width: 80%
   
   
Prediction
-----------

It predicts features updated using Predict Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/9.png
   :alt: Clustering Houses
   :width: 80%
   
   
Print the prediction results
-----------------------------

It prints the prediction results.

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/10a.png
   :alt: Clustering Houses
   :width: 80%
