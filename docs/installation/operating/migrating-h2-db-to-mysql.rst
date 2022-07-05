Migrating from H2 DB to MySQL
=============================

Fire Insights comes with an embedded H2 DB.

There are times when we start with the embedded H2 DB, but then want to want to an MySQL. It is always recommended to start with MySQL database with Fire Insights for long term stability and reliability.

Below are the steps for migrating the data from H2 DB to MySQL.

Migrate H2 DB data to MySQL using executable jar file.
-----------------------------------------------------


Create the MySQL tables
+++++++++++++++++++++++
- Open the MYSQL script present in the folder scripts using the following icon-

    .. figure:: ../../_assets/DB_Migration/Open_Script_Button.png
        :alt: Open Script Button
        :width: 110%
 
- Select the whole script and press on the execute icon-

    .. figure:: ../../_assets/DB_Migration/Execute_button.PNG
        :alt: Execute Button
        :width: 3% 

- On running the MySQL script firedb database will be created along with the tables-

    .. figure:: ../../_assets/DB_Migration/Created_DB.png
        :alt: Fire Database
        :width: 110%

Stop Fire server
++++++++++++++++++

- Stop the Fire server
- ./run-fire-server.sh stop


Migrate data from H2 DB to MySQL database
+++++++++++++++++++++++++++++++++++

- Update the ``properties.txt`` file in ``/fire-3.1.0_spark_2.4/dbmigration`` folder with the database specific details for the source and destination databases.
- Update the username, password and database urls for the databases like the following example::
    
    
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
- Run the command - ``java -jar dbmigration.jar properties.txt``

Configure the properties file to point to MySQL database
++++++++++++++++++++++++++++++++++++

Update the ``db.properties`` file to point to MySQL database

Restart Fire server
++++++++++++++++++

- Restart the Fire server
- ./run-fire-server.sh start
