Troubleshooting
^^^^^^^^^^^^^^^

Could not create Java Virtual Machine
+++++++++++++++++++++++++++++++++++++

**Problem**

When starting the fire server, running into the error "Could not create Java Virtual Machine".

**Solution**

This problem can be because ::

  * JDK 32 bit instead of 64 bit
  * OR Java 17 is not installed. Some other version of Java is installed.

Running into an exception when saving files
+++++++++++++++++++++++++++++++++++++++++++

**Problem**

org.apache.spark.SparkException: Job aborted due to stage failure: Task 1 in stage 33.0 failed 1 times, most recent failure: Lost task 1.0 in stage 33.0 (TID 131, localhost): java.io.IOException: (null) entry in command string: null chmod 0644 

**Solution**

If you run into an exception like above, then there is problem with the setup of ``winutils.exe``.


UnsatisfiedLinkError on NativeIO$Windows.access0
++++++++++++++++++++++++++++++++++++++++++++++++

**Problem**

Running a workflow fails with::

  java.lang.UnsatisfiedLinkError: org.apache.hadoop.io.nativeio.NativeIO$Windows.access0

**Solution**

``hadoop.dll`` is missing or does not match the Hadoop version. Download the matching ``hadoop.dll``, copy it to ``C:\hadoop\bin`` and ``C:\Windows\System32``, and restart the system. See :doc:`prerequisites-install`.

Port 8080 is already in use
+++++++++++++++++++++++++++

**Problem**

The Fire Server does not come up because another application is already using port 8080.

**Solution**

Find the process using the port::

  netstat -ano | findstr :8080

Stop that process, or start the Fire Server on a different port and open that port in the browser::

  .\run-fire-server.bat start 9090

No supported Python found when running install-fire-python.bat
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

**Problem**

``install-fire-python.bat`` fails with::

  error: no CPython >=3.9.2,<3.10 found.

**Solution**

The Agent and Polars engines need 64-bit Python 3.9, version 3.9.2 or later. Python 3.9.0, 3.9.1 and 3.10 or later are not accepted.

* Install Python 3.9 from https://www.python.org/downloads/windows/ and run the script again.
* If Python 3.9 is installed but not detected, pass its path explicitly::

    .\install-fire-python.bat --python C:\path\to\python.exe

Native ARM64 Python is not supported
++++++++++++++++++++++++++++++++++++

**Problem**

On a Windows on ARM machine, ``install-fire-python.bat`` fails with::

  error: this is a native ARM64 Python, which Fire cannot use.

**Solution**

Install the **x64** build of Python 3.9 (for example, https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe). Windows on ARM runs it under the built-in emulation, and the install works normally. Then run ``install-fire-python.bat`` again, passing the x64 interpreter with ``--python`` if needed.

Dependency install fails in install-fire-python.bat
+++++++++++++++++++++++++++++++++++++++++++++++++++

**Problem**

``install-fire-python.bat`` fails with::

  error: dependency install failed.

**Solution**

* Check that the machine can reach PyPI (https://pypi.org). If a proxy is required, set the ``HTTP_PROXY`` and ``HTTPS_PROXY`` environment variables before running the script.
* If pip reports ``no matching distribution``, a pre-built package is not available for the Python version or platform being used. Confirm that 64-bit Python 3.9 is being used. Do **not** install Visual Studio C++ Build Tools: the script never compiles packages, by design.
* On machines without internet access, install from a local folder of wheel files::

    .\install-fire-python.bat --find-links C:\path\to\wheels

Engine venv not found
+++++++++++++++++++++

**Problem**

``run-fire-polars.bat start`` or ``run-fire-agent.bat start`` fails with::

  ERROR: engine venv not found at engine-venv\Scripts\python.exe

**Solution**

The engine virtual environment has not been created in this install directory. This is expected after an upgrade, since the new directory does not contain ``engine-venv``. Run the below, then start the engine again::

  .\install-fire-python.bat

Agent or Polars engine does not start
+++++++++++++++++++++++++++++++++++++

**Problem**

``run-fire-polars.bat start`` or ``run-fire-agent.bat start`` fails with::

  ERROR: server is not listening on port 8089 after 5 seconds.

**Solution**

* Read the Python error printed above this message in the command prompt.
* Check whether another process is already using the port (8089 for Polars, 8200 for Agents)::

    netstat -ano | findstr :8089

  Stop that process, or start the engine on a different port, for example ``.\run-fire-polars.bat start 8090``.

Cannot recreate or delete engine-venv
+++++++++++++++++++++++++++++++++++++

**Problem**

Re-running ``install-fire-python.bat``, or deleting the ``engine-venv`` folder, fails because files are in use.

**Solution**

A running engine keeps files in ``engine-venv`` locked. Stop both engines, then try again::

  .\run-fire-agent.bat stop
  .\run-fire-polars.bat stop
