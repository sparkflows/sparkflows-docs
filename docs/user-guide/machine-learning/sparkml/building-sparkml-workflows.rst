Building Apache Spark ML Workflows
==================================

Below is an example Spark ML workflow. It builds a Classification Model for Churn prediction on Telco data.

.. figure:: ../../../_assets/tutorials/machine-learning/telco-churn-prediction/telco-churn-prediction-wf.png
   :alt: Machine Learning
   :width: 90%

There is a certain pattern to be followed when building the predictive Spark ML workflows.

* Read in the Data
	-	Multiple Connectors and Read-Structured nodes are available to read incoming dataset. ``Read CSV`` is one of the common node to read data in CSV format.
	- 	It is advisable to have data validated and processed. This step is important to ensure that ML Workflow don't break while processing and only the selected features are being processed.
* Perform feature engineering
	-	Various Feature Engineering steps can be executed to ensure that right set of Features have been selected to achieve max accuracy.
	-	Data Profiling step such as Correlation can be executed to identify correlation between different feature which in turn helps in Feature Selection.
* Convert strings to numeric values
	-	Feature data must be represented in Numeric Values for Model Building.
	- 	String Indexer node can be used to index String Categorical data in a column. It would result in corresponding Numeric values facilitating Model Building.
	-	One Hot Encoder node can also be used for this purpose.
* Use the Vector Assembler node to create a features columns. It will contain data from all the columns which would be used as features in the Model.
	-	A set of incoming column can be selected as Feature List. Featue List would be used to determine predicted value.
	-	Feature List needs to be selected based on the Feature Selection method.
* Split the dataframe for training and test
	-	Multiple Split nodes can be used to split the data into Trainig and Test Dataset. Percentage value in the node determines the split percentage.
* Use a model build node like Regression/Classification/Clustering to create the model on the training dataset
	-	Multiple Regression/Classification/Clustering ML Nodes are available to traing the model. 
* Use a Predict node for predicting on the test dataset using the Model created
	-	ML Model built in the previous step can be applied on the Test Dataset using the Predict Node to predict values.
* Use an Evaluator node for evaluating the model results
	-	Evaluator node can be used to evaluate accuracy of the Model. Various Steps can be taken to improve accuracy of the Model some of them are Feature Engineering, Re-Configuring Regression ML node and so on.

