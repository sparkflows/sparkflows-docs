Model Serving
=============

Fire Insights allows you to save your models. These models can be saved to:

- HDFS : when running on a Hadoop Cluster
- S3 : when running on AWS
- ADLS : when running on Azure
- Local file system : when running on your laptop or independent machine

Once these models are saved, they can be served in various ways.


.. toctree::
   :maxdepth: 2

   scoring-with-workflows.rst
   serving-sparkmllib-models.rst
   serving-h2-models.rst
   serving-sagemaker-models.rst
   serving-scikit-learn-models.rst
   serving-tensorflow-models.rst
   mlflow.rst
   
   

