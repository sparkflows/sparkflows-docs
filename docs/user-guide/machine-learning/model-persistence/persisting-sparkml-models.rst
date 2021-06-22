Persisting SparkML Models
=========================

Spark ML Models
---------------

Spark ML models are saved into a directory with multiple files in it. Fire Insights has processors for saving and loading the Spark ML models.

Save Model processor
+++++++++++++++++++++

NodeModelSave processor, saves the given Apache Spark ML model at the given location.

.. figure:: ../../../_assets/model/savemodelconfigurations.PNG
   :alt: Modelsave
   :width: 80%
   
ML Save Workflow
+++++++++++++++++++++

The below workflow uses the NodeModelSave for saving the Spark ML model at the given location.

.. figure:: ../../../_assets/model/mlmodelsave.png
   :alt: Modelsave
   :width: 80%
   
   
Load Model processor
+++++++++++++++++++++

ML Load Model reads in the Spark ML model from the specified location.

.. figure:: ../../../_assets/model/loadmodelconfigurations.PNG
   :alt: Modelsave
   :width: 80%   
   
   
   
ML Load Workflow
+++++++++++++++++++++
   
The below workflow reads in the ML model from the given location. It then uses the Predict node for the predictions.

.. figure:: ../../../_assets/model/mlmodelload.png
   :alt: Model Load Workflow
   :width: 80%   
   
