Azure Container Apps
=====================

This document describes the steps for installing Fire Insights on Azure Container Apps.

Once Fire is installed, it can be connected to various Apache Spark and Kubernetes clusters to leverage their scalability to execute the jobs.

Fire Insights stores metadata in a relational store.

MySQL needs to be set up before installing Fire Insights.

Step 1: Create a container app
-----------------
Navigate to the Container Apps in Azure Dashboard and click on Create. It will require you to fill in the basic information about the container, as shown below.

.. figure:: ../../_assets/azure/basic-configuration.png
      :width: 60%
      :alt: Basic Configuration


Step 2: Configure container configuration
------------------------------------------
Next step is to provide the image details and the container environment variables that allow the container to connect to a remote MySQL instance.

.. figure:: ../../_assets/azure/configure-container.png
      :width: 60%
      :alt: Container Configuration




