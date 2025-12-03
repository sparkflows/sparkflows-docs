Model Serving
=============

Sparkflows allows you to save your models. These models can be saved to:

- **HDFS :** When running on a Hadoop Cluster.
- **S3 :** When running on AWS.
- **ADLS :** When running on Azure.
- **Local file system :** When running on your laptop or independent machine.

Once these models are saved, they can be served in various ways.


.. panels::
    :container: container-lg pb-3

    :doc:`/user-guide/machine-learning/model-serving/scoring-with-workflows`

    Models built with the workflows can be saved onto the File System then, can be scored with another workflow.

    ---

    :doc:`/user-guide/machine-learning/model-serving/serving-sparkmllib-models`

    Apache Spark MLlib models get saved as files on the File System.

    ---

    :doc:`/user-guide/machine-learning/model-serving/serving-h2-models`

    H2O allows you to persist the models you have built to either a Plain Old Java Object (POJO) or a Model ObJect, Optimized (MOJO).

    ---

    :doc:`/user-guide/machine-learning/model-serving/serving-sagemaker-models`

    When the SageMaker models are built it automatically provides a REST endpoint for online scoring of the models.

    ---

    :doc:`/user-guide/machine-learning/model-serving/serving-scikit-learn-models`

    SaveAsPickle processors used for persisting the Scikit Learn models as pickle files.

    ---

    :doc:`/user-guide/machine-learning/model-serving/serving-tensorflow-models`

    Provide NodeSaveKerasModel and NodeLoadKerasModel processors for persisting the Tensorflow models.


.. toctree::
   :hidden:

   scoring-with-workflows.rst
   serving-sparkmllib-models.rst
   serving-h2-models.rst
   serving-sagemaker-models.rst
   serving-scikit-learn-models.rst
   serving-tensorflow-models.rst
   
   

