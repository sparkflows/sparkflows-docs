Running on Custom Port
=======================

By default the Fire server runs on the following ports:

    * 8080 (http)
    * 8443 (https)
    
Below are the steps for running Fire server on a different port:

    - Navigate to the conf folder under Sparkflows install directory 
    - Open application.properties file:

        - Configure http and https port numbers: Default 8080 for http and 8443 for https
        - http.port=8080
        - https.port=8443
    - In the Fire UI, under Administration/Configuration update the below property with the right port number:
        - app.postMessageURL
    - Restart Fire server using one of the commands below depending on the environment (Unix/Linux or Windows)
       - run-fire-server.sh start
       - run-fire-server.bat

