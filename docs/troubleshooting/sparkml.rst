SparkML
====

This document explains some of the common issues and corresponding resolutions related to SparkML.

1. SparkML workflow with xgboost are failing
----------
**Problem**
+++++
xgboost workflow are failing with java.lang.Exception: Error :Failed to execute the workflow:  /tmp/libxgboost4j14342423119254343105.so: libgomp.so.1: cannot open shared object file: No such file or directory.

**Solution**
++++++++
There could be different reasons for this issue:

* Ensure that libgomp1 package is installed on the machine.

::

    sudo apt install --reinstall libgomp1 (ubuntu )
    sudo yum install libgomp -y (Centos/RHEL)




