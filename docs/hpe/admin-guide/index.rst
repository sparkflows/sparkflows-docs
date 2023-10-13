HPE Unified Analytics Admin Guide
===================

HPE Unified Analytics provides a platform for different distributed systems like datastore, analytics engine, scheduler and query engine for running different analytical operations. Sparkflows leverages 
these frameworks and tools to help you build ML and analytical workflows using drag-n-drop wizard.

Here is quick snap, of how the HPE UA Dashboard looks like.

.. figure:: ../../_assets/hpe/hpe-ua-dashboard.png
   :scale: 100%
   :alt: HPE UA Dashboard
   :align: center


Once you get access to the HPE UA Dashboard, you can go to **Main Menu** > **Applications & Frameworks** > **Analytics** to view the different frameworks and tools available that Sparkflows leverages for executing
the workflows.

.. figure:: ../../_assets/hpe/hpeua-frameworks.png
   :scale: 100%
   :alt: HPE UA Frameworks
   :align: center

Setup Sparkflows on HPE UA
--------------------------

1. Now with the sparkflows tar file, you need to extract it, and copy the **fire-spark_3.2.1-core-3.1.0-jar-with-dependencies.jar** and **workflowexecutecloud_livy.py** to the maprfs, 
with the support from HPE team. Once you have uploaded the files, you can view them, by navigating to **Main Menu** > **Data Engineering** > **Data Sources** > **Browse** 

Here is the screenshot

.. figure:: ../../_assets/hpe/hpe-ua-datasources.png
   :scale: 100%
   :alt: HPE UA Data sources
   :align: center


2. Use the Helm chart to install the Sparkflows, from one of the edge node of the HPE UA. Make sure you’ve configured the sparkflows deployment.yaml stored in the helm chart directory with the correct MySQL instance configuration.
If there is an instance of Sparkflows running, first uninstall it using the below command

::

  $ helm uninstall fire-ezua -n sparkflows

Run the command to install Sparkflows with MySQL support, in a separate namespace - sparkflows

::

  $ helm install fire-ezua -n sparkflows fire

To validate if the installation was successful, run the following command

::

  $ kubectl get pods -n sparkflows 
  NAME                                              READY   STATUS    RESTARTS       AGE
  fire-ezua-sparkflows-fire-7746b99c89-2kdhr        2/2     Running   1 (174m ago)   175m


To fetch the logs for debugging purpose, run the following command

::

  $ kubectl logs -f <pod name> -n sparkflows

Find the exposed service port by running this command

::
  
  $ kubectl get svc -n sparkflows

