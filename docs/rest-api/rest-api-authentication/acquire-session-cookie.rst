Acquire Session Cookie using curl command
==================

When invoking the REST APIs of Fire Insights with curl, the first step is to log in and save the incoming cookie into a text file. This file would then be used in making subsequent REST calls via curl.

Save the incoming cookies using the ``-c`` option of the ``curl`` into a file.

In the below example, the Fire Insights web server is running on local machine at: ``localhost:8080``

You can replace it with your machine name and port.

**CURL**::

    curl -i -X POST -d username=admin -d password=admin -c /tmp/cookies.txt localhost:8080/authenticate
    
In the above:

    * username = admin
    * password = admin
    * Incoming cookie gets saved into: /tmp/cookies.txt
    * REST API endpoint: localhost:8080/authenticate 
