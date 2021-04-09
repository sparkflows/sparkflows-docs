Installing JDBC Drivers for Dashboard
=======================

Dashboard work with JDBC sources. The appropriate JDBC jars have to be installed.

Below are the steps for installing the JDBC driver for Interactive Dashboards::

  Download the JDBC jar file
  Copy it into `fire-server-lib` directory under the Fire installation
  Restart fire-server

Download the JDBC jar file
--------------------------

Download the JDBC jar file for the Database you are looking to connect to.

Copy it into fire-server-lib
--------------------------

Under the Fire installation directory, there is ``fire-server-lib`` directory.

Copy the downloaded JDBC jar file into it.


Restart Fire Server
------------

Restart Fire server with ``./run-fire-server.sh restart``

 
Downloading MySQL Connector
---------------------------

- MySQL connector can be downloaded from : https://dev.mysql.com/downloads/connector/j/
- After downloading untar it with : ``tar xvf mysql-connector-java-8.0.11.tar.gz`` 
- After untaring the jdbc jar file is available in the directory
- Use the jar file (mysql-connector-java-8.0.11.jar) for installation in Fire

