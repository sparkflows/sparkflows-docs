Installing JDBC Drivers
=======================

Fire has JDBC Processors for reading from JDBC sources or writing to JDBC sinks.

In order to connect to a JDBC source like Oracle/DB2 etc. the JDBC driver needs to be installed in Fire.

Below are the steps for installing the JDBC driver into Fire:

- *Download the JDBC jar file*
- *Copy it into `fire-user-lib` directory under the Fire installation*
- *Also copy it into `fire-server-lib` directory under the Fire installation*
- *Restart fire*

Download the JDBC jar file
--------------------------

Download the JDBC jar file for the Database you are looking to connect to.

Copy it into fire-user-lib
--------------------------

Under the Fire installation directory, there is ``fire-user-lib`` directory.

Copy the downloaded JDBC jar file into it.

Copy it into fire-server-lib
--------------------------

Under the Fire installation directory, there is ``fire-server-lib`` directory.

Copy the downloaded JDBC jar file into it.

Restart Fire
------------

Restart Fire with ``./run-fire.sh restart``

Fire Server does not need to be restarted.


Downloading MySQL Connector
---------------------------

- MySQL connector can be downloaded from : https://dev.mysql.com/downloads/connector/j/
- After downloading untar it with : tar xvf mysql-connector-java-5.1.46.tar.gz 
- After untaring the jdbc jar file is available in the directory
- Use the jar file (mysql-connector-java-5.1.46.jar) for installation in Fire

