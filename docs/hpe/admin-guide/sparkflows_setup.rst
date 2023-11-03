Setup Sparkflows on HPE UA
=====

This document explains in detail the steps involved in setting up Sparkflows on HPE UA.

To setup, follow the steps below :

#. Get the Sparkflows TAR file and unzip it.
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
