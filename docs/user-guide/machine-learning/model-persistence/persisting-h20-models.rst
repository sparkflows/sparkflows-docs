Persisting H2O Models
=====================

H2O Models
----------

H2O Models can be saved in binary format or in MOJO format. Fire Insights has processors for saving and reading them back.

Save H2o Model processor
+++++++++++++++++++++

H2OModelSave Processor saves the H2O model at the specified path in the binary format.

.. figure:: ../../../_assets/model/h2omodelsaveconfigurations.PNG
   :alt: Modelsave
   :width: 80%
   
Load H2o Model processor
+++++++++++++++++++++
   
H2OModelLoad Processor loads the H2O model in binary format from the specified path.

.. figure:: ../../../_assets/model/h2omodelloadconfiguration.PNG
   :alt: Modelsave
   :width: 80%

More details of saving and loading the H2O Models is available here:

http://docs.h2o.ai/h2o/latest-stable/h2o-docs/save-and-load-model.html



Save and Load H2O Workflow
++++++++++++++++++++++++++
   

Below is a workflow, which saves the generated H2O model on the file system.

.. figure:: ../../../_assets/model/h2o_means_model_save_score.PNG
   :alt: Modelsave
   :width: 80%
   
 
Below is a workflow, which load back the saved model and used in batch scoreing. 

.. figure:: ../../../_assets/model/h2o_means_model_load_score.PNG
   :alt: Modelload
   :width: 80%
   
