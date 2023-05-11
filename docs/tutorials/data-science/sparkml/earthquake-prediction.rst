Earthquake Prediction
=====================

Objective
---------
As the motivation behind earthquake prediction is to empower crisis measures to decrease demise and devastation, inability to give notice of a significant earthquake that happens, or possibly a satisfactory assessment of the hazard, can bring about legitimate risk, or even political cleansing.

Dataset
-------

Dataset contains 2 columns as below:

* **Acoustic_data** - Acoustic wave reading.
* **Time_to_failure** - Time remaining before the next earthquake.

   .. figure:: ../../../_assets/tutorials/machine-learning/earthquake_prediction/input.png
      :alt: Stock Forecasting
      :width: 65%

Random Forest Regression Workflow for Earthquake Prediction
-----------------------------------------------------------
Random Forest Regression model belongs to family of bagging regression. It is a supervised learning model that uses ensemble learning method for regression. Ensemble learning method is a technique that combines predictions from multiple models to make prediction more accurately than a single model.

Features of Random Forest -

* Aggregates many decision trees.
* Prevents overfitting.

   .. figure:: ../../../_assets/tutorials/machine-learning/earthquake_prediction/earthquake-wf.png
      :alt: Stock Forecasting
      :width: 65%


Prepare data for modeling
--------------------------

Follow workflow arrow-

* **ZipWithIndex**- Creates new feature column from DataFrame index as ID.

* **Group data**- Creates new feature column as key obtained by ID divided by length of data. 

   .. figure:: ../../../_assets/tutorials/machine-learning/earthquake_prediction/group-output.png
      :alt: Stock Forecasting
      :width: 65%

* **Feature Engineering**- Groups by data on key to create all statistical measures (min, max, mean, quartiles, etc.) as new feature.

   .. figure:: ../../../_assets/tutorials/machine-learning/earthquake_prediction/feature-eng.png
      :alt: Stock Forecasting
      :width: 65%

* **Feature Vector** - Merge multiple columns to form vector.

   .. figure:: ../../../_assets/tutorials/machine-learning/earthquake_prediction/vector.png
      :alt: Stock Forecasting
      :width: 65%
   

Data modeling
-------------

* Before we create Random Forest Regression Model, split data (80:20) into train and test for performance evaluation.

Random Forest Regression
++++++++++++++++++++++++

* Sets feature vector corresponding to label(time_to_failure_label).
* Sets number of features for each split node of tree.
* For regression the measure of impurity is variant.
* In random forest, the impurity decrease from each feature can be averaged across trees to determine the final importance of the variable.
* The maxBins signifies the maximum number of bins used for splitting the features, where the suggested value is 100 to get better result.
* The maxDepth is the maximum depth of the tree (for example, depth 0 means one leaf node, depth 1 means one internal node plus two leaf nodes).
* Information gain is calculated by comparing the entropy of the dataset before and after a transformation.

   .. figure:: ../../../_assets/tutorials/machine-learning/earthquake_prediction/random-forest-regression-config1.png
      :alt: Stock Forecasting
      :width: 65%
   
   .. figure:: ../../../_assets/tutorials/machine-learning/earthquake_prediction/random-forest-regression-config2.png
      :alt: Stock Forecasting
      :width: 65%

Model evaluation
----------------

* Multiple ways to evaluate regression model such as R-Square, Root Mean Square Error(RMSE), Mean Square Error(MSE).

   .. figure:: ../../../_assets/tutorials/machine-learning/earthquake_prediction/evaluator.png
      :alt: Stock Forecasting
      :width: 65%
