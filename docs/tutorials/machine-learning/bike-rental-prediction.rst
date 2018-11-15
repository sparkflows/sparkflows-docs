Bike Rental Prediction
======================

This workflow reads in a dataset.it then Predicts the number of bikes to be rented in any given hour.

Worklow
-------

Below is the workflow. It does the following:

* Reads data from a sample dataset.
* Extract hour from time using datatype timestamp.
* Calculate Count to datatype double.
* Assemble features for modelling.
* Calculate vectorindexer.
* Split it.
* GBTRegression.
* Prediction.
* RegressionEvaluator.
* Correlation with columns.
* Summary analysis.
* Calculate count for rental per hour.
* Analyse using Graph.

.. figure:: ../../_assets/tutorials/machine-learning/bike-rental-prediction/1.PNG
   :alt: Bike Rental Prediction
   :align: center
   :width: 60%

Reading from Dataset
---------------------

It reads sample Dataset file.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/bike-rental-prediction/2.PNG
   :alt: Bike Rental Prediction
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/machine-learning/bike-rental-prediction/2a.PNG
   :alt: Bike Rental Prediction
   :align: center
   :width: 60%
