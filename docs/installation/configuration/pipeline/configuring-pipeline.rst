Configuring Pipelines
======================

Fire uses Apache Airflow for executing Pipelines. Hence Airflow has to be installed on the same machine as Fire.

Below are the configurations needed in Fire for Airflow.

.. figure:: ../../../_assets/user-guide/pipelines-configuration.PNG
   :alt: Pipelines Configuration
   

- Set airflow.enabled to true
- Set airflow.dag value to ‘/home/sparkflows/airflow’
- Set airflow.endpointURL value to ‘http://localhost:8090’ or whatever port the airflow webserver is listening to


