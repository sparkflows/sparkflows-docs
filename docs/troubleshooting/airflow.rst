Airflow
=======

This page contains details on troubleshooting Airflow.

Airflow using Docker image gets installed by default at port 8080.

Make sure to change the fire server port to 8090 or any other open/available port.
Refer:
https://docs.sparkflows.io/en/latest/installation/configuration/running-different-port.html?highlight=fire%20port#running-fire-server-on-custom-port

Under Administration/Configuration, there is the config app.postMessageURL. It determines the Fire URL to which the results from the spark driver are posted back to the fire server. Ensure that it is set up correctly.

