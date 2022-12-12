Docker Installation Steps on Windows 10
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sparkflows can be installed and run on Windows 10 using the Docker image from the Docker Hub.


Prerequisites
-------------
* Windows 10 Pro / Enterprise / Education with support for Hyper-V (https://learn.microsoft.com/en-us/virtualization/hyper-v-on-windows/reference/hyper-v-requirements)

* Enable Hyper-V on Windows if disaled by following the steps below::
    * Goto Control Panel >> Programs >> Turn Windows Features on or off >> Enable below Hyper-V features.
    
      .. figure:: ../../_assets/docker-install/hyperv.png
         :alt: Quickstart
         :width: 90%
         
    * Restart the System.
    * Once the system starts, verify whether the Hyper-V Manager is running.

* Docker Desktop (https://docs.docker.com/docker-for-windows/install/)
    * Download the Docker Desktop Installer (As of this writing, tested with version: 4.13.1)
    * Use the below Configuration ( The option should be un-checked ):
    
      .. figure:: ../../_assets/docker-install/hyperv-docker.png
         :alt: Quickstart
         :width: 90%
    * Adjust the amount of cores, memory given to Docker as seen below:
    
      .. figure:: ../../_assets/docker-install/docker-resources.png
         :alt: Quickstart
         :width: 90%
    * Verify that the docker is up and running and the the docker version by running ``docker --version``
    

Installation Steps
---------------------------

* Download/Pull the Sparkflows docker image.

* Start the docker image using the `docker run` command below::

* Open your web browser and navigate to:: 
  
    http://localhost :8080

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

    
