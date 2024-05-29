Apache Livy Logs
===============

Sparkflows empowers you to Save the Livy Logs in S3 through Livy connection once you've established one successfully. 

This document provides an in-depth guide to the steps required for Configuring Logs via a Livy Connection.

Prerequisites
-------------
* AWS S3 Bucket with Write permission.
* AWS S3 Bucket is accessible from Fire Insights Machine/Container.


Following the steps given below would allow you to successfully Configuring Logs using a Livy Connection:


Step 1 : Login to Fire Insights
------------

#. Open Fire Insights **Login page** to enter your credentials and click **Sign in**.
#. Once you **Sign in**, If you already created Apache Livy Connection, you need to update the connection.

    `Click Here <https://docs.sparkflows.io/en/latest/installation/connection/compute-connection/livy.html>`_ to access detailed documentation on connecting Fire Insights to Apache Livy.
#. Click on **LIVY** tab and update **Livy Log File S3 location**

    Livy Log File S3 location : s3://sparkflows-bucket/logs

    .. figure:: ../../../_assets/aws/livy/livy-logs.png
         :alt: livy
         :width: 60%
    
#. Update the **Apache Livy Connection**
#. Now you can submit the job on **Apache Livy**, the logs would be persistent and it can be view from **Executions** page

    .. figure:: ../../../_assets/aws/livy/wf_execution_livy.png
         :alt: livy
         :width: 60%

    .. figure:: ../../../_assets/aws/livy/livy_logs_execution.png
         :alt: livy
         :width: 60%

    .. figure:: ../../../_assets/aws/livy/livy_view_logs.png
         :alt: livy
         :width: 60%

