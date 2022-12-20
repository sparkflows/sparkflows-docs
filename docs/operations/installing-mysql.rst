Installing MySQL
================

This document captures the details for installing MySQL on Centos7. Fire Insights by default runs with embedded H2 DB. Fire Insights can be configured wity MySQL.

Steps for installing MySQL on Centos7
--------------------------------------

* Check your hostname

To check your hostname run::

 hostname
 hostname -f
 
* Update your system

Run below command to update your system::

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
 
* Install MySQL as usual and start the service

Install MySQL as usual and start the service. During installation, you will be asked if you want to accept the results from the .rpm file’s GPG verification. If no error or mismatch occurs, enter y::

 sudo yum install mysql-server
 sudo systemctl start mysqld

Harden MySQL Server
-------------------

* Harden security Concern

Run the mysql_secure_installation script to address several security concerns in a default MySQL installation::

 sudo mysql_secure_installation
 
* To check Existing password generated
 
To check Existing password generated::
 
 sudo grep 'temporary password' /var/log/mysqld.log
 
* You can also create new password while installing too.

Using MySQL
------------

The standard tool for interacting with MySQL is the mysql client which installs with the mysql-server package. The MySQL client is used through a terminal

* Root Login

To log in to MySQL as the root user::
 
 mysql -u root -p
 
* When prompted, enter the root password you assigned when the mysql_secure_installation script was run

You’ll then be presented with a welcome header and the MySQL prompt as shown below::

 mysql>
 

To Provide access from remote pcs
--------------------------------

In order to access MySQL from Remote PC, run below command::
 
 CREATE USER 'root'@'%' IDENTIFIED BY 'password';
 GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
 FLUSH PRIVILEGES;

NOTES * The Port on which MySQL Running ie 3306, should be accessible from target machine.

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

If you forget your root MySQL password, it can be reset.

* Stop the current MySQL server instance

Stop the current MySQL server instance, then restart it with an option to not ask for a password::

 sudo systemctl stop mysqld
 sudo mysqld_safe --skip-grant-tables &
 
* Reconnect to the MySQL server

Reconnect to the MySQL server with the MySQL root account::

 mysql -u root
 
* Use the following commands to reset root’s password

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

Download the MySQL JDBC driver from http://www.mysql.com/downloads/connector/j/5.1.html

Extract the JDBC driver JAR file from the downloaded file. For example:

tar zxvf mysql-connector-java-8.0.11.tar.gz

mysql-connector-java.jar
