Sybase Connection
================

Fire Insights provides the capability to create Sybase connection and use the connection for reading from and writing to Sybase tables. Below are the steps for creating Sybase connection in Fire Insights:

  * Download Sybase JDBC Driver
  * Install the JDBC Driver
  * Restart Fire Insights
  * Create the Sybase Connection

Download Sybase JDBC Driver
-------------

- Sybase JDBC Driver can be downloaded from : https://osdn.net/projects/sfnet_id2d/downloads/jdbc%20drivers/jconn4.jar/
- Ensure that the JDBC JAR file is available in the directory.
- Use the JAR file (jconn4.jar) for installation in the Fire.


Install the JDBC Driver
--------

In order to install the JDBC driver, copy the driver jdbc jar file into ``fire-user-lib`` and ``fire-server-lib`` directories under the Fire installation home directory.

Restart Fire Server
------------

Once you have copied the JDBC driver into the required folder, restart the Fire server with ``./run-fire-server.sh restart`` for it to register the new driver.

This will restart the Fire services automatically.

Or else, you can also wait for 60 minutes and the JDBC driver would be automatically registered with Fire Insights.

Create the Sybase Connection
-----

Create the Sybase Connection at Global, Group or Project level.

Connection Details
++++

Enter the configuration details with the help of table given below and click on ``Add Connection``.

   .. figure:: ../../../_assets/connections/sybase-storage.png
      :alt: postgresql
      :width: 60%

   
   .. figure:: ../../../_assets/connections/sybase-connection.png
      :alt: postgresql
      :width: 60%  

Test Connection and Save
+++++

Once you have entered the connection details, click on ``Test Connection``. If the connection is successful, click on ``Save`` to save the connection. 

Now, you are ready to start using the Connection in workflows.


.. Note:: Make sure that Sybase URL should be accessible from Sparkflows web server URL.


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
        - Choose JDBC as Connection Type
      * - Connection Name
        - Connection Name
        - Add a unique Connection Name
      * - Username 
        - Username
        - Username for Sybase
      * - Password
        - Password
        - Password for Sybase
      * - Title 
        - Title for selected Connection
        - Add a unique Title
      * - Description
        - Connection Description
        - Add some Connection Description
      * - Url
        - Url for Sybase
        - JDBC Url for Sybase
      * - Driver Class
        - Driver Class Name for Sybase
        - com.sybase.jdbc4.jdbc.SybDriver (by default)

.. Note:: Url for Sybase: jdbc:sybase:Tds:hostname:port/database

Run Workflows using Sybase JDBC JAR
-----------------

When running workflows, select the checkbox for the JAR file (jconn4.jar) in the Workflow Execution Page.
