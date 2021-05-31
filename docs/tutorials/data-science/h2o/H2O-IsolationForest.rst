H2O - Isolation Forest
======================

This workflow performs Anomaly Detection with Isolation Forests using H2O of credit card fraud sample dataset.

Anomaly detection is a common data science problem where the goal is to identify odd or suspicious observations, events, or items in our data that might be indicative of some issues in our data collection process (such as broken sensors, typos in collected forms, etc.) or unexpected events like security breaches, server failures, and so on.

Workflow
-------

The below workflow:

* ReadCSV - Read the creditcardfraud_sampled csv dataset.
* H2OPCA - Reduce the number of features using PCA.
* Split With Stratified Sampling - Split With Stratified Sampling, returns a stratified sample without replacement based on the fraction given on each stratum.
* H2OIsolationForest - Isolation Forest, identifies anomalies or outliers, isolates observations by randomly selecting a feature and then randomly selecting a split value between the maximum and minimum values of that selected feature. This split depends on how long it takes to separate the points.
* H2OModelSave - Saves an H2O binary ML Model.
* H2OScore - To Enable the test metrics.
* SQL-Filter - Receives an input data frame, creates a temporary table on top of that data frame. Filter the required columns.
* Correlation - The prediction h2o frame contains two columns: predict showing a normalized anomaly score and mean_length showing the average number of splits across all trees to isolate the observation. These two columns should have the property of inverse proportion by their definition, as the fewer random splits you need to isolate the observation, the more anomalous it is. 


.. figure:: ../../../_assets/tutorials/machine-learning/H20-IsolationForest/isolationForestWorkflow.png
   :alt: H2O Kmeans
   :width: 90%
