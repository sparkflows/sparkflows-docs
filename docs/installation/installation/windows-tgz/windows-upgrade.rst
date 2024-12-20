Upgrade
=======

Overview
-----

This document describes the steps to Upgrade Sparkflows on Windows environment. 


Below are the steps to upgrade Sparkflows.

#. Login into the Windows VM

   Login into the Windows VM:

#. Stop Sparkflows existing service

   #. Goto inside the sparkflow binary extracted directory using Command line::


       cd  fire-3.X.Y_spark_3.3.0

   #. Stop the Sparkflows server by running the following::


       .\run-fire-server.bat stop

   #. Keep a backup of firedb from file explorer. You can create a backup folder and copy firedb.* files from user home directory to the backup folder.



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
