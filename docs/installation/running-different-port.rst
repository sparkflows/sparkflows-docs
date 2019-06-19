Running on Another Port
=======================

There are 2 processes involved when running Fire.

- fire server
- fire

Users Browser talks with ``fire server``, and in turn ``fire server`` talks with ``fire``.

Both ``fire server`` and ``fire`` processes can be configured to listen on different ports.

Running Fire Server on Another Port
-----------------------------------------

If you choose to run the FIRE project on a port other than the ``default 8080 (http) and 8443 (https)``, please follow the following instructions for ``configuring http and https ports``::

    - Navigate to the conf folder under Sparkflows install directory 
    - Open application.properties file:

        - Configure http and https port numbers: Default 8080 for http and 8443 for https
        - http.port=8080
        - https.port=8443
    - In the Fire UI, under Administration/Configuration update the below property with the right port number.
        - app.postMessageURL
    - Restart Fire Server using one of the commands below depending on the environment (Unix/Linux or Windows)
      - run-fire-server.sh start
      - run-fire-server.bat


Running Fire on Another Port
----------------------------

Fire by default runs on port 8081.

In order to run Fire on another port:

- Navigate to the conf folder under Sparkflows install directory 
    - Open ``application.properties`` file:
    
    - Configure the http port
    - ``fire.http.port=8081``
- Restart Fire using ``./run-fire.sh start``


