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
  
Browse Users Home Directory on HDFS
-----------------------------------

Gets all the files and folders in the users home directory::

  curl -i --header "Accept:application/json" -X GET -b /tmp/cookies.txt localhost:8080/hdfs

Open HDFS file
--------------

Accepts HDFS file path and returns first X bytes of content::

  curl -X GET --header 'Accept: text/plain' --header 'path: /home/ec2-user/settings.xml' 
  
http://localhost:8080/openHdfsFile' -b /tmp/cookies.txt

Upload file
-----------

Uploads selected file at specified path
File name:test.txt
path:/home/ec2-user::

  curl -X POST --header 'Content-Type: multipart/form-data' --header 'Accept: text/plain' --header 'path: /home/ec2-user/' -F 'file=@test.txt' 'http://localhost:8080/uploadFile' -b /tmp/cookies.txt
  
Get Users home directory
------------------------

  curl -X GET --header 'Accept: text/plain' 'http://localhost:8080/userHomeDir' -b /tmp/cookies.txt



