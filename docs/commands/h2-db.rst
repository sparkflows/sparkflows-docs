H2 Database
===========

By default Fire Insights uses the H2 DB for storing the metadata. These include users, groups, projects, workflows etc.


Logging into H2 DB
--------------------

    java -cp ~/fire-3.1.0/db/h2/h2-1.4.199.jar  org.h2.tools.Shell
    URL: jdbc:h2:./firedb
    Driver : org.h2.Driver
    User : fire
    Password : fire

Compacting the H2 DB
--------------------

    SHUTDOWN COMPACT
    
    
List all Tables
------------------

    sql> show tables;
    
Describe the table
------------------

    sql> show columns from ANALYSIS_FLOW_EXECUTE_RESULT;
    
Get count of records in a table
----------------
    
    sql> select count(*) from ANALYSIS_FLOW_EXECUTE_RESULT;
    
Dump the H2 DB to a text file
----------------

    SCRIPT TO 'filename';
    

Save the results of query into a file
--------------

    CALL CSVWRITE('result.csv', 'select ANALYSIS_FLOW_EXECUTION_ID, RESULT from ANALYSIS_FLOW_EXECUTE_RESULT limit 10');
    
