Serving Spark MLlib Models
===========================

Fire Insights creates Apache Spark MLlib models. These models get saved as files on the File System.

NodeModelSave, Spark MLWritable: the standard model storage format included with Spark.

.. figure:: ../../_assets/model/SparkMLModelSave.png
   :alt: SaveML Model
   :align: center
   :width: 30%

Once the SparkML model is saved, they can be used for serving.

Batch Model Scoring:
--------------------

By using NodeModelLoad & selecting the particluar type, model will be loaded in workflow and it can be used for score-or-predict the input data.

.. figure:: ../../_assets/model/SparkMLModelScore.png
   :alt: LoadML Model & Score
   :align: center
   :width: 30%
