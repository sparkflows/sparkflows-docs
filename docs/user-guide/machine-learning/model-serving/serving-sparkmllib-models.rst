Serving Spark MLlib Models
===========================

Fire Insights creates Apache Spark MLlib models. These models get saved as files on the File System.

NodeModelSave saves the Spark ML models as files. It uses the Spark interfaces to save the model.

.. figure:: ../../../_assets/model/SparkMLModelSave.png
   :alt: SaveML Model
   :width: 80%

Once the SparkML model is saved, they can be loaded and used in scoring. Fire Insights enables saving both Spark ML models and pipelines.

Batch Model Scoring:
--------------------

By using NodeModelLoad & selecting the particular type of model to be loaded, the model would be loaded in the workflow and it can be used for scoring the input data.

.. figure:: ../../../_assets/model/SparkMLModelScore.png
   :alt: LoadML Model & Score
   :width: 80%

Online Scoring with Kafka and Spark Streaming:
---------------------------------------------

Scalable messaging platform like Kafka to send newly acquired data to a long running Spark Streaming process. The Spark process can then make a new prediction based on the new data.


