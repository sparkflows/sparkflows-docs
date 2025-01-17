Service Principal
======

This guide provides step-by-step instructions for creating a Service Principal in Azure. The Service Principal will be used to authenticate and access Azure resources, such as Azure Storage from Fire Insights.

Prerequisites
----

#. Azure Account: You need an Azure subscription with sufficient permissions to create Service Principals and assign roles.
#. Azure Storage Account: A storage account with the necessary data (e.g., invoice files) must be available.

Step 1: Create a Service Principal in Azure
-----

#. Register an Application in Azure Active Directory

    #. Go to the Azure Portal:
      
       #. Navigate to the [Azure portal](https://portal.azure.com/).

    #. Open Azure Active Directory:

       #. In the left-hand menu, select Azure Active Directory.

    #. Register a New Application:

       #. Go to App registrations > New registration.
       #. Provide a name for your application (e.g., `Databricks-Service-Principal`).
       #. Leave the other fields as default and click Registe

          .. figure:: ../../../_assets/azure/service_principal.png
             :alt: adls
             :width: 70%

    #. Note Down the Application Details:

       #. After registration, note down the Application (client) ID and Directory (tenant) ID from the overview page.

          .. figure:: ../../../_assets/azure/service_principal_1.png
             :alt: adls
             :width: 70%

#. Create a Client Secret

   #. Go to Certificates & Secrets:

      #. In the left-hand menu of your registered application, select Certificates & secrets.

   #. Create a New Client Secret:

      #. Click New client secret.
      #. Provide a description and set an expiration period.
      #. Click Add.

   #. Note Down the Client Secret:

      #. Copy the Client Secret value. You won’t be able to see it again after leaving the page.

         .. figure:: ../../../_assets/azure/service_principal_2.png
             :alt: adls
             :width: 70%


Step 2: Assign Roles to the Service Principal
-----

#. Assign Roles to the Service Principal

   #. Go to Your Storage Account:

      #. Navigate to your Azure Storage Account in the Azure portal.

   #. Open Access Control (IAM):

      #. In the left-hand menu, click Access Control (IAM).

   #. Add a Role Assignment:

      #. Click + Add and select Add role assignment.

   #. Select the Role:

      #. In the Role tab, search for and select Storage Blob Data Contributor (or Storage Blob Data Reader for read-only access).

         .. figure:: ../../../_assets/azure/service_principal_3.png
             :alt: adls
             :width: 70%


   #. Assign Access to the Service Principal:

      #. In the Members tab, click Select members.
      #. Search for the name of your Service Principal (the application you registered earlier).
      #. Select the Service Principal and click Select.

         .. figure:: ../../../_assets/azure/service_principal_4.png
             :alt: adls
             :width: 70%
 
        
   #. Review and Assign:

      #. Click Review + assign to confirm the role assignment.



Now you can use these details to Configured ADLS in Fire Insights, `click here. <https://docs.sparkflows.io/en/latest/azure/admin-guide/adls/adls-configuration.html>`_

.. Note:: The above Configurations are needed for Interactive mode, For Execution mode the Compute engine need to have access of resources.


