Airflow Snowflake Operators
======

The Airflow Snowflake Operators provide seamless integration between Apache Airflow and Snowflake. These operators allow you to automate tasks like executing SQL queries, loading data into Snowflake, or managing Snowflake objects (like tables, schemas, and databases) as part of your data workflows. By using these operators, you can integrate Snowflake tasks into your larger ETL or data engineering pipelines.

Pre-Requisites
------

#. Apache Airflow installed (with the Snowflake provider: apache-airflow-providers-snowflake).
#. Snowflake account and proper setup (with a user, role, and permissions).
#. Snowflake Python Connector (snowflake-connector-python) installed in your Airflow environment.
#. Airflow connection to Snowflake set up in the Airflow UI or via environment variables.
#. Snowflake warehouse and database available for the required operations.
#. Network configuration for communication between Airflow and Snowflake (including IP whitelisting if necessary).
#. Ensure the Snowflake user has the necessary roles and permissions to execute queries and manage data.

Apache Airflow Installation
----

Airflow Version: Ensure that you have a working installation of Apache Airflow (preferably 2.x version). Airflow is the orchestrator that you will use to manage workflows, including interactions with Snowflake.

To install Apache Airflow, use:
::

    pip install apache-airflow

.. Note:: Ignore this step if you already have Airflow running with 2.x

If you want to use Snowflake integration, you should install the necessary provider:
::

    pip install apache-airflow-providers-snowflake

Snowflake Account and Setup
----

You need access to a Snowflake account to interact with the Snowflake cloud data platform.

#. Sign Up/Log In to Snowflake

   #. If you don’t have a Snowflake account, sign up for a free trial or get access through your organization: Snowflake Sign Up.

#. Create or Use an Existing Database: Ensure that you have a database, schema, and appropriate permissions to run queries or operations. You’ll need these details for the connection configuration.
