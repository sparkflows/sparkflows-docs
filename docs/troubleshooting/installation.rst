Installation
============

This document segment goes over some of the common issues and their resolution that our users tend to run into:


1. No Browser Content After Starting Fire
---------------

**Problem**
++++++++

I do not see anything in my browser after I start Fire.

**Solution**
++++++++
Please check the logs for exceptions and the root cause. The server log file is named **fireserver.log** and will be written in the install directory.

Possible causes for Fire not to start could be:

* H2 database was not created OR it is failing to find the table.
* H2 database was schema was not updated.
* The server did not start properly because some other Application is running on the configured port. The default configured port for Fire is **:8080**. 

  The HTTP and HTTPS ports for Fire can be updated in **conf/application.properties**.

2. Fire Insights Page Not Opening at :8080
--------------------------

**Problem**
++++++++

Fire Insights page does not open when I go to :8080. Some other UI is displayed.

**Solution**
++++++++

* It is possible that there is some other application running on port 8080 (or the port on which Fire Insights is listening).
* Fire by default runs on port 8080.
* The resolution would be to run Fire server on some other port which is not being used by any other application. 
* Details for running Fire on another port is at `Sparkflows Documentation on Running Different Ports. <https://docs.sparkflows.io/en/latest/installation/configuration/running-different-port.html>`_

3. Getting Error: Could Not Connect to Fire at Localhost
----------------------------

**Problem**
++++++++

On certain pages I get the error following error: 

**Could not connect to fire at localhost.**

**Solution**
+++++++

* The reason for it is that the Fire Insight helper process is not starting. 

  Check out the log files namely, **fireserver.log** and **fire.log** for errors. They are written in the install directory.

* If you are using Ubuntu, you may have to do the following:
  
   - sudo dpkg-reconfigure dash
   - https://unix.stackexchange.com/questions/442510/how-to-use-bash-for-sh-in-ubuntu
   - And then select **No**.

4. Getting Error: Unable to Create New Active Thread
----------------

**Problem**
++++++

Getting the following error: 

**Unable to create new active thread.**


**Solution**
+++++++

Details and resolution can be found at the `Troubleshooting Documentation. <https://dzone.com/articles/troubleshoot-outofmemoryerror-unable-to-create-new>`_

5. Keystore Error on Starting Fire
-------------

**Problem**
++++++++
Getting the following error when starting Fire:

**keytool error: java.io.IOException: Keystore was tampered with, or password was incorrect**

**Solution**
++++++++

* The **KEYSTORE_PASSWORD** and the **keystore.jks** do not correspond to each other.
* To validate, one can use the keytool command below. 
* If the keytool commands below throws the same keytool error, it means that one would need to create and use the correct **keystore.jks** and the corresponding password.
  ::  
      keytool -list -keystore <path of keystore.jks> -storepass <passoword_for_jks>`
 
  More details can be found in the `Official Documentation. <https://docs.oracle.com/javase/8/docs/technotes/tools/unix/keytool.html>`_

6. Error: java.net.BindException - Cannot Assign Requested Address
----------------------------

**Problem**
++++++++

Getting the following error : 

**java.net.BindException:Cannot assign requested address**

**Solution**
+++++++

Make sure that you do not have mapped public IP to private IP in **/etc/hosts**, as Fire Insights by default use localhost for subprocess.

7. Error Running Docker Commands: docker: Invalid Reference Format
------------------------

**Problem** 
++++++++

Getting the following error when trying to run docker commands: 

**docker: invalid reference format**

**Solution**
+++++++++

It usually happens when copying the Docker commands to a Windows machine and then the unseen **NBSP** characters gets added in the command. 

To fix it, copy the docker command first to an editor where NBSP characters can be seen like notepad++ or sublime and then remove the character and run the docker command.

These characters are not seen on notepad on Windows or Word and other text editors.
