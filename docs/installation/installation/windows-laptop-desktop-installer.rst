Windows Installer for Laptop and Desktop
====================================

You can download and use the Installer for installing/upgrading Fire Insights on your laptop or desktop.

This is not recommended to use on the server, where you need better control over the Installation process.

Prerequisites
-------------

- JDK 1.8
- Sufficient permission to Download and install Sparkflows in user directory and have write permission to download winutils.exe inside windows directory and set environment path.

Java 8 can be downloaded and installed from here : https://www.oracle.com/java/technologies/javase-jdk8-downloads.html

You may have to set JAVA_HOME after the installation.

.. note::  If you have multiple versions of Java installed on you system, you can update the PATH using the steps outlined in either of the links below:

           * https://javatutorial.net/set-java-home-windows-10
           * https://www.java.com/en/download/help/path.xml
           


Download
--------

Download the installer from : https://www.sparkflows.io/windows-download


Run and Execute
-------

Once Downloaded Open and run the installer file::

  
By default Fire Insights listens on port 8080 (http) and port 8443 (https).

The port numbers can also be updated in the file conf/application.properties.


**Log into Fire Insights**

 - In your Browser go to http://<system-ip>:port

 -	Login with below credentials :
    - Username : admin
    - Password : admin

.. note::  On Windows, the PySpark engine will not get installed. Below are he funcationalities that will not be available on bare metal windows install. We recommend either docker on windows to access all functionalities or install Sparkflows on Linux

           * AutoML
           * Prophet
           * ARIMA
           * Scikit learn models
           * Keras/Tensorflow models
           * A few other python native packages.
