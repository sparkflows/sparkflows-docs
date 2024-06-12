Configuring Fire Insights for Jupyterhub
=============

This document outlines the steps to configure Fire Insights for Jupyterhub.

Steps
-----

Fire Insights can be configured to connect to Jupyter Notebook. Below are the steps involved in it:

Step 1: Login to Fire Web Server URL
++++++++++++++++++++++++++++++

#. Login to Fire web server URL.
#. Goto **ADMINISTRATION -->> Configurations** and select **NOTEBOOK**.

   .. figure:: ../../_assets/operating/jupyter_notebook_1.PNG
      :alt: operating
      :width: 60%

#. Update the below parameters:

   ::

      notebook.enabled : true
      notebook.serverHost : jupyternotebook server url
      notebook.serverToken : Administrator Token being used
    
   .. note::  Ensure that you replace 'localhost' with your domain name or IP address where Fire is running to ensure accessibility.

Step 2 : Jupyterhub Tab 
+++++++++++++++++++++++++++++++

#. After saving the above configuration, refresh the web server URL to see **JupyterHub**. tab inside the project.

   .. figure:: ../../_assets/operating/jupyter_notebook-access.PNG
      :alt: operating
      :width: 60%

Step 3 : Create Jupyter Notebook
+++++++++++++++++++++++++++++++
