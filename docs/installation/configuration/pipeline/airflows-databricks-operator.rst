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
