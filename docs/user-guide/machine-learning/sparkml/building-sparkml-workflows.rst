Building Apache Spark ML Workflows
==================================

Below is an example Spark ML workflow. It builds a Classification Model for Churn prediction on Telco data

There is a certain pattern to be followed when building the predictive Spark ML workflows.

* Read in the Data
* Perform feature engineering
* Convert strings to numeric values
* Use the Vector Assembler node to create a features columns. It will contain data from all the columns which would be used as features in the Model.
* Split the dataframe for training and test
* Use a model build node like Regression/Classification/Clustering to create the model on the training dataset
* Use a prediction node for predicting on the test dataset using the Model created
* Use an Evaluator node for evaluating the model results


