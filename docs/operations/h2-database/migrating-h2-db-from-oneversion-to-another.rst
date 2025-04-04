Migrate H2 DB from one Version to Another
===========

This document outlines the steps to successfully migrate H2 Database from one version to another. It will cover the following:

* Migration of H2 Database from **1.4.199 to 2.3.232**

Migration from version 1.4.199 to 2.3.232
------------

Follow the steps below to move H2 database from **1.4.199 to 2.3.232**.

**Pre-Requisites**
++++++++++++++++

- firedb.mv file
- h2-1.4.199.jar
- h2-2.3.232.jar

**Step 1 : Backing Up the H2 Database**
+++++++++++++++++++++++++++++++++++++++++++

#. Run the JAR file for H2 version 1.4.199 or access the SQL terminal to run commands.

   Firstly make sure that the fire-server is not running in the background whether its Windows or Linux Machine then download the H2 DB JAR of v1.4.199 from the     URL below:

   Download Link : `h2-1.4.199.jar. <https://sparkflows-release.s3.us-east-1.amazonaws.com/fire/h2-db-jar/h2-1.4.199.jar>`_
 

    * For Windows Machine

      Step 1 - Double click and open the h2-1.4.199.jar downloaded from the above URL which will open the login page for **firedb** , then add in the username and 
      password and click on **Connect** button to connect to the H2 DB

      .. figure:: ../..//_assets/DB_Migration/windows-h2-console-login.png
           :alt: Windows H2 Console Login
           :width: 80%

      .. figure:: ../..//_assets/DB_Migration/windows-h2-console.png
           :alt: Windows H2 Console
           :width: 80%
      

      Step 2 - In the H2 console of version 1.4.199, run the following command:

         ::
  
          SCRIPT TO '/path/db/h2/backup.sql';

      (Using an absolute path for the backup.sql file is preferred and make sure to keep the backup.sql file in **/db/h2** folder in the fire-server files)

      .. figure:: ../..//_assets/DB_Migration/windows-console-cmd-after-run.png
           :alt: Windows H2 Console Command Run
           :width: 80%

      The backup.sql contains the script as well as data. Once the backup.sql file is generated, exit the instance and process of h2-1.4.199.jar


    * For Linux Machine

      Step 1 - Login to the linux machine, Create a folder name ``migration_db``

      ::

         mkdir migration_db


      Step 2 - Copy the ``firedb.mv`` file you wanted to migrate.

      Step 3 - Download the ``h2-1.4.199.jar`` file from download link shared above.
      
      Step 4 - Now to access the h2 console enter the below command:
        
         ::
  
          java -cp h2-1.4.199.jar org.h2.tools.Shell

      This command will give access to H2 Shell for v1.4.199 , now enter the **H2 DB URL, Driver, User and Password** fields. If the details are entered correctly       **Connected** will be seen and you will get access to sql command prompt like the below image

      .. figure:: ../..//_assets/DB_Migration/linux-h2-console.png
           :alt: Sparkflows Linux H2 Console
           :width: 80%

      Step 5 - In the H2 console of version 1.4.199, run the following command:

         ::
  
          SCRIPT TO '/absolute_path/backup.sql';

      (Using an absolute path for the backup.sql file is preferred and make sure to keep the backup.sql file in **migration_db** folder)

      .. figure:: ../..//_assets/DB_Migration/linux-h2-console-script-run.png
           :alt: Sparkflows Linux H2 Console Script Creation
           :width: 80%

      The backup.sql contains the script as well as data. Once the backup.sql file is generated, exit the instance and process of h2-1.4.199.jar. 


**Step 2 : Modifying the Backup SQL File**
++++++++++++++++++++++++++++++++++++++++++++

#. Open the file **backup.sql** in any editor like **VS Code**, **Notepad**, **vi editor** etc. 

#. Now, apply the following changes in the **backup.sql** file (make these changes if present in backup.sql file).


  * Find for all instances of **BELONGS_TO_TABLE** and remove all occurrences in the backup.sql file (from nearly 89-90 places on backup.sql file).

   .. Note:: You can use replace functionality in editor for removing **BELONGS_TO_TABLE** from backup.sql all at once and replace it with an empty space.


  * Search for the following line in backup.sql file:

   ::
       
       CREATE PRIMARY KEY SYSTEM_LOB_STREAM_PRIMARY_KEY ON SYSTEM_LOB_STREAM(ID, PART);

 
  * Now, replace the above line with the line below: 

   ::
    
       ALTER TABLE SYSTEM_LOB_STREAM ADD PRIMARY KEY (ID, PART);

  * Find all instances of the line below:

   ::

       INSERT INTO "PUBLIC"."SPRING_SESSION" VALUES

  * Delete all related ``INSERT`` statements starting with the above value, as shown below.

   .. figure:: ../..//_assets/DB_Migration/remove-queries-spring-session.png
        :alt: Open Script Button
        :width: 110%


  * Similarly, find all instances of the line below:

   ::

       INSERT INTO "PUBLIC"."SPRING_SESSION_ATTRIBUTES" VALUES

  * Delete all related ``INSERT`` statements starting with the above value, as shown below.

   .. figure:: ../..//_assets/DB_Migration/remove-queries-spring-session-attributes.png
        :alt: Open Script Button
        :width: 110%


**Step 3 : Preparing for Migration**
++++++++++++++++++++++++++++++++++++++

Ensure the modified **backup.sql file** and the H2 JAR file for version **2.3.232** are in the same directory. If the h2 jar of version 2.3.232 is not present in **migration_db** folder, download the jar from the below link and add it to the **migration_db** folder

   Download Link : `h2-2.3.232.jar. <https://sparkflows-release.s3.us-east-1.amazonaws.com/fire/h2-db-jar/h2-2.3.232.jar>`_



**Step 4 : Executing the Migration**
++++++++++++++++++++++++++++++++++++++++

#. After the changes done in previous steps, run the following command in the same directory (**migration_db**) where **backup.sql** file and h2 jar of version **2.3.232** are present to migrate data.

   ::

      java -cp h2-2.3.232.jar org.h2.tools.RunScript -url jdbc:h2:file:/target_path/firedb -script backup.sql

  .. note:: Make sure to quit/exit the running instance of h2 jar 1.4.199 before running the above command and use **target_path** as **migration_db/new** with absolute path

* For Windows Machine

   In the below image we can see that after running the command the **fire.mv.db** is created successfully in Windows in the same folder.

   .. figure:: ../..//_assets/DB_Migration/windows-h2-version-migration.png
      :alt: Sparkflows Windows H2 Version Migration
      :width: 80%
     

* For Linux Machine

   In the below image we can see that after running the command the **fire.mv.db** is created successfully in Linux in the **target_path** folder.

   .. figure:: ../..//_assets/DB_Migration/linux-h2-version-migration.PNG
      :alt: Sparkflows Linux H2 Version Migration
      :width: 80%

**Step 5 : Finalizing Migration**
++++++++++++++++++++++++++++++++++++

#. Once the above command runs successfully, a new **firedb.mv.db** file will be generated in the same directory where we ran the above command.

#. Now, move the **firedb.mv.db** file to the root location from where the db is read. 

#. Delete the **firedb.trace.db** file and start the server ensuring that the H2 database script runs first.


  .. Note:: Make sure to delete the **firedb.trace.db** and run the required **H2 database script** before starting the server.
