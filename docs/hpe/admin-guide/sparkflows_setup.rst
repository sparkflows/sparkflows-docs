Setup Sparkflows on HPE UA
=====

This document explains in detail the steps involved in setting up Sparkflows on HPE UA.

To setup, follow the steps below :

Step 1 : Download and Unzip Sparkflows TAR File
------------------------------------------------

#. Download the **Sparkflows TAR file** and extract its contents.
#. Copy the **fire-spark_3.3.1-core-3.1.0-jar-with-dependencies.jar** from **fire-x.y.z/fire-core-jar** folder.
#. Copy the **workflowexecutecloud_livy.py** shared by Sparkflows.

.. note:: The latest Sparkflows TAR will be shared by Sparkflows.

Step 2 : Install Sparkflows
---------------
#. Copy the **fire-spark_3.3.1-core-3.1.0-jar-with-dependencies.jar** and **workflowexecutecloud_livy.py** to the **MapRFS** with HPE team's support.

   Once you finish uploading the files, you can view them, by navigating to **Main Menu** > **Data Engineering** > **Data Sources** > **Browse** 

   .. figure:: ../../_assets/hpe/hpe-ua-datasources.png
      :width: 60%
      :alt: HPE UA Data sources
   
#. If you prefer to use **MySQL** for storing the metadata of Sparkflows then connect with HPE team to deploy a MySQL instance.
   
   Make sure to configure the sparkflows **deployment.yaml** file located in the helm chart directory with the correct MySQL instance settings.

#. Configuring **Keycloak**

   For Configuring Keycloak, update **application.properties** from previous steps of `Keycloak Documentation. <https://docs.sparkflows.io/en/latest/hpe/admin-guide/keycloak_setup.html>`_

#. Build Sparkflows **Docker Image** with updated **application.properties** file.

#. Navigate to the **Tools & Frameworks** section on left side and click on **Import Framework**.

   .. figure:: ../../_assets/hpe/hpe-ua-add-import-framework.png
     :width: 60%
     :alt: HPE UA Import framework

#. Fill all the information for the **framework details**.

   .. figure:: ../../_assets/hpe/hpe-ua-framework-add-details.png
      :width: 60%
      :alt: HPE UA Add framework details


#. Connect with the Sparkflows team to get the latest **chart** for the HPE environment. Upload the new chart. 

   Make sure the chart version doesn’t match the existing uploaded version in the HPE EZUA platform, else it will throw the error as shown in the screenshot below.

   .. figure:: ../../_assets/hpe/hpe-ua-upload-chart.png
      :width: 60%
      :alt: HPE UA Add framework details

#. Now you can override the **chart values** in this step. Make sure you’ve used **virtualService variable** in the EZUA section. Failure to do so will result in DNS allocation for the newly installed service. You need to use the same domain name, which was used in the Keycloak section.
  
   .. figure:: ../../_assets/hpe/hpe-ua-chart-config.png
      :width: 60%
      :alt: HPE UA Add Configure chart values
 
   Following is the list of configurations that you need to override:

   **sso.clientId:** The registered client Id in the Keycloak that will be used to authenticate the users

   **sso.clientSecret:** The client secret used for the OAuth

   **sso.accessTokenUri:** Used to generate the access token. This is available from the step 5 of the Keycloak setup.

   **sso.userAuthorizationUri:** Used to validate the auth token. This is available from the step 5 of the Keycloak setup.
   
   **sso.userInfoUri:** Used to fetch the user details. This is available from the step 5 of the Keycloak setup.
   database.host: Used to configure the MySQL database host which stores the metadata of Sparkflows

#. As a final step, review the configuration, submit the new framework. It might take upto 10 minutes to bring the new framework.




