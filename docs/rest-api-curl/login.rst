Acquire Session Cookie
==================

When invoking the REST API's of Fire Insights with curl, the first step is to log in and save the incoming cooking into a text file. This file would then be used in making subsequent REST calls.

Save the incoming cookies using the ``-c`` option of ``curl''

In the below examples, the Sparkflows Fire server is running on the local machine at : ``localhost:8080``

You can replace it with your own machine name and port.

**CURL**::

    curl -i -X POST -d username=admin -d password=admin -c /tmp/cookies.txt localhost:8080/login
    
In the above:

    * username = admin
    * password = admin
    * Incoming cookie gets saved into : /tmp/cookies.txt
    * REST API endpoint : localhost:8080/login    
