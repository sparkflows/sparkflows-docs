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


Selinux
--------

Just ensure that selinux should be disabled so that we can install Hadoop on it.
