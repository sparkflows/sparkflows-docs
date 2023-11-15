Aurora MySQL Database
==============

Fire can easily be setup up to run with Aurora MySQL.

Further details of the Aurora MySQL database can be found here : https://aws.amazon.com/rds/aurora/

Pre-requisites
------

* Aurora MySQL with Engine version 8.0.x
* JDBC driver JAR file need to be copied to Sparkflows folder ``fire-user-lib`` & ``fire-server-lib`` directory inside ``fire-x.y.z``.
* MySQL should be accessible from the Fire Insights Machine.

The memory Pre-requisites for Aurora MySQL:

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


Create Aurora MySQL database on AWS
-------------

* Login to AWS.
* Create Aurora MySQL Database which is accessible from machine where Fire is running.

Create the DB for Fire in Aurora MySQL
-------------------------------

* Create the database for Fire in Aurora MySQL.
* Let us call it ``firedb``::

    create database firedb;


Create the User for Fire in Aurora MySQL and grant it Permissions
----------------------------------------------------------

Create the User for Fire in MySQL::

    CREATE user 'fire'@'%' IDENTIFIED BY 'fire';

    GRANT ALL PRIVILEGES ON firedb.* TO 'fire'@'%' WITH GRANT OPTION;

 
* In ``CREATE`` user, the user we are creating is ``fire`` who is allowed to access the database from anywhere ``%`` and his password is ``fire``.

* Next, this user has been granted all ``permissions``. This, of course, can further be restricted according to your personal usage.

Configure Fire to connect to Aurora  MySQL
----------------------------------

* Copy ``db.properties.mysql`` file into the ``conf`` directory as ``db.properties``::

    cd   fire-x.y.z
    cp   conf.orig/db.properties.mysql   conf/db.properties

 

* Update the following fields in ``conf/db.properties`` based on the values you used in creating the DB for Fire. The below assumes that the database name you created for Fire is ``firedb``. It also assumes that MySQL has been installed on the ``same machine`` as Fire::


    # Connection url for the database "firedb"

    spring.datasource.url=jdbc:mysql://Endpoint:3306/firedb

    spring.datasource.driverClassName=com.mysql.jdbc.Driver

    spring.jpa.database=MYSQL

    # Username and password

    spring.datasource.username=fire
    
    spring.datasource.password=fire
    

Install the MySQL Connector JAR file
-------------------------------------

* Download the MySQL JDBC driver from http://www.mysql.com/downloads/connector/j/5.1.html

* Extract the ``JDBC driver JAR file`` from the downloaded file. For example::

    tar zxvf mysql-connector-java-8.0.11.tar.gz
 
 * Just copy the path location for ```JDBC driver JAR file``

 
* Copy the mysql JDBC driver JAR file to the ``fire-user-lib`` & ``fire-server-lib`` directory of ``fire-x.y.z``::

    cd fire-x.y.z
    cp /pathlocation of jdbc jar file/mysql-connector-java.jar      fire-server-lib
    cp /pathlocation of jdbc jar file/mysql-connector-java.jar      fire-user-lib
  
  
Create the Tables for Fire in Aurora
----------------------------------- 

* Create the tables for Fire in MySQL by executing the ``create-mysql-db.sh`` script::

    cd fire-x.y.z

    ./create-mysql-db.sh


Troubleshooting
---------------

MySQL has a problem where one of the default users in the user table is ``'' @ localhost``, which winds up denying all localhost users later in the table. If you are accessing mysql from localhost, assuming Fire and MySQL have been installed on the same machine, then you need to delete this entry in ``mysql.user`` table::


    Select user, host from user where user = ''          

    #You should see an entry for this and host equals localhost.

    DELETE from user WHERE user = '' AND host = 'localhost';

    flush privileges;

    #this reloads privileges - important step. otherwise you will get access denied error even though you log in with the correct user.


Below is a link on stackoverflow that talks about this:

            http://stackoverflow.com/questions/1412339/cannot-log-in-with-created-user-in-mysql
