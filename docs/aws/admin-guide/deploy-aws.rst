AWS Deployment Document
======

Overview
++++

This document describes the steps to deploy Sparkflows on AWS. Sparkflows can run the jobs on the same machine, or it can be connected to an AWS EMR cluster for job executions.

- Prerequisite
- Machine Specification
- Installation and setup on AWS EC2
- DNS Certificates setup for HTTPS
- Install Sparkflows
- Accessing Sparkflows & Creating Users
- Compute Connection for Submitting the job

Prerequisite
++++

You need to have:

- EC2 Instance.
- S3 Bucket with Read, Write Permission


Machine Specifications
++++

.. list-table:: 
   :widths: 10 40 30
   :header-rows: 1

   * - Title
     - Details
     - Notes
   * - OS
     - RHEL : 8+ , CentOS : 7+, Ubuntu : 20.04
     - Any of these OS are preferred
   * - RAM / Memory
     - 30+ GB based on the size of the data to be processed
     - More memory the better
   * - Disk
     - 500+ GB (1TB+ preferred), SSD
     - Root directory should have 100+ GB, Home directory of the user with which Sparkflows is installed should have 200+ GB, /tmp should have 50+ GB
   * - vCPU Cores
     - 8+
     - More vCPU cores the better

More Information can be found here: 

https://docs.sparkflows.io/en/latest/installation/installation/infrastructure.html


Software Specifications
++++

.. list-table:: 
   :widths: 10 40 30
   :header-rows: 1

   * - Title
     - Details
     - Notes
   * - Java
     - JDK 8
     - Java 8 is needed
   * - Python
     - Python 3.7
     - Python 3.7 is needed
   * - Port
     - Port 8443 open for https access for the users, Port 8080 opens if http access is needed.
     - The port is configurable
   * - Users
     - Root access is needed during installation for installing JDK, Another user (can be called sparkflows) would be used for the installation of Sparkflows.
     - This user can be “sparkflows”
   * - HTTPS
     - Ensure DNS and https certificates are set up.
     - HTTPS certificate available

Installation and setup on AWS EC2
++++

Setup EC2 Machine and Configure Network Settings

Infrastructure Prerequisites for deploying on AWS:

Detailed Information can be found here:

https://docs.sparkflows.io/en/latest/installation/installation/infrastructure.html

DNS Certificate setup
++++

You can use AWS Certificate Manager to set up DNS

Detailed Information can be found here:
 
https://docs.sparkflows.io/en/latest/aws/admin-guide/configuring-aws-certificate.html


Install Sparkflows
++++

Sparkflows can be installed in one of two ways:

- Using Sparkflows tgz file.
- Using Sparkflows Docker Image.

It is easier to install using the Docker Image.

Using Sparkflows tgz file
------

SSH into the AWS Instance
++++

SSH into the AWS Instance using:

- Public ipv4 IP from the AWS console and
- The `PEM` file (key file) downloaded while bringing up the AWS Instance
And the command as below:
- ssh -i sparkflows.pem ec2-user@21.xxx.xxx.113

Download and install JDK 8
++++

Install Open JDK 1.8 by running::


    sudo yum install -y java-1.8.0-openjdk-devel

Check the version of JAVA by running::


    java -version

On successful installation and checking java version, one would see the below:



Download the latest Sparkflows TAR
++++

Install `wget` command using::


          sudo yum -y install wget

Download the latest TAR from::


    wget https://sparkflows-release.s3.amazonaws.com/fire/rel-3.1.0/3/fire-3.2.28_spark_3.2.1.tgz

Extract the TAR by using::


    tar xvf fire-3.2.28_spark_3.2.1.tgz


Create DB tables with Schema

Sparkflows metadata can be stored in RDS or it has embedded h2 db by default.

Goto inside the sparkflow binary extracted directory::



    cd  fire-3.1.0_spark_3.2.1

Create the DB and schema by running the following::


    ./create-h2-db.sh



Install Python
++++

Run the below commands to install all the Python dependencies::


    cd ..
    sudo yum -y update
    sudo yum install -y gcc openssl-devel bzip2-devel libffi-devel zlib-devel
    wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
   tar xzf Python-3.7.0.tgz
   cd Python-3.7.0
   ./configure --enable-optimizations
   sudo yum -y install make
   sudo make altinstall

Check the system wide version of python installed by::


    python3.7 --version

Install Python Libraries

Create the virtual environment, activate it and install the python libraries inside it by::


    python3.7 -m venv venv
    source venv/bin/activate
    pip install pip --upgrade
    pip install pystan
    pip install convertdate

Install all the other python libraries from the `requirements.txt` file::


    pip install -r fire-3.2.8_spark_3.2.1/dist/fire/requirements.txt

.. Note:: This can run into `Memory error` if there is not enough free RAM on the machine. In that case, please split the dependencies in `requirements.txt` into multiple parts and install.

Check if all dependencies are installed by running::


    pip list

Start Sparkflows Server
++++

By default Sparkflows will run on 8080(http) and 8443(https). To configure and customize the port, it can be done via `application.properties` which can be found in `fire-3.2.8_spark_3.2.1/conf` .

Start the Sparkflows server by running the below::


    ./run-fire-server.sh start

Using Sparkflows Docker Image
------

Sparkflows can be installed and run on Linux (Ubuntu) using the Docker image from the Docker Hub.

Download and install Docker on your Linux machine
++++

* Docker Desktop (https://docs.docker.com/engine/install/)
    * Download the Docker CE
    * Verify that the docker is up and running and the the docker version by running ``docker --version``
    * Executing the Docker Command Without Sudo(Optional)::
    
        sudo usermod -aG docker ${USER}

Installation Steps
++++

* Set up the environment variables. The local mount directory is ``/home/username/sparkflows`` - create this directory by using mkdir in the below docker run command. Please update it to directory structure on your machine. Replace ``XX`` with the Sparkflows version you want to install::
    
    export SPARK_VERSION=3.2.1
    export RELEASE_VERSION=3.X.XX
    export FIRE_VERSION=3.1.0
    export SPARKFLOWS_ROOT=/home/username/sparkflows

* Pull the latest Sparkflows docker image from Docker hub::

    docker pull sparkflows/fire:py_${SPARK_VERSION}_${RELEASE_VERSION}


* Start the docker image using the ``docker run`` command below. The local mount directory is ``(/home/username/sparkflows)`` in the below docker run command. Please update it to directory structure on your machine. Reduce/Increase the memory allocated (Eg: Using ``-m 8g`` will allocate 8GB to the Sparkflows container) to a lower value depending on the RAM on the machine. We recommend 16GB or above::
    
    
    docker run -m 16g -p 8080:8080 -p 9443:9443 \
    -v ${SPARKFLOWS_ROOT}:/usr/local/fire-${RELEASE_VERSION}_spark_${SPARK_VERSION} \
    -e KEYSTORE_PASSWORD=12345678 \
    -e FIRE_HTTP_PORT=8080 \
    -e FIRE_HTTPS_PORT=9443 \
    -e FIRE_VERSION=${FIRE_VERSION} \
    sparkflows/fire:py_${SPARK_VERSION}_${RELEASE_VERSION}

Detailed Information can be found here:
 
https://docs.sparkflows.io/en/latest/installation/installation/docker-linux-install.html



Accessing Sparkflows & Creating Users
-------

Pick the public IP or DNS of the machine from AWS Console -> Instances and hit the URL: http://sparkflows_IP:8080
By default Sparkflows comes with default user `admin` and `test` with default password as `admin` and `test` respectively.
If you want to create new users, it can done from Sparkflows administration tab by choosing `Users` as shown in the screenshot below:


Submitting jobs to EMR cluster
------

By default Sparkflows job can be submitted on the local machine itself. It can be configured to submit the jobs to AWS EMR cluster for scalability.


More Information can be found here: 

https://docs.sparkflows.io/en/latest/aws/admin-guide/emr-livy/index.html


Additional requirements
----

* The machine needs to have access to the Internet only to install dependencies. 

* Access to s3 bucket to store the data(optional)

* If using s3 as a data source, the IAM role for s3 bucket should be added to the EC2 instance created for Sparkflows.


More Information can be found here:

https://docs.sparkflows.io/en/latest/aws/admin-guide/aws-ec2-configure.html
