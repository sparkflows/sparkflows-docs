Install MySQL
================

This document captures the details for installing MySQL on CentOS 7.x. Sparkflows by default runs with embedded H2 database. Sparkflows can be configured with MySQL.

Steps for installing MySQL on CentOS 7.x
--------------------------------------

* Check your hostname 

To check your hostname run::

 hostname
 hostname -f
 
* Update your system :

Run the below command to update your system::

 sudo yum update
 
* Install wget if its not on your system 

You will need wget to complete this guide. It can be installed as follows::
 
 sudo yum install wget
 
Install MySQL
---------------

MySQL must be installed from the community repository.
 
* Download and add the repository
 
Download and add the repository, then update:: 
 
 wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
 sudo rpm -ivh mysql-community-release-el7-5.noarch.rpm
 sudo yum update
 
* Install MySQL and start the service

Install MySQL, as usual, and start the service. During installation, you will be asked if you want to accept the results from the .rpm file’s GPG verification. If no error or mismatch occurs, enter y::

 sudo yum install mysql-server
 sudo systemctl start mysqld

Harden MySQL Server
-------------------

* Harden security concern

Run the mysql_secure_installation script to address several security concerns in a default MySQL installation::

 sudo mysql_secure_installation
 
* Check existing password generated
 
To check existing password generated::
 
 sudo grep 'temporary password' /var/log/mysqld.log
 
* You can also create new password while installation.

Using MySQL
------------

The standard tool for interacting with MySQL is the MySQL client which installs with the mysql-server package. The MySQL client is used through a terminal.

* Root Login

To log in to MySQL as the root user::
 
 mysql -u root -p
 
* When prompted, enter the root password you assigned when the mysql_secure_installation script was running.

You’ll then be presented with a welcome header and the MySQL prompt as shown below::

 mysql>
 

Provide access from remote machines
--------------------------------

In order to access MySQL from remote machines, run the below command::
 
 CREATE USER 'root'@'%' IDENTIFIED BY 'password';
 GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
 FLUSH PRIVILEGES;

NOTES * The port on which MySQL is running, i.e. 3306, should be accessible from target machine.

Create a New MySQL User and Database
-----------------------------------

In the example below, testdb is the name of the database, testuser is the user, and password is the user’s password::

 create database testdb;
 create user 'testuser'@'localhost' identified by 'password';
 grant all on testdb.* to 'testuser' identified by 'password';
 
Create a Sample Table
--------------------

* Log back in as testuser

Login with testuser::

 mysql -u testuser -p

* Create a sample table

Create a sample table called customers. This creates a table with a customer ID field of the type INT for integer (auto-incremented for new records, used as the primary key), as well as two fields for storing the customer’s name::

 use testdb;
 create table customers (customer_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, first_name TEXT, last_name TEXT);
 
Reset the MySQL Root Password
-------------------------------

If you forget your root MySQL password, it can be reset by following the below steps.

* Stop the current MySQL server instance.

Stop the current MySQL server instance, then restart it with an option to not ask for a password::

 sudo systemctl stop mysqld
 sudo mysqld_safe --skip-grant-tables &
 
* Reconnect to the MySQL server

Reconnect to the MySQL server with the MySQL root account::

 mysql -u root
 
* Use the following commands to reset root’s password.

Use the following commands to reset root’s password. Replace password with a strong password::

 use mysql;
 update user SET PASSWORD=PASSWORD("password") WHERE USER='root';
 flush privileges;
 exit
 
* Restart MySQL

Then restart MySQL::

 sudo systemctl start mysqld
 

MySQL JDBC Driver
-----------------


- MySQL connector can be downloaded from : https://dev.mysql.com/downloads/connector/j/ or you can download it directly from maven repository : https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.11/
- After downloading, untar it with : ``tar xvf mysql-connector-java-8.0.11.tar.gz`` 
- After untaring, the jdbc jar file is available in the directory.
- Use the jar file (mysql-connector-java-8.0.11.jar) for installation in Fire.
