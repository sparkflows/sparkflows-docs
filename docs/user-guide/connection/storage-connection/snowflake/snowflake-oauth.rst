Snowflake Oauth Connection
=======

Sparkflows provides the capability to create "Snowflake Connection" and use the connection to access various resources, using OAuth.
Using Snowflake with OAuth, SSO with OAuth for user loggedIn must be enabled. Below are the steps user will have to follow:

    1. **SSO Authentication for User Login:**
       Users log in to the Sparkflows application through Single Sign-On (SSO), which can be implemented using protocol like OAuth. When users 
       authenticate via SSO, the application receives an access token, which will be used to identify the user in subsequent requests.

    2. **OAuth Connection for Snowflake Access:**
       Sparkflows allows users to create a connection to Snowflake, where the data storage and retrieval happen. This connection relies on OAuth for secure, delegated access to Snowflake resources. The OAuth setup with Snowflake includes configuring Sparkflows as an authorized OAuth client for Snowflake.

Once the connection is established, the user’s OAuth token (from SSO login) is passed through to Snowflake. This OAuth token grants the application access to specific Snowflake resources without requiring the user to re-authenticate.

Follow the steps below to create a Snowflake connection using OAuth authentication:

Step 1 : Navigate to Connections Page
-------------

#. Login to **Sparkflows** using your credentials.
#. From the dashboard page, go to **Administration** and select **Global/Group Connections**, as shown below.

   .. figure:: ../../../..//_assets/credential_store/create-snowflake-connection/fire_admin_page.PNG
      :alt: Credential Store
      :width: 65%

Step 2 : Add Connection
-----------
#. From the connections page, click on **Add Connection** button located at the top right corner of the page.
#. Choose either **Add Connection For All** or **Add Connection For Group** from the dropdown based on your requirements, as shown below. An 'Add Connection' dialog box will open.

   .. figure:: ../../../..//_assets/credential_store/create-snowflake-connection/connections-add.png
      :alt: Credential Store
      :width: 65%



Step 3 : Add Connection Parameter
--------------------------
#. In 'Add Connection' dialog box as shown below, add the connection parameters using the below table.

   .. figure:: ../../../..//_assets/credential_store/create-snowflake-connection/choose-snowflake.png
      :alt: Credential Store
      :width: 65%


   .. list-table:: 
      :widths: 10 20 20
      :header-rows: 1


      * - Title
        - Description
        - Value
      * - Credential Store  
        - Select the Credential Store from drop-down
        - Choose specific Credential Store from drop-down or Select Do not use Credential Store
      * - Select Category
        - Select Category of Connection Type
        - Select Storage Connection
      * - Connection Type 
        - Select the Connection type from drop-down
        - Choose Snowflake as Connection Type
      * - Authentication Type 
        - Select the ``USER_CREDENTIAL`` or ``OAUTH``
        - Choose ``OAUTH`` as Authentication Type
      * - Connection Name
        - Connection Name
        - Add a unique Connection Name
      * - Url
        - Url for Snowflake
        - Url for Snowflake

  
   .. figure:: ../../../..//_assets/credential_store/create-snowflake-connection/connection-config-dialogbox.png
      :alt: Credential Store
      :width: 65%

  


Step 4 : Test and save the connection
------

#. After adding the parameters, click on **Test Connection** button to verify the connection.
#. Once the success notification is received, click on **Save** button to store the connection details.

   .. figure:: ../../../..//_assets/credential_store/create-snowflake-connection/oauth-parameters.png
      :alt: Credential Store
      :width: 65%

   Once you save the connection, resources can be used inside workflow editor etc. using the above connection.

  .. Note:: Make Sure Sparkflows User Login (Using OAuth) should have sufficient privilege of Snowflake resources.


Documentation
-----

Reference guide : https://docs.sparkflows.io/en/latest/snowflake/index.html









