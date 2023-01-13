Install JDBC Drivers for Workflows
=======================

Fire Insights has JDBC Processors for reading data from JDBC sources or writing to JDBC sinks.

In order to connect to a JDBC source like Oracle/DB2/Postgres etc. the JDBC driver needs to be installed in Fire.

Below are the steps for installing the JDBC driver :

- *Download the JDBC JAR file.*
- *Copy it into "fire-user-lib" and "fire-server-lib" directory under the Fire installation home directory.*
- *Restart Fire.*

Download the JDBC JAR File
-------------------------- 

Download the JDBC JAR file for the database you are looking to connect to.

Copy it into fire-user-lib & fire-server-lib
--------------------------

Under the Fire installation home directory, there is "fire-user-lib" and "fire-server-lib" directory.

Copy the downloaded JDBC JAR file into it.


Restarting Fire Server
------------

Restart the Fire server with ``./run-fire-server.sh restart``

This will restart the Fire services automatically.


Running Workflows Depending on the JARS Added
---------------------------

When running workflows which depend on the JAR file, select the checkbox for that JAR file in the Workflow Execution Page. 

Downloading the JDBC JAR Files
---------------------------

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


JDBC Drivers
-------

When using the JDBC processors, the following can be used for the JDBC Driver. Below are the JDBC URLs for some databases :

* MySQL : com.mysql.jdbc.Driver
* PostgreSQL : org.postgresql.Driver
* Oracle : oracle.jdbc.driver.OracleDriver

Example JDBC URLs
----------------

Below are some examples of JDBC URLs for reading from Relational sources when using the JDBC Processors :

* MySQL : jdbc:mysql://localhost:3306/mydb
* PostgreSQL : jdbc:postgresql://localhost:5432/mydb


