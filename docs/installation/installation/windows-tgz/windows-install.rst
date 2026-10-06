Installation
^^^^^^^^^^^^

Sparkflows can be installed to run independently on Windows.

A Sparkflows installation on Windows runs the following processes:

.. list-table::
   :widths: 25 25 15 35
   :header-rows: 1

   * - Process
     - Script
     - Default port
     - Required?
   * - Fire Server (web UI)
     - ``run-fire-server.bat``
     - 8080
     - Yes
   * - Fire helper process
     - ``run-fire.bat``
     - 8081
     - Yes
   * - Polars engine
     - ``run-fire-polars.bat``
     - 8089
     - Only to run Polars jobs
   * - Agent engine
     - ``run-fire-agent.bat``
     - 8200
     - Only to run Agents

All commands below are run from the Sparkflows install directory (for example ``C:\Users\<user>\fire-3.X.Y_spark_3.5.2``) in a Command Prompt.


Installation Steps of Sparkflows with H2 DB
-------------------------------------------

* Download the fire tgz file from:

  * https://www.sparkflows.io/download

* Unpack the downloaded tgz file. Below are some tools which can be used for it::

    WinRar : https://www.rarlab.com/download.htm
    WinZip : https://www.winzip.com
    7-Zip : https://www.7-zip.org/download.html

* Create H2 DB::

    cd <fire install_dir>
    .\create-h2-db.bat

* Launch Fire Server::

    cd <fire install_dir>
    .\run-fire-server.bat start

  .. note::  To verify whether the Fire Server is running, you can navigate to the fire home directory in your File Explorer.
             Find the log folder. In the log folder, open fireserver or fireserver.log to see the logs from the server.

* Launch the Fire helper process. It executes workflows and must be running alongside the Fire Server::

    .\run-fire.bat start

* Open your web browser and navigate to::

    <machine_name>:8080

* Login with::

    admin/admin

.. note::  Admin user account comes preconfigured with Sparkflows.

           * admin/admin

           You may change these usernames and passwords in Fire under the menu Administration/Users.


Running Agents and Polars Jobs
-----------------------------------------

To run Agents and Polars jobs, start the Agent and Polars engines. Both engines run out of a single Python virtual environment (``engine-venv``) inside the Sparkflows install directory, which has to be created once before the engines can start.

Python Prerequisites
++++++++++++++++++++

* **Python 3.9** (64-bit), version 3.9.2 or later within 3.9.x. Python 3.9.0, 3.9.1 and 3.10 or later are not supported.

  * Download Python 3.9 from https://www.python.org/downloads/windows/ (for example, `Python 3.9.13 64-bit <https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe>`_).

* Internet access to download the Python packages from PyPI. For offline installs, see the ``--find-links`` option below.

.. note:: Visual Studio C++ Build Tools and Windows Developer Mode are **not** required.

Step 1 : Create the engine virtual environment
++++++++++++++++++++++++++++++++++++++++++++++

Run the below from the Sparkflows install directory::

    .\install-fire-python.bat

The script finds a supported Python 3.9 interpreter, creates the ``engine-venv`` folder in the install directory, installs the required packages and verifies the installation. When it completes, it prints ``Done.``

The script accepts the following options:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Option
     - Description
   * - ``--python PATH``
     - Path to the Python 3.9 ``python.exe`` to use, if it is not detected automatically. For example: ``.\install-fire-python.bat --python C:\Python39\python.exe``
   * - ``--find-links PATH``
     - Install from a local folder of wheel files instead of PyPI (offline install).
   * - ``--keep``
     - Reuse an existing ``engine-venv`` instead of recreating it.
   * - ``--dir PATH``
     - Sparkflows install directory. Defaults to the directory of the script.

.. note:: Running the script again deletes and recreates ``engine-venv``, unless ``--keep`` is passed. Stop the Polars and Agent engines before re-running it, since a running engine keeps files in ``engine-venv`` locked.

Step 2 : Start the Polars engine
++++++++++++++++++++++++++++++++

::

    .\run-fire-polars.bat start

The Polars engine starts on port 8089 by default. To use a different port, pass it after ``start``, for example ``.\run-fire-polars.bat start 8090``.

Step 3 : Start the Agent engine
+++++++++++++++++++++++++++++++

::

    .\run-fire-agent.bat start

The Agent engine starts on port 8200 by default. To use a different port, pass it after ``start``, for example ``.\run-fire-agent.bat start 8201``.

Each script prints ``Server started (pid <pid>)`` once the engine is listening on its port. If it reports ``ERROR: engine venv not found``, run Step 1 first.

Check the engine status
+++++++++++++++++++++++

::

    .\run-fire-polars.bat status
    .\run-fire-agent.bat status

Both scripts also accept ``restart``.


Stopping Sparkflows
-------------------

Stop the processes with the below. The Polars and Agent engines only need to be stopped if they were started::

    .\run-fire-agent.bat stop
    .\run-fire-polars.bat stop
    .\run-fire.bat stop
    .\run-fire-server.bat stop


.. note::  On Windows, the PySpark engine will not get installed. Below are the functionalities that will not be available on bare metal windows install. We recommend either docker on windows to access all functionalities or install Sparkflows on Linux.

           * AutoML
           * Prophet
           * ARIMA
           * Scikit learn models
           * Keras/Tensorflow models
           * A few other python native packages.
