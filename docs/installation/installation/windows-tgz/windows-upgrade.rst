Upgrade
=======

Overview
--------

This document describes the steps to upgrade Sparkflows on a Windows environment.

All commands below are run in a Command Prompt.

Sparkflows Upgrade
------------------

Below are the steps to upgrade Sparkflows.

#. Login into the Windows

   Login into the Windows Machine.

#. Stop the existing Sparkflows processes

   #. Open the command line (terminal) on your system.
   #. Navigate to the directory where the existing Sparkflows binary has been extracted, using the ``cd`` (change directory) command::

       cd fire-3.X.Y_spark_3.5.2

   #. If the Agent and Polars engines are running, stop them::

       .\run-fire-agent.bat stop
       .\run-fire-polars.bat stop

   #. Stop the Fire helper process and the Fire Server::

       .\run-fire.bat stop
       .\run-fire-server.bat stop

   #. Keep a backup of firedb from File Explorer. Create a backup folder and copy the ``firedb.*`` files from the user home directory to the backup folder.

#. Download the latest Sparkflows TGZ

   Download the latest TGZ into the user home directory from::

      https://www.sparkflows.io/download

#. Unpack the downloaded tgz file. Below are some tools which can be used for it::

      WinRar : https://www.rarlab.com/download.htm
      WinZip : https://www.winzip.com
      7-Zip : https://www.7-zip.org/download.html

#. Create DB tables with schema

   #. Go inside the newly extracted Sparkflows directory using the command line::

       cd fire-3.X.Y_spark_3.5.2

   #. Update the DB and schema by running the following::

       .\create-h2-db.bat

#. Start the Fire Server and the Fire helper process

   ::

       .\run-fire-server.bat start
       .\run-fire.bat start

   .. note::  To verify whether the Fire Server is running, navigate to the fire home directory in your File Explorer.
              Find the log folder. In the log folder, open fireserver or fireserver.log to see the logs from the server.

#. Recreate the engine virtual environment and start the engines (only if you use Agents or Polars jobs)

   The new install directory does not contain ``engine-venv``, so it has to be created again before the engines can start. This needs Python 3.9 (64-bit, version 3.9.2 or later), as described in :doc:`windows-install`.

   #. Create the engine virtual environment::

       .\install-fire-python.bat

   #. Start the Polars and Agent engines::

       .\run-fire-polars.bat start
       .\run-fire-agent.bat start

#. Open your web browser and navigate to::

    <machine_name>:8080

#. Login with::

    your login credentials
