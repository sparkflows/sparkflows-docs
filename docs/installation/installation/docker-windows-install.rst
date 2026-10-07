Windows Installation using Docker
=================================

Run Sparkflows on Windows in a Docker container, using the Sparkflows image from Docker Hub.

Before You Install
------------------

* **Who this is for:** anyone who wants the full Sparkflows feature set on a Windows machine. Unlike the bare-metal Windows install, the Docker image includes the PySpark engine, so AutoML, Prophet, ARIMA, Scikit-learn and Keras/TensorFlow models are available.
* **How long it takes:** downloading the image (a 4 GB download) takes from a few minutes to over an hour, depending on your internet connection. Starting Sparkflows then takes 2-4 minutes.
* **What you will do:** install Docker Desktop, download the Sparkflows image, start a container, and log in from your browser.

All commands on this page are for **Windows PowerShell**. In PowerShell, a long command can be split over several lines by ending each line with a space followed by a backtick (`````).


Docker Requirements
-------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Requirement
     - Details
   * - Windows
     - A 64-bit version of Windows supported by Docker Desktop. See the `Docker Desktop for Windows system requirements <https://docs.docker.com/desktop/setup/install/windows-install/>`_.
   * - Memory
     - 16 GB RAM or more on the machine. The Sparkflows container needs at least 8 GB; 16 GB is recommended.
   * - Disk space
     - About 20 GB free. The image is a 4 GB download that takes about 10.5 GB on disk once Docker extracts it. When the container starts, Sparkflows unpacks another 3.3 GB inside it.
   * - Ports
     - 8080 (HTTP) and 8443 (HTTPS) free on the machine, or two other free ports.
   * - Internet access
     - To download Docker Desktop and the Sparkflows image.


Step 1 : Install Docker Desktop
-------------------------------

#. Download and install Docker Desktop for Windows from https://docs.docker.com/desktop/setup/install/windows-install/. Follow the steps on that page; it covers enabling WSL 2 or Hyper-V, which Docker Desktop needs.
#. Start **Docker Desktop**, and wait until it shows that the Docker engine is running.


Step 2 : Verify Docker
----------------------

Open PowerShell and run::

    docker version

The output should have both a **Client** and a **Server** section. If it shows an error such as ``error during connect``, Docker Desktop is not running yet; start it and try again.


Step 3 : Download the Sparkflows Image
--------------------------------------

Download the image from Docker Hub::

    docker pull sparkflows/fire:py_3.5.2_3.X.XX

Replace ``3.X.XX`` with the Sparkflows version to install, for example ``sparkflows/fire:py_3.5.2_3.3.42``. The available versions are listed under **Tags** at https://hub.docker.com/r/sparkflows/fire/tags. In ``py_3.5.2_3.3.42``, ``3.5.2`` is the Spark version and ``3.3.42`` is the Sparkflows version.

The download is about 4 GB, and the image takes about 10.5 GB on disk once Docker extracts it. Depending on your internet connection, the download takes from a few minutes to over an hour.


Step 4 : Start Sparkflows
-------------------------

Start the Sparkflows container. Replace ``3.X.XX`` with the version you downloaded::

    docker run -d --name sparkflows -m 16g `
      -p 8080:8080 -p 8443:8443 `
      -v sparkflows-data:/root `
      -e KEYSTORE_PASSWORD=12345678 `
      -e FIRE_HTTP_PORT=8080 `
      -e FIRE_HTTPS_PORT=8443 `
      -e DB=h2 `
      sparkflows/fire:py_3.5.2_3.X.XX

What each option does:

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Option
     - Meaning
   * - ``-d --name sparkflows``
     - Runs the container in the background, and names it ``sparkflows``. The other commands on this page use this name.
   * - ``-m 16g``
     - Gives the container up to 16 GB of memory. Use ``-m 8g`` on a machine with less RAM; 8 GB is the minimum.
   * - ``-p 8080:8080``
     - Makes the Sparkflows web UI available over **HTTP** on port 8080 of your machine.
   * - ``-p 8443:8443``
     - Makes the Sparkflows web UI available over **HTTPS** on port 8443 of your machine.
   * - ``-v sparkflows-data:/root``
     - Stores the Sparkflows data, including the H2 database (``/root/firedb.mv.db``), in a Docker volume named ``sparkflows-data``. The volume is kept when the container is removed or upgraded, so your projects and settings are not lost.
   * - ``KEYSTORE_PASSWORD``
     - Password of the HTTPS keystore included in the image. Use ``12345678``.
   * - ``FIRE_HTTP_PORT`` / ``FIRE_HTTPS_PORT``
     - The ports Sparkflows listens on inside the container. They must match the ``-p`` values.
   * - ``DB=h2``
     - Uses the embedded H2 database. See `Choose the Database`_.

Use other ports
+++++++++++++++

If port 8080 or 8443 is already in use, change both the ``-p`` values and ``FIRE_HTTP_PORT`` / ``FIRE_HTTPS_PORT`` to the same new ports. For example, for ports 9090 and 9443::

    -p 9090:9090 -p 9443:9443 `
    -e FIRE_HTTP_PORT=9090 `
    -e FIRE_HTTPS_PORT=9443 `

Then open Sparkflows on the new HTTP port, for example http://localhost:9090.

Choose the Database
+++++++++++++++++++

.. list-table::
   :widths: 15 45 40
   :header-rows: 1

   * - Database
     - When to use it
     - Setup
   * - H2 (``DB=h2``)
     - Evaluation, development and single-user use. This is the default.
     - None. H2 runs inside the container, and its data is stored in the ``sparkflows-data`` volume.
   * - MySQL (``DB=mysql``)
     - Teams and production use, where the database is managed and backed up separately.
     - An existing MySQL server, with an empty database named ``firedb``.

To use MySQL:

#. Create an empty database named ``firedb`` on the MySQL server. Sparkflows always uses this database name::

       CREATE DATABASE firedb;

#. Start the container with the MySQL settings below instead of ``-e DB=h2``. Replace the example values for ``DB_HOST``, ``DB_PORT``, ``DB_USERNAME`` and ``DB_PASSWORD`` with the details of your MySQL server. ``host.docker.internal`` is the address of the Windows machine as seen from the container, so keep it if MySQL runs on the same machine::

    docker run -d --name sparkflows -m 16g `
      -p 8080:8080 -p 8443:8443 `
      -v sparkflows-data:/root `
      -e KEYSTORE_PASSWORD=12345678 `
      -e FIRE_HTTP_PORT=8080 `
      -e FIRE_HTTPS_PORT=8443 `
      -e DB=mysql `
      -e DB_HOST="host.docker.internal" `
      -e DB_PORT=3306 `
      -e DB_USERNAME="sparkflows" `
      -e DB_PASSWORD="your-mysql-password" `
      sparkflows/fire:py_3.5.2_3.X.XX


Step 5 : Verify Sparkflows Is Running
-------------------------------------

#. Check that the container is running::

       docker ps

   The ``sparkflows`` container should be listed with the status **Up**. If it is not listed, run ``docker ps -a`` to see whether it stopped, then see `Docker Troubleshooting`_.

#. Follow the container logs::

       docker logs -f sparkflows

   Sparkflows is starting when the logs show ``Started oejs.Server``, about 2-4 minutes after the container starts. Press **Ctrl+C** to stop following the logs; the container keeps running.

#. Sparkflows is ready when its login page loads in your browser. See `Step 6 : Log In`_ for the addresses to open.


Step 6 : Log In
---------------

#. Open Sparkflows in your browser:

   * Over HTTP: http://localhost:8080
   * Over HTTPS: https://localhost:8443. The image includes its own certificate, which browsers do not recognize, so the browser shows a security warning the first time. Continue to the site to open Sparkflows.

   If Sparkflows runs on another machine, use that machine's host name or IP address instead of ``localhost``.
#. Log in with the default user ``admin`` / ``admin``.
#. Change the default password right away: open the user menu at the top right, then **User Profile -> Change Password**.

.. note:: Anyone who can reach the Sparkflows port can try the default login, so change the password before sharing the machine or opening the port on a network.

New users can be added under **Administration -> Users**.


Step 7 : Configure Sparkflows
-----------------------------

To customize Sparkflows, for example connections, authentication or engines, follow :doc:`/installation/configuration/index`.


Stop and Start
--------------

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Command
     - What it does
   * - ``docker stop sparkflows``
     - Stops Sparkflows. Your data in the ``sparkflows-data`` volume is kept.
   * - ``docker start sparkflows``
     - Starts Sparkflows again. Wait for the login page to load, as in `Step 5 : Verify Sparkflows Is Running`_.

You only need to remove the container (``docker rm -f sparkflows``) and run ``docker run`` again when you change the image version or the container settings, such as ports or the database. Your data in the volume is kept.


Upgrade the Sparkflows Container
--------------------------------

Your data is kept during an upgrade because the new container uses the same ``sparkflows-data`` volume. Back up your data first; see `Back Up Your Data`_.

#. Download the new image. Replace ``3.X.XX`` with the new version::

       docker pull sparkflows/fire:py_3.5.2_3.X.XX

#. Remove the existing container. This removes only the container, not the ``sparkflows-data`` volume::

       docker rm -f sparkflows

#. Start a new container with the same ``docker run`` command as in `Step 4 : Start Sparkflows`_, using the new image tag.

#. Verify the upgrade as in `Step 5 : Verify Sparkflows Is Running`_. Your previous projects, workflows and settings are available after you log in.


Back Up Your Data
-----------------

With the H2 database, all Sparkflows data is in the ``sparkflows-data`` volume. To save it to ``sparkflows-backup.tgz`` in the current folder, stop the container, copy the volume to a file, then start Sparkflows again. Replace ``3.X.XX`` with the version you are running::

    docker stop sparkflows
    docker run --rm -v sparkflows-data:/root -v "${PWD}:/backup" `
      --entrypoint tar sparkflows/fire:py_3.5.2_3.X.XX `
      czf /backup/sparkflows-backup.tgz -C /root .
    docker start sparkflows

With MySQL, also back up the MySQL database with your usual MySQL backup tools.


Uninstall
---------

#. Remove the container::

       docker rm -f sparkflows

#. Remove the image. Replace ``3.X.XX`` with the version you downloaded::

       docker rmi sparkflows/fire:py_3.5.2_3.X.XX

#. Optionally, remove the data volume.

   .. warning:: This permanently deletes all your Sparkflows data, including projects, workflows and users. Back up your data first if you may need it.

   ::

       docker volume rm sparkflows-data


Docker Troubleshooting
----------------------

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Problem
     - Solution
   * - ``error during connect`` when running a ``docker`` command
     - Docker Desktop is not running. Start it, wait until the engine is running, and run the command again.
   * - ``The term '-e' is not recognized`` (or another option) when running ``docker run``
     - A line of the multi-line command has a character, usually a space, after the backtick (`````). Make sure each line ends with a space, then a backtick, with nothing after it.
   * - ``invalid containerPort``, ``invalid reference format`` or a similar error when running ``docker run``
     - A line of the multi-line command is missing the space before the backtick, so the line break becomes part of a value. Add a space before each backtick.
   * - ``port is already allocated`` or ``Bind for 0.0.0.0:8080 failed``
     - Another application, or another Sparkflows container, is using the port. Stop it, or use other ports as described in `Use other ports`_.
   * - ``Conflict. The container name "/sparkflows" is already in use``
     - A container named ``sparkflows`` already exists. Start it with ``docker start sparkflows``, or remove it with ``docker rm -f sparkflows`` and run ``docker run`` again. Your data in the volume is kept.
   * - The container is not listed by ``docker ps``
     - It has stopped. Run ``docker logs sparkflows`` to see why. If the machine is short of memory, close other applications or lower ``-m`` to ``8g``.
   * - The browser cannot open http://localhost:8080
     - Sparkflows may still be starting; wait a few minutes and try again.
   * - The logs show ``Unknown database 'firedb'``
     - With ``DB=mysql``, create a database named ``firedb`` on the MySQL server, then remove the container and run ``docker run`` again.
