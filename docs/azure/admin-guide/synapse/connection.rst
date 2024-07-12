Azure Synapse Connection
=======

Sparkflows enables you to create Azure Synapse as a Compute Connection and submit the Job onto it. 

This document outlines the steps to create Azure Synapse as a Compute Connection.

Azure Pre-requisites
++++

In order to Create Azure Synapse Compute Connection in Sparkflows, the User needs to have the following pre-requisites in Azure:

.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Recommended
     - Value
   * - Client Id	
     - Client Id
     - Client Id
   * - Client Secret Key
     - Client Secret Key generated during registration of app in Azure portal
     - Client Secret Key
   * - Azure Synapse URL	
     - Azure Synapse URL	
     - Synapse URL
   * - Pool Name	
     - Synapse Pool Name	
     - Synapse Pool Name
   * - Tenant Id	
     - Azure Tenant Id	
     - Azure Tenant Id

For more information on setting up Azure Synapse, `click here. <https://learn.microsoft.com/en-us/azure/synapse-analytics/quickstart-create-workspace>`_

Creating Azure Synapse Connection
++++++++++++++

Sparkflows enables you to create **Azure Synapse Connection** and use it to submit **jobs/workflows**. Connections can be at various levels:

  * **Global**  : Everyone has access to these connections.
  * **Group**   : Users belonging to the group have access to these connections.
  * **Project** : The owner of the project and the groups with which the project has been shared with have access to the project level connections.

Below are the steps to create Azure Synapse Connection:

Step 1 : Enable Azure Synapse in Sparkflows
--------------------

#. **Login** to Sparkflows.
#. Navigate to **Administration -> Configurations -> Connection**. 
#. **Enable** the Azure Synapse connection by setting the below parameter:

   ::

       connection.synapse.enabled : true

   .. figure:: ../../../_assets/azure/synapse_configuration.png
      :alt: synapse
      :width: 60%

Step 2 : Add and Save the Connection
-------------------

Once you save the above configurations:

#. Navigate to **Administration -> Global Connections -> Add Connections** as shown below:

   .. figure:: ../../../_assets/aws/livy/administration.png
     :alt: synapse
     :width: 60%

#. Click on **Add Connection For Group**.

   .. figure:: ../../../_assets/azure/synapse_addconnection.png
      :alt: synapse
      :width: 60%

#. On the pop-up window, select connection as **Compute Connection** and enter other parameters as shown below:

   .. figure:: ../../../_assets/azure/synapse_connection.png
      :alt: synapse
      :width: 60%

#. Once you have selected  the connection type & groups, add the **additional connection parameters** needed as per your environment. 

   For more details refer the following tables and images:

   **For GENERAL tab**:


   .. list-table:: 
      :widths: 10 20 30
      :header-rows: 1

      * - Title
        - Description
        - Value
      * - Connection name
        - Connection Name
        - Name of Connection
      * - Postback URL
        - Postback URL
        - Postback URL through which Azure Synapse sent result back to Sparkflows
      * - Client Id	
        - Client Id
        - Client Id for ADLS Configuration
      * - Client Secret Key
        - Client Secret Key generated during registration of app in Azure portal
        - Client Secret Key
      * - Title 
        - Title of Selected Connection
        - Title of Selected Connection  
      * - EndPoint URL	
        - Azure Synapse URL	
        - Synapse URL
      * - Description 
        - Connection Description 
        - Connection Description
      * - Driver Class
        - Driver Class for selected Connection type 
        - It Comes with default value  
      * - Pool Name	
        - Synapse Pool Name	
        - Synapse Pool Name
      * - Tenant Id	
        - Azure Tenant Id	
        - Azure Tenant Id


   .. figure:: ../../../_assets/azure/synapse-general.png
      :alt: synapse
      :width: 60%
   
  
   **For AZURE SYNAPSE tab**:


   .. list-table:: 
      :widths: 10 20 30
      :header-rows: 1

      * - Title
        - Description
        - Value
      * - File Path 
        - File Path 
        - Fire core JAR file path
      * - Driver Memory 
        - Driver Memory 
        - Driver Memory need to be used
      * - Driver Cores  
        - Driver Cores  
        - Driver Cores need to be used 
      * - Executor Memory  
        - Executor Memory  
        - Executor Memory need to be used
      * - Executor Cores  
        - Executor Cores  
        - Executor Cores need to be used
      * - Executor Count  
        - Executor Count  
        - Executor Count need to be used
 
   .. figure:: ../../../_assets/azure/synapse_azuretab.png
      :alt: synapse
      :width: 60%

#. Once you have updated the above parameters, click on **Save** to save the connection.

