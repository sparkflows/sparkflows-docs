Fire Server & Workflow Execution Logs
=====================================


Where do I find the logs of the Fire Server
-------------------------------------------

When running on linux or mac the logs of the Fire Web Server are in the file ``nohup.out`` under the directory where Fire has been installed. It would be something like ``...../fire-1.4.3``


Where do I find the logs of the workflows when running on my Cluster
---------------------------------------------------------------------

The logs are in the directory ``/tmp/fire/workflowlogs`` on the machine on which the Fire server is running::

  Each workflow execution has its own log file.

The json representation of the workflow is in ``/tmp/fire/workflows`` when running in ``YARN client mode``. They are in ``.fireStaging`` directory under the ``users home directory on HDFS`` when running in ``YARN cluster mode``.


