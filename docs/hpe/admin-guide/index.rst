HPE Unified Analytics Admin Guide
===================

HPE Unified Analytics provides a platform for different distributed systems like datastore, analytics engine, scheduler and query engine for running different analytical operations. Sparkflows leverages 
these frameworks and tools to help you build ML and analytical workflows using drag-n-drop wizard.

This document explains in detail the steps involved in setting up Sparkflows on HPE UA and Configuring Livy in Sparkflows.

Step 1 : Access HPE UA Dashboard
-------------------------
#. **Login** to the **HPE UA Dashboard** using your credentials. 
   
   Here is quick snap, of how the HPE UA Dashboard looks like.

   .. figure:: ../../_assets/hpe/hpe-ua-dashboard.png
      :width: 60%
      :alt: HPE UA Dashboard

Step 2 : Access Frameworks and Tools
----------------
#. To access the different frameworks and tools that Sparkflows uses for executing workflows :

   Navigate to **Main Menu** > **Applications & Frameworks** > **Analytics** from the dashboard.

   .. figure:: ../../_assets/hpe/hpeua-frameworks.png
      :width: 60%
      :alt: HPE UA Frameworks

Step 3 : Setup Sparkflows on HPE UA
--------------------------
To setup, follow the steps below :

#. Get the Sparkflows tar file and unzip it.
#. Copy the **fire-spark_3.2.1-core-3.1.0-jar-with-dependencies.jar** and **workflowexecutecloud_livy.py** to the **MapRFS** with HPE team's support.

   Once you finish uploading the files, you can view them, by navigating to **Main Menu** > **Data Engineering** > **Data Sources** > **Browse** 

   .. figure:: ../../_assets/hpe/hpe-ua-datasources.png
      :width: 60%
      :alt: HPE UA Data sources
   
#. Use the Helm chart to install Sparkflows on one of the HPE UA edge nodes.
   
   Make sure to configure the sparkflows deployment.yaml file located in the helm chart directory with the correct MySQL instance settings.

   If there's an existing instance of Sparkflows, initiate the uninstallation process using the comands given below :
   ::

     $ helm uninstall fire-ezua -n sparkflows

#. Run the command to install Sparkflows with MySQL support, in a separate namespace - sparkflows :
   ::

     $ helm install fire-ezua -n sparkflows fire

#. To validate if the installation was successful, run the following command :
   ::

        $ kubectl get pods -n sparkflows 
        NAME                                              READY   STATUS    RESTARTS       AGE
        fire-ezua-sparkflows-fire-7746b99c89-2kdhr        2/2     Running   1 (174m ago)   175m


#. To fetch the logs for debugging purpose, run the following command :
   ::

     $ kubectl logs -f <pod name> -n sparkflows

#. Find the exposed service port by running the below command :
   ::
  
     $ kubectl get svc -n sparkflows


Step 4 : Configure Livy Connection
-------------------
Sparkflows connects with Livy to submit the Spark jobs of the workflow on the cluster powered by HPE UA. 

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
