Windows Installer for Laptop and Desktop
====================================

You can download and use the Installer for installing/upgrading Fire Insights on your laptop or desktop.

This is not recommended to use on the server, where you need better control over the Installation process.

Prerequisites
-------------

- JDK 1.8

Java 8 can be downloaded and installed from here : https://www.oracle.com/java/technologies/javase-jdk8-downloads.html

You may have to set JAVA_HOME after the installation.


Download
--------

Download the installer from : https://www.sparkflows.io/download


Execute
-------

Execute the installer with ::

  java -jar sparkflows-installer.exe

By default Fire Insights listens on port 8080 (http) and port 8443 (https).

The port numbers can also be updated in the file conf/application.properties.


**Log into Fire Insights**

 - In your Browser go to http://<system-ip>:port

 -	Login with below credentials :
    - Username : admin
    - Password : admin
