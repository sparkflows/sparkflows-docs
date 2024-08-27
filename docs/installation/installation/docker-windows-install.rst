Windows Installation using Docker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

    * Goto Settings -> Shared Drive and then Share the entire Drive with Docker and click Apply.

Installation Steps
---------------------------

* Pull the latest Sparkflows docker image from Docker hub. Replace ``XX`` with the Sparkflows version you want to install::

    docker pull sparkflows/fire:py_3.2.1_3.X.XX
   
* Start the docker image using the `docker run` command below. The local mount directory is ``(C:\Users\sparkflows)`` in the below docker run command. Please update it to directory structure on your machine. Replace ``XX`` with the Sparkflows version you want to install. Reduce/Increase the memory allocated (Eg: Using ``-m 8g`` will allocate 8GB to the Sparkflows container) to a lower value depending on the RAM on the machine. We recommend 16GB or above::
    
    docker run -m 16g -p 8080:8080 -p 8443:8443 -v  C:\Users\sparkflows:/usr/local/fire-3.X.XX_spark_3.2.1 -e FIRE_VERSION=3.1.0 -e KEYSTORE_PASSWORD=12345678 -e FIRE_HTTP_PORT=8080 -e FIRE_HTTPS_PORT=8443  sparkflows/fire:py_3.2.1_3.X.XX

* To add any customization to the install, please let the Sparkflows image to come up after running the previous command. Once, the Sparkflows UI is accessible from browser, one can configure Sparkflows to suit ones need by following the steps outlined in the link - https://docs.sparkflows.io/en/latest/installation/configuration/index.html. The properties files will be available in the mounted directory. ``/home/username/sparkflows`` is the mounted directory in the representative example above.

* In order to use MySQL database as the datastore, pass the db configuration as environment variable as shown below. Reduce/Increase the memory allocated (Eg: Using ``-m 8g`` will allocate 8GB to the Sparkflows container) to a lower value depending on the RAM on the machine. We recommend 16GB or above::

    docker run -m 16g -p 8080:8080 -p 8443:8443 -v  C:\Users\sparkflows:/usr/local/fire-3.X.XX_spark_3.2.1 \
    -e FIRE_VERSION=3.1.0 \
    -e KEYSTORE_PASSWORD=12345678 \
    -e FIRE_HTTP_PORT=8080 \
    -e FIRE_HTTPS_PORT=8443 \
    -e DB_HOST=sparkflows-db.abc.rds.amazonaws.com \
    -e DB_PASSWORD=DB123 \
    -e DB_USERNAME=sparkflows \
    -e DB_PORT=3306 \
    sparkflows/fire:py_3.2.1_3.X.XX

* For the ``h2db`` to be accessible on the mounted directory, please edit the path in ``conf/db.properties`` to working directory and restart docker image::
   
   spring.datasource.url = jdbc:h2:file:./firedb  (By default it would be ~/firedb)

* Open your web browser and navigate to:: 
  
    http://localhost:8080

* Login with:: 

    admin/admin or test/test

    
.. note::  Two user accounts come preconfigured with Sparkflows.

           * admin/admin
           * test/test
    
    You may change the default passwords in Sparkflows from User Profile or Create new users using Menu Administration/Users. 


Stopping the Sparkflows docker image
------------------------------------
* Get the running container name of the Sparkflows image::

     docker ps
     
* Stop the container by::

     docker stop image_name
     

Upgrading Steps
---------------------------
* Stop the container by::

     docker stop image_name

* Pull the latest Sparkflows docker image from Docker hub. Replace ``XX`` with the Sparkflows version you want to install::

    docker pull sparkflows/fire:py_3.2.1_3.X.XX

* Upgrade the either the MySQL or the H2DB table by running the BAT script::

    .\create-mysql-db.bat
    .\create-h2-db.bat
    
* Start the docker image using the `docker run` command below. The local mount directory is ``(C:\Users\sparkflows)`` in the below docker run command. Please update it to directory structure on your machine. Replace ``XX`` with the Sparkflows version you want to install::
    
    docker run -p 8080:8080 -p 8443:8443 -v  C:\Users\sparkflows:/usr/local/fire-3.X.XX_spark_3.2.1 -e FIRE_VERSION=3.1.0 -e KEYSTORE_PASSWORD=12345678 -e FIRE_HTTP_PORT=8080 -e FIRE_HTTPS_PORT=8443  sparkflows/fire:py_3.2.1_3.X.XX

* The Sparkflows services should start and all the previous configurations and workflows should be seen in the application.

    
