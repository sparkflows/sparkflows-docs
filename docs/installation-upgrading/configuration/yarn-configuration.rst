YARN Configurations
==================

Fire can submit jobs to a YARN cluster. It can submit the spark jobs to run on YARN in either client or cluster mode.


Client Mode
-----------

For configuring to run in client mode, the below configurations apply::

    spark.deploy-mode : client

In this mode, the spark driver runs on the same machine on which Fire is running. The workflow json file is written out to the directory **/tmp/fire/workflows** on the machine on which Fire is running.


Cluster Mode
------------

For configuring to run in cluster mode, the below configurations apply::

    spark.deploy-mode : cluster

In this mode, the spark driver runs on the spark cluster. The workflow json file is written out onto HDFS in the directory **.fireStaging** under the users HOME directory on HDFS.

The spark job is able to read the workflow json file from HDFS.

Impersonation
-------------

 * Normally ``app.impersonateUsers` is set to ``true`` so that the jobs are run as the logged in user.

.. note::  The logged in user into Fire should exist on HDFS

