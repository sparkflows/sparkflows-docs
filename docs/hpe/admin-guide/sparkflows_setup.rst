Setup Sparkflows on HPE UA
=====

This document explains in detail the steps involved in setting up Sparkflows on HPE UA.

To setup, follow the steps below :

Step 1 : Download and Unzip Sparkflows TAR File
----------------

#. Download the Sparkflows TAR file and extract its contents.

.. note:: The latest Sparkflows TAR will be shared by Sparkflows.

Step 2 : Install Sparkflows
---------------
#. Copy the **fire-spark_3.3.1-core-3.1.0-jar-with-dependencies.jar** and **workflowexecutecloud_livy.py** to the **MapRFS** with HPE team's support.

   Once you finish uploading the files, you can view them, by navigating to **Main Menu** > **Data Engineering** > **Data Sources** > **Browse** 

   .. figure:: ../../_assets/hpe/hpe-ua-datasources.png
      :width: 60%
      :alt: HPE UA Data sources
   
#. If you prefer to use MySQL for storing the metadata of Sparkflows then connect with HPE team to deploy a MySQL instance.
   
   Make sure to configure the sparkflows deployment.yaml file located in the helm chart directory with the correct MySQL instance settings.

#. Once you've decided on the Sparkflows' url to be used, navigate to the keycloak web ui, and login to the server with admin credentials. For the keycloak server details, connect with the HPE team :
   ::
     
     Server: https://keycloak.dev.hpeua.com/
     Username: admin
     Password: ******************

#. Select the UA realm from the left drop down menu and click on clients to view the list of clients currently registered.

   .. figure:: ../../_assets/hpe/hpe-keycloak-clients.png
      :width: 60%
      :alt: HPE UA Keycloak clients

#. Click on the ua client and then navigate to the settings section. Scroll down and add the sparkflows oidc callback url

   .. figure:: ../../_assets/hpe/keycloak-redirect-uris.png
      :width: 60%
      :alt: HPE UA Keycloak callback urls

#. Navigate to the Credentials section to copy the client secret, which will be used in sparkflows application properties.

   .. figure:: ../../_assets/hpe/client-details.png
      :width: 60%
      :alt: HPE UA Keycloak Client secrets


#. Navigate to the Tools & Frameworks section on left side and click on Import Framework

   .. figure:: ../../_assets/hpe/hpe-ua-add-import-framework.png
     :width: 60%
     :alt: HPE UA Import framework

#. Fill all the information for the framework details

   .. figure:: ../../_assets/hpe/hpe-ua-framework-add-details.png
      :width: 60%
      :alt: HPE UA Add framework details


#. Connect with the Sparkflows team to get the latest chart for the HPE environment. Upload the new chart. Make sure the chart version doesn’t match the existing uploaded version in the HPE ezua platform, else it will throw the error as shown in the screenshot below.

   .. figure:: ../../_assets/hpe/hpe-ua-upload-chart.png
      :width: 60%
      :alt: HPE UA Add framework details

#. Now you can override the chart values in this step. Make sure you’ve used “virtualService” variable in the ezua section. Failure to do so will result in dns allocation for the newly installed service. You need to use the same domain name, which was used in the Keycloak section.
  
   .. figure:: ../../_assets/hpe/hpe-ua-configure-chart-values.png
      :width: 60%
      :alt: HPE UA Add Configure chart values
#. As a final step, review the configuration, submit the new framework. It might take upto 10 minutes to bring the new framework.




