Install JDBC Drivers for Workflows
=======================

Fire Insights has JDBC Processors for reading data from JDBC sources or writing to JDBC sinks.

In order to connect to a JDBC source like Oracle/DB2/Postgres etc. the JDBC driver needs to be installed in Fire Insights.

Below are the steps for installing the JDBC driver :

- *Download the JDBC JAR file.*
- *Copy it into "fire-user-lib" and "fire-server-lib" directory under the Fire installation home directory.*
- *Restart Fire.*

Copy it into fire-user-lib & fire-server-lib
--------------------------

Under the Fire installation home directory, there is "fire-user-lib" and "fire-server-lib" directory.

Copy the downloaded JDBC JAR file into it.


Restarting Fire Server
------------

Once you have copied the JDBC driver into the required folder, restart the Fire server with ``./run-fire-server.sh restart`` for it to register the new driver.

This will restart the Fire services automatically.

Or else, you can also wait for 60 minutes and the JDBC driver would be automatically registered with Fire Insights.


Downloading the JDBC JAR File
-------------------------- 

This section describes the details for downloading the the JDBC JAR file for a variety of Databases.


MySQL
+++++

- MySQL connector can be downloaded from : https://dev.mysql.com/downloads/connector/j/ or you can download it directly from maven repository : https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.11/
- After downloading, untar it with : ``tar xvf mysql-connector-java-8.0.11.tar.gz`` 
- After untaring, the JDBC JAR file is available in the directory.
- Use the JAR file (mysql-connector-java-8.0.11.jar) for installation in the Fire.

PostgreSQL
++++++++++

- PostgresSQL JDBC drivers can be downloaded from : https://jdbc.postgresql.org/download

.. note:: Already included in Sparkflows package.

Oracle
++++++

- Oracle JDBC drivers can be downloaded from : https://www.oracle.com/technetwork/database/features/jdbc/jdbc-drivers-12c-download-1958347.html

Teradata
++++++++

- Teradata JDBC drivers can be downloaded from : https://downloads.teradata.com/download/connectivity/jdbc-driver

https://dwgeek.com/steps-to-connect-teradata-database-from-spark-examples.html/

Azure Synapse
+++++++++++++

- https://docs.microsoft.com/en-us/azure/synapse-analytics/sql/connect-overview
- https://docs.microsoft.com/en-us/sql/connect/jdbc/microsoft-jdbc-driver-for-sql-server?view=sql-server-ver15

Sybase
++++++

- Sybase JDBC drivers can be downloaded from : https://osdn.net/projects/sfnet_id2d/downloads/jdbc%20drivers/jconn4.jar/

HANA
++++

- HANA JDBC drivers can be downloaded from : https://support.sap.com/en/product/connectors.html


JDBC Driver Class
-------

When using the JDBC processors, the following can be used for the JDBC Driver Class :

* MySQL : com.mysql.jdbc.Driver
* PostgreSQL : org.postgresql.Driver
* Oracle : oracle.jdbc.driver.OracleDriver
* Sybase : com.sybase.jdbc4.jdbc.SybDriver
* HANA : com.sap.cloud.db.jdbc

JDBC URLs
----------------

Below are some examples of JDBC URLs for reading from Relational sources when using the JDBC Processors :

* MySQL : jdbc:mysql://localhost:3306/mydb
* PostgreSQL : jdbc:postgresql://localhost:5432/mydb
* Sybase : jdbc:sybase:Tds:localhost:5000/mydb
* HANA : jdbc:sap://hanaServer:30015/



