Installation
============

This document segment goes over some of the common issues and their resolution that our users tend to run into:

1. I do not see anything in my browser after I start Fire
------------------------------------------------------------

Please check the logs for exceptions and the root cause. The server log file is named ``fireserver.log`` and will be written in the install directory.

Possible causes for Fire not to start could be:

* H2 database was not created OR it is failing to find the table.
* H2 database was schema was not updated.
* The server did not start properly because some other Application is running on the configured port. The default configured port for Fire is ``:8080``. The HTTP and HTTPS ports for Fire can be updated in ``conf/application.properties``.


2. Fire Insights page does not open when I go to :8080. Some other UI is displayed
-----------------------------------------------------------------------------------

* It is possible that there is some other application running on port ``8080`` (or the port on which Fire Insights is listening)
* Fire by default runs on port ``8080``.
* The resolution would be to run Fire server on some other port which is not being used by any other application. 
* Details for running Fire on another port is here : https://docs.sparkflows.io/en/latest/installation/configuration/running-different-port.html 


3. On certain pages I get the error : Could not connect to fire at localhost
---------------------------------------

* The reason for it is that the Fire Insight helper process is not starting. Check out the log files namely, ``fireserver.log`` and ``fire.log`` for errors. They are written in the install directory.
* If you are using Ubuntu, you may have to do the following:
   - sudo dpkg-reconfigure dash
   - https://unix.stackexchange.com/questions/442510/how-to-use-bash-for-sh-in-ubuntu
   - And then select ``No``.


4. Getting the error : Unable to create new active thread
-------------------------------

Details and resolution can be found here: https://dzone.com/articles/troubleshoot-outofmemoryerror-unable-to-create-new

5. Keystore Error on starting Fire
--------------------------------

If you run into error ``keytool error: java.io.IOException: Keystore was tampered with, or password was incorrect`` when starting Fire it means:

* The ``KEYSTORE_PASSWORD`` and the ``keystore.jks`` do not correspond to each other.
* To validate, one can use the keytool command below. 
* If the keytool commands below throws the same ``keytool error``, it means that one would need to create and use the correct ``keystore.jks`` and the corresponding password.
  - keytool -list -keystore <path of keystore.jks> -storepass <passoword_for_jks>`
  - More details can be found here: https://docs.oracle.com/javase/8/docs/technotes/tools/unix/keytool.html

6. Getting the error : ``java.net.BindException:Cannot assign requested address``
-------------------------------

Make sure that you donot have mapped public ip to private ip in ``/etc/hosts``, As Fire Insights by default use localhost for subprocess.

7. Getting the error when trying to run docker commands: docker: ``invalid reference format``
-------------------------------

Usually happens when copying the Docker commands to a Windows machine and then the unseen `NBSP` characters gets added in the command. 

To fix it, copy the docker command first to an editor where NBSP characters can be seen like notepad++ or sublime and then remove the character and run the docker command.

These characters are not seen on notepad on Windows or word and other text editors.
