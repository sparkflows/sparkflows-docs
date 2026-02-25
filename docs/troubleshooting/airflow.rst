Airflow
=======

This document contains details on troubleshooting Airflow.

1. Airflow Access Issue with URL
----------------------

**Problem**
++++
Facing Airflow access issue with URL.

**Solution**
+++++

* **Adjusting Docker Port:**

  * By default, Airflow using the Docker image is configured to run on port **8080**.
  * To mitigate potential conflicts, it is crucial to modify the fire server port to a different value, such as **8090** or any other open/available port.
  * For detailed instructions, refer the `Sparkflows Documentation on Running Custom Ports. <https://docs.sparkflows.io/en/latest/installation/configuration/running-different-port.html>`_


* **Configuration Setting: app.postMessageURL**
  
  * Access the **Administration/Configuration** section.
  * Verify the configuration for **app.postMessageURL**. This setting dictates the Fire URL to which results from the Spark driver are posted back to the Fire server.
  * Ensure that the app.postMessageURL is correctly configured to establish seamless communication between the Spark driver and the Fire server.

2. Airflow MWAA Sync Issue
----------------------

**Problem**
++++
Facing Airflow MWAA issue with Sync.

**Solution**
+++++

* **S3 configuration Issue:**

  * Make sure that dags folder is proper folder structure as **s3://sparkflows-bucket/dags/**.
  * Make sure that s3 bucket is accessible from Airflow MWAA.

* **VPC Issue**

  * Make sure that your VPC must have both enabled **Enable DNS resolution & Enable DNS hostnames**.

* **requirements.txt Issue**

  * Make sure that **requirements.txt** should be in proper folder structure and is compatible with Airflow MWAA version.

