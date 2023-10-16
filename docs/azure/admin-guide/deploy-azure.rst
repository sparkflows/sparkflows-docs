Installation Guide
======

Sparkflows can run the jobs on the same machine, or it can be connected to an Databricks cluster for job executions. 

This document describes the steps to deploy Sparkflows on Azure.

Step 1 : Prerequisites Check
++++

Before you begin, ensure that you have the following prerequisites in place:

**VM Privileges**
-------
Ensure that you have VM with sufficient privileges to install packages.

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

Step 2 : Procure an VM and setup the Networking
++++
Setup VM with one of the recommended OS and Configure the Network Settings.

For detailed information on Infrastructure Prerequisites for deploying on AWS, `click here. <https://docs.sparkflows.io/en/latest/installation/installation/infrastructure.html>`_

Step 3 : Install Sparkflows
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

  

   .. note::
            * Run all the below steps as a user with sudo permission. If unsure, please run the below commands as `root` user.
            * If you are using Ubuntu, you may have to run the following and then select ``No``. ::

              sudo dpkg-reconfigure dash


#. **Download and install JDK 8**

   On CentOS, install and Open JDK 1.8 by running the following :
       
     ::
         
         sudo yum install -y java-1.8.0-openjdk-devel

   On Ubuntu, install and Open JDK 1.8 by running the following :
       
     ::
         
         sudo apt install openjdk-8-jdk
        

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

   * For CentOS, install `wget` command using :
     ::

        sudo yum -y install wget

   * For Ubuntu, install `wget` command using :
     ::

        sudo apt-get install wget (Ubuntu)

   * Download the latest TAR from :
     ::

        wget https://sparkflows-release.s3.amazonaws.com/fire/rel-3.1.0/3/fire-3.x.y_spark_3.2.1.tgz

   * Extract the TAR by using :
     ::

       tar xvf fire-3.x.y_spark_3.2.1.tgz


   * Create DB tables with Schema :
     
     Sparkflows metadata can be stored in RDS or it has embedded h2 db by default.
     
     * Go to inside the sparkflows binary extracted directory :
       ::
          cd  fire-3.x.y_spark_3.2.1

     * Create the DB and schema by running the following :
       ::
          ./create-h2-db.sh

       .. Note:: For detailed information on connecting to RDS, `click here. <https://docs.sparkflows.io/en/latest/installation/configuration/database/mysql-db.html#>`_

#. **Install Python**
   
   * For CentOS, run the below commands to install all the Python dependencies using :
     ::
        cd ..

     ::

        sudo yum -y update

     ::

        sudo yum install -y gcc openssl-devel bzip2-devel libffi-devel zlib-devel

     ::

        wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz

     ::

        tar xzf Python-3.7.0.tgz

     ::

        cd Python-3.7.0

     ::

        sudo ./configure --enable-optimizations

     ::

        sudo yum -y install make

     ::

        sudo make altinstall

     ::

        cd ..

   * For Ubuntu, run the below commands to install all the Python dependencies using :
     ::
        cd ..

     ::

        sudo apt -y update

     ::

        sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev wget libbz2-dev

     ::

        wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz

     ::

        tar xzf Python-3.7.0.tgz

     ::

        cd Python-3.7.0

     ::

        sudo ./configure --enable-optimizations

     ::

        sudo make altinstall

     ::

        cd ..

   * Check the system wide version of python installed by running : 
     ::
        python3.7 --version

   * Install Python Libraries :
     
     Create the virtual environment, activate it and install the python libraries inside it by running :
     ::
        python3.7 -m venv venv

     ::

        source venv/bin/activate

     ::

        pip install pip --upgrade

     ::

        pip install pystan

     ::

        pip install convertdate

   * Install all the other python libraries from the `requirements.txt` file :
     ::
        pip install -r fire-3.x.y_spark_3.2.1/dist/fire/requirements.txt

     .. Note:: This can run into `Memory error` if there is not enough free RAM on the machine. In that case, please split the dependencies in `requirements.txt` into multiple parts and install.

   * Check if all dependencies are installed by running :
     ::
        pip list

#. **Start Sparkflows Server**

   By default Sparkflows will run on 8080(http) and 8443(https). 

   To adjust and personalize the port settings :

   You can modify the configurations in the **application.properties** file located within **fire-3.x.y_spark_3.2.1/conf**.

   Start the Sparkflows server by running the below :
     
       ::
         
            ./run-fire-server.sh start

**Using Sparkflows Docker Image**
------
Sparkflows can be installed and run on Linux (Ubuntu) using the Docker image from the Docker Hub.

To download Sparkflows using Docker Image, follow the steps given below :

#. **Download and install Docker on your Linux machine**

   * Docker Desktop (https://docs.docker.com/engine/install/)
      * Download the Docker CE
      * Verify that the docker is up and running and the the docker version by running the following :
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


Step 3 : Accessing Sparkflows & Creating Users
++++
Pick the public IP or DNS of the machine from AWS Console -> Instances and hit the URL: http://sparkflows_IP:8080

By default Sparkflows comes with default user **admin** and **test** with default password as **admin** and **test** respectively.

If you want to create new users, it can be done from Sparkflows **Administration Tab** by choosing **Users** as shown in the image below :

      .. figure:: ../../_assets/aws/livy/administration.PNG
         :alt: livy
         :width: 60%

Step 4 : Reloading Sample Project
++++

Fire Insights by default comes with sample Project which can be reloaded in Fire Insight application.

For detailed information, `click here. <https://docs.sparkflows.io/en/latest/installation/installation/load-sample-projects.html>`_

Step 5 : Submitting Jobs to Databricks Cluster
++++
By default Sparkflows job can be submitted on the local machine itself. 

It can be configured to submit the jobs to AWS EMR cluster for scalability.

For more information, `click here. <https://docs.sparkflows.io/en/latest/aws/admin-guide/emr-livy/index.html>`_



