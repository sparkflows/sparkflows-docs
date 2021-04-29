Running on Another Port
=======================

There are 2 processes involved when running Fire.

- fire server
- fire

User's Browser talks with ``fire server``, and in turn ``fire server`` talks with ``fire``.

Both ``fire server`` and ``fire`` processes can be configured to listen on different ports.

Running Fire Server on Another Port
-----------------------------------------

By default the fire server runs on the following ports:

    * 8080 (http)
    * 8443 (https)
    
Below are the steps for running fire server on a different port.

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

In order to run Fire on a different port:

- Navigate to the conf folder under Sparkflows install directory 
    - Open ``application.properties`` file:
    
    - Configure the http port
    - ``fire.http.port=8081``
- Restart Fire using ``./run-fire.sh start``


