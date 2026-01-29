ClickHouse Connection
=======

Sparkflows provides the capability to create ClickHouse connection and use the connection for reading from and writing to ClickHouse tables. Below are the steps for creating ClickHouse connection in Sparkflows:

  * Download ClickHouse JDBC Driver
  * Install the JDBC Driver
  * Restart Sparkflows
  * Create the ClickHouse Connection

Download ClickHouse JDBC Driver
-------------

- ClickHouse JDBC Driver can be downloaded from maven repository: https://repo1.maven.org/maven2/com/clickhouse/clickhouse-jdbc/0.5.0/clickhouse-jdbc-0.5.0.jar
- Use the JAR file (clickhouse-jdbc-0.5.0.jar) for installation in the Fire.

Install the JDBC Driver
--------

In order to install the JDBC driver copy the driver jdbc jar file into ``fire-user-lib`` and ``fire-server-lib`` directories under the Fire installation home directory.

Restart Fire Server
------------

Once you have copied the JDBC driver into the required folder, restart the Fire server with ``./run-fire-server.sh restart`` for it to register the new driver.

This will restart the Fire services automatically.

Or else, you can also wait for 60 minutes and the JDBC driver would be automatically registered with Sparkflows.

Create the ClickHouse Connection
-----

Clickhouse JDBC uses the MySQL-compatible interface for connectivity. So, you can create Clickhouse connection by selecting the connection type as MySQL.

Create the Clickhouse Connection at Global, Group or Project level.

Connection Details
++++

Enter the configuration details with the help of table given below and click on ``Add Connection``.

.. figure:: ../../../_assets/installation/connection/mysql_storage.PNG
   :alt: connection
   :width: 60%


.. figure:: ../../../_assets/installation/connection/clickhouse_connection.png
   :alt: connection
   :width: 60%  
                                                 
Test Connection and Save
+++++

Once you have entered the connection details, click on ``Test Connection``. If the connection is successful,  click on ``Save`` to save the connection. 

Now, you are ready to start using the Connection in workflows.


.. Note:: Make sure that ClickHouse URL should be accessible from Sparkflows web server URL.

Connection Field Details
----------------------

.. list-table:: 
   :widths: 10 20 20
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
     - Choose MySQL as Connection Type
   * - Connection Name
     - Connection Name
     - Add a unique Connection Name
   * - Username 
     - Username
     - Username for ClickHouse
   * - Password
     - Password
     - Password of ClickHouse
   * - Title 
     - Title for selected Connection
     - Add a unique Title
   * - Description
     - Connection Description
     - Add some Connection Description
   * - Url
     - Url for ClickHouse
     - JDBC Url for ClickHouse
   * - Driver Class
     - Driver Class Name for ClickHouse
     - com.clickhouse.jdbc.ClickHouseDriver (by default)














