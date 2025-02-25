Migrate from H2 Database to MySQL
=============================

Fire Insights comes with an embedded H2 database.

There are times when we start with the embedded H2 database, but then want to migrate to MySQL. It is always recommended to start with MySQL database with Fire Insights for long term stability and reliability.

Below are the steps for migrating the data from H2 database to MySQL.

Migrate H2 Database Data to MySQL Using Executable Jar File.
-----------------------------------------------------


**Step 1 : Create the MySQL Tables**
+++++++++++++++++++++++++++++++++++++
#. Open the **fire-schema.mysql** MySQL script present in the folder **/fire-3.1.0_spark_2.4/db/mysql** using the icon shown below:

   .. figure:: ../..//_assets/DB_Migration/Open_Script_Button.png
        :alt: Open Script Button
        :width: 110%
 
#. Select the whole script and press the execute icon shown below:

   .. figure:: ../..//_assets/DB_Migration/Execute_button.PNG
        :alt: Execute Button
        :width: 3% 

#. On running the MySQL script, firedb database will be created along with the tables, as shown below.

   .. figure:: ../..//_assets/DB_Migration/Created_DB.png
        :alt: Fire Database
        :width: 110%

**Step 2 : Stop the Fire Server**
+++++++++++++++++++++++++++++++++++
  Before proceeding with the migration, stop the Fire server using the following command:

  ::
    
      ./run-fire-server.sh stop


**Step 3 : Migrate Data from H2 Database to MySQL Database**
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. Update the **properties.txt** file located in **/fire-3.1.0_spark_2.4/dbmigration** folder with the database specific details for the source and destination databases.
#. Update the username, password and database URLs for the databases, like the following example::
    
    
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
 
#. Run the migration command by following these steps:
 - Open the command prompt.
 - Navigate to **dbmigration** folder inside **fire-3.1.0_spark_2.4**.
 - Run the following command to execute the migration process.
   ::

       java -jar dbmigration.jar properties.txt

**Step 4 : Configure the Properties File to Point to MySQL Database**
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

  After successfully migrating the data, update the **db.properties** file to point to the MySQL database.

**Step 5 : Restart the Fire Server**
+++++++++++++++++++++++++++++++++++++++++
  Start the Fire server again using the following command:
  ::

     ./run-fire-server.sh start

.. note::  If the database migration process throws an exception or error then resolve the issue and then re-execute the MYSQL script, then restart the migration process again.
