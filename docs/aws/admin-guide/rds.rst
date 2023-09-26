RDS Setup and Configurations
===========

Fire Insights can easily be setup up to run with MySQL.

You can set it up directly from AWS RDS or it can be installed on an EC2 machine.

To find more details of the MySQL database, visit : `MySQL Official Website <https://www.mysql.com/>`_

Steps for installing MySQL are also available here : `MySQL Installation Guide <https://docs.sparkflows.io/en/latest/operations/installing-mysql.html>`_

This document explains the steps needed to setup and configure the RDS. Below is a brief outline of steps involved in the process :

#. Pre-Requisites
#. Install MySQL
#. Create DB for Fire in MySQL
#. Create MySQL User and Grant it Permissions 
#. Configure Fire to connect to MySQL
#. Install the MySQL Connector JAR File
#. Create the Tables for Fire in MySQL


Step 1 : Pre-requisites
------
Before you start with the setup and configuration process, ensure you meet the following pre-requisites :
   
* MySQL with Engine version 8.0.x
* JDBC driver JAR file need to be copied to Sparkflows folder **fire-user-lib** & **fire-server-lib** directory inside **fire-x.y.z**.
* MySQL should be accessible from the Fire Insights Machine.


Step 2 : Install MySQL
-------------

* Install MySQL on a machine or you can use MySQL running on AWS Cloud Infrastructure.
* It might be easier to install it on the same machine you are installing Fire Insights on.

  To get more information on setting AWS RDS, visit : `AWS Guide <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html>`_

  .. note:: Make sure that MySQL database should be accessible from Fire Insights Machine.

Step 3 : Create the DB for Fire in MySQL
-------------------------------

* Create the database for Fire in MySQL.
  
  Let us call it **firedb**::

    create database firedb;

  .. note:: If you are using AWS RDS Console, add database name as firedb from console itself.

Step 4 : Create a MySQL User and Grant Permissions 
---------------------------------------------------

* Create the User for Fire in MySQL using the below command::

    CREATE user 'fire'@'%' IDENTIFIED BY 'fire';

    GRANT ALL PRIVILEGES ON firedb.* TO 'fire'@'%' WITH GRANT OPTION;

 
  In **CREATE** user, the user we are creating is **fire** who is allowed to access the database from anywhere **%** and his password is **fire**.

  Next, this user has been granted all **permissions**. This, of course, can further be restricted based on your personal usage.

  .. note:: This step is essential only if you are installing on a separate VM.

Step 5 : Configure Fire to connect to MySQL
----------------------------------

* Copy **db.properties.mysql** file into the **conf** directory as **db.properties** using the below command::

    cd   fire-x.y.z
    cp   conf.orig/db.properties.mysql  conf/db.properties

 

* Update the following fields in **conf/db.properties** based on the values you used in creating the database for fire. 

  The below assumes that the database name you created for Fire is **firedb**. 

  It also assumes that MySQL has been installed on the **same machine** as Fire::


    # Connection url for the database "firedb"

    spring.datasource.url=jdbc:mysql://localhost:3306/firedb #(Replace localhost with either the IP/hostname)

    spring.datasource.driverClassName=com.mysql.jdbc.Driver

    spring.jpa.database=MYSQL

    # Username and password

    spring.datasource.username=fire
    
    spring.datasource.password=fire

Step 6 : Install the MySQL Connector JAR File
-------------------------------------

* Download the MySQL JDBC driver from `MySQL Website <https://dev.mysql.com/downloads/connector/j/?os=26>`_

* Extract the **JDBC driver JAR file** from the downloaded file. For example::

    tar zxvf mysql-connector-java-8.0.11.tar.gz
 
 * Just copy the path location for **JDBC driver JAR file**.

 
* Copy the MySQL JDBC driver JAR file to the **fire-user-lib** & **fire-server-lib** directory of **fire-x.y.z**::

    cd fire-x.y.z
    cp /pathlocation of jdbc jar file/mysql-connector-java.jar fire-server-lib
    cp /pathlocation of jdbc jar file/mysql-connector-java.jar fire-user-lib
  
  
Step 7 : Create the Tables for Fire in MySQL
----------------------------------- 

.. Note::  If running on Linux, follow the steps below :

* Create the tables for Fire in MySQL by executing the **create-mysql-db.sh** or **create-mysql-db.bat** script, depending on OS::

    cd fire-x.y.z

    ./create-mysql-db.sh

Troubleshooting
---------------

MySQL has a problem where one of the default users in the user table is ``'' @ localhost``, which winds up denying all localhost users later in the table. If you are accessing MySQL from localhost, assuming Fire and MySQL have been installed on the same machine, then you need to delete this entry in **mysql.user** table::


    select user, host from user where user = ''          

    #you should see an entry for this and host equals localhost.

    DELETE from user WHERE user = '' AND host = 'localhost';

    flush privileges;

    #this reloads privileges - It is an important step in the process or otherwise you will get "access denied error" even though you log in with the correct user.


To read more about this, visit : `stackoverflow official website <http://stackoverflow.com/questions/1412339/cannot-log-in-with-created-user-in-mysql>`_
            

