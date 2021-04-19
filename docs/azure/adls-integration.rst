ADLS Integration
================

Fire Insights is integrated with Azure data lake storage. Once configured you can use the filesystem for accessing data from it.

Below are the steps for configuring Fire Insights with ADLS using managed identity.

Managed identity allow the users to access the Azure resources without hardcoding any credentials in code.

System identity need to be enabled 
-----------------------------------

System identity needs to be enabled on the VM where Fire Insights is installed.

.. figure:: ../_assets/configuration/identity.PNG
   :alt: adls
   :width: 40%

In storage account, add the role to provide the access
------------------------------------------------------

In storage account, add the role to provide the access to Azure vm with needed access 

.. figure:: ../_assets/configuration/storage.PNG
   :alt: adls
   :width: 40%
   
Configure ADLS in Fire Insights
----------------------

Add the below parameters in Administration/Configuration in Fire Insights.

 - ``azure.enabled to true``
 - ``azure.homeDir as abfs://containerName@storageAccountName.dfs.core.windows.net`` 


.. figure:: ../_assets/configuration/azure_configurations.PNG
   :alt: adls
   :align: center
   :width: 40%

ADLS page in Fire Insights
-------------------

Save the above configuration, refresh the page & Ccick on the Data menu to see the ADLS page

.. figure:: ../_assets/configuration/adls.PNG
   :alt: adls
   :width: 40%
   
Go to Data/ADLS page
------------------------

Click on ADLS to see ADLS FILESYSTEM in `DATA`

.. figure:: ../_assets/configuration/adls-file.PNG
   :alt: adls
   :width: 40%

Once the above configurations are done, you can start using files on ADLS while creating datasets and workflows.


