Azure Container Apps
=====================

Once Fire is installed, it can be connected to various Apache Spark and Kubernetes clusters to leverage their scalability to execute the jobs.

Fire Insights stores metadata in a relational store. 

This document describes the steps for installing Fire Insights on Azure Container Apps.

.. note:: MySQL needs to be set up before installing Fire Insights.

Step 1 : Open Container Apps Configuration Window
-----------------
#. Login to **Azure Dashboard**.
#. Navigate to **Container Apps**.

   .. figure:: ../../../_assets/azure/search-container.png
      :width: 60%
      :alt: Basic Configuration
#. Click on **Create** to open the configuration window.

   .. figure:: ../../../_assets/azure/click-create.png
      :width: 60%
      :alt: Basic Configuration

Step 2 : Enter Basic Configuration Details
-----------------
#. Fill in the basic information about the container as shown below:

   .. figure:: ../../../_assets/azure/basic-configuration.png
      :width: 60%
      :alt: Basic Configuration

Step 3 : Enter Container Configuration Details
------------------------------------------
To allow the container to connect to a remote MySQL instance, enter the following details:

#. Click on **Container** tab located on the configuration window.

#. Provide image and container environmet details as shown below:

   .. figure:: ../../../_assets/azure/configure-container.png
      :width: 60%
      :alt: Container Configuration

   .. note:: Make sure you provide atleast 2vCPU and 4GB RAM to the container. 

Step 4 : Enter Ingress Configuration Details 
-------------------------------
The Ingress configuration allows you to connect to the deployed container. To configure:

#. Click on **Enable check box** located in front of Ingress.
#. Enter the configuration details as shown below:

   .. figure:: ../../../_assets/azure/configure-ingress.png
      :width: 60%
      :alt: Ingress Configuration

   .. note:: In the above case, we have used **8080** as the target port, because by default the container runs on 8080 for http and 9443 for https with self-signed certificate.

Step 5 : Create the Container
-----------
#. Wait for the above configurations to be validated and then finally, click on **create**.

   .. figure:: ../../../_assets/azure/running-validation.png
      :width: 60%
      :alt: Ingress Configuration


   Once you click on create, it will deploy the container. 

   Now, you can track the progress on the below screen:

   .. figure:: ../../../_assets/azure/deployment-complete.png
      :width: 80%
      :alt: Deployment complete
