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

Databricks Account
-----

You need a Databricks account to interact with their APIs and manage clusters, notebooks, and jobs. Databricks integrates with Apache Spark and provides managed Spark clusters, making it suitable for big data and machine learning tasks.

 #. Sign up for a Databricks account if you don’t have one already: Databricks Sign Up
 #. Databricks Workspace: Ensure you have access to a Databricks workspace where you can manage notebooks, jobs, and clusters.

Databricks API Token
------

To authenticate with Databricks via Airflow, you will need an API Token. This token is required to set up the connection between Airflow and Databricks.

Steps to generate an API token:

 #. Log in to your Databricks Workspace.
 #. Navigate to the User Settings in the top-right corner (click on your username).
 #. Click on Generate New Token in the Access Tokens section.
 #. Save the generated token in a secure place as you will use it in the Airflow connection configuration.

Databricks Connection in Airflow
-----

Airflow uses connections to store authentication details securely. You need to set up a connection for Databricks in the Airflow UI.

Steps to set up the connection in Airflow UI:

 #. Go to the Airflow UI:
 #. Open the Airflow web interface, typically accessible at http://localhost:8080 (or your custom URL).
 #. Create a new connection:
 #. Navigate to Admin → Connections.
 #. Click on the "+" button to add a new connection.
 #. Configure the Databricks connection:
 #. Conn Id: databricks_default (or another custom ID).
 #. Conn Type: Select Databricks.
 #. Host: The URL of your Databricks instance, e.g., https://<databricks-instance>.azuredatabricks.net (for Azure Databricks) or https://<databricks-instance>.databricks.com (for AWS).
 #. Token: Paste the API token you generated earlier.
 #. Click Save to store the connection.

Python Environment (with Required Libraries)
------

Ensure that your Python environment has the necessary libraries installed to use the Databricks operators. These include the Airflow Databricks provider and any other dependencies your DAGs may require.

To install the required package for Databricks integration in Airflow, use:
::

    pip install apache-airflow-providers-databricks

Airflow DAG Setup
----

Once the Airflow connection and Databricks API token are set up, and your Databricks cluster is ready, you can now start building your Airflow DAGs to interact with Databricks.

Permissions and Roles
-----

Ensure that the Databricks user you're using has the appropriate permissions to:

 #. Run Pipelines
 #. Create and manage clusters (if required by your Airflow tasks).
 #. Execute notebooks and run jobs.
