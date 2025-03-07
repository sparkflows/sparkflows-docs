PostgreSQL Connection
================

Fire Insights provides the capability to create "PostgreSQL connection" and use the connection for reading from and writing to PostgreSQL tables. Below are the steps for creating PostgreSQL connection in Fire Insights:

  * Download PostgreSQL JDBC Driver
  * Install the JDBC Driver
  * Restart Fire Insights
  * Create the PostgreSQL Connection

Download PostgreSQL JDBC Driver
-------------

- PostgreSQL JDBC Driver can be downloaded directly from maven repository : https://repo1.maven.org/maven2/org/postgresql/postgresql/42.3.2/postgresql-42.3.2.jar
- Ensure that the JDBC JAR file is available in the directory.
- Use the JAR file (postgresql-42.3.2.jar) for installation in the Fire.

Install the JDBC Driver
--------

In order to install the JDBC driver copy the driver jdbc jar file into ``fire-user-lib`` and ``fire-server-lib`` directories under the Fire installation home directory.

Restart Fire Server
------------

Once you have copied the JDBC driver into the required folder, restart the Fire server with ``./run-fire-server.sh restart`` for it to register the new driver.

This will restart the Fire services automatically.

Or else, you can also wait for 60 minutes and the JDBC driver would be automatically registered with Fire Insights.

Create the PostgreSQL Connection
-----

Create the PostgreSQL Connection at Global, Group or Project level.

Connection Details
++++

Enter the configuration details with the help of table given below and click on ``Add Connection``.

   .. figure:: ../../../_assets/postgresql/postgre-storage.png
      :alt: postgresql
      :width: 60%

   
   .. figure:: ../../../_assets/postgresql/postgre-connection.png
      :alt: postgresql
      :width: 60%


Test Connection and Save
+++++

Once you have entered the connection details, click on ``Test Connection``. If the connection is successful,  click on ``Save`` to save the connection. 

Now, you are ready to start using the Connection in workflows.


.. Note:: Make sure that PostgreSQL URL should be accessible from Sparkflows web server URL.


Connection Field Details
----------------------

   .. list-table:: 
      :widths: 25 25 50
      :header-rows: 1

      * - Title
        - Description
        - Value
      * - Credential Store  
        - Select the Credential Store from drop-down
        - Choose specific Credential Store from drop-down or Select Do not use Credential Store
      * - Select Category
        - Select Category of Connection Type
        - Select Storage Connection
      * - Connection Type 
        - Select the Connection type from drop-down
        - Choose Postgres as Connection Type
      * - Connection Name
        - Connection Name
        - Add an unique Connection Name
      * - Username 
        - Username
        - Username for Postgres
      * - Password
        - Password
        - Password of Postgres
      * - Title 
        - Title for selected Connection
        - Add an unique Title
      * - Description
        - Connection Description
        - Add some Connection Description
      * - Url
        - Url for Postgres
        - JDBC Url for Postgres
      * - Driver Class
        - Driver Class Name for Postgres
        - org.postgresql.Driver (by default)

Run Workflows using PostgreSQL JDBC JAR
-----------------

When running workflows, select the checkbox for the JAR file (postgresql-42.3.2.jar) in the Workflow Execution Page.

