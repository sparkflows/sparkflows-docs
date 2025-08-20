
Prerequisites
=============

Supported Linux Versions
-------------------------

::

  - CentOS : 7
  - Ubuntu : 20.04
  - RHEL : 8


Below are required for installing Sparkflows on Linux machine::

  - JDK 17 installed.
  - Java and JAR should be in the PATH.
  - 8 GB+ of RAM (16 GB+ recommended).

If you are installing on Ubuntu, please run the following And then select **No** ::

      sudo dpkg-reconfigure dash


Below is needed if Sparkflows would connect and submit jobs to an Apache Spark Cluster::

  - Spark 3.X is needed on the cluster


If there is need to run the PySpark engine (optional)::

  - Python 3.9 needs to be set up on the machine

    
Downloading and Installing Java 17
+++++++++++++++++++++++++++++++++++++

* Java 17 can be downloaded and installed from `here <https://jdk.java.net/17?>`_.

* Set the **JAVA_HOME** property.

There are various ways for Installing Java 17 on Linux. Some are listed below.


Install using Linux RPM Package
.................................


- Download the Linux x64 RPM Package.

- Install the package::

    yum install java-17-openjdk-devel -y (this has to be run as the root user)

- Update ``.bash_profile`` to add the below::

    export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
    export PATH=$JAVA_HOME/bin:$PATH

Install OpenJDK17 JDK using yum
...............................

    .. code-block:: bash

  	yum -y update

    .. code-block:: bash

  	sudo yum install java-17-openjdk-devel -y


Install OpenJDK17 JDK using apt
..............................

    .. code-block:: bash

	sudo apt install openjdk-17-jdk -y

Check Installation of JAVA 17
...............................

We can check the version of JAVA by running the following command:
  
  .. code-block:: bash

      java -version

On successful installation and checking java version, one would see the below:

   .. figure:: ../../../_assets/aws/aws-deployment/java17.png
      :alt: aws-deployment
      :width: 60%


References
------------

* `Install JAVA on CentOS and Fedora <https://www.digitalocean.com/community/tutorials/how-to-install-java-on-centos-and-fedora>`_
* `OpenJDK download link <https://openjdk.java.net/install/>`_
* `Install OpenJDK on Ubuntu <https://docs.datastax.com/en/jdk-install/doc/jdk-install/installOpenJdkDeb.html>`_
