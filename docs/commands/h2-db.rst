H2 Database
===========

By default Sparkflows uses the H2 DB for storing the metadata. These include users, groups, projects, workflows, workflow executions etc.

Shut down Sparkflows before logging into H2 DB or doing any operations on the H2 DB.

Logging into H2 DB
--------------------

::

    java -cp ~/fire-x.y.z/db/h2/h2-1.4.199.jar  org.h2.tools.Shell
    URL: jdbc:h2:./firedb
    Driver : org.h2.Driver
    User : fire
    Password : fire

Compacting the H2 DB
--------------------

When the H2 DB file sizes get too large, it is important to compact them.

SHUTDOWN COMPACT fully compacts the database (re-creating the database may further reduce the database size). If the database is closed normally (using SHUTDOWN or by closing all connections), then the database is also compacted, but only for at most the time defined by the database setting h2.maxCompactTime in milliseconds (see there).

::

    SHUTDOWN COMPACT

In case the H2 DB is corrupted (logs in fireserver.log would indicate that), SHUTDOWN COMPACT can be used to get it back to good shape.

After running SHUTDOWN COMPACT, it can display `Error: org.h2.jdbc....:Database is already closed`
This is fine and can be ignored.

Recreating the H2 DB to further reduce the database size
---------------------

Exporting the content of H2 DB to a sql file, deleting all objects from H2 DB and recreating the H2 DB from the sql file brings up the H2 DB to a clean state.

https://stackoverflow.com/questions/41469066/why-does-recreating-h2-database-reduce-the-size-drastically

::

    SCRIPT TO 'mydb.sql'; 
    DROP ALL OBJECTS; 
    RUNSCRIPT FROM 'mydb.sql';

    
List all Tables
------------------

::

    sql> show tables;
    
Describe the table
------------------

::

    sql> show columns from ANALYSIS_FLOW_EXECUTE_RESULT;
    
Get count of records in a table
----------------

::

    sql> select count(*) from ANALYSIS_FLOW_EXECUTE_RESULT;
    
Dump the H2 DB to a text file
----------------

::

    SCRIPT TO 'filename';
    

Save the results of query into a file
--------------

::

    CALL CSVWRITE('result.csv', 'select ANALYSIS_FLOW_EXECUTION_ID, RESULT from ANALYSIS_FLOW_EXECUTE_RESULT limit 10');
    

Listing and Cleaning Old Workflow Executions
------------------

::

    SELECT COUNT(*) FROM ANALYSIS_FLOW_EXECUTE_RESULT;

    SELECT COUNT(*) FROM ANALYSIS_FLOW_EXECUTION;

    SELECT MAX(ID) FROM ANALYSIS_FLOW_EXECUTION WHERE TIMESTAMPDIFF(DAY, START_TIME , CURRENT_TIMESTAMP()) > 30;

    DELETE FROM ANALYSIS_FLOW_EXECUTE_RESULT WHERE ANALYSIS_FLOW_EXECUTION_ID  <  XXX;

    DELETE FROM ANALYSIS_FLOW_EXECUTION WHERE ID  <  XXX;

    
