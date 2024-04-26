Configuring Fire Insights for JupyterLab
=============

This document outlines the steps to configure Fire Insights for JupyterLab.

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
      notebook.serverHost : jupyternotebook server url which include token
      notebook.serverToken : Token being used
    
   .. note::  Ensure that you replace 'localhost' with your domain name or IP address where Fire is running to ensure accessibility.

Step 2 : Open Jupyter Notebook
+++++++++++++++++++++++++++++++

#. After saving the above configuration, refresh the web server URL to see **Jupyter Notebook**. Open it.

   .. figure:: ../../_assets/operating/jupyter_notebook-access.PNG
      :alt: operating
      :width: 60%

Step 3 : Access Jupyter Notebook
+++++++++++++++++++++++++++++++

#. After clicking on Jupyter Notebook, a new page will open where you can run Python code.
   
   .. figure:: ../../_assets/operating/jupyter_notebook_2.PNG
      :alt: operating
      :width: 60%

   .. figure:: ../../_assets/operating/jupyter_notebook_command.PNG
      :alt: operating
      :width: 60%

 
