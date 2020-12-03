Installing MySQL
================

This document captures the details for installing MySQL on Centos7

Below are steps on how to install MYSQL on Centos7
----------------------------------------------------

* To check your hostname run::

 hostname -f
 
* Update your system::

 sudo yum update
 
* You will need wget to complete this guide. It can be installed as follows::
 
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

Download
--------

Download MySQL from https://dev.mysql.com/downloads/mysql/


Create Database
---------------

create database test;

Create User and Grant Permissions
-----------

CREATE user 'fire'@'%' IDENTIFIED BY 'fire';
GRANT ALL PRIVILEGES ON firedb.* TO 'fire'@'%' WITH GRANT OPTION;


MySQL JDBC Driver
-----------------

Download the MySQL JDBC driver from http://www.mysql.com/downloads/connector/j/5.1.html

Extract the JDBC driver JAR file from the downloaded file. For example:

tar zxvf mysql-connector-java-8.0.11.tar.gz

mysql-connector-java.jar
