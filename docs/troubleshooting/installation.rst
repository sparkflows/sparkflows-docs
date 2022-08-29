Installation
============

I do not see anything in my browser after I start Fire
------------------------------------------------------------

Do check in the logs for exceptions and the root cause. The log files are in fireserver.log.

Possible causes are:

* The H2 database was not created and it is failing to the find the table.
* The server did not start properly because some other Application is running on the configured port. The default configured port for Fire is ``:8080``

The http and https ports for Fire can be updated in ``conf/application.properties``.


Fire UI does not get displayed when I go to :8080. Some other UI is displayed
-----------------------------------------------------------------------------------

Fire by default runs on ``port 8080``. It is possible that you have ``some other application running on port 8080``, and you are seeing its output. In this case, the solution is to ``run the Fire server on some other port`` which is not being used by any other application. Details for running Fire on another port is here : https://docs.sparkflows.io/en/latest/installation/configuration/running-different-port.html


On certain pages I get the error : Could not connect to fire at localhost
---------------------------------------

The reason for it is the the fire process is not starting. Check out the log files : fireserver.log and fire.log.

If you are using Ubuntu, you may have to do the following:

- sudo dpkg-reconfigure dash
- https://unix.stackexchange.com/questions/442510/how-to-use-bash-for-sh-in-ubuntu

Select 'No'


Getting the error : unable to create new active thread
-------------------------------

https://dzone.com/articles/troubleshoot-outofmemoryerror-unable-to-create-new



