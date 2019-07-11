Windows Installation Prerequisites
+++++++++++++

Below are the Prerequisites for installing Fire Insights on a windows machine::

  - JDK 1.8 installed.
  - java and jar have to be in the PATH
  - 5GB+ of RAM.
  - Python 3.X (when running Python and PySpark, otherwise not needed)

Check JDK 1.8
-------------

* Check the JDK version installed on your machine::

    Open terminal window 
    Type the following command to check your java version : java -version

* If JDK 1.8 is not installed, follow the JDK installation steps mentioned below.


Install JDK 1.8
---------------

* Download JDK 1.8 for windows using below link::

    https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html

* Install java by double clicking on downloaded exe file

* After installation, make sure that java 1.8 is in the path::

    Open a new terminal window 
    Type the following command to check your java version : java -version

.. note::  If you have multiple versions of Java installed on you system, you can update the PATH using the steps outlined here:

           * https://www.java.com/en/download/help/path.xml
           * https://javatutorial.net/set-java-home-windows-10
           
           
           
 
.. note:: In order to connect Fire Insights to an Apache Spark cluster, it has to be installed on the edge node of the cluster.

   
