Migrate from H2 Database to MySQL
=============================

Fire Insights comes with an embedded H2 database.

There are times when we start with the embedded H2 database, but then want to migrate to MySQL. It is always recommended to start with MySQL database with Fire Insights for long term stability and reliability.

Below are the steps for migrating the data from H2 database to MySQL.

Migrate H2 Database Data to MySQL Using Executable Jar File.
-----------------------------------------------------

**Step 1 : Stop the Fire Server**
+++++++++++++++++++++++++++++++++++
Before proceeding with the migration, stop the Fire server using the following command:

  * For Linux OS -
      
    ::
   
        ./run-fire-server.sh stop

  * For Windows OS -

    ::
   
        run-fire-server.bat stop

**Step 2 : Run the H2 DB Script**
+++++++++++++++++++++++++++++++++++++

* For **Linux OS** - Update the existing schema for Fire of H2 DB by executing the **create-h2-db.sh** file ::

         cd fire-x.y.z

         ./create-h2-db.sh

* For **Windows OS** - Update the existing schema for Fire of H2 DB by executing the **create-h2-db.bat** file by double clicking on it.

.. note::  Before running the H2 DB script, please add the following H2 DB SQL statements to the **fire-schema.h2.sql** file.

::

    ALTER TABLE user_configs DROP COLUMN program_parameters;
    ALTER TABLE webapp DROP COLUMN condition;
    ALTER TABLE webapp_stage DROP COLUMN condition;
    ALTER TABLE application_connection DROP COLUMN organisation;
    ALTER TABLE application_connection DROP COLUMN bucket;

**Step 3 : Create the MySQL Database with its Tables**
+++++++++++++++++++++++++++++++++++++

   #. **Method 1** -

      * Open the **fire-schema.mysql** MySQL script present in the folder **/fire-3.1.0_spark_2.4/db/mysql** using the icon shown below:

         .. figure:: ../..//_assets/DB_Migration/Open_Script_Button.png
              :alt: Open Script Button
              :width: 110%
 
      * Select the whole script and press the execute icon shown below:

         .. figure:: ../..//_assets/DB_Migration/Execute_button.PNG
              :alt: Execute Button
              :width: 3% 

      * On running the MySQL script, firedb database will be created along with the tables, as shown below.

         .. figure:: ../..//_assets/DB_Migration/Created_DB.png
           :alt: Fire Database
           :width: 110%

   #. **Method 2** -

      * In this method we must have created the database **firedb** beforehand using the mysql command line by running the following commands ::

         CREATE DATABASE IF NOT EXISTS firedb;
         use firedb;
 
      * Then make sure to update **conf/db.properties** file to point to MySQL DB like the example given below :: 

            spring.datasource.url=jdbc:mysql://localhost:3306/firedb
            spring.jpa.database = MYSQL
            spring.datasource.username = root
            spring.datasource.password = root
            spring.datasource.driverClassName=com.mysql.cj.jdbc.Driver


      * For **Linux OS** - Create the tables for Fire in MySQL by executing the **create-mysql-db.sh** file ::

         cd fire-x.y.z

         ./create-mysql-db.sh

      * For **Windows OS** - Create the tables for Fire in MySQL by executing the **create-mysql-db.bat** file by double clicking on it.

.. note::  Please make sure to run the SQL command **SET GLOBAL max_allowed_packet=268435456;** on the SQL console of MySQL to increase packet size limit. This ensures that large records or bulk inserts from the H2 database do not fail during migration due to the default packet size restriction. Increasing the limit to 256 MB allows the migration to handle large data payloads without encountering “Packet too large” or “Communication link failure” errors. This command can only be executed by a user with MySQL administrative privileges (such as the root user or any account with the SUPER or SYSTEM_VARIABLES_ADMIN privilege)

**Step 4 : Migrate data from H2 Database to MySQL Database**
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. Create a folder with the name of **dbmigration** in **/fire-x.y.z** folder and add a **properties.txt** file in the same folder with the database specific details for the source and destination databases given in the next step.

#. Update the username, password and database URLs for the databases, like the following example in **properties.txt** ::
    
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
 - Open the command prompt for Windows OS or terminal in Linux OS.
 - Navigate to **dbmigration** folder inside **fire-x.y.z**.
 - Run the following command to execute the migration process.

   ::

       java -jar dbmigration.jar properties.txt

Download Link : `dbmigration.jar. <https://sparkflows-release.s3.us-east-1.amazonaws.com/fire/common/dbmigration.jar>`_

.. note::  Please make sure to add super user detials for the destination DB and also provide the username and password for the same in the above mentioned **properties.txt** file to run the migration cleanly without any privilege related errors.

**Step 5 : Configure the db.properties file to point to MySQL Database**
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

  After successfully migrating the data, make sure to update the **conf/db.properties** file to point to the MySQL database.

**Step 6 : Restart the Fire Server**
+++++++++++++++++++++++++++++++++++++++++
  
For **Linux OS** - Start the Fire server again using the following command:

  ::

     ./run-fire-server.sh start

For **Windows OS** - Start the Fire server again using the following command:

  ::

     run-fire-server.bat start

.. note::  If the database migration process throws an exception or error then resolve the issue and then re-execute the MYSQL script, then restart the migration process again.

Troubleshooting
---------------

Post running the dbmigration step if errors are seen in relation to data too long for column **description** on **analysis_flow_execution** table then add the below at the end of the **fire-schema.mysql.sql** script present in **db/mysql/** folder. Post this run the **create-mysql-db.sh** to recreate the db and its tables for MySQL and try the DB Migration step again.

::

    ALTER TABLE analysis_flow_execution MODIFY COLUMN description VARCHAR(1000);
