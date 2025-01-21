Data Proc Connection
====

Fire Insights can be used to create Dataproc connections and automate the creation of workflows/pipelines that interact with Dataproc clusters for large-scale data processing.

Step 1 : Enable Dataproc Connection
---------

To Enable Dataproc Connection:

#. Click on **CONNECTION** tab and set the below value to true:

   ::

     connection.dataproc.enabled : true

   .. figure:: ../../../_assets/gcp/dataproc_connection.PNG
      :alt: GCP Configuration Details
      :width: 60%

Step 2 : Add Dataproc Connection
--------------

Dataproc Connection details can be specified in Global Connections. To add:

#. From the Administrataion page, click on **Global Connections**.
#. Click on **Add Connection** button located on the top-right corner.
#. In the Add Connection dialog-box:

   Specify the **Connection Name** and **Postback Url** in the General tab.
   
   .. figure:: ../../../_assets/gcp/dataproc_create.PNG
      :alt: GCP Configuration Details
      :width: 60%

#. Specify the **location of Fire Core JAR**, **Project Id**, **Region**, **Dataproc Cluster name**, **Main Class**  in the Dataproc tab.
 
   .. figure:: ../../../_assets/gcp/dataproc_configurations.PNG
      :alt: GCP Configuration Details
      :width: 60%

#. **Save** the connection. Once saved, you can use this connection to submit Jobs, view BigQuery and browse Google Storage.
