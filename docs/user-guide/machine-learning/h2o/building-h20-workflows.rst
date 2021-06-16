Building H2O Workflows
==================================

Below is an example H2O workflow. It builds a Classification Model for Churn prediction on Telco data

There is a certain pattern to be followed when building the predictive Spark ML workflows.

* Read in the Data
* Perform feature engineering
* Split the dataframe for training and test
* Use a model building node like Regression/Classification/Clustering to create the model on the training dataset
* Use a prediction node for predicting on the test dataset using the Model created


