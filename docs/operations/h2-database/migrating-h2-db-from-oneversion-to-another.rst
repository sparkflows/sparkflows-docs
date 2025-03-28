Migrate H2 DB from one Version to Another
===========

This document outlines the steps to successfully migrate H2 Database from one version to another. It will cover the following:

* Migration of H2 Database from **1.4.199 to 2.3.232**

* Migration of H2 Database from **1.4.199 to 2.2.224**


Migration from version 1.4.199 to 2.3.232
------------

Follow the steps below to move H2 database from **1.4.199 to 2.3.232**.

**Step 1 : Backing Up the H2 Database**
+++++++++++++++++++++++++++++++++++++++++++

#. Run the JAR file for H2 version 1.4.199 or access the SQL terminal to run commands.

#. In the H2 console/SQL terminal of version 1.4.199, run the following command:

   ::
  
       SCRIPT TO 'backup.sql';

   (Using an absolute path for the backup.sql file is preferred.) 

   The above file contains the script as well as data.

**Step 2 : Modifying the Backup SQL File**
++++++++++++++++++++++++++++++++++++++++++++

#. Open the file **backup.sql** in any editor like **VS Code**, **Notepad**, etc. 

#. Now, apply the following changes in the **backup.sql** file (make these changes if present in backup.sql file).


  * Find for all instances of **BELONGS_TO_TABLE** and remove all occurrences in the backup.sql file (from nearly 89-90 places on backup.sql file).

   .. Note:: You can use replace functionality in editor for removing **BELONGS_TO_TABLE** from backup.sql all at once and replace it with an empty space.


  * Search for the follwing line in backup.sql file:

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

Ensure the modified **backup.sql file** and the H2 JAR file for version **2.3.232** are in the same directory.


**Step 4 : Executing the Migration**
++++++++++++++++++++++++++++++++++++++++

#. After the changes done in previous steps, run the following command in the same directory where **backup.sql** file and h2 jar of version **2.3.232** are present to migrate data.

   ::

      java -cp h2-2.3.232.jar org.h2.tools.RunScript -url jdbc:h2:file:./firedb -script backup.sql


  .. note:: Make sure to quit/exit the running instance of h2 jar 1.4.199 before running the following command:
            :: 
               java -cp h2-2.3.232.jar org.h2.tools.RunScript -url jdbc:h2:file:./firedb -script backup.sql


**Step 5 : Finalizing Migration**
++++++++++++++++++++++++++++++++++++

#. Once the above command runs successfully, a new **firedb.mv.db** file will be generated in the same directory where we ran the above command.

#. Now, move the **firedb.mv.db** file to the location from where the db is read. 

#. Delete the **firedb.trace.db** file and start the server ensuring that the H2 database script runs first.


  .. Note:: Make sure to delete the **firedb.trace.db** and run the required **H2 database script** before starting the server.











Migration from version 1.4.199 to 2.2.224
-----------

Follow the steps below to move H2 database from **1.4.199 to 2.2.224**.
  
**Step 1 : Backing Up the H2 Database**
+++++++++++++++++++++++++++++++++++++++++++++
  
#. Run the JAR file for H2 version 1.4.199 or access the SQL terminal to run commands.
#. In the H2 console/sql terminal of version 1.4.199, run the following command:
  
   ::
  
       SCRIPT TO 'backup.sql';

   (You can also specify an absolute path for backup.sql if needed.)

   The above file contains the script as well as data.
    
**Step 2 : Modifying the Backup SQL File**
++++++++++++++++++++++++++++++++++++++++++++++

#. Open the file **backup.sql** in any editor like **VS Code**, **Notepad**, etc. 
#. Now, apply the following changes in the **backup.sql** file (make these changes if present in backup.sql file).
    
  * Find for all instances of **BELONGS_TO_TABLE** and remove all occurrences in the backup.sql file (from nearly 89-90 places on backup.sql file).

   .. Note:: You can use replace functionality in editor for removing **BELONGS_TO_TABLE** from backup.sql all at once and replace it with an empty space.

  * Search for the follwing line in backup.sql file:

   ::
       
       CREATE PRIMARY KEY SYSTEM_LOB_STREAM_PRIMARY_KEY ON SYSTEM_LOB_STREAM(ID, PART);

 
  * Now, replace the above line with the line below: 

   ::
    
       ALTER TABLE SYSTEM_LOB_STREAM ADD PRIMARY KEY (ID, PART);


**Step 3 : Preparing for Migration**
++++++++++++++++++++++++++++++++++++++++
Ensure that both the **backup.sql** file and h2 jar of version **2.2.224** are in the same directory.

**Step 4 : Executing the Migration**
+++++++++++++++++++++++++++++++++++++++

#. After the changes done in previous steps, run the following command in the same directory where **backup.sql** file and h2 jar of version **2.2.224** are present to migrate data. 

   ::
  
      java -cp h2-2.2.224.jar org.h2.tools.RunScript -url jdbc:h2:file:./firedb -script backup.sql

  .. Note:: Make sure to quit/exit the running instance of h2 jar 1.4.199 before running the following command:
            ::
             java -cp h2-2.2.224.jar org.h2.tools.RunScript -url jdbc:h2:file:./firedb -script backup.sql

**Step 5 : Finalizing Migration**
++++++++++++++++++++++++++++++++++++++

#. Once the above command runs successfully a new **firedb.mv.db** file will be generated in the same directory where we ran the above command. 
#. Now, move the **firedb.mv.db** file to the location from where the db is read. 
#. Delete the **firedb.trace.db** file and start the server ensuring that the H2 database script runs first.

  .. Note:: Make sure to delete the **firedb.trace.db** and run the required **H2 database script** before starting the server.
