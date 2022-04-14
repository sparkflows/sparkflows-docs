Integration with MLflow
=======================

Fire Insights provides the integration MLflow Model Registry.

More Info: https://docs.databricks.com/applications/mlflow/index.html


Prerequisites
-------------

Below are the Prerequisites for installing MLflow on a Mac or Linux machine::

  Python 3.7+ 
  pip 21.0+

Installing MLflow on Linux:
-----------------------------

::

    pip install mlflow
    
    
Run Mlflow UI:
--------------

::

    mlflow ui
    MLFlow UI - http://localhost:5000
    
Once login to above url, you will see MLflow UI page

.. figure:: ../../_assets/user-guide/machine-learning/sparkml/mlflow/mlflow.PNG
   :alt: mlflow
   :width: 60% 
    
    
.. note:: Make sure to change localhost to your ip or domain name and by default mlflow run on port 5000   



Integrating MLflow with Fire Insights
------------------------------------

In Fire Insights, nodes in python ml packages have integration with mlflow by calling the Mlflow API's paramerts, metrics, model, etc. Fire Insights, workflows will be registered as experiments in mlflow with name and each execution will be separate run's in mlflow.


Below is the example workflow for regression to predict the house price with RidgeRegression Node.
.. figure:: ../../_assets/user-guide/machine-learning/sparkml/mlflow/mlflow_wf.PNG
   :alt: mlflow
   :width: 60% 
 
 
 

Once the above workflow got executed successfully, it will save the model in MLflow.

.. figure:: ../../_assets/user-guide/machine-learning/sparkml/mlflow/mlflow_executions.PNG
   :alt: mlflow
   :width: 60% 



In MLflow, executed workflow is registered as an experiment and with different executions.

From RidgeRegression  model parameters, metrics etc shared with Mlflow registry.

.. figure:: ../../_assets/user-guide/machine-learning/sparkml/mlflow/mlflow_experiment.PNG
   :alt: mlflow
   :width: 60% 


.. figure:: ../../_assets/user-guide/machine-learning/sparkml/mlflow/mlflow_result.PNG
   :alt: mlflow
   :width: 60%    



