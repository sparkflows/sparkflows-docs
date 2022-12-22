MySQL Database
==============

Fire can easily be setup up to run with MySQL

More details of the MySQL database can be found here : https://www.mysql.com/

Pre requisites
------

* MySQL with Engine version 8.0.x
* JDBC driver JAR file need to be copied to Sparkflows folder ``fire-user-lib`` & ``fire-server-lib`` directory inside ``fire-x.y.z``.
* MySQL should be accessible from Sparkflows Machine.


Install MySQL
-------------

* Install MySQL on a machine or you can use MySQL running on Cloud Infrastructure.
* It might be easier to install it on the same machine you are installing Fire on.

.. note:: Make sure that MySQL DB should be accessible from Fire Machine.

Create the DB for Fire in MySQL
-------------------------------

* Create the database for Fire in MySQL
* Let us call it ``firedb``::

    create database firedb;


Create the User for Fire in MySQL and grant it Permissions
----------------------------------------------------------

Create the User for Fire in MySQL::

    CREATE user 'fire'@'%' IDENTIFIED BY 'fire';

    GRANT ALL PRIVILEGES ON firedb.* TO 'fire'@'%' WITH GRANT OPTION;

 
* In ``CREATE`` user, the user we are creating is ``fire`` who is allowed to access the database from anywhere ``%`` and his password is ``fire``.

* Next, this user has been granted all ``permissions``. This, of course can be further restricted based on your use case.

Configure Fire to connect to MySQL
----------------------------------

* Copy ``db.properties.mysql`` file into the ``conf`` directory as ``db.properties``::

    cd   fire-x.y.z
    cp   conf.orig/db.properties.mysql   conf/db.properties

 

* Update the following fields in ``conf/db.properties`` based on the values you used in creating the DB for fire. The below assumes that the database name you created for Fire is ``firedb``. It also assumes that MySQL has been installed on the ``same machine`` as Fire::


    # Connection url for the database "firedb"

    spring.datasource.url=jdbc:mysql://hostame:3306/firedb (Replace hostname with either the IP/hostname)

    spring.datasource.driverClassName=com.mysql.jdbc.Driver

    spring.jpa.database=MYSQL

    # Username and password

    spring.datasource.username=fire
    
    spring.datasource.password=fire

Install the MySQL Connector Jar file
-------------------------------------

* Download the MySQL JDBC driver from http://www.mysql.com/downloads/connector/j/5.1.html

* Extract the ``JDBC driver JAR file`` from the downloaded file. For example::

    tar zxvf mysql-connector-java-8.0.11.tar.gz
 
 * just copy the path location for ```JDBC driver JAR file``

 
* copy the mysql JDBC driver JAR file to the ``fire-user-lib`` & ``fire-server-lib`` directory of ``fire-x.y.z``::

    cd fire-x.y.z
    cp /pathlocation of jdbc jar file/mysql-connector-java.jar      fire-server-lib
    cp /pathlocation of jdbc jar file/mysql-connector-java.jar      fire-user-lib
  
  
Create the Tables for Fire in MySQL
----------------------------------- 

* Create the tables for Fire in MySQL by executing the ``create-mysql-db.sh`` or ``create-mysql-db.bat``script, depending on OS::

    cd fire-x.y.z

    ./create-mysql-db.sh

.. note::  If running on Linux

::

     create-mysql-db.bat

.. note::  If running on Windows


Troubleshooting
---------------

MySQL has a problem where one of the default users in the user table is ``'' @ localhost``, which winds up denying all localhost users later in the table. If you are accessing mysql from localhost, assuming Fire and MySQL have been installed on the same machine, then you need to delete this entry in ``mysql.user`` table::


    select user, host from user where user = ''          

    #you should see an entry for this and host equals localhost.

    DELETE from user WHERE user = '' AND host = 'localhost';

    flush privileges;

    #this reloads privileges - important step. otherwise you will get access denied error even though you log in with the correct user.


Here is a link on stackoverflow that talks about this:

            http://stackoverflow.com/questions/1412339/cannot-log-in-with-created-user-in-mysql
            

