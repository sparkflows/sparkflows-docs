Migrate from H2 Database to MySQL
=============================

Fire Insights comes with an embedded H2 database.

There are times when we start with the embedded H2 database, but then want to migrate to MySQL. It is always recommended to start with MySQL database with Fire Insights for long term stability and reliability.

Below are the steps for migrating the data from H2 database to MySQL.

Migrate H2 database data to MySQL using executable jar file.
-----------------------------------------------------


Create the MySQL tables
+++++++++++++++++++++++
- Open the ``fire-schema.mysql`` MySQL script present in the folder ``/fire-3.1.0_spark_2.4/db/mysql`` using the following icon-

    .. figure:: ..//_assets/DB_Migration/Open_Script_Button.png
        :alt: Open Script Button
        :width: 110%
 
- Select the whole script and press the execute icon-

    .. figure:: ..//_assets/DB_Migration/Execute_button.PNG
        :alt: Execute Button
        :width: 3% 

- On running the MySQL script, firedb database will be created along with the tables-

    .. figure:: ..//_assets/DB_Migration/Created_DB.png
        :alt: Fire Database
        :width: 110%

Stop Fire Server
++++++++++++++++++

- Stop the Fire server.
- ./run-fire-server.sh stop


Migrate data from H2 database to MySQL database
+++++++++++++++++++++++++++++++++++

- Update the ``properties.txt`` file in ``/fire-3.1.0_spark_2.4/dbmigration`` folder with the database specific details for the source and destination databases.
- Update the username, password and database URLs for the databases like the following example::
    
    
    #source db
    datasource.url = jdbc:h2:file:~/firedb
    datasource.username = fire
    datasource.password = fire
    datasource.driverClassName = org.h2.Driver

    #destination db
    destinationDatasource.url = jdbc:mysql://localhost:3306/firedb?useSSL=false 
    destinationDatasource.username = root 
    destinationDatasource.password = root
    destinationDatasource.driverClassName = com.mysql.cj.jdbc.Driver
 

- Open the command prompt.
- Navigate to ``dbmigration`` folder inside ``fire-3.1.0_spark_2.4``.
- Run the command - ``java -jar dbmigration.jar properties.txt``.

Configure the properties file to point to MySQL database
++++++++++++++++++++++++++++++++++++

Update the ``db.properties`` file to point to MySQL database.

Restart Fire Server
++++++++++++++++++

- Restart the Fire server.
- ./run-fire-server.sh start

.. note::  If the database migration process throws an exception or error then resolve the issue and then re-execute the MYSQL script, then restart the migration process again.
