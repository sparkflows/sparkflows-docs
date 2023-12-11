GCP Configuration
=====

Fire Insights is seamlessly integrated with Google cloud platform. With Fire Insights you can perform self-serve data processing, analytics and machine learning on Google Cloud.

Below are the steps:


Step 1 : Specify GCP Configuration
----------

GCP Configuration details can be specified in the Fire Insights Administration UI inside GCP tab. To configure:

#. Login to Fire Insights and navigate to **ADMINISTRATION->Configurations->GCP**.
#. Enable Google Cloud Integration flag by selecting the value as **True**.
#. Specify the **Project Id**.
#. Specify the **path** to the Service Account Key file.

   .. figure:: ../../_assets/gcp/gcp_enable.PNG
      :alt: GCP Configuration Details
      :width: 60%

Step 2 : Enable Dataproc Connection
---------

To Enable Dataproc Connection:

#. Click on **CONNECTION** tab and set the below value to true:

   ::

     connection.dataproc.enabled : true

   .. figure:: ../../_assets/gcp/dataproc_connection.PNG
      :alt: GCP Configuration Details
      :width: 60%

Step 3 : Add Dataproc Connection
--------------

Dataproc Connection details can be specified in Global Connections. To add:

#. From the Administrataion page, click on **Global Connections**.
#. Click on **Add Connection** button located on the top-right corner.
#. In the Add Connection dialog-box:

   Specify the **Connection Name** and **Postback Url** in the General tab.
   
   .. figure:: ../../_assets/gcp/dataproc_create.PNG
      :alt: GCP Configuration Details
      :width: 60%

#. Specify the location of **Fire Core jar**, **Project Id**, **Region**, **Dataproc Clucter name**, **Main Class**  in the Dataproc tab.
 
   .. figure:: ../../_assets/gcp/dataproc_configurations.PNG
      :alt: GCP Configuration Details
      :width: 60%

#. **Save** the connection. You can use this connection to submit Jobs, View BigQuery and Browse Google Storage.
