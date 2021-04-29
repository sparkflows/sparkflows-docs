MapR Integration
=====================

This document describes details when installing Fire Insights on a MapR cluster.

Download Fire Insights
---------------------

* Download MapR specific binary from : https://www.sparkflows.io/archives

Turn off Impersonation
----------------------

* In Administration / Configuration of Sparkflows::

    Turn off impersonation : Set app.impersonateUsers = false
    Set maprfs : hdfs.namenodeURI = maprfs:///
    Set spark-submit appropriately : spark.spark-submit = /opt/mapr/spark/xyz/bin/spark-submit
    
Update http port
----------------

* Set ``http port` to be different in `conf/application.properties`` if there are other processes using the specified ports

Fire User
---------

* Fire has to be installed as a user which can submit jobs to the MapR cluster. Say we installed Fire as user ``mapr``::

    Create a mapr user in sparkflows and log in as that user
    Start using Sparkflows

