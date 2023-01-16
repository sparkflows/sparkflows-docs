Model Persistence
================

Save / Load Model allows you to save your model to files and load them later in order to make predictions.

Fire Insights allows you to save the ML Model created. The ML Models can be loaded in the same or other workflows to be used for scoring. The ML Models can also be downloaded from HDFS Browse Page.

The ML models can be saved into the following locations:

- HDFS : when Fire Insights is connected to a Hadoop Cluster
- S3 : when Fire is configured and connected to AWS.
- Local Machine FileSystem : when Fire is running in local mode

In order to save onto S3, the model path can be provided as ``s3://models/priceprediction``

.. panels::
    :container: container-lg pb-3

    :doc:`/user-guide/machine-learning/model-persistence/persisting-sparkml-models`

    Spark ML models are saved into a directory with multiple files in it. Fire Insights has processors for saving and loading the Spark ML models

    ---

    :doc:`/user-guide/machine-learning/model-persistence/persisting-h20-models`

    H2O Models can be saved in binary format or in MOJO format. Fire Insights has processors for saving and reading them back.

    ---

    :doc:`/user-guide/machine-learning/model-persistence/persisting-scikit-learn-models`

    Scikit-Learn models are persisted with pickle. Fire Insights has processors for saving and loading the pickle files
    
.. toctree::
   :hidden:

   persisting-sparkml-models.rst
   persisting-h20-models.rst
   persisting-scikit-learn-models.rst
   
   
   
