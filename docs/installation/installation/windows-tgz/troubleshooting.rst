Troubleshooting
===============

Find the symptom you see, run the check, and apply the fix. All commands are run in a **Command Prompt**, from the Sparkflows installation folder unless shown otherwise.

Where to Find the Logs
----------------------

All logs are in the ``log`` folder of the installation folder.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Log file
     - Contents
   * - ``log\fireserver.log``
     - The Sparkflows web server.
   * - ``log\fireserver-error.log``
     - Errors from the web server.
   * - ``log\fire_<date>.log``
     - The helper process, which runs workflows.
   * - ``log\agent_<date>.log``, ``log\polars_<date>.log``
     - The Agent and Polars engines.

To see the latest lines of a log, for example the last 50 lines of the web server error log::

    powershell -Command "Get-Content log\fireserver-error.log -Tail 50"

To ask Sparkflows support for help, send:

* The ``log`` folder.
* ``conf\version.txt``.
* The exact error message, and the steps that led to it.

Do not send the rest of the ``conf`` folder: files such as ``db.properties``, ``keystore.properties``, ``keystore.jks`` and ``aes-key.txt`` contain passwords and keys. If support asks for a configuration file, remove passwords from it first.


Sparkflows Does Not Start
-------------------------

.. list-table::
   :widths: 22 22 26 30
   :header-rows: 1

   * - Symptom
     - Likely cause
     - Check
     - Fix
   * - ``Could not create Java Virtual Machine`` when starting
     - 32-bit Java, or a Java version other than 17.
     - ``java -version`` shows version 17 and ``64-Bit``.
     - Install 64-bit JDK 17. See :doc:`prerequisites-install`.
   * - ``'java' is not recognized``, or the wrong Java version starts
     - ``JAVA_HOME`` or ``PATH`` does not point to JDK 17.
     - ``echo %JAVA_HOME%`` and ``where java``. The first ``java`` listed must be in the JDK 17 folder.
     - Fix ``JAVA_HOME`` and ``PATH``, then open a **new** Command Prompt.
   * - Port 8080 never starts listening
     - The web server failed during startup.
     - Read the latest lines of the logs: ``powershell -Command "Get-Content log\fireserver-error.log -Tail 50"``, then the same for ``log\fireserver.log``.
     - Fix the error shown in the log, then start the web server again.
   * - ``Access is denied`` or other permission errors in the logs
     - Sparkflows is in a protected folder such as ``C:\Program Files``.
     - Check the path of the installation folder.
     - Extract Sparkflows into your user folder (``%USERPROFILE%``) instead. See :doc:`windows-install`.
   * - The web server does not start because port 8080 is in use
     - Another application, or another copy of Sparkflows, is using the port.
     - See `Find What Is Using a Port`_.
     - Stop that application, or change ``http.port`` in ``conf\application.properties``. See :doc:`/installation/configuration/running-different-port`.
   * - Database errors such as ``Database may be already in use`` at startup
     - Another copy of Sparkflows is already using the H2 database (``%USERPROFILE%\firedb.mv.db``).
     - ``netstat -ano | findstr ":8080 :8081" | findstr LISTENING`` shows another Sparkflows still running.
     - Stop all Sparkflows processes, then start again.
   * - Database errors that a table is missing
     - The database tables were not created or not updated for this release.
     - Check whether ``.\create-h2-db.bat`` was run in this installation folder.
     - Stop Sparkflows, run ``.\create-h2-db.bat``, then start again.


Cannot Open Sparkflows in the Browser
-------------------------------------

.. list-table::
   :widths: 22 22 26 30
   :header-rows: 1

   * - Symptom
     - Likely cause
     - Check
     - Fix
   * - http://localhost:8080 does not load
     - The web server is still starting, or has stopped.
     - ``netstat -ano | findstr :8080 | findstr LISTENING`` shows nothing.
     - Wait a few minutes after start. If nothing is listening, see `Sparkflows Does Not Start`_.
   * - Sparkflows opens on this machine but not from other machines
     - Windows Firewall blocks port 8080, or the wrong address is used.
     - Open ``http://<hostname>:8080`` from the other machine, using this machine's host name or IP address.
     - Allow incoming connections on port 8080 in Windows Firewall.
   * - The login page opens, but workflows do not run
     - The helper process is not running.
     - ``netstat -ano | findstr :8081 | findstr LISTENING`` shows nothing.
     - Start it with ``.\run-fire.bat start``, and check ``log\fire_<date>.log``.


Workflows Fail
--------------

.. list-table::
   :widths: 22 22 26 30
   :header-rows: 1

   * - Symptom
     - Likely cause
     - Check
     - Fix
   * - ``java.io.IOException: (null) entry in command string: null chmod 0644`` when saving files
     - ``winutils.exe`` is missing or not found.
     - ``echo %HADOOP_HOME%`` shows ``C:\hadoop``, and ``where winutils`` shows ``C:\hadoop\bin\winutils.exe``.
     - Set up ``winutils.exe``. See :doc:`prerequisites-install`. Then restart Sparkflows from a new Command Prompt.
   * - ``java.lang.UnsatisfiedLinkError: org.apache.hadoop.io.nativeio.NativeIO$Windows.access0``
     - ``hadoop.dll`` is missing, not on ``PATH``, or does not match Hadoop 3.3.x. The Microsoft C Runtime may also be missing.
     - ``dir C:\hadoop\bin\hadoop.dll``, and check that ``PATH`` contains ``%HADOOP_HOME%\bin``.
     - Install ``hadoop.dll`` for Hadoop 3.3.x and the Microsoft C Runtime. See :doc:`prerequisites-install`. Then restart Sparkflows from a new Command Prompt.


Agents and Polars
-----------------

.. list-table::
   :widths: 22 22 26 30
   :header-rows: 1

   * - Symptom
     - Likely cause
     - Check
     - Fix
   * - ``error: no CPython >=3.9.2,<3.10 found.``
     - Python 3.9.2 or later (below 3.10) is not installed, or is not found.
     - ``py -3.9 --version``
     - Install 64-bit Python 3.9. If it is installed but not found, run ``.\install-fire-python.bat --python C:\path\to\python.exe``.
   * - ``error: this is a native ARM64 Python, which Fire cannot use.``
     - A native ARM64 Python is installed on Windows on ARM.
     - The error message itself.
     - Install the **x64** build of Python 3.9, for example https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe, and run ``.\install-fire-python.bat`` again, with ``--python`` if needed.
   * - ``error: dependency install failed.``
     - PyPI cannot be reached, or a package is not available for this Python version or platform.
     - Open https://pypi.org from this machine. Check that the Python used is 64-bit Python 3.9.
     - Set ``HTTP_PROXY`` and ``HTTPS_PROXY`` if a proxy is required. On machines without internet access, use ``.\install-fire-python.bat --find-links C:\path\to\wheels``. Do not install Visual Studio C++ Build Tools; they are not needed.
   * - ``ERROR: engine venv not found at engine-venv\Scripts\python.exe``
     - ``engine-venv`` has not been created in this installation folder. This is expected after an upgrade.
     - ``dir engine-venv\Scripts\python.exe``
     - Run ``.\install-fire-python.bat``, then stop and start the web server.
   * - ``ERROR: server is not listening on port 8089 after 5 seconds.`` (or 8200)
     - The engine failed to start, or another process uses the port.
     - Read the Python error printed above the message. See `Find What Is Using a Port`_.
     - Fix the error shown, or free the port.
   * - Re-running ``install-fire-python.bat``, or deleting ``engine-venv``, fails because files are in use
     - A running engine keeps files in ``engine-venv`` locked.
     - ``.\run-fire-polars.bat status`` and ``.\run-fire-agent.bat status``
     - Stop both engines with ``.\run-fire-agent.bat stop`` and ``.\run-fire-polars.bat stop``, then try again.


Upgrade Problems
----------------

.. list-table::
   :widths: 22 22 26 30
   :header-rows: 1

   * - Symptom
     - Likely cause
     - Check
     - Fix
   * - The new release does not start, or shows database errors
     - The database was not updated for the new release.
     - Check whether ``.\create-h2-db.bat`` was run in the **new** installation folder.
     - Stop Sparkflows, run ``.\create-h2-db.bat`` in the new installation folder, then start again.
   * - Settings, such as the port, are back to their defaults after the upgrade
     - The new release has its own ``conf`` folder.
     - Compare the ``conf`` folders of the old and new installation folders.
     - Make your changes again in the new ``conf`` folder.
   * - The upgrade cannot be fixed
     - —
     - —
     - Roll back to the previous release. See :doc:`windows-upgrade`.


Find What Is Using a Port
-------------------------

#. Find the process ID (PID) that is listening on the port, for example 8080. The PID is the last number on the line::

       netstat -ano | findstr :8080 | findstr LISTENING

#. Find out which program it is. Replace ``<pid>`` with the number from the previous step::

       tasklist /FI "PID eq <pid>"

#. If it is a Sparkflows process (``java.exe`` or ``python.exe`` started from the installation folder), stop it with its own script, for example ``.\run-fire-server.bat stop``. If it is another program, close that program, or change the Sparkflows port instead.

#. Only if the process cannot be stopped any other way, end it::

       taskkill /PID <pid> /F
