Model Persistence
================

Save / Load Model allows you to save your model to files and load them later in order to make predictions.

Fire Insights allows you to save the ML Model created. The ML Models can be loaded in the same or other workflows to be used for scoring. The ML Models can also be downloaded from HDFS Browse Page.

The ML models can be saved into the following locations:

- HDFS : when Fire Insights is connected to a Hadoop Cluster
- S3 : when the jobs are running on EMR or on Databricks cluster on AWS. Even when Fire is running in local standalone mode on AWS, the models can be saved onto S3.

In order to save onto S3, the model path can be provided as ``s3://models/priceprediction``

.. toctree::
   :maxdepth: 2

   persisting-sparkml-models.rst
   persisting-h20-models.rst
   persisting-scikit-learn-models.rst
   
   
   
