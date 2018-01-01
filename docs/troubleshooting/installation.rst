Installation
============


Installation Pre-requisites
---------------------------

Below are the Pre-requisites before installing Fire::

    JDK 1.7+ installed on the machine

    java and jar have to be in the PATH

    If running on a Spark cluster, Spark 1.6+ is needed on the cluster.

    3GB+ of RAM available on the machine.


With which user should Fire be installed
----------------------------------------

If Fire needs to be connected with a Spark cluster the below is needed:

* Fire needs to be installed as a user which can impersonate other users. Impersonation for this user has to be set up in HDFS configs.
* If you disable impersonation in Fire, then the user with which Fire is installed needs to be able to submit jobs to the cluster.

More Details are available here : https://www.sparkflows.io/connecting-sparkflows-with-spark-cl



I do not see anything in my browser after I start Sparkflows
------------------------------------------------------------

Do check in the logs for exceptions and the root cause. On Linux and Mac, the log files are in nohup.out.

Possible causes are:

* The H2 database was not created and it is failing to the find the table.
* The server did not start properly because some other Application is running on the configured port. The default configured port for Sparkflows is :8080

The http and https ports for Fire can be updated in conf/application.properties.


Sparkflows UI does not get displayed when I go to :8080. Some other UI is displayed
-----------------------------------------------------------------------------------

Sparkflows by default runs on port 8080. It is possible that you have some other application running on port 8080, and you are seeing its output.In this case, the solution is to run the Fire server on some other port which is not being used by any other application.Details for running Fire on another port is here : https://www.sparkflows.io/run-fire-on-different-port


