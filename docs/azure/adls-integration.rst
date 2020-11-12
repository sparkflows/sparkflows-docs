ADLS Integration
================

Fire Insights integrated with azure data lake storage, once configured you can use the filesystem for accessing data from it.

Below are the steps to Configured adls using managed identity

Managed identity allow the users to access the azure resources without hardcoding any credentials in code.

System identity need to be enabled 
-----------------------------------

System identity need to be enabled on vm where Fire Insights is running or need to be install

.. figure:: ../_assets/configuration/identity.PNG
   :alt: adls
   :align: center
   :width: 40%

In storage account, add the role to provide the access
------------------------------------------------------

In storage account, add the role to provide the access to Azure vm with needed access 

.. figure:: ../_assets/configuration/storage.PNG
   :alt: adls
   :align: center
   :width: 40%
   
login to Fire Insights 
----------------------------------

login to Fire Insights application and add below parameter in Configuration under administration section for AZURE.

 - ``azure.enabled to true``
 - ``azure.homeDir as abfs://containerName@storageAccountName.dfs.core.windows.net`` 


.. figure:: ../_assets/configuration/azure_configurations.PNG
   :alt: adls
   :align: center
   :width: 40%

Save Configuration
-------------------

Save the above configuration and refresh the page & Click on Data browser to see ADLS page

.. figure:: ../_assets/configuration/adls.PNG
   :alt: adls
   :align: center
   :width: 40%
   
Click on Data browser
------------------------

Click on ADLS to see ADLS FILESYSTEM in `DATA BROWSERS`

.. figure:: ../_assets/configuration/adls-file.PNG
   :alt: adls
   :align: center
   :width: 40%

Once the above configurations done, you can start using those file while creating dataset and workflow.
