Acquire Session Cookie
==================

As the first step, log into Sparkflows and get the session id.

In the below examples, the Sparkflows Fire server is running on the local machine at : ``localhost:8080``

You can replace it with your own machine name and port.

**CURL**::

    curl -i -X POST -d username=admin -d password=admin -c /tmp/cookies.txt localhost:8080/login
    
In the above:

    * username = admin
    * password = admin
    * Result/Session ID gets saved into : /tmp/cookies.txt
    * REST API endpoint : localhost:8080/login    
