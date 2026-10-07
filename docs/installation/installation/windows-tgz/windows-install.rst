Installation
============

Install Sparkflows from the TGZ package, start it, check that it works, and secure it. Complete :doc:`prerequisites-install` first.

All commands on this page are run in a **Command Prompt**, from the Sparkflows installation folder.

Sparkflows Processes
--------------------

A Sparkflows installation on Windows runs these processes:

.. list-table::
   :widths: 24 26 14 36
   :header-rows: 1

   * - Process
     - Script
     - Default port
     - Required?
   * - Sparkflows web server
     - ``run-fire-server.bat``
     - 8080
     - Yes
   * - Sparkflows helper process
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


Step 1 : Download and Extract Sparkflows
----------------------------------------

#. Download the Sparkflows TGZ file from https://www.sparkflows.io/download.

#. Extract it into a folder that your Windows user can write to, such as your user folder (``%USERPROFILE%``, for example ``C:\Users\<user>``). This creates a folder such as ``C:\Users\<user>\fire-3.X.Y_spark_3.5.2``, the **installation folder**.

   .. warning:: Do not extract Sparkflows into ``C:\Program Files`` or another protected folder. Sparkflows writes logs and files into its installation folder, and fails with permission errors there.

   Windows 10 and 11 can extract the file from a Command Prompt::

       cd %USERPROFILE%
       tar -xzf fire-3.X.Y_spark_3.5.2.tgz

   You can also use a tool such as `7-Zip <https://www.7-zip.org/download.html>`_.

#. Go to the installation folder::

       cd %USERPROFILE%\fire-3.X.Y_spark_3.5.2

#. Note the installed version. ``releaseVersion`` in this file is the Sparkflows version::

       type conf\version.txt


Step 2 : Set Up the Database
----------------------------

Sparkflows stores its users, projects and workflows in a database.

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - Database
     - When to use it
     - Where the data is
   * - H2 (default)
     - Evaluation, development and single-user use. No setup beyond the command below.
     - ``%USERPROFILE%\firedb.mv.db`` (and ``firedb.trace.db``)
   * - MySQL or PostgreSQL
     - Teams and production use, where the database is managed and backed up separately.
     - On your database server. See :doc:`/installation/configuration/database/index`.

.. note:: **For production use**, set up MySQL or PostgreSQL now: complete :doc:`/installation/configuration/database/index`, then continue with `Step 3 : Start Sparkflows`_. Do not start Sparkflows on H2 and move to another database later.

To use H2, create the database::

    .\create-h2-db.bat

The command creates the database tables, or updates them if the database already exists.

To use MySQL or PostgreSQL, configure ``conf\db.properties`` as described in :doc:`/installation/configuration/database/index`, then run ``.\create-mysql-db.bat`` or ``.\create-postgres-db.bat`` instead.

Back up the database before changing the database configuration later. See :doc:`windows-upgrade` for the files to back up.


Step 3 : Start Sparkflows
-------------------------

#. Start the Sparkflows web server::

       .\run-fire-server.bat start

   If Python 3.9 is installed, this command can also build the Python environment for the Polars and Agent engines the first time it runs. That takes a few minutes. Either way, the web server starts. To set up Agents and Polars, follow `Step 6 : Enable Agents and Polars (Optional)`_.

#. Start the Sparkflows helper process, which runs workflows::

       .\run-fire.bat start

The web server uses the ports set in ``conf\application.properties`` (``http.port=8080`` and ``https.port=8443``). To use other ports, change them there before starting Sparkflows. See :doc:`/installation/configuration/running-different-port`.


Step 4 : Verify Sparkflows Is Running
-------------------------------------

#. Check that both processes are listening on their ports::

       netstat -ano | findstr ":8080 :8081" | findstr LISTENING

   Both ``:8080`` and ``:8081`` should be listed. It can take a few minutes after start for port 8080 to appear.

#. Check the web server log, ``log\fireserver.log`` in the installation folder. Errors are in ``log\fireserver-error.log``::

       type log\fireserver.log

#. Open http://localhost:8080 in your browser. Sparkflows is ready when the login page loads.

   To open Sparkflows from another machine, use ``http://<hostname>:8080``, where ``<hostname>`` is the host name or IP address of this machine. Windows Firewall must allow incoming connections on port 8080.

   .. note:: HTTP is not encrypted. Before you make Sparkflows available beyond a trusted internal network, set up HTTPS with a trusted certificate. See :doc:`/installation/configuration/https/index`.

If a check fails, see :doc:`troubleshooting`.


Step 5 : Log In and Secure Sparkflows
-------------------------------------

#. Log in with the default user ``admin`` / ``admin``.
#. **Change the default password right away**: open the user menu at the top right, then **User Profile -> Change Password**.

.. warning:: Change the ``admin`` password before other people can reach this machine, and before you allow access to port 8080 through Windows Firewall. Anyone who can reach the port can try the default login.

New users can be added under **Administration -> Users**.


Step 6 : Enable Agents and Polars (Optional)
--------------------------------------------

Agents and Polars jobs run on two engines that use a Python environment, ``engine-venv``, in the installation folder. This needs Python 3.9; see :doc:`prerequisites-install`.

#. **Create the Python environment.** Run this from the installation folder. If ``engine-venv`` already exists, the script recreates it::

       .\install-fire-python.bat

   The script finds Python 3.9, creates ``engine-venv``, installs the required packages and checks them. It prints ``Done.`` when it completes. It needs internet access to PyPI.

   .. list-table::
      :widths: 30 70
      :header-rows: 1

      * - Option
        - Description
      * - ``--python PATH``
        - The Python 3.9 ``python.exe`` to use, if it is not found automatically. For example: ``.\install-fire-python.bat --python C:\Python39\python.exe``
      * - ``--find-links PATH``
        - Install from a local folder of wheel files instead of PyPI, on machines without internet access.
      * - ``--keep``
        - Reuse the existing ``engine-venv`` instead of recreating it.
      * - ``--dir PATH``
        - The Sparkflows installation folder. Defaults to the folder of the script.

   Running the script again deletes and recreates ``engine-venv``, unless ``--keep`` is used. Stop the Polars and Agent engines first.

#. **Start the engines**, after the web server is running::

       .\run-fire-polars.bat start
       .\run-fire-agent.bat start

   Each script prints ``Server started (pid <pid>)`` when its engine is running.

#. **Verify the engines**::

       .\run-fire-polars.bat status
       .\run-fire-agent.bat status

   Each prints ``Running on port <port>``. Engine logs are in the ``log`` folder, for example ``log\agent_<date>.log``.


Start, Stop and Status
----------------------

Run these from the installation folder.

.. list-table::
   :widths: 22 26 26 26
   :header-rows: 1

   * - Process
     - Start
     - Stop
     - Status
   * - Web server
     - ``.\run-fire-server.bat start``
     - ``.\run-fire-server.bat stop``
     - ``netstat -ano | findstr :8080``
   * - Helper process
     - ``.\run-fire.bat start``
     - ``.\run-fire.bat stop``
     - ``netstat -ano | findstr :8081``
   * - Polars engine
     - ``.\run-fire-polars.bat start``
     - ``.\run-fire-polars.bat stop``
     - ``.\run-fire-polars.bat status``
   * - Agent engine
     - ``.\run-fire-agent.bat start``
     - ``.\run-fire-agent.bat stop``
     - ``.\run-fire-agent.bat status``

To restart a process, stop it, then start it again.

To stop all of Sparkflows, stop the engines first, then the helper process and the web server::

    .\run-fire-agent.bat stop
    .\run-fire-polars.bat stop
    .\run-fire.bat stop
    .\run-fire-server.bat stop

Next, see :doc:`windows-upgrade` to upgrade and back up, or :doc:`troubleshooting` if something does not work.
