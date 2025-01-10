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
