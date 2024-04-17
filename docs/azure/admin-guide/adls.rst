Azure Data Lake Storage
========

This document describes the steps for configuring ADLS in Sparkflows running on a virtual machine.


Azure pre-requisites
++++

In order to configure ADLS in Fire Insights, the User needs to have the following pre-requisites in Azure:



.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Recommended
     - Value
   * - Home Directory	
     - Home Directory Path on Azure storage
     - The path must match the format eg: abfs://containerName@storageAccountName.dfs.core.windows.net
   * - Client Id	
     - Client Id
     - Application (client) ID in register application
   * - Client Secret Key
     - Client Secret Key
     - Client Secret Key generated during registration of app in Azure portal
   * - Azure Client EndPoints	
     - Azure Client EndPoints	
     - EndPoints with OAuth 2.0 token endpoint (v1) in register application
   * - Azure ADLS Access Type		
     - Azure ADLS can be accessed in many ways but currently supporting servicePrincipal and managedIdentity	
     - Value should be either servicePrincipal or managedIdentity

Configure ADLS in Sparkflows
+++++++++++++++

Once the above pre-requisites from Azure are available, you can configure ADLS in Sparkflows using the below steps:

Step 1 : Open Sparkflows in Web Browser
----------------

#. Open a **web browser**.
#. Enter the URL: http://sparkflows_IP:8080 and replace **sparkflows_IP** with your instance's **actual IP/DNS**.

Step 2 : Configure ADLS
--------------

#. **Login** to Sparkflows.
#. Access Sparkflows **Administration** Tab.

   .. figure:: ../../_assets/aws/livy/administration.png
      :alt: livy
      :width: 70%



#. Select **Configurations** Tab.
#. Select **AZURE** Tab.
#. Enter **parameter details** setup in Azure.
#. Save the **configurations**.

.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Recommended
     - Value
   * - Enable Azure		
     - Enable Azure for accessing the Azure Data Lake storage
     - true
   * - Home Directory	
     - Home Directory Path on Azure storage
     - The path must match the format eg: abfs://containerName@storageAccountName.dfs.core.windows.net
   * - Client Id	
     - Client Id
     - Application (client) ID in register application
   * - Client Secret Key
     - Client Secret Key
     - Client Secret Key generated during registration of app in Azure portal
   * - Azure Client EndPoints	
     - Azure Client EndPoints	
     - EndPoints with OAuth 2.0 token endpoint (v1) in register application
   * - Azure ADLS Access Type		
     - Azure ADLS can be accessed in many ways but currently supporting servicePrincipal and managedIdentity	
     - Value should be either servicePrincipal or managedIdentity

.. figure:: ../..//_assets/azure/azure_configure.PNG
      :width: 70%
      :alt: adls

Step 3 : Browse ADLS
--------------

Once the above **configurations** are saved, you can browse ADLS as below:

#. Click on **DATA** Tab.
#. Select **ADLS**.
#. You can browse ADLS file and folder.

   .. figure:: ../../_assets/azure/adls_browse.PNG
      :width: 70%
      :alt: adls

