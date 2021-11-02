Linux/Mac OS Installation Prerequisites
=============

Supported Linux Versions
-------------------------

::

  - CentOS : 7+
  - Ubuntu : 18+
  - RHEL : 8+

Prerequisites
-------------

Below are the Prerequisites for installing Fire Insights on a Mac or Linux machine::

  - JDK 1.8+ installed.
  - java and jar have to be in the PATH
  - 8 GB+ of RAM.
  - Python 3.6+ (when running Python and PySpark, otherwise not needed)


If Fire would be connected to an Apache Spark Cluster::

  - Spark 2.X is needed on the cluster
  - Fire has to be installed on an Edge node of the Spark Cluster


If using Python and PySpark (not needed for the core features of Fire Insights) ::

  - Python 3.X can be set up with the Python virtual environment and activated

    
Downloading and Installing Java 8
---------------------------------

Java 8 can be downloaded and installed from here : https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html

You may have to set JAVA_HOME after the installation.

There are various ways for Installing Java 8 on Linux. Some are listed below.


Using Linux RPM Package
+++++++++++++++++++

- Download the Linux x64 RPM Package

- Install the package::

    yum localinstall jdk-8u202-linux-x64.rpm (this has to be run as the root user)

- Update ``.bash_profile`` to add the below::

    export JAVA_HOME=/usr/java/jdk1.8.0_202-amd64/
    export PATH=$PATH:$JAVA_HOME/bin

Install OpenJDK8 JDK using yum
++++++++++++++++++

::

  yum -y update
  yum install java-1.8.0-openjdk-devel

Installing on Mac
+++++++++++++++++

- Download the dmg file
- Install it


Reference
---------

Links
+++++

* https://www.digitalocean.com/community/tutorials/how-to-install-java-on-centos-and-fedora



Download OpenJDK
+++++++++++++

- https://openjdk.java.net/install/

- Install OpenJDK on Ubuntu

https://docs.datastax.com/en/jdk-install/doc/jdk-install/installOpenJdkDeb.html


    
