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

.. Note:: Ignore this step if you already have Snowflake account setup.


Snowflake User and Role Setup
-----

You must have a Snowflake user account with appropriate roles and permissions to interact with Snowflake via Airflow.

#. Create a Snowflake User:

   #. Log in to Snowflake.
   #. Create a user with permissions to run queries, manage data, etc.
   #. Example SQL to create a user:
      ::

          CREATE USER my_user PASSWORD = 'your_password' 
          DEFAULT_ROLE = my_role 
          MUST_CHANGE_PASSWORD = FALSE;

.. Note:: Ignore this step if you already have Snowflake User and Role Setup.


#. Assign Roles: The Snowflake user must have the appropriate role with permissions to interact with the Snowflake resources. A role like SYSADMIN or a custom role that has access to the necessary databases and schemas would be required.

   #. Example SQL to assign a role:
      ::

          GRANT ROLE SYSADMIN TO USER my_user;

.. Note:: Ignore this step if you already Assign Roles.

#. Create or Use a Warehouse: Ensure a Snowflake Virtual Warehouse is available to run your queries or data transformations.

   #. Example SQL to create a warehouse:
      ::
          CREATE WAREHOUSE my_warehouse 
          WITH WAREHOUSE_SIZE = 'SMALL' 
          AUTO_SUSPEND = 60 
          AUTO_RESUME = TRUE;

.. Note:: Ignore this step if you already have Warehouse.

Snowflake Connector (Python Snowflake Connector)
-----

You must install the Snowflake Python connector (snowflake-connector-python) in your Airflow environment to allow Airflow to communicate with Snowflake.

::

    pip install snowflake-connector-python

You also need the SQLAlchemy Snowflake dialect if you're using SQLAlchemy (which is often used with Airflow's SnowflakeOperator)

::

    pip install snowflake-sqlalchemy

.. Note:: Ignore this step if its already got installed with ``apache-airflow-providers-snowflake`` .


Airflow Snowflake Connection
----

Airflow requires a connection to authenticate and authorize access to Snowflake. The Snowflake connection can be set up in the Airflow UI or via environment variables.


**A. Using Username and Password Authentication**
+++++

Below are the steps to create Snowflake Connection using Username and Password

Setup via the Airflow UI:

#. Go to the Airflow UI

   #. Open the Airflow web interface, typically accessible at http://localhost:8080 or your custom Airflow instance.

#. Create a New Connection

   #. Navigate to Admin → Connections.
   #. Click on the "+" button to add a new connection.

#. Configure the Snowflake connection

   #. Conn Id: Give a name for the connection, e.g., snowflake_default.
   #. Conn Type: Select Snowflake.
   #. Host: The URL of your Snowflake instance, e.g., xy12345.snowflakecomputing.com.
   #. Schema: The default schema for your queries, e.g., PUBLIC.
   #. Database: The Snowflake database you want to interact with, e.g., MY_DB.
   #. Login: The Snowflake user you created, e.g., my_user.
   #. Password: The password for the Snowflake user.
   #. Warehouse: The Snowflake warehouse to use, e.g., my_warehouse.
   #. Role (optional): The Snowflake role, e.g., SYSADMIN or your custom role.

#. Save the connection.

   Example
::

    Conn Id: snowflake_default
    Conn Type: Snowflake
    Host: xy12345.snowflakecomputing.com
    Schema: PUBLIC
    Database: MY_DB
    Login: my_user
    Password: your_password
    Warehouse: my_warehouse
    Role: SYSADMIN

You can also set up the connection using environment variables or a .env file for production use.


**B. Using Key-Pair Authentication**
+++++++++++++++++++++++++++++++++++++

To use the **Run Snowflake Command** node in a pipeline, a connection in Airflow with type Snowflake needs to be created. 

Follow the steps below for the same:

**Step 1 : Navigate to Airflow Connections**

 * Open your Airflow UI and Go to **Admin > Connections**.
 * Click on ``+`` to add a new record.
 * Select **Snowflake** from the dropdown in the Connection Type, as shown below.

   .. figure:: ../../../_assets/configuration/airflow/af-keypair-add-connection.PNG
      :alt: airflow
      :width: 60%

**Step 2 : Configure the Snowflake Connection**

In the Connection form, set the following fields:

 * ``Login`` : Enter your Snowflake username.
 * ``Account`` : Enter your Snowflake account name (e.g., dwrpeje-zu65584).
 * ``Warehouse`` : Provide the name of your Snowflake warehouse.
 * ``Private Key`` : Paste the private key content in PEM format (plain text).
 * ``Password`` : Leave this field empty when using keypair authentication.

  .. figure:: ../../../_assets/configuration/airflow/af-keypair-config-details.PNG
      :alt: airflow
      :width: 60%

After saving, ensure the connection appears in the list of connections under **Admin > Connections**, as shown below:

  .. figure:: ../../../_assets/configuration/airflow/af-connection-list.png
      :alt: airflow
      :width: 60%

**Step 3 : Use the Connection in Sparkflows Pipeline**

 * In your Sparkflows pipeline, add the **Run Snowflake Command** node.
 * In the node settings, select the Snowflake connection you created above i.e. **SnowflakeKeyPair**, as shown below.

   .. figure:: ../../../_assets/configuration/airflow/run-sf-command-node.png
      :alt: airflow
      :width: 60%

 * When the pipeline runs, Sparkflows will trigger the **RunSnowflakeCommand Airflow Operator** using the selected Snowflake connection.




























Network and Security Configurations
----

Ensure that your Airflow environment can communicate with the Snowflake instance:

#. IP Whitelisting: If Snowflake has IP whitelisting enabled, ensure that the IP addresses of your Airflow worker nodes are whitelisted in Snowflake.

#. Encryption and TLS: Make sure that the connection is secured and Snowflake’s network policies are adhered to, especially for sensitive data.

Airflow DAG Configuration
-----

Once the connection is configured and the Python packages are installed, you can now define your Airflow DAGs to interact with Snowflake.

Permissions for Airflow Snowflake User
-----
Ensure the Snowflake user you created for Airflow has the required permissions to execute the queries. This includes:

#. Read Permissions: Access to the databases and tables you intend to query.
#. Write Permissions: If you are writing data, ensure the user has the appropriate permissions on the target schema or database.


Example of granting permissions:

::

     GRANT SELECT ON DATABASE MY_DB TO USER my_user;

.. Note:: Make sure that Airflow and Snowflake should be accessible.
