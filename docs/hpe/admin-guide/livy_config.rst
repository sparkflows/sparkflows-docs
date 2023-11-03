Configure Livy Connection
=====

Sparkflows connects with Livy to submit the Spark and PySpark jobs of the workflow on the cluster powered by HPE UA. 

Follow the below steps to configure the Livy connection in Sparkflows:

#. Navigate to **Administration** > **Connections** > **Add Connection** > **Connection for All** to reach a Modal window.
   
   Now, enter the **Livy URLs** and the **credentials**, that has been provided by the HPE UA Team.

   .. figure:: ../../_assets/hpe/livy-connection.png
      :width: 40%
      :alt: HPE UA Data sources

#. Upload the JAR **(fire-spark_3.2.1-core-3.1.0-jar-with-dependencies.jar)** that will be used to run the Spark job in the MapRFS. 

   Next, upload the **workflowexecutecloud_livy.py** to the MapRFS and configure the path in the Livy Tab, as shown below :

   .. figure:: ../../_assets/hpe/livy-tab-connection.png
      :width: 40%
      :alt: HPE UA Data sources

   Also, update the **Docker image** designated for executing PySpark jobs in the above configuration.

#. If you're connecting to an S3-compatible storage without a verified SSL certificate, include the following configuration to bypass SSL validation :
   ::

     spark.driver.extraJavaOptions:-Dcom.amazonaws.sdk.disableCertChecking=true,spark.executor.extraJavaOptions:-Dcom.amazonaws.sdk.disableCertChecking=true,spark.kubernetes.container.image:sparkflows/fire-hpe:3.1.0_13

#. Finally **test** the connection and **save** it. 

   Now you can start submitting the workflows on the Livy cluster.
