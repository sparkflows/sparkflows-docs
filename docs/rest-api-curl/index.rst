REST API Examples using curl
==========

This topic contains a range of examples that demonstrate how to use the Fire Insights API using curl.

Acquire Session Cookie Using CURL
--------------------------------

When invoking the REST API's of Fire Insights with curl, the first step is to log in and save the incoming cooking into a text file. This file would then be used in making subsequent REST calls via curl.

Save the incoming cookies using the ``-c`` option of ``curl`` into a file.

In the below examples, the Fire Insights web server is running on the local machine at : ``localhost:8080``

You can replace it with your machine name and port.

**CURL**::

    curl -i -X POST -d username=admin -d password=admin -c /tmp/cookies.txt localhost:8080/login
    
In the above:

    * username = admin
    * password = admin
    * Incoming cookie gets saved into : /tmp/cookies.txt
    * REST API endpoint : localhost:8080/login



There are various categories of REST API's available:


.. toctree::
   :maxdepth: 2

   processors.rst
   dataset.rst
   workflow.rst
   workflow-execution.rst
   dashboard.rst
   hdfs.rst
   hive.rst
   scheduler.rst
   
   
   

