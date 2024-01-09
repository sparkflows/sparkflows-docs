Logs
=====

Where do I find the logs of the Fire Server?
-------------------------------------------
The logs of the Fire web server is in the file **fireserver.log**. Logs of the Fire processes are in the file **fire.log** under the directory where Fire has been installed.


Where do I find the logs of the job executions when running on my Cluster?
---------------------------------------------------------------------
The logs are in the directory **/tmp/fire/workflowlogs** on the machine on which the Fire server is running::

Each workflow execution has its own log file.

The JSON representation of the workflow is in **/tmp/fire/workflows** when running in **YARN client mode**. They are in **.fireStaging** directory under the users home directory on HDFS when running in **YARN cluster mode**.


