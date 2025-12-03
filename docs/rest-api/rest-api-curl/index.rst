REST API Examples using Curl
==========

This topic contains a range of examples that demonstrates how to use the Sparkflows APIs using curl.

Acquire Session Cookie Using curl
-----------------------------

When invoking the REST APIs of Sparkflows with curl, the first step is to log in and save the incoming cookie into a text file. This file would then be used in making subsequent REST calls via curl.

Save the incoming cookies using the ``-c`` option of ``curl`` into a file.

In the examples below, Sparkflows web server is running on the local machine at: ``localhost:8080``

You can replace it with your machine name and port.

* Login and save the session cookie into /tmp/cookies.txt*::

    curl -i -X POST -d username=admin -d password=admin -c /tmp/cookies.txt localhost:8080/login
    
In the above:

    * username = admin
    * password = admin
    * Incoming cookie gets saved into : /tmp/cookies.txt
    * REST API endpoint : localhost:8080/login



There are various categories of REST API's available:

.. panels::
    :container: container-lg pb-3
    :column: text-center col-lg-6 col-md-6 col-sm-6 col-xs-12 p-2

    :doc:`/rest-api/rest-api-curl/processors`

    ---

    :doc:`/rest-api/rest-api-curl/dataset`

    ---

    :doc:`/rest-api/rest-api-curl/workflow`

    ---

    :doc:`/rest-api/rest-api-curl/workflow-execution`

    ---

    :doc:`/rest-api/rest-api-curl/dashboard`

    ---

    :doc:`/rest-api/rest-api-curl/hdfs`

    ---

    :doc:`/rest-api/rest-api-curl/hive`

    ---

    :doc:`/rest-api/rest-api-curl/scheduler`
    
     ---

    :doc:`/rest-api/rest-api-curl/users`
    
     ---

    :doc:`/rest-api/rest-api-curl/groups`
    
    ---

    :doc:`/rest-api/rest-api-curl/import-workflow`

.. toctree::
   :hidden:

   processors.rst
   dataset.rst
   workflow.rst
   workflow-execution.rst
   dashboard.rst
   hdfs.rst
   hive.rst
   scheduler.rst
   users.rst
   groups.rst
   import-workflow.rst
   
   
   

