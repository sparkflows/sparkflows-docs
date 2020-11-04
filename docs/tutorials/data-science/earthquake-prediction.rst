Earthquake Prediction
=====================

Objective
---------
As the motivation behind earthquake prediction is to empower crisis measures to decrease demise and devastation, inability to give notice of a significant earthquake that happens, or possibly a satisfactory assessment of the hazard, can bring about legitimate risk, or even political cleansing.

Dataset
-------

Data set contains 2 columns as follows:-

Acoustic_data - Acoustic wave reading

Time_to_failure - Time remaining before the next earthquake

.. figure:: ../../_assets/tutorials/machine-learning/earthquake_prediction/earthquake_data.png
   :alt: Stock Forecasting
   :align: center
   :width: 100%

Random Forest Regression Workflow for Earthquake Prediction
---------------------------------------------------------
Random Forest Regression model belongs to family of bagging regression. It is a supervised learning model that uses ensemble learning method for regression. Ensemble learning method is a technique that combines predictions from multiple models to make prediction accurately than a single model.

Features of Random Forest:-

* Aggregates many decision trees
* Prevents overfitting

.. figure:: ../../_assets/tutorials/machine-learning/earthquake_prediction/earthquake_flow.png
   :alt: Stock Forecasting
   :align: center
   :width: 100%


Prepare data for modeling
--------------------------

Follow workflow arrow

* Arrow 1- ZipWithIndex to create new feature column as ID

* Arrow 2- Group data to create new feature column as key obtained by ID divided by length of data 

.. figure:: ../../_assets/tutorials/machine-learning/earthquake_prediction/group_data.png
   :alt: Stock Forecasting
   :align: center
   :width: 100%

* Arrow 3- Feature engineering to group by data on key to create all statistical measures as new feature

.. figure:: ../../_assets/tutorials/machine-learning/earthquake_prediction/feature_eng.png
   :alt: Stock Forecasting
   :align: center
   :width: 100%

* Arrow 4 - Merge multiple columns to create feature vector

.. figure:: ../../_assets/tutorials/machine-learning/earthquake_prediction/feature_vector.png
   :alt: Stock Forecasting
   :align: center
   :width: 100%
