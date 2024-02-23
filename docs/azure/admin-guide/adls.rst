Azure Data Lake Storage
========

This document describes the steps for Configuring ADLS in Fire Insights running on a virtual machine.

Inorder to Configure ADLS in Fire Insights, User need to have below pre-requisites in Azure.

Azure pre-requisites
++++

The Azure pre-requisites needed to Configure ADLS in Fire Insights:

.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Recommended
     - Value
   * - Home Directory	
     - Home Directory Path on azure storage
     - The path must match the format eg abfs://containerName@storageAccountName.dfs.core.windows.net
   * - Client Id	
     - Client Id
     - Client Id for ADLS Configuration
   * - Client Secret Key
     - Client Secret Key generated during registration of app in Azure portal.
     - Client Secret Key
   * - Azure Client EndPoint	
     - Azure Client EndPoint	
     - EndPoint
   * - Azure ADLS Access Type		
     - Azure ADLS can be accessed in many ways but currently supporting servicePrincipal and managedIdentity.	
     - Value should be either servicePrincipal or managedIdentity

Configuring ADLS in Fire Insights
+++++++++++++++

Once the above pre-requisites from Azure is available, you can Configure ADLS in Fire Insights using below steps:
