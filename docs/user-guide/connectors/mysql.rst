MySQL
=====

Fire Insights provides an easy way to read from and write to MySQL.

Below are the steps for it:

  * Download and install the MySQL JDBC Driver.
  * Install the JDBC Driver
  * Restarte Fire Insights
  * Create MySQL Connection
  * Use the ReadJDBC or WriteJDBC node in workflows with the MySQL Connection created

Download the MySQL JDBC Driver
-------------

- MySQL JDBC Driver can be downloaded from : https://dev.mysql.com/downloads/connector/j/ or you can download it directly from maven repository : https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.11/
- After downloading, untar it with : ``tar xvf mysql-connector-java-8.0.11.tar.gz`` 
- After untaring, the JDBC JAR file is available in the directory.
- Use the JAR file (mysql-connector-java-8.0.11.jar) for installation in the Fire.

Install the JDBC Driver
--------

Below are the steps for installing the JDBC driver :

- *Copy the driver jdbc jar file into "fire-user-lib" and "fire-server-lib" directories under the Fire installation home directory.*
- *Restart Fire Insights.*

Restart Fire Server
------------

Once you have copied the JDBC driver into the required folder, restart the Fire server with ``./run-fire-server.sh restart`` for it to register the new driver.

This will restart the Fire services automatically.

Or else, you can also wait for 60 minutes and the JDBC driver would be automatically registered with Fire Insights.

Create MySQL Connection
-------------

* JDBC Driver Class : com.mysql.jdbc.Driver
* JDBC Url : jdbc:mysql://localhost:3306/mydb

Use the ReadJDBC node in workflow
-------------

Use the WriteJDBC node in workflow
-------------


