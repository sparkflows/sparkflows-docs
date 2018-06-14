Microsoft SQL Server Database
==============

Fire can easily be setup up to run with Microsoft SQL Server.

More details of the MySQL database can be found here : https://www.microsoft.com/en-us/sql-server/default.aspx

Install Microsoft SQL Server
-------------

* Install Microsoft SQL Server on a machine.
* It might be easier to install it on the same machine you are installing Fire on.

Create the DB for Fire in Microsoft SQL Server
-------------------------------

* Create the database for Fire in Microsoft SQL Server
* Let us call it ``firedb``::

    create database firedb;


Create the User for Fire in Microsoft SQL Server and grant it Permissions
----------------------------------------------------------

Create the User for Fire in Microsoft SQL Server::

    CREATE user 'fire'@'%' IDENTIFIED BY 'fire';

    GRANT ALL PRIVILEGES ON firedb.* TO 'fire'@'%' WITH GRANT OPTION;

 
* In ``CREATE`` user, the user we are creating is ``fire`` who is allowed to access the database from anywhere ``%`` and his password is ``fire``.

* Next, this user has been granted all ``permissions``. This, of course can be further restricted based on your use case.

Configure Fire to connect to Microsoft SQL Server
----------------------------------

* Copy ``db.properties.mysql`` file into the ``conf`` directory as ``db.properties``::

    cd   fire-1.x.y
    cp   conf.orig/db.properties.sqlserver   conf/db.properties

 

* Update the following fields in ``conf/db.properties`` based on the values you used in creating the DB for fire. The below assumes that the database name you created for Fire is ``firedb``. It also assumes that Microsoft SQL Server has been installed on the ``same machine`` as Fire::


    # Connection url for the database "firedb"

    spring.datasource.url=jdbc:mysql://localhost:3306/firedb

    spring.datasource.driverClassName=com.mysql.jdbc.Driver

    spring.jpa.database=MYSQL

    # Username and password

    spring.datasource.username=fire
    

Install the Microsoft SQL Server Connector Jar file
-------------------------------------

* Download the Microsoft SQL Server JDBC driver from http://www.mysql.com/downloads/connector/j/5.1.html
  
* Copy the Microsoft SQL Server JDBC driver JAR file to the ``fire-server-lib`` directory of ``fire-2.x.y``::

    cd fire-2.x.y
    cp /usr/share/java/mysql-connector-java.jar      fire-server-lib
  
  
Create the Tables for Fire in Microsoft SQL Server
----------------------------------- 

* Create the tables for Fire in Microsoft SQL Server by executing the ``create-sqlserver-db.sh`` script::

    cd fire-2.x.y

    ./create-sqlserver-db.sh


