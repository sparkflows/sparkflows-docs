Running on Another Port
=======================

There are 2 processes involved:

- fire server
- fire

Both fire server and fire can be configured to listen on different ports.

Running Fire Server on Another Port
-----------------------------------------

If you choose to run the FIRE project on a port other than the ``default 8080 (http) and 8443 (https)``, please follow the following instructions for ``configuring http and https ports``::

    - Navigate to the conf folder under Sparkflows install directory 
    - Open application.properties file:

        - Configure http and https port numbers: Default 8080 for http and 8443 for https
        - http.port=8080
        - https.port=8443
    - Restart Fire Server using run-fire-server.sh or run-fire-server.bat depending on the environment (Unix/Linux or Windows)


Running Fire on Another Port
----------------------------

Fire by default runs on port 8081.

In order to run Fire on another port:

- Navigate to the conf folder under Sparkflows install directory 
    - Open application.properties file:
    
    - Configure the http port
    - fire.http.port=8081
- Restart Fire using ./run-fire.sh


