Upgrade
=======

Overview
-----

This document describes the steps to Upgrade Sparkflows on Windows environment. 

Sparkflows Upgrade
---------

Below are the steps to upgrade Sparkflows.

#. Login into the Windows

   Login into the Windows Machine.

#. Stop Sparkflows existing service

   #. Open the command line (terminal) on your system.
   #. ``Navigate`` to the directory where the Sparkflow binary has been extracted. You can do this using the ``cd`` (change directory) command.::


       cd  fire-3.X.Y_spark_3.3.0

   #. Stop the Sparkflows server by running the following::


       .\run-fire-server.bat stop

   #. Keep a backup of firedb from file explorer. You can create a backup folder and copy ``firedb.*`` files from user home directory to the backup folder.



#. Download the latest Sparkflows TGZ

   #. Download the latest TAR from into user home directory::

      https://www.sparkflows.io/download  

#. Unpack the downloaded tgz file. Below are some tools which can be used for it::
   
      WinRar : https://www.rarlab.com/download.htm
      WinZip : https://www.winzip.com
      7-Zip : https://www.7-zip.org/download.html

#. Create DB tables with Schema

   #. Goto inside the sparkflow binary extracted directory using Command line::


       cd  fire-3.X.Y_spark_3.3.0

   #. Update the DB and schema by running the following::


      .\create-h2-db.bat


#. Start Sparkflows Server


   #. Start the Sparkflows server by running the below::

      
       .\run-fire-server.bat start

      .. note::  To verify whether the Fire Server is running, you can navigate to the fire home directory in your File Explorer.
           Find the log folder. In the log folder, open fireserver or fireserver.log to see the logs from the server. 

#. Open your web browser and navigate to:: 
  
    <machine_name>:8080

#. Login with::

    your login credentials


