Docker Image on Linux
^^^^^^^^^^^^^^^^^^^^^

Sparkflows can be installed and run on Linux (Ubuntu, CentOS, RHEL) using the Docker image from the Docker Hub.


Prerequisites
-------------

* Docker Desktop (https://docs.docker.com/engine/install/)
    * Download the Docker CE
    * Verify that the docker is up and running and the the docker version by running ``docker --version``
    

Installation Steps
---------------------------

* Pull the latest Sparkflows docker image from Docker hub::

    docker pull sparkflows/fire:py_3.2.1_3.1.0


* Start the docker image using the `docker run` command below::
    
    export SPARKFLOWS_ROOT=/home/username/sparkflows
    docker run -p 8080:8080 -p 9443:9443 -v $SPARKFLOWS_ROOT:/usr/local/fire-3.1.0_spark_3.2.1 -e KEYSTORE_PASSWORD=12345678 -e FIRE_HTTP_PORT=8080 -e FIRE_HTTPS_PORT=9443  sparkflows/fire:py_3.2.1_3.1.0
    The local mount directory is (/home/username/sparkflows) in the above docker run command. Please update it to directory structure on your machine.

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


Stopping the Sparkflows docker image
------------------------------------
* Get the running container name of the Sparkflows image::

     docker ps
     
* Stop the container by::

     docker stop image_name

    
