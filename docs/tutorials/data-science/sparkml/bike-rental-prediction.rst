Bike Rental Prediction
======================

This workflow reads in a dataset and then it predicts the number of bikes to be rented in any given hour.

Workflow
-------

The below workflow:

* Reads data from a sample dataset.
* Extracts hour from time using datatype Timestamp.
* Calculates Count to datatype double.
* Assembles features for modelling.
* Calculates VectorIndexer.
* Splits the dataset.
* Uses GBTRegression Node.
* Makes prediction on future data.
* Uses RegressionEvaluator Node.

.. figure:: ../../../_assets/tutorials/machine-learning/bike-rental-prediction/bike-sharing-wf.png
   :alt: Bike Rental Prediction
   :width: 65%

Reading from Dataset
---------------------

It reads the sample Dataset File.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../../_assets/tutorials/machine-learning/bike-rental-prediction/read-config.png
   :alt: Bike Rental Prediction
   :width: 65%
   
Processor Output
^^^^^^

.. figure:: ../../../_assets/tutorials/machine-learning/bike-rental-prediction/read-output.png
   :alt: Bike Rental Prediction
   :width: 65%
   
Extract Hour from Time using Datatype Timestamp
------------------------------------------------

It extracts hour from the timestamp column using the DateTimeFieldExtract Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../../_assets/tutorials/machine-learning/bike-rental-prediction/exact-hour-config.png
   :alt: Bike Rental Prediction
   :width: 65%
   
Processor Output
^^^^^^

.. figure:: ../../../_assets/tutorials/machine-learning/bike-rental-prediction/exact-hour-output.png
   :alt: Bike Rental Prediction
   :width: 65%
   
Cast Count to Double type
-----------------------------------

It casts count field to double using the CastColumnType Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../../_assets/tutorials/machine-learning/bike-rental-prediction/cast-count-config.png
   :alt: Bike Rental Prediction
   :width: 65%
   
Processor Output
^^^^^^

.. figure:: ../../../_assets/tutorials/machine-learning/bike-rental-prediction/cast-count-output.png
   :alt: Bike Rental Prediction
   :width: 65%

Assemble Features for Modelling
---------------------------------

It assembles the columns to be used in model building into a feature vector using the VectorAssembler Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../../_assets/tutorials/machine-learning/bike-rental-prediction/Assemble-features-config.png
   :alt: Bike Rental Prediction
   :width: 65%
   
Processor Output
^^^^^^

.. figure:: ../../../_assets/tutorials/machine-learning/bike-rental-prediction/assemble-features-output.png
   :alt: Bike Rental Prediction
   :width: 65%

Calculate VectorIndexer
-----------------------

It identifies the categorical features and then index them using the VectorIndexer Node. 

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../../_assets/tutorials/machine-learning/bike-rental-prediction/vector-indexer-config.png
   :alt: Bike Rental Prediction
   :width: 65%
   
Processor Output
^^^^^^

.. figure:: ../../../_assets/tutorials/machine-learning/bike-rental-prediction/vector-indexer-output.png
   :alt: Bike Rental Prediction
   :width: 65%
   
Split it
---------

It will split the dataset into separate training and test sets using the Split Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../../_assets/tutorials/machine-learning/bike-rental-prediction/split-config.png
   :alt: Bike Rental Prediction
   :width: 65%
   
   
GBTRegression
--------------

It validates held out test sets in order to know about high confidence using the GBTRegression Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../../_assets/tutorials/machine-learning/bike-rental-prediction/gbtregression-config.png
   :alt: Bike Rental Prediction
   :width: 65%
   
   
Prediction
-----------

It will make prediction on the future data using the Prediction Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../../_assets/tutorials/machine-learning/bike-rental-prediction/predict-config.png
   :alt: Bike Rental Prediction
   :width: 65%
   


RegressionEvaluator
-------------------

It validates held out test sets in order to know about high confidence using the RegressionEvaluator Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../../_assets/tutorials/machine-learning/bike-rental-prediction/regression-evaluator-config.png
   :alt: Bike Rental Prediction
   :width: 65%
   
   
