Migrating from H2 DB to MySQL
=============================

Fire Insights comes with an embedded H2 DB.

There are times when we start with the embedded H2 DB, but then want to want to an MySQL. It is always recommended to start with MySQL database with Fire Insights for long term stability and reliability.

Below are the steps for migrating the data from H2 DB to MySQL.

Migrate H2 DB data to MySQL using executable jar file.
-----------------------------------------------------


Create the MySQL tables
+++++++++++++++++++++++

- Run MySQL script to generate fire database and tables in MySQL.

Stop Fire server
++++++++++++++++++

- Stop the Fire server
- ./run-fire-server.sh stop


Migrate data from H2 DB to MySQL database
+++++++++++++++++++++++++++++++++++

- Open the command prompt.
- Go to the `migratedb` folder inside `fire-ui`.
- Run command - ``java -jar migratedb.jar <MySQL JDBC URL> <MySQL user name> <MySQL password>``

Configure the properties file to point to MySQL database
++++++++++++++++++++++++++++++++++++

Update the db.properties file to point to MySQL database

Restart Fire server
++++++++++++++++++

- Restart the Fire server
- ./run-fire-server.sh start


