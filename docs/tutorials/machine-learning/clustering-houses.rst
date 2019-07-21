Clustering Houses
=================

This workflow reads in a dataset. It then performs KMeans Clustering on the Housing Dataset.

Workflow
-------

Below is the workflow. It does the following:

* Reads data from a sample dataset.
* Prints the results.
* Assembles the features for predictions.
* Splits it.
* Perform KMeans Clustering.
* ML Model save.
* ML Model Load.
* Prediction.
* Print the prediction results.

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/1.PNG
   :alt: Clustering Houses
   :align: center
   :width: 60%

Reading from Dataset
---------------------

It reads sample Dataset file.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/2.PNG
   :alt: Clustering Houses
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/2a.PNG
   :alt: Clustering Houses
   :align: center
   :width: 60%
   
Prints the results
------------------

It prints the sample dataset file results.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/3.PNG
   :alt: Clustering Houses
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/3a.PNG
   :alt: Clustering Houses
   :align: center
   :width: 60%
   
Assemble the features for predictions
-------------------------------------

It assembles the features for predictions using VectorAssembler Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/4.PNG
   :alt: Clustering Houses
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/4a.PNG
   :alt: Clustering Houses
   :align: center
   :width: 60%
   
Split it
---------

It splits features of prediction using Split Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/5.PNG
   :alt: Clustering Houses
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/5a.PNG
   :alt: Clustering Houses
   :align: center
   :width: 60%
   
Perform KMeans Clustering
-------------------------

It performs KMeans Clustering on the Housing Dataset using KMeans Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/6.PNG
   :alt: Clustering Houses
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/6a.PNG
   :alt: Clustering Houses
   :align: center
   :width: 60%
   
ML Model save
---------------

It will save ML Model with given path using ModelSave Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/7.PNG
   :alt: Clustering Houses
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/7a.PNG
   :alt: Clustering Houses
   :align: center
   :width: 60%
   
ML Model Load
--------------

It will Load ML Model with given path using ModelSave Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/8.PNG
   :alt: Clustering Houses
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/8a.PNG
   :alt: Clustering Houses
   :align: center
   :width: 60%


Prediction
-----------

It predicts features updated using Predict Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/9.PNG
   :alt: Clustering Houses
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/9a.PNG
   :alt: Clustering Houses
   :align: center
   :width: 60%
   
Print the prediction results
-----------------------------

It Print the prediction results.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/10.PNG
   :alt: Clustering Houses
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/clustering-houses/10a.PNG
   :alt: Clustering Houses
   :align: center
   :width: 60%
