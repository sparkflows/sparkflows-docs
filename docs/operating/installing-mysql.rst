Installing MySQL
================

This document captures the details for installing MySQL on Centos7

Below are steps on how to install MYSQL on Centos7
----------------------------------------------------

* check your hostname run

To check your hostname run::

 hostname -f
 
* Update your system

Run below command to update your system::

 sudo yum update
 
* Install wget if its not on your system

You will need wget to complete this guide. It can be installed as follows::
 
 yum install wget
 
Install MySQL
---------------

MySQL must be installed from the community repository.
 
* Download and add the repository, then update
 
 * ``wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm``
 * ``sudo rpm -ivh mysql-community-release-el7-5.noarch.rpm``
 * ``sudo yum update``
 
* Install MySQL as usual and start the service. During installation, you will be asked if you want to accept the results from the .rpm file’s GPG verification. If no error or mismatch occurs, enter y. 

 * ``sudo yum install mysql-server``
 * ``sudo systemctl start mysqld``

Harden MySQL Server
-------------------

* Run the mysql_secure_installation script to address several security concerns in a default MySQL installation::

 sudo mysql_secure_installation
 
* To check already password generated::
 
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

 Inorder to Access MYSQL from Remote PC, run below command
 
* ``GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'Sparkflows@123' WITH GRANT OPTION;``
* ``FLUSH PRIVILEGES;``

NOTES * The Port on which MYSQL Running ie 3306, should be accessible from target machine.

MySQL JDBC Driver
-----------------

Download the MySQL JDBC driver from http://www.mysql.com/downloads/connector/j/5.1.html

Extract the JDBC driver JAR file from the downloaded file. For example:

tar zxvf mysql-connector-java-8.0.11.tar.gz

mysql-connector-java.jar
