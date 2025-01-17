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

    #. Note Down the Application Details:

       #. After registration, note down the Application (client) ID and Directory (tenant) ID from the overview page.

#. Create a Client Secret

   #. Go to Certificates & Secrets:

      #. In the left-hand menu of your registered application, select Certificates & secrets.

   #. Create a New Client Secret:

      #. Click New client secret.
      #. Provide a description and set an expiration period.
      #. Click Add.

   #. Note Down the Client Secret:

      #. Copy the Client Secret value. You won’t be able to see it again after leaving the page.



