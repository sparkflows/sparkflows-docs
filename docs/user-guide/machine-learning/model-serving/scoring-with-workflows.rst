Scoring with Workflows
======================

Fire Insights enables you to build workflows. Workflows provide for reading data, transforming them and also creating machine learning models. 
Fire Insights supports a number of ML frameworks including Scikit Learn, H2O, Spark ML, Keras etc.

Models built with the workflows can be saved onto the File System. The models can then be scored with another workflow.

Data Preparation and Scoring Environments
-----------------------------------------

The workflows built with Fire Insights can run on a variety of environments. These include:

* Standalone machine
* AWS - EMR
* Azure - HDInsights
* Databricks
* Cloudera

In any of these environments, Fire Insights does not need to be installed for model scoring.
When running on Standalone machine, scoring can be performed with running java/python using the supplied jar/wheel files and the workflow json.

When running on clusters, scoring can be performed with spark-submit using the supplied jar/wheel files and the workflow json.


Workflow Patterns for Scoring Models
------------------------------------

There are a few patterns by which Fire Insights enables Data Preparation/Feature Engineering and Model Scoring.

* One workflow for Data Preparation/Feature Engineering, another for Model Training and the third for Model Scoring
* One workflow for Data Preparation/Feature Engineering plus Model Training. And another workflow for Data Preparation/Feature Engineering plus Model Scoring.

Using 3 Workflows
-----------------

In this pattern, one workflow is built to read in the input datasets, perform Data Preparation and also Feature Engineering.
This workflow prepares the input datasets to be used for Training and also Scoring and saves it to the File System.

The second workflow reads in the prepared data, builds the model and then save it to the File System.

The third workflow also reads in the prepared data, reads in the ML model and then scores the input data. The result of scoring can be saved to the File System, Relational Database, Cassandra, MongoDB, HIVE etc.

Using 2 workflows
-----------------

In this pattern, one workflow is built to read in the input datasets, perform Data Preparation/Feature Engineering and then finally build the ML Model.

For the second workflow, the first workflow is cloned with one click, and the model nodes are removed from the workflow. They are replaced with nodes which read in the model and then score the datasets.



