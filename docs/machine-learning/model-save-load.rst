Model Save/Load
================

Save/ Load Model allows you to save your model to file and load it later in order to make predictions.

Fire Insights allows you to save the ML Model created. The ML Models can be loaded in the same or other workflows to be used for scoring. The ML Models can also be downloaded from HDFS Browse.

Spark ML Models
---------------

Spark ML models are saved into a directory with multiple files in it. Fire Insights has processors saving and loading the Spark ML models.

H2O Models
----------

H2O Models can be saved in binary format or in MOJO format. Fire Insights has processors for them.

More details of saving and loading the H2O Models is available here:

http://docs.h2o.ai/h2o/latest-stable/h2o-docs/save-and-load-model.html


Scikit-Learn Models
--------------------

Scikit-Learn models are persisted with pickle. Fire Insights has processors for saving and loading the pickle models.

More details of the pickle format is available here:

https://scikit-learn.org/stable/modules/model_persistence.html


