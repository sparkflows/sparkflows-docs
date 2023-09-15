Deployment Guide
======

Sparkflows can run the jobs on the same machine, or it can be connected to an AWS EMR cluster for job executions. 

This document describes the steps to deploy Sparkflows on AWS.

Overview
++++

Below is a brief overview of the steps involved in the deployment process :

#. Prerequisites Check
  
   * EC2 Instance Privileges
   * S3 Bucket Permissions 
   * EMR Cluster Access
   * Machine Specifications
   * Software Specifications
#. Installation and Setup on AWS EC2
#. DNS Certificates Setup for HTTPS
#. Install Sparkflows
#. Accessing Sparkflows & Creating Users
#. Compute Connection for Submitting the Job

Step 1 : Prerequisites Check
++++

Before you begin, ensure that you have the following prerequisites in place:

**EC2 Instance Privileges**
-------
Ensure that you have EC2 Instance with sufficient privileges.

**S3 Bucket Permissions**
--------
Ensure that you have S3 Bucket with Read, Write Permissions.

**EMR Cluster Access**
---------
Ensure that you have EMR Cluster with Livy URL accessible from Sparkflows Instance.

**Machine Specifications**
---------
Ensure that you have the following prerequisites with regard to machine specifications :

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

To get more information, `click here. <https://docs.sparkflows.io/en/latest/installation/installation/infrastructure.html>`_


**Software Specifications**
------
Ensure that you have the following prerequisites with regard to software specifications :

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
     - Port 8443 open for https access for the users, Port 8080 opens if http access is needed
     - The port is configurable
   * - Users
     - Root access is needed during installation for installing JDK, Another user (can be called sparkflows) would be used for the installation of Sparkflows
     - This user can be “sparkflows”
   * - HTTPS
     - Ensure DNS and https certificates are set up
     - HTTPS certificate available

Step 2 : Installation and setup on AWS EC2
++++

Setup EC2 Machine and Configure the Network Settings.

For detailed information on Infrastructure Prerequisites for deploying on AWS, `click here. <https://docs.sparkflows.io/en/latest/installation/installation/infrastructure.html>`_

Step 3 : DNS Certificate setup
++++

Use AWS Certificate Manager to set up DNS.

For detailed information, `click here. <https://docs.sparkflows.io/en/latest/aws/admin-guide/configuring-aws-certificate.html>`_


Step 4 : Install Sparkflows
++++

Sparkflows can be installed in one of the following two ways:

* Using Sparkflows tgz file.
* Using Sparkflows Docker Image.

**Note :** It is easier to install using the Docker Image.

**Using Sparkflows tgz file**
------
Follow the below steps to install Sparkflows using tgz file :

#. **SSH into the AWS Instance**
   
   SSH into the AWS Instance using:

   * Public ipv4 IP from the AWS console and 
   * The `PEM` file (key file) downloaded while bringing up the AWS Instance and
   * The command as below :
     ::
         ssh -i sparkflows.pem ec2-user@21.xxx.xxx.113

#. **Download and install JDK 8**

   Install and Open JDK 1.8 by running the following :
       
     ::
         
         sudo yum install -y java-1.8.0-openjdk-devel

#. **Check Java Version**
   
   Check the version of JAVA by running the following :

     :: 
      
         java -version

   On successful installation and checking java version, one would see the below:

      .. figure:: ../../_assets/aws/aws-deployment/install.png
         :alt: aws-deployment
         :width: 60%

#. **Download the latest Sparkflows TAR**
   
    To download, follow the steps given below :

   * Install `wget` command using :
     ::

        sudo yum -y install wget

   * Download the latest TAR from :
     ::

        wget https://sparkflows-release.s3.amazonaws.com/fire/rel-3.1.0/3/fire-3.2.28_spark_3.2.1.tgz

   * Extract the TAR by using :
     ::

       tar xvf fire-3.2.28_spark_3.2.1.tgz


   * Create DB tables with Schema :
     
     Sparkflows metadata can be stored in RDS or it has embedded h2 db by default.
     
     * Go to inside the sparkflows binary extracted directory :
       ::
          cd  fire-3.1.0_spark_3.2.1

     * Create the DB and schema by running the following :
       ::
          ./create-h2-db.sh

#. **Install Python**
   
   * Run the below commands to install all the Python dependencies using :
     ::
        cd ..
        sudo yum -y update
        sudo yum install -y gcc openssl-devel bzip2-devel libffi-devel zlib-devel
        wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
        tar xzf Python-3.7.0.tgz
        cd Python-3.7.0
        ./configure --enable-optimizations
        sudo yum -y install make
        sudo make altinstall

   * Check the system wide version of python installed by running : 
     ::
        python3.7 --version

   * Install Python Libraries
     
     Create the virtual environment, activate it and install the python libraries inside it by running :
     ::
        python3.7 -m venv venv
        source venv/bin/activate
        pip install pip --upgrade
        pip install pystan
        pip install convertdate

   * Install all the other python libraries from the `requirements.txt` file :
     ::
        pip install -r fire-3.2.8_spark_3.2.1/dist/fire/requirements.txt

     .. Note:: This can run into `Memory error` if there is not enough free RAM on the machine. In that case, please split the dependencies in `requirements.txt` into multiple parts and install.

   * Check if all dependencies are installed by running
     ::
        pip list

#. **Start Sparkflows Server**

   By default Sparkflows will run on 8080(http) and 8443(https). 

   To adjust and personalize the port settings :

   You can modify the configurations in the **application.properties** file located within **fire-3.2.8_spark_3.2.1/conf**.

   Start the Sparkflows server by running the below
   ::
      ./run-fire-server.sh start

**Using Sparkflows Docker Image**
------

Sparkflows can be installed and run on Linux (Ubuntu) using the Docker image from the Docker Hub.

To download Sparkflows using Docker Image, follow the steps given below :

#. **Download and install Docker on your Linux machine**

   * Docker Desktop (https://docs.docker.com/engine/install/)
      * Download the Docker CE
      * Verify that the docker is up and running and the the docker version by running the following
        ::
            docker --version
     
      * Executing the Docker Command Without Sudo(Optional) :
        ::
           sudo usermod -aG docker ${USER}

#. **Installation Steps**

   * Set up the environment variables. The local mount directory is (**/home/username/sparkflows**).

     Create this directory by using **mkdir** in the below docker run command. 

     Please update it to directory structure on your machine. 

     Replace **XX** with the Sparkflows version you want to install :
     ::
        export SPARK_VERSION=3.2.1
        export RELEASE_VERSION=3.X.XX
        export FIRE_VERSION=3.1.0
        export SPARKFLOWS_ROOT=/home/username/sparkflows

   * Pull the latest Sparkflows docker image from Docker hub :
     ::
         docker pull sparkflows/fire:py_${SPARK_VERSION}_${RELEASE_VERSION}


   * Start the docker image using the docker run command below :
  
     The local mount directory is (**/home/username/sparkflows**) in the below docker run command. 

     Please update it to directory structure on your machine. 

     Reduce/Increase the memory allocated to a lower value depending on the RAM on the machine. 

     Eg: Using ``-m 8g`` will allocate 8GB to the Sparkflows container.
     ::
        docker run -m 16g -p 8080:8080 -p 9443:9443 \
        -v ${SPARKFLOWS_ROOT}:/usr/local/fire-${RELEASE_VERSION}_spark_${SPARK_VERSION} \
        -e KEYSTORE_PASSWORD=12345678 \
        -e FIRE_HTTP_PORT=8080 \
        -e FIRE_HTTPS_PORT=9443 \
        -e FIRE_VERSION=${FIRE_VERSION} \
        sparkflows/fire:py_${SPARK_VERSION}_${RELEASE_VERSION}

     **Note :** We recommend 16GB or above.
     
     For detailed information, `click here. <https://docs.sparkflows.io/en/latest/installation/installation/docker-linux-install.html>`_


Step 5 : Accessing Sparkflows & Creating Users
++++

Pick the public IP or DNS of the machine from AWS Console -> Instances and hit the URL: http://sparkflows_IP:8080

By default Sparkflows comes with default user **admin** and **test** with default password as **admin** and **test** respectively.

If you want to create new users, it can be done from Sparkflows **Administration Tab** by choosing **Users** as shown in the image below :

   .. figure:: ../../_assets/aws/livy/administration.PNG
      :alt: livy
      :width: 60%

Step 6 : Submitting Jobs to EMR Cluster
++++

By default Sparkflows job can be submitted on the local machine itself. 

It can be configured to submit the jobs to AWS EMR cluster for scalability.

For more information, `click here. <https://docs.sparkflows.io/en/latest/aws/admin-guide/emr-livy/index.html>`_


Additional requirements
++++

* The machine needs to have access to the Internet only to install dependencies. 

* Access to S3 bucket to store the data(optional).

* If using S3 as a data source, the IAM role for S3 bucket should be added to the EC2 instance created for Sparkflows.

For more information, `click here. <https://docs.sparkflows.io/en/latest/aws/admin-guide/aws-ec2-configure.html>`_
