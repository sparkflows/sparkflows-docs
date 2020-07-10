Installer for laptop/desktop
============================

You can download and use the Installer for installing/upgrading Fire Insights on your laptop or desktop.

This is not recommended to use on the server, where you need better control over the Installation process.

Prerequisites
-------------

- JDK 1.8 or later

- Winutils.exe for windows

   - Create bin folder in hadoop directory : C:\\hadoop\\bin
   - Copy the downloaded winutils.exe to the bin directory : C:\\hadoop\\bin\\winutils.exe
   - Add it in a new Environment Variable : HADOOP_HOME = C:\\hadoop
   
     If you don't have winutils.exe in your system, Installer will update it.  

Download
--------

Download the installer from : https://www.sparkflows.io/download


Execute
-------

Execute the installer with :

java -jar sparkflows.jar

Default port for sparkflows is : 8080

You can also change the port number while installing or starting the server.

When you finish, Browse to http://<system-ip>:8080

 -	Login with admin/admin
