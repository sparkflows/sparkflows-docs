Install using Docker Image
==========
Sparkflows can be installed and run on Linux (Ubuntu) using the Docker image from the Docker Hub.

This document explains in detail the steps required to install Sparkflows using Docker image.

Follow the steps given below to install :

Step 1 : Download and Install Docker on Linux Machine
---------------------

Docker Desktop (https://docs.docker.com/engine/install/)
  * Download the Docker CE
  * Verify that the docker is up and running and the the docker version by running the following :
    ::
            docker --version
     
  * Executing the Docker Command Without Sudo(Optional) :
    ::
           sudo usermod -aG docker ${USER}

Step 2 : Set up Environment Variables
------------------

Set up the environment variables. The local mount directory is (**/home/username/sparkflows**).

Create this directory by using **mkdir** in the below docker run command. 

Please update it to directory structure on your machine. 

Replace **XX** with the Sparkflows version you want to install :
::
        export SPARK_VERSION=3.2.1
        export RELEASE_VERSION=3.X.XX
        export FIRE_VERSION=3.1.0
        export SPARKFLOWS_ROOT=/home/username/sparkflows

Step 3 : Pull the Latest Sparkflows Docker Image
---------

Pull the latest Sparkflows docker image from Docker hub :
::
         docker pull sparkflows/fire:py_${SPARK_VERSION}_${RELEASE_VERSION}

Step 4 : Start the Docker Image
---------
Start the docker image using the docker run command below :
  
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

.. Note:: We recommend 16GB or above.
     
For detailed information, `click here. <https://docs.sparkflows.io/en/latest/installation/installation/docker-linux-install.html>`_
