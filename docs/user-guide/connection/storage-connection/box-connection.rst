Box Connection
======
Sparkflows provides the capability to create a Box Storage Connection and use it for reading from and writing to files stored in your Box account. This allows workflows to directly access Box folders and integrate cloud-stored data into pipelines.

Connections can be at various levels:

* Global : Everyone has access to these connections.
* Group : Users belonging to the group have access to these connections.
* Project : The owner of the project and the groups with which the project has been shared with have access to the project level connections.

This guide shows how to create a Box Storage Connection in Sparkflows.

Steps for Creating Box Connection
----
Follow the steps below to create a Box connection:

**Step 1: Create the OAuth Setting**
+++++++++++++++++++++++++++++++++++++++
Before creating the connection, you must configure OAuth for Box. The steps for the same are as follows:

1. Go to **Administration --> OAuth --> Add OAuth Setting**.

   .. figure:: ../../../_assets/connections/administration-OAuth-card.png
      :alt: box connection
      :width: 60%

2. Fill in the following details:

  * Credential Store: Select where the OAuth credentials will be stored.

  * Provider Name: Choose the OAuth provider, in this case Box.
  
  * Grant Type: Select the authentication method, which is JWT Bearer for Box.
  
  * JSON Key File / Private Key: Upload the Box service account JSON file that contains the private key used to generate the access token.

   .. figure:: ../../../_assets/connections/box-connection-oauth-authentication.png
      :alt: box connection
      :width: 60%

3. Click **Get Access Token**. A dialog will appear showing the generated access token.

   .. figure:: ../../../_assets/connections/oauth-token-details.png
      :alt: box connection
      :width: 60%

4. Click **Save** to store the OAuth setting.

**Step 2: Create the Box Connection**
+++++++++++++++++++++++++++++++++++++++

After OAuth is configured, proceed to create the storage connection.

1. Navigate to **Administration --> Connections --> Add Connection** and select **Add Connection For All**.

2. Enter the configuration details using the table below.

   .. list-table:: 
      :widths: 25 25 50
      :header-rows: 1

      * - Title
        - Description
        - Value
      * - Credential Store  
        - Select the Credential Store from drop-down
        - Choose a Credential Store or select Do Not Use Credential Store
      * - Select Category
        - Select Category of Connection Type
        - Select Storage Connection
      * - Connection Type 
        - Select the Connection type from drop-down
        - Choose Box as Connection Type
      * - Connection Name
        - Connection Name
        - Enter a unique connection name (e.g., box-connection)
      * - OAuth Config 
        - OAuth setting to authenticate Box
        - Select the OAuth configuration created earlier
      * - Home Directory
        - Optional starting directory in Box
        - Leave empty or specify a Box folder path

   .. figure:: ../../../_assets/connections/box-connection-configuration.png
      :alt: box connection
      :width: 60%

**Step 3: Test Connection and Save**
+++++++++++++++++++++++++++++++++++++++

1. After entering all details, click **Test Connection**.
2. Sparkflows will attempt to authenticate with Box using the OAuth configuration. If successful, click **Save**.

You are now ready to use the Box Connection in workflows. Once the connection is saved, you can use the Read and Save nodes to interact with Box.
















