Databricks Workspace Connection
=====

Sparkflows enables you to create Databricks Workspace connection and use the connection to sync to Airflow and use it in pipelines.

Sparkflows supports two types of authentication for Databricks Workspace connections:

  * **Access Token (PAT)** : Personal Access Token based authentication
  * **AAD Token** : Azure Active Directory (Service Principal) based authentication

Connections can be at various levels:

  * Global : Everyone has access to these connections.
  * Group  : Users belonging to the group have access to these connections.

Below are the steps required to create Databricks Workspace connection:

Step 1 : Go to Connections Page
----------

#. **Login** to Sparkflows web server URL as an **Admin**.
#. Navigate to **ADMINISTRATION** Page from the top bar.
#. Click **Global Connections** from the Administration Page.

   .. figure:: ../../_assets/installation/connection/databricks-admin.png
      :alt: connection
      :width: 60%

   **Note :** Global Connections are available for everyone to use.

Step 2 : Open Add Connection Window
-----------------------

#. Click **Add Connection** button located on the top-right corner of the Connections Page.

   .. figure:: ../../_assets/installation/connection/databricks-connection.png
      :alt: connection
      :width: 60%

Step 3 : Enter Parameter Details
----------------
#. Enter parameter details in the Add Connection window.

   For more details refer the following tables and images:

   **GENERAL Tab:**

   .. list-table::
      :widths: 10 20 20
      :header-rows: 1

      * - Title
        - Description
        - Value
      * - CREDENTIAL STORE  
        - Select the Credential Store from drop-down
        - Choose specific Credential Store from drop-down or Select Do not use Credential Store
      * - Select Category
        - Select Category as Workspace
        - Select Workspace
      * - CONNECTION TYPE 
        - Select Workspace Databricks
        - Select Workspace Databricks
      * - CONNECTION NAME
        - Connection Name
        - Add a unique Connection Name
      * - AUTH TYPE
        - Select Authentication Type
        - Select either Access Token (PAT) or AAD Token
      * - TITLE
        - Title for selected Connection
        - Add a unique Title
      * - DESCRIPTION
        - Connection Description
        - Add some Connection Description
      * - URL
        - URL for Databricks Workspace
        - Add Databricks Workspace Url from the Databricks. Example: https://xxxxxxxx.databricks.net


   **Option 1: Access Token (PAT) Authentication**

   If you select **Access Token (PAT)** as Auth Type, you need to provide:

   .. list-table::
      :widths: 10 20 20
      :header-rows: 1

      * - Title
        - Description
        - Value
      * - TOKEN
        - Personal Access Token
        - Add the Personal Access Token generated from Databricks

   .. figure:: ../../_assets/installation/connection/Workspace_PAT_Token.png
      :alt: PAT Authentication
      :width: 60%


   **Option 2: AAD Token Authentication**

   If you select **AAD Token** as Auth Type, you need to provide:

   .. list-table::
      :widths: 10 20 20
      :header-rows: 1

      * - Title
        - Description
        - Value
      * - CLIENT ID
        - Azure AD Application (Service Principal) Client ID
        - Add the Client ID from Azure AD Service Principal
      * - CLIENT SECRET
        - Azure AD Application (Service Principal) Client Secret
        - Add the Client Secret from Azure AD Service Principal
      * - ACCESS TOKEN URI
        - Azure AD OAuth 2.0 Token Endpoint
        - Add the Access Token URI. Example: https://login.microsoftonline.com/{tenant-id}/oauth2/token

   .. figure:: ../../_assets/installation/connection/Workspace_AAD_Token.png
      :alt: AAD Token Authentication
      :width: 60%

   .. note:: For detailed steps on how to obtain Client ID and Client Secret from Azure, refer to `this guide <https://docs.sparkflows.io/en/latest/azure/admin-guide/azure-databricks-via-jdbc.html>`_.

   .. note:: Make sure to update Databricks Workspace URL with absolute path and it should be accessible from Sparkflows application.

   
   **WORKSPACE DATABRICKS Tab:**

   .. list-table:: 
      :widths: 10 20 20
      :header-rows: 1

      * - Title
        - Description
        - Value
      * - Fire core JAR
        - Path of Fire core JAR dependencies
        - Absolute path of Fire core JAR  
      * - Python file
        - Path of Pyspark main file
        - Absolute path of Pyspark main file
      * - Fire PySpark libraries
        - Path of Fire pyspark libraries
        - Absolute path of Fire PySpark libraries
      * - DBFS Scratch directory
        - Scratch directory on DBFS where it has Read/Write/Delete Permissions.
        - Scratch directory on DBFS where it has Read/Write/Delete Permissions. (User can update absolute DBFS path).
     
   .. figure:: ../../_assets/connections/databricks_workspace_2.png
      :alt: connection
      :width: 60%

Step 4 : Test and Save Connection
---------------

#. Click **TEST CONNECTION**. You will get a success notification.
#. Click **SAVE** to save the connection.

   Once you save the connection, it can be used to Sync this connection for Airflow.

   For detailed information, `click here. <https://docs.sparkflows.io/en/latest/tutorials/pipelines/dbpl-create-cluster.html>`_

