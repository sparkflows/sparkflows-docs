H2 Database
===========

Fire can be setup up to easily run with H2 database. Fire runs H2 in embedded mode.

More details of the H2 database can be found here : http://www.h2database.com/html/main.html

 
If you are want to run multiple instances of Fire for high availability, configure Fire to run with MySQL.

Creating/Upgrading the H2 database
----------------------------------

The H2 database is used for storing the metadata of the DataSets, Workflows, Users, Groups, Roles etc.

Execute the following steps on your CLI:


* Mac/Linux::

    cd <install_dir>/sparkflows-fire-1.4.1
    ./create-h2-db.sh

* Windows::

    cd <install_dir>\sparkflows-fire-1.4.1
    .\create-h2-db.bat

 

If you would like to use different values for the db, username, password, update them in ``<install_dir>/sparkflows-fire-1.4.0/conf/db.properties``::


    spring.datasource.url = jdbc:h2:file:~/firedb

    spring.datasource.username = fire

    spring.datasource.password = fire

    spring.datasource.driverClassName = org.h2.Driver

 

Note: firedb is created in the users home directory and the name is firedb.mv.db



Recreating H2 database
----------------------
 
If you need to recreate the H2 database, follow the steps below to create a new empty H2 DB::

 
    Stop the running Fire server
    Move the existing firedb files to another temp location on your disk.
    Recreate the H2 DB using the steps in the above section for creating a brand new install.
