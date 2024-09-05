PostgreSQL Database
==============

Fire Insights can easily be setup up to run with PostgreSQL.

More details of the PostgreSQL database can be found here : https://www.postgresql.org/

Pre-requisites
------
* Postgres JAR file needs to be copied to Sparkflows folder fire-user-lib & fire-server-lib directory inside fire-x.y.z.
* PostgreSQL should be accessible from the Fire Insights Machine.

The memory Pre-requisites for PostgreSQL:

Memory
++++

.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Recommended
     - Value
   * - Memory
     - 16GB+
     - More the memory would be preferable
   * - vCPU
     - 8+
     - More the vCPU would be preferable, if data size is bigger
   * - Disk Size
     - 50GB+
     - Depending on Job Compute, If running locally



Install PostgreSQL
-------------

* Install PostgreSQL on a machine or you can use PostgreSQL running on Cloud Infrastructure.
* It might be easier to install it on the same machine on which you are installing Fire Insights on.

.. note:: Make sure that PostgreSQL database should be accessible from Fire Insights Machine.

Create the DB for Fire in PostgreSQL
-------------------------------

* Create the database for Fire in PostgreSQL
* Let us call it the database name as ``firedb`` and to make this database run the following query in PostgreSQL setup::

    create database firedb;

Configure Fire to connect to PostgreSQL
----------------------------------

* Copy ``db.properties.postgres`` file into the ``conf`` directory as ``db.properties``::

    cd   fire-x.y.z
    cp   conf.orig/db.properties.postgres   conf/db.properties

 

* Update the following fields in ``conf/db.properties`` based on the values you used in creating the database for fire. The below assumes that the database name you created for Fire is ``firedb``. It also assumes that PostgreSQL has been installed on the ``same machine`` as Fire::


    # Connection url for the database "firedb"

    spring.datasource.url=jdbc:postgresql://localhost:5432/firedb #(Replace localhost with either the IP/hostname)

    spring.datasource.driverClassName=org.postgresql.Driver

    spring.jpa.database=POSTGRESQL

    # Username and password

    spring.datasource.username=postgres #(Replace postgres with the correct username)
    
    spring.datasource.password=password #(Replace password with the correct password)

    # Custom Dialect used to run Sparkflows on Postgres SQL DB  
  
    spring.jpa.database-platform= fireui.util.CustomPostgreSQLDialect

* Copy ``db.properties.postgres`` file into the ``conf`` directory as ``quartz.properties``::

    cd   fire-x.y.z
    cp   conf.orig/quartz.postgres.properties   conf/quartz.properties

Install the PostgreSQL JAR file
-------------------------------------

* Download the PostgreSQL jar file with the version ``42.7.3`` from https://jdbc.postgresql.org/download/

* Just copy the path location for ``JAR file``

 
* Copy the PostgreSQL JAR file to the ``fire-user-lib`` & ``fire-server-lib`` directory of ``fire-x.y.z``::

    cd fire-x.y.z
    cp /pathlocation of postgres jar file/postgresql-42.7.3.jar      fire-server-lib
    cp /pathlocation of postgres jar file/postgresql-42.7.3.jar      fire-user-lib
  
  
Create the Tables for Fire in PostgreSQL
----------------------------------- 

.. Note::  If running on Linux::

* Create the tables for Fire in PostgreSQL by executing the ``create-postgres-db.sh`` script::

    cd fire-x.y.z

    ./create-postgres-db.sh

.. Note::  If running on Windows::

* Create the tables for Fire in PostgreSQL by executing the ``create-postgres-db.bat`` script::

    cd fire-x.y.z

    create-postgres-db.bat
            

