Windows Installation using Docker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sparkflows can be installed and run on Windows 10 using the Docker image from the Docker Hub.


Prerequisites
-------------
* Windows 10 Pro / Enterprise / Education with support for Hyper-V
    (https://learn.microsoft.com/en-us/virtualization/hyper-v-on-windows/reference/hyper-v-requirements)

* Enable Hyper-V on Windows if disabled by following the steps below::
    * Go to **Control Panel >> Programs >> Turn Windows Features on or off >> Enable below Hyper-V features**.
    
      .. figure:: ../../_assets/docker-install/hyperv.png
         :alt: hyperv
         :width: 50%
         
    * Restart the System.
    * Once the system starts, verify whether the Hyper-V Manager is running.

* Docker Desktop (https://docs.docker.com/docker-for-windows/install/)
    * Download the Docker Desktop Installer (As of this writing, tested with version: **4.13.1**)
    * Use the below Configuration (The option should be **un-checked** ):
    
      .. figure:: ../../_assets/docker-install/hyperv-docker.png
         :alt: hyperv-docker
         :width: 50%
    * Adjust the amount of cores, memory given to Docker as seen below:
    
      .. figure:: ../../_assets/docker-install/docker-resources.png
         :alt: docker-resources
         :width: 50%
    * Verify that the docker is up and running and the docker version by running **docker --version**.

    * Go to **Settings -> Shared Drive**, then share the entire Drive with Docker and click Apply.

* About 20 GB of free disk space. The Sparkflows image is about 10.5 GB, and the application unpacks another 3.3 GB inside the container.

* Ports 8080 (HTTP) and 8443 (HTTPS) free on the machine.


Installation Steps
---------------------------

* Pull the latest Sparkflows docker image from Docker hub. Replace ``XX`` with the Sparkflows version you want to install. The download takes several minutes::

    docker pull sparkflows/fire:py_3.5.2_3.X.XX

* Start the container using the **docker run** command below (PowerShell syntax; each line ends with a space, then a backtick). Replace ``XX`` with the Sparkflows version you want to install. Reduce/Increase the memory allocated (Eg: Using ``-m 8g`` will allocate 8GB to the Sparkflows container) depending on the RAM on the machine. We recommend 16GB or above::

    docker run -d --name sparkflows -m 16g `
      -p 8080:8080 -p 8443:8443 `
      -v sparkflows-data:/root `
      -e KEYSTORE_PASSWORD=12345678 `
      -e FIRE_HTTP_PORT=8080 `
      -e FIRE_HTTPS_PORT=8443 `
      -e DB=h2 `
      sparkflows/fire:py_3.5.2_3.X.XX

  ``-v sparkflows-data:/root`` stores the Sparkflows data, including the H2 database (``/root/firedb.mv.db``), in a Docker volume named ``sparkflows-data``. The data is kept when the container is removed or upgraded.

  .. note:: Running ``docker volume rm sparkflows-data`` deletes all your Sparkflows data.

* To use other ports, change both the ``-p`` values and ``FIRE_HTTP_PORT`` / ``FIRE_HTTPS_PORT`` to match. For example: ``-p 9090:9090 -p 9443:9443 -e FIRE_HTTP_PORT=9090 -e FIRE_HTTPS_PORT=9443``.

* In order to use MySQL database as the datastore, pass the db configuration as environment variables as shown below::

    docker run -d --name sparkflows -m 16g `
      -p 8080:8080 -p 8443:8443 `
      -v sparkflows-data:/root `
      -e KEYSTORE_PASSWORD=12345678 `
      -e FIRE_HTTP_PORT=8080 `
      -e FIRE_HTTPS_PORT=8443 `
      -e DB=mysql `
      -e DB_HOST=sparkflows-db.abc.rds.amazonaws.com `
      -e DB_PASSWORD=DB123 `
      -e DB_USERNAME=sparkflows `
      -e DB_PORT=3306 `
      sparkflows/fire:py_3.5.2_3.X.XX

* Wait for Sparkflows to start. Follow the container logs with::

    docker logs -f sparkflows

  Sparkflows is ready when the logs show ``Started oejs.Server``, about 2-3 minutes after starting. Press **Ctrl+C** to stop following the logs; the container keeps running.

* Open your web browser and navigate to::

    http://localhost:8080

* Login with::

    admin/admin, analyst/analyst or business/business

.. note::  Admin user account comes preconfigured with Sparkflows.

           * admin/admin

           You may change the default passwords in Sparkflows from User Profile -> Change Password, or create new users using Menu Administration/Users.

* To add any customization to the install, configure Sparkflows by following the steps outlined in the link - https://docs.sparkflows.io/en/latest/installation/configuration/index.html.


Stopping the Sparkflows docker image
------------------------------------
* Stop the container by::

     docker stop sparkflows

* Start it again by::

     docker start sparkflows


Upgrading Steps
---------------------------
* Pull the new Sparkflows docker image from Docker hub. Replace ``XX`` with the Sparkflows version you want to upgrade to::

    docker pull sparkflows/fire:py_3.5.2_3.X.XX

* Remove the existing container. The data in the ``sparkflows-data`` volume is kept::

    docker rm -f sparkflows

* Start the new container by running the same **docker run** command used during installation, with the new image tag.

* The Sparkflows services should start and all the previous configurations and workflows should be seen in the application.
