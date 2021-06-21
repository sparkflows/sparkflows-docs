Building H2O Workflows
==================================

Below is an example H2O workflow. It builds a Regression Model for predicting the number of Bike Rentals at a given day/hour.

.. figure:: ../../../_assets/tutorials/machine-learning/h2o-gbm/1.PNG
   :alt: H2O GBM
   :width: 90%

There is a certain pattern to be followed when building the predictive H2O workflows.

* Read in the Data
* Perform feature engineering
* Split the dataframe for training and test
* Use a model building node like Regression/Classification/Clustering to create the model on the training dataset
* Use a prediction node for predicting on the test dataset using the Model created


