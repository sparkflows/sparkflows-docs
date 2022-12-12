Docker Installation Steps on Linux
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sparkflows can be installed and run on Linux (Ubuntu, CentOS) using the Docker image from the Docker Hub.


Prerequisites
-------------

* Docker Desktop (https://docs.docker.com/engine/install/)
    * Download the Docker CE
    * Verify that the docker is up and running and the the docker version by running ``docker --version``
    

Installation Steps
---------------------------

* Pull the latest Sparkflows docker image from Docker hub::

    docker pull sparkflows/fire:xx.yy


* Start the docker image using the `docker run` command below::
    
    docker run -p 8080:8080 -p 9443:9443 -v $SPARKFLOWS_DATA:/usr/local/fire-xx.yy -v $SPARKFLOWS_DB:/root -e KEYSTORE_PASSWORD=12345678 -e FIRE_HTTP_PORT=8080 -e FIRE_HTTPS_PORT=9443  sparkflows/fire:xx.yy

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

    
