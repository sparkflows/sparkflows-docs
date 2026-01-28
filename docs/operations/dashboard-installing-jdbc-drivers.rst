Install JDBC Drivers for Dashboard
=======================

Dashboard work with JDBC sources. The appropriate JDBC jars have to be installed.

Below are the steps for installing the JDBC driver for interactive dashboards::

  Download the JDBC jar file.
  Copy it into `fire-server-lib` directory under the Fire installation.
  Restart fire server.

Download the JDBC JAR file
--------------------------

Download the JDBC jar file for the database you are looking to connect to.

Copy it into fire-server-lib & fire-user-lib
--------------------------

Under the Fire installation directory, there is ``fire-server-lib`` and ``fire-user-lib`` directory.

Copy the downloaded JDBC jar file into it.

Download MySQL Connector
---------------------------

- MySQL connector can be downloaded from : https://dev.mysql.com/downloads/connector/j/ or directly from maven repository : https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.11/
- After downloading, untar it with : ``tar xvf mysql-connector-java-8.0.11.tar.gz``. 
- After untaring, the JDBC jar file is available in the directory.
- Use the jar file (mysql-connector-java-8.0.11.jar) for installation in Fire.

Download Clickhouse JDBC Driver
---------------------------

- Clickhouse JDBC Driver can be downloaded from maven repository : https://repo1.maven.org/maven2/com/clickhouse/clickhouse-jdbc/0.5.0/clickhouse-jdbc-0.5.0.jar
- Use the jar file (clickhouse-jdbc-0.5.0.jar) for installation in Fire.

Restart Fire Server
------------

Restart Fire server with ``./run-fire-server.sh restart``.

 


