Microsoft SQL Server Database
==============

Fire can easily be setup up to run with Microsoft SQL Server.

Further details of the Microsoft SQL Server database can be found here : https://www.microsoft.com/en-us/sql-server/default.aspx

Install Microsoft SQL Server
-------------

* Install Microsoft SQL Server on a machine.
* It might be easier to install it on the same machine you are installing Fire on.

Create the DB for Fire in Microsoft SQL Server
-------------------------------

* Create the database for Fire in Microsoft SQL Server.
* Let us call it ``firedb``::

    CREATE DATABASE firedb;


Create the User for Fire in Microsoft SQL Server and grant it Permissions
----------------------------------------------------------

Create the User for Fire in Microsoft SQL Server and give it Permissions.


Configure Fire to connect to Microsoft SQL Server
----------------------------------

* Copy ``db.properties.sqlserver`` file into the ``conf`` directory as ``db.properties``::

    cd   fire-x.y.z
    cp   conf.orig/db.properties.sqlserver   conf/db.properties

 

* Update the following fields in ``conf/db.properties`` based on the values you used in creating the DB for fire. The below assumes that the database name you created for Fire is ``firedb``. It also assumes that Microsoft SQL Server has been installed on the ``same machine`` as Fire::


    # Connection url for the database "firedb"

    spring.datasource.url=jdbc:sqlserver://localhost:1433;databaseName=firedb

    spring.datasource.driverClassName=com.microsoft.sqlserver.jdbc.SQLServerDriver

    spring.jpa.database=SQLSERVER

    # Username and password

    spring.datasource.username=fire
    
    spring.datasource.password=fire
    
    spring.jpa.hibernate.dialect=org.hibernate.dialect.SQLServer2008Dialect
    


Install the Microsoft SQL Server Connector JAR file
-------------------------------------

* Download the Microsoft SQL Server JDBC driver from https://mvnrepository.com/artifact/com.microsoft.sqlserver/mssql-jdbc/12.10.0.jre11 
* Ensure that the JDBC JAR file is available in the directory.
* Use the JAR file (mssql-jdbc-12.10.0.jre11.jar) for installation in the Fire.
* Copy the Microsoft SQL Server JDBC driver JAR file to the ``fire-server-lib`` directory of ``fire-x.y.z``

  
  
Create the Tables for Fire in Microsoft SQL Server
----------------------------------- 

* Tables in Microsoft SQL Server can be created by using the DDL script : ``db/sqlserver/fire-schema.sqlserver.sql``


* Tables can also be created by executing the ``create-sqlserver-db.sh`` script::

    cd fire-x.y.z

    ./create-sqlserver-db.sh


