Bike Rental Prediction
======================

This workflow reads in a dataset. It then predicts the number of bikes to be rented in any given hour.

Workflow
-------

Below is the workflow. It does the following:

* Reads data from a sample dataset.
* Extracts hour from time using datatype timestamp.
* Calculates Cost Count to datatype double.
* Assembles features for modelling.
* Calculates vectorindexer.
* Splits it.
* GBTRegression.
* Prediction.
* RegressionEvaluator.

.. figure:: ../../_assets/tutorials/machine-learning/bike-rental-prediction/1.png
   :alt: Bike Rental Prediction
   :width: 100%

Reading from Dataset
---------------------

It reads sample Dataset file.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/bike-rental-prediction/2.png
   :alt: Bike Rental Prediction
   :width: 100%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/bike-rental-prediction/2a.png
   :alt: Bike Rental Prediction
   :width: 100%
   
Extract hour from time using datatype timestamp
------------------------------------------------

It extracts hour from time using datatype timestamp using DateTimeFieldExtract Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/bike-rental-prediction/3.png
   :alt: Bike Rental Prediction
   :width: 100%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/bike-rental-prediction/3a.png
   :alt: Bike Rental Prediction
   :width: 100%
   
Calculate Count to datatype double
-----------------------------------

It Calculates cast the Count field to datatype double using CastColumnType Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/bike-rental-prediction/4.png
   :alt: Bike Rental Prediction
   :width: 100%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/bike-rental-prediction/4a.png
   :alt: Bike Rental Prediction
   :width: 100%

Assemble features for modelling
---------------------------------

It Assembles features columns into a feature vector using VectorAssembler Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/bike-rental-prediction/5.png
   :alt: Bike Rental Prediction
   :width: 100%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/bike-rental-prediction/5a.png
   :alt: Bike Rental Prediction
   :width: 100%

Calculate vectorindexer
-----------------------

It identifies categorical features and index them using vectorindexer Node. 

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/bike-rental-prediction/6.png
   :alt: Bike Rental Prediction
   :width: 100%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/bike-rental-prediction/6a.png
   :alt: Bike Rental Prediction
   :width: 100%
   
Split it
---------

It will split our dataset into seperate training and test sets using split Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/bike-rental-prediction/7.png
   :alt: Bike Rental Prediction
   :width: 100%
   
   
GBTRegression
--------------

It validates held out test sets in order to know about high confidence using GBTRegression Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/bike-rental-prediction/8.png
   :alt: Bike Rental Prediction
   :width: 100%
   
   
Prediction
-----------

It will make prediction on future data using Prediction Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/bike-rental-prediction/9.png
   :alt: Bike Rental Prediction
   :width: 100%
   


RegressionEvaluator
-------------------

It validates held out test sets in order to know about high confidence using RegressionEvaluator Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/bike-rental-prediction/10.png
   :alt: Bike Rental Prediction
   :width: 80%
   
   
