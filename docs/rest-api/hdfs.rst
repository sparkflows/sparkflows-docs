HDFS REST API
=============

Overview
--------

The HDFS REST API's, allow you to interact with the HDFS of the Hadoop Cluster Sparkflows is connected to.

Below are the various HDFS API's available in Sparkflows

They should be executed after you have logged into Sparkflows

Open a Directory
----------------

Returns the list of files/directories in the given folder (/tmp)
path:/tmp::

  curl -i --header "Accept:application/json" -H "Content-Type:application/json" -H "path:/tmp" -X GET -X GET -b /tmp/cookies.txt localhost:8080/openHdfsDir
