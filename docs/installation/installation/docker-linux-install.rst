Docker Image on Linux
^^^^^^^^^^^^^^^^^^^^^

Sparkflows can be installed and run on Linux (Ubuntu, CentOS, RHEL) using the Docker image from the Docker Hub.


Prerequisites
-------------

* Docker Desktop (https://docs.docker.com/engine/install/)
    * Download the Docker CE
    * Verify that the docker is up and running and the the docker version by running ``docker --version``
* Install AWS CLI if running docker on EC2::

   sudo apt install awscli -y [On Ubuntu]
   yum install awscli -y [On RHEL/CentOS]
* If running Docker on EC2 instance, via AWS CLI one need to update the number of hops to 2 instead of the default value of 1 which is set for EC2 instance using the command below. Replace the actual instance ID value in the command below inplace of `i-0fe0xxxxxxxxxxx`::

   aws ec2 modify-instance-metadata-options --instance-id i-0fe0xxxxxxxxxxx --http-tokens required --http-endpoint enabled --http-put-response-hop-limit 2

Installation Steps
---------------------------

* Set up the environment variables. The local mount directory is ``/home/username/sparkflows`` - create this directory by using mkdir in the below docker run command. Please update it to directory structure on your machine. Replace ``XX`` with the Sparkflows version you want to install::
    
    export SPARK_VERSION=3.2.1
    export RELEASE_VERSION=3.X.XX
    export FIRE_VERSION=3.1.0
    export SPARKFLOWS_ROOT=/home/username/sparkflows

* Pull the latest Sparkflows docker image from Docker hub::

    docker pull sparkflows/fire:py_${SPARK_VERSION}_${RELEASE_VERSION}


* Start the docker image using the `docker run` command below. The local mount directory is ``(/home/username/sparkflows)`` in the below docker run command. Please update it to directory structure on your machine::
    
    
    docker run -p 8080:8080 -p 9443:9443 \
    -v ${SPARKFLOWS_ROOT}:/usr/local/fire-${RELEASE_VERSION}_spark_${SPARK_VERSION} \
    -e KEYSTORE_PASSWORD=12345678 \
    -e FIRE_HTTP_PORT=8080 \
    -e FIRE_HTTPS_PORT=9443 \
    -e FIRE_VERSION=${FIRE_VERSION} \
    sparkflows/fire:py_${SPARK_VERSION}_${RELEASE_VERSION}


* To add any customization to the install, please let the Sparkflows image to come up after running the previous command. Once, the Sparkflows UI is accessible from browser, one can configure Sparkflows to suit ones need by following the steps outlined in the link - https://docs.sparkflows.io/en/latest/installation/configuration/index.html. The properties files will be available in the mounted directory. ``/home/username/sparkflows`` is the mounted directory in the representative example above.

* For the ``h2db`` to be accessible on the mounted directory, please edit the path in ``conf/db.properties`` to working directory and restart docker image::
   
   spring.datasource.url = jdbc:h2:file:./firedb  (By default it would be ~/firedb)

* Open your web browser and navigate to:: 
  
    http://localhost:8080

* Login with:: 

    admin/admin or test/test

    
.. note::  Two user accounts come preconfigured with Sparkflows.

           * admin/admin
           * test/test
    
    You may change these usernames and passwords in Sparkflows as an admin under the menu Administration/Users 

Override the Keystore file
------------------------------------
* Generate the keystore.jks file and copy into the local **conf** directory, where the sparkflows has been mounted ($SPARKFLOWS_ROOT). Also update the keystore.properties file with the new password.

* Now restart the container, in order for the new keystore file to be used.::

   docker restart <container-id>


Stopping the Sparkflows docker image
------------------------------------
* Get the running container name of the Sparkflows image::

     docker ps
     
* Stop the container by::

     docker stop <container-id>


Upgrading Steps
---------------------------
* Stop the container by::

     docker stop <container-id>

* Set up the environment variables. The local mount directory is ``(/home/username/sparkflows)`` in the below docker run command. Please update it to directory structure on your machine. Replace ``XX`` with the Sparkflows version you want to install::
    
    export SPARK_VERSION=3.2.1
    export RELEASE_VERSION=3.X.XX
    export FIRE_VERSION=3.1.0
    export SPARKFLOWS_ROOT=/home/username/sparkflows

* Pull the latest Sparkflows docker image from Docker hub::

    docker pull sparkflows/fire:py_${SPARK_VERSION}_${RELEASE_VERSION}


* Upgrade the either the MySQL or the H2DB table by running the sh script::

    .\create-mysql-db.sh
    .\create-h2-db.sh

* Start the docker image using the `docker run` command below. The local mount directory is ``(/home/username/sparkflows)`` in the below docker run command. Please update it to directory structure on your machine::
    
    
    docker run -p 8080:8080 -p 9443:9443 \
    -v ${SPARKFLOWS_ROOT}:/usr/local/fire-${RELEASE_VERSION}_spark_${SPARK_VERSION} \
    -e KEYSTORE_PASSWORD=12345678 \
    -e FIRE_HTTP_PORT=8080 \
    -e FIRE_HTTPS_PORT=9443 \
    -e FIRE_VERSION=${FIRE_VERSION} \
    sparkflows/fire:py_${SPARK_VERSION}_${RELEASE_VERSION}
 
* The Sparkflows services should start and all the previous configurations and workflows should be seen in the application.
    
