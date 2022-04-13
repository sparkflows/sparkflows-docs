Integration with MLflow
=======================

Fire Insights integrates deeply with Apache MLflow.

Fire Insights can be configured to output the models to MLflow.

Prerequisites
-------------

Below are the Prerequisites for installing MLflow on a Mac or Linux machine::

  - Python 3.7+ 
  - pip 21.0+

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



