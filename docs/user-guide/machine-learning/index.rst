
Machine Learning
==========

Fire Insights has extensive ML capabilities. It has a number of nodes for doing ML.

Fire Insights supports a variety of ML engines : Apache Spark ML, H2O, Scikit-learn, Prophet, ARIMA, Keras and Statsmodel.

.. panels::
    :container: container-lg pb-3

    :doc:`/user-guide/machine-learning/sparkml/index`

    Provides Apache Spark based different processors.

    ---

    :doc:`/user-guide/machine-learning/h2o/index`

    Provides H2O processors like H2ODRF, H2OKMeans, H2OGBM, H2OGLRM, H2OGLM, H2OXGBoost.

    ---

    :doc:`/user-guide/machine-learning/sklearn/index`

    Provides Scikit Learn based Classification and Regression Processors.

    ---

    :doc:`/user-guide/machine-learning/feature-selection`

    Feature Selection using Correlation or Feature Importance.
    
    ---

    :doc:`/user-guide/machine-learning/model-persistence/index`

    Save model to files and load them later in order to make predictions.

    ---

    :doc:`/user-guide/machine-learning/model-serving/index`

    Models can be saved to HDFS ,S3, ADLS or Local file system.

    ---

    :doc:`/user-guide/machine-learning/mlflow`

    Integrates deeply with Apache MLflow and can be configured to output the models to MLflow.



.. toctree::
   :hidden:

   sparkml/index.rst
   h2o/index.rst
   sklearn/index.rst
   feature-selection.rst
   model-persistence/index.rst
   model-serving/index.rst
   mlflow.rst
   
   

   
   
