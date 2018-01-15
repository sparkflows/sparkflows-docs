MySQL Database
==============

Fire can easily be setup up to run with MySQL

More details of the MySQL database can be found here : https://www.mysql.com/

Install MySQL
-------------

* Install MySQL on a machine

Create the DB for Fire in MySQL
-------------------------------

* Create the database for Fire in MySQL
* Let us call it ``firedb``


Create the User for Fire in MySQL and grant it Permissions
----------------------------------------------------------

Create the User for Fire in MySQL::

    CREATE user 'fire'@'%' IDENTIFIED BY 'fire';

    GRANT ALL PRIVILEGES ON firedb.* TO 'fire'@'%' WITH GRANT OPTION;

 
* In ``CREATE`` user, the user we are creating is ``fire`` who is allowed to access from anywhere ``%`` and his password is ``fire``.

* Next, this user has been granted all ``permissions``. This, of course can be further restricted based on your use case.

Configure Fire to connect to MySQL
----------------------------------

Copy ``db.properties.mysql`` file into the ``conf`` directory as ``db.properties``::

    cd   fire-1.x.y
    cp   conf.orig/db.properties.mysql   conf/db.properties

 

Update the following fields in ``conf/db.properties`` based on the values you used in creating the DB for fire::


    # Connection url for the database "firedb"

    spring.datasource.url=jdbc:mysql://localhost:3306/firedb

    spring.datasource.driverClassName=com.mysql.jdbc.Driver

    spring.jpa.database=MYSQL

    # Username and password

    spring.datasource.username=fire
    

Install the MySQL Connector Jar file
-------------------------------------

* Download the MySQL JDBC driver from http://www.mysql.com/downloads/connector/j/5.1.html

* Extract the ``JDBC driver JAR file`` from the downloaded file. For example::

    tar zxvf mysql-connector-java-5.1.42.tar.gz
  
* Copy the JDBC driver into ``/usr/share/java`` on the machine on which fire is running::

    sudo cp mysql-connector-java-5.1.42/mysql-connector-java-5.1.42-bin.jar /usr/share/java/mysql-connector-java.jar
  
* If the target directory does not yet exist on this host, you can create it before copying the JAR file. For example::

    sudo mkdir -p /usr/share/java/
  
* Also copy the mysql JDBC driver JAR file to the ``user-lib`` directory of ``fire-1.x.y``::

    cd fire-1.x.y    (if you are not already in that directory)
    cp /usr/share/java/mysql-connector-java.jar      user-lib
  
  
Create the Tables for Fire in MySQL
----------------------------------- 

* Create the tables for Fire in MySQL by executing the ``create-mysql-db.sh`` script::

    cd fire-1.x.y      (if you are not already in that directory)

    ./create-mysql-db.sh


Troubleshooting
---------------

MySQL has a problem where one of the default users in the user table is '' @ localhost, which winds up denying all localhost users later in the table. If you are accessing mysql from localhost, assuming Fire and MySQL on same machine, then you need to delete this entry in mysql.user table::


    select user, host from user where user = ''          

    #you should see an entry for this and host equals localhost.

    DELETE from user WHERE user = '' AND host = 'localhost';

    flush privileges;

    #this reloads privileges - important step. otherwise you will get access denied error even though you log in with the correct user.


Here is a link on stackoverflow that talks about this:

            http://stackoverflow.com/questions/1412339/cannot-log-in-with-created-user-in-mysql
            

