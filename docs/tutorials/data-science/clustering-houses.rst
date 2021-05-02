Clustering Houses
=================

Here we have a housing dataset available to us. We need to cluster the houses in the best possible way.

We will perform the clustering usign KMeans algorithm availabe in Apache Spark ML.

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
* Prints the results.
* Assembles the features for predictions.
* Splits it.
* Perform KMeans Clustering.
* Prediction.
* Print the prediction results.

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/1.PNG
   :alt: Clustering Houses
   :width: 60%

Reading from Dataset
---------------------

First we read in the Housing Dataset using the ``Read CSV`` node.

Below are the parameters which we use:

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/2.PNG
   :alt: Clustering Houses
   :width: 60%
   
After reading, the ``Read CSV`` node output looks like below:

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/2a.PNG
   :alt: Clustering Houses
   :width: 60%
   
Prints the results
------------------

We print a few records which have been read in to view them.

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/3a.PNG
   :alt: Clustering Houses
   :width: 60%
   
Assemble the features for predictions
-------------------------------------

Next we assemble the features we want to use in the KMeans Clustering. We use the ``Vector Assembler`` node for it.
More details for Vector Assemblem in Apache Spark ML can be found here : https://spark.apache.org/docs/latest/ml-features.html#vectorassembler


.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/4.PNG
   :alt: Clustering Houses
   :width: 60%
   
The output of the Vector Assembler node looks like below:

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/4a.PNG
   :alt: Clustering Houses
   :width: 60%
   
Split it
---------

It splits features of prediction using Split Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/5.PNG
   :alt: Clustering Houses
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/5a.PNG
   :alt: Clustering Houses
   :width: 60%
   
Perform KMeans Clustering
-------------------------

It performs KMeans Clustering on the Housing Dataset using KMeans Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/6.PNG
   :alt: Clustering Houses
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/6a.PNG
   :alt: Clustering Houses
   :width: 60%
   
Prediction
-----------

It predicts features updated using Predict Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/9.PNG
   :alt: Clustering Houses
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/9a.PNG
   :alt: Clustering Houses
   :width: 60%
   
Print the prediction results
-----------------------------

It Print the prediction results.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/10.PNG
   :alt: Clustering Houses
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/10a.PNG
   :alt: Clustering Houses
   :width: 60%
