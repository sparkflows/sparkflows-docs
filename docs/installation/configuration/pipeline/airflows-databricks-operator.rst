Airflow Databricks Operator
==========

The Airflow Databricks Operator allows you to integrate Databricks with Apache Airflow to automate workflows such as running jobs, submitting notebooks, and managing clusters on Databricks.

Pre-Requisites
-----

#. Apache Airflow installed (with the Databricks provider).
#. Databricks account and workspace.
#. Databricks API token for authentication.
#. Set up a Databricks connection in Airflow using the API token.
#. Ensure your Python environment has necessary libraries (like apache-airflow-providers-databricks).
#. Airflow DAGs properly set up to submit Databricks jobs or notebooks.
#. Proper permissions in Databricks for the user executing tasks.

Apache Airflow Installation
----

Airflow Version: Ensure that you have a working installation of Apache Airflow (usually version 2.x) on your machine or cloud environment. Airflow provides a platform to programmatically author, schedule, and monitor workflows.

To install Apache Airflow, use:


::
    
    pip install apache-airflow


.. Note:: Ignore this step if you already have Airflow running with 2.x
