YARN Configurations
==================

Fire can submit jobs to a YARN cluster. It can submit the spark jobs to run on YARN in either client or cluster mode.


Client Mode
-----------

While configuring to run in client mode, set the following parameter under **Administration/Configuration**::

    spark.deploy-mode : client

In this mode, the spark driver runs on the same machine on which Fire is running. The workflow JSON file is written out to the directory **/tmp/fire/workflows** on the machine on which Fire is running.


Cluster Mode
------------

While configuring to run in cluster mode, set the following parameter under **Administration/Configuration**::

    spark.deploy-mode : cluster

In this mode, the spark driver runs on the spark cluster. The workflow JSON file is written out onto HDFS in the directory **.fireStaging** under the users home directory on HDFS.

The spark job reads the workflow JSON file from HDFS.

Impersonation
-------------

 * Normally **app.impersonateUsers** is set to **true** so that the jobs are run as the logged in user.

.. note::  The logged in user into Fire should exist on HDFS.

