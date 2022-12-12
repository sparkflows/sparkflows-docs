Docker Installation on Windows 10
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sparkflows can be installed and run on Windows 10 using the Docker image from the Docker Hub.


Prerequisites
-------------
* Windows 10 Pro / Enterprise / Education with support for Hyper-V
    (https://learn.microsoft.com/en-us/virtualization/hyper-v-on-windows/reference/hyper-v-requirements)

* Enable Hyper-V on Windows if disaled by following the steps below::
    * Goto ``Control Panel`` >> ``Programs`` >> ``Turn Windows Features on or off`` >> ``Enable below Hyper-V features``.
    
      .. figure:: ../../_assets/docker-install/hyperv.png
         :alt: hyperv
         :width: 50%
         
    * Restart the System.
    * Once the system starts, verify whether the Hyper-V Manager is running.

* Docker Desktop (https://docs.docker.com/docker-for-windows/install/)
    * Download the Docker Desktop Installer (As of this writing, tested with version: ``4.13.1``)
    * Use the below Configuration (The option should be ``un-checked`` ):
    
      .. figure:: ../../_assets/docker-install/hyperv-docker.png
         :alt: hyperv-docker
         :width: 50%
    * Adjust the amount of cores, memory given to Docker as seen below:
    
      .. figure:: ../../_assets/docker-install/docker-resources.png
         :alt: docker-resources
         :width: 50%
    * Verify that the docker is up and running and the the docker version by running ``docker --version``
    

Installation Steps
---------------------------

* Pull the latest Sparkflows docker image from Docker hub::

    docker pull sparkflows/fire:py_3.2.1_3.1.0


* Start the docker image using the `docker run` command below::
    
    export SPARKFLOWS_DATA=/c/Users/sparkflows/data
    export SPARKFLOWS_ROOT=/c/Users/sparkflows/root
    export SPARKFLOWS_DB=/c/Users/sparkflows/db
    docker run -p 8080:8080 -p 9443:9443 -v $SPARKFLOWS_ROOT:/usr/local/fire-3.1.0_spark_3.2.1 -v $SPARKFLOWS_DATA:/usr/local/data -v $SPARKFLOWS_DB=/home/sparkflows -e KEYSTORE_PASSWORD=12345678 -e FIRE_HTTP_PORT=8080 -e FIRE_HTTPS_PORT=9443  sparkflows/fire:py_3.2.1_3.1.0

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

    
