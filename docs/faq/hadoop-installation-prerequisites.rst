Hadoop Installation Pre-Requisites
==================================

Below are the pre-requisites for installing Hadoop:

- Linux
- JDK 1.8 installed
- IPV6 disabled
- Selinux disabled

Linux
-----

It requires Minimum Configuration of Linux Machine as belows:

- VCPUS: 8 vcores
- RAM: 32 GB

JDK
---

It requires java 8 to be installed on the Linux Machine. Below are the steps added to install oracle java:

- http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
- wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "https://download.oracle.com/otn-pub/java/jdk/8u201-b09/42970487e3af4f5aa5bca3f542482c60/jdk-8u201-linux-x64.rpm"
- yum localinstall jdk-8u201-linux-x64.rpm

Just ensure that java is installed properly by checking it using below command:

- Java -version

.. figure:: ../_assets/user-guide/java-version.PNG
   :alt: Sparkflows
   :align: center

Set the below in .bash_profile

- export JAVA_HOME=/usr/java/jdk1.8.0_201-amd64/

Selinux
--------

Just ensure that selinux should be disabled so that we can install Hadoop on it.

- sudo setenforce 0

To disable it permanently

- edit /etc/selinux/config
SELINUX=disabled

- reboot

Steps Involved in Installing Hadoop
------------------------------------

- Install bind-utils : Otherwise Cloudera Manager gives **host not found**

  - yum install bind-utils

- Install Cloudera Manager

  - cd
  - wget https://archive.cloudera.com/cm5/installer/latest/cloudera-manager-installer.bin
  - chmod u+x cloudera-manager-installer.bin
  - ./cloudera-manager-installer.bin
  - Accept Licenses
  
- Open ports on Linux Machine
  
  - Open the ports 7180 and 8080 
  
After Installation of Cloudera Manager
--------------------------------------

- go to http://host-ip:7180/
 
  - Log in with admin/admin
  - Select Cloudera Express Installation
  - For host, give the hostname IP (private IP)
  - Install using Parcels
  - Include the Kafka parcels
  - User : sparkflows ( As per as updated on machine while creating Linux Machine)
  - Supply the private key
