Application gateways
========

This document describes the steps for Configuring Fire Insights with Application gateways.

Step 1 : Login to Azure portal and add Application gateways
-----------------
#. Login to **Azure Dashboard**.
#. Navigate to **Virtual Machine**.
#. Navigate to **Load Balancing**.

   .. figure:: ../../_assets/azure/app_loadbalancer.PNG
      :width: 60%
      :alt: Basic Configuration

#. Navigate to **Add load balancing >> Create new >> Application Gateway**.

   .. figure:: ../../_assets/azure/app_gateway.PNG
      :width: 60%
      :alt: Basic Configuration

Step 2 : Create an application gateway
-----------------


#. Navigate to  **Create an application gateway**.

   .. figure:: ../../_assets/azure/app_detail.PNG
      :width: 60%
      :alt: Basic Configuration

   .. figure:: ../../_assets/azure/app_more_details.PNG
      :width: 60%
      :alt: Basic Configuration

Step 3 : Configure Application gateway
-----------------


#. Navigate to  **Configuration** in Application gateway.

   .. figure:: ../../_assets/azure/app_waf2.PNG
      :width: 60%
      :alt: Basic Configuration

#. Navigate to  **Web application firewall**.

Disabled ``Inspect request body`` in ``Global parameters``

   .. figure:: ../../_assets/azure/app_firewall.PNG
      :width: 60%
      :alt: Basic Configuration

Step 4 : Access Fire Insight application using Application gateway
-----------------

Now you Access Fire Insight application using ``Application gateway ip``

::

    http://application_gateway_ip

.. Note:: Make sure to change ``application_gateway_ip`` with actual ip


