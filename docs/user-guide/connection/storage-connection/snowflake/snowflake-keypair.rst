Snowflake Key-Pair Authentication
=======

Sparkflows provides the capability to create "Snowflake Connection" and use the connection to access various resources using Key-Pair Authentication.

Pre-requisites
-------------

- the private key is stored in AWS Secrets Manager, 
- the configured ARN must have the **secretsmanager:GetSecretValue** permission to retrieve the secret.
- Sparkflows machine would have access to ARN

How to create private key and configure it in snowflake
---------------------------------------

Snowflake supports using key pair authentication for enhanced authentication security as an alternative to basic authentication, such as username and password.

Reference guide : `Configuring key-pair authentication in Snowflake. <https://docs.snowflake.com/en/user-guide/key-pair-auth>`_   


Configuring Credential Store 
-------------
- If a user wants to configure AWS Secrets Manager for Snowflake authentication, they need to create a credential store and configure it in the connection settings.
- If the user wants to test and use a different ARN for accessing the Secrets Manager, they can configure it in the credentials store.
- By default, the ARN configured at the user group level will be used to fetch AWS secrets.


   .. figure:: ../../../..//_assets/credential_store/create-snowflake-connection/snowflake_credential_store.png
      :alt: Credential Store
      :width: 65%

Follow the steps below to create a **Snowflake connection using Key-Pair Authentication**:

Step 1 : Navigate to Connections Page
-------------

#. Login to **Fire Insights** using your credentials.
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
#. In 'Add Connection' dialog box as shown below, add the connection parameters using the below table for **key-pair** authentication.

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
        - Select the ``USER_CREDENTIAL``, ``OAUTH`` or ``KEY-PAIR``
        - Choose ``KEY-PAIR`` as Authentication Type
      * - Connection Name
        - Connection Name
        - Add a unique Connection Name
      * - Url
        - Url for Snowflake
        - Url for Snowflake
      * - User Name
        - User Name for the connection
        - Enter the Username for the selected connection
      * - Secret Key Name
        - Secret Key Name for the connection
        - Enter the Secret Key Name for the selected connection

  
   .. figure:: ../../../..//_assets/credential_store/create-snowflake-connection/snowflake_key_pair_auth.png
      :alt: Credential Store
      :width: 65%

  


Step 4 : Test and Save the connection
------

#. After adding the parameters, click on **Test Connection** button to verify the connection.
#. Once the success notification is received, click on **Save** button to store the connection details.

   .. figure:: ../../../..//_assets/credential_store/create-snowflake-connection/sf-connection-test.png
      :alt: Credential Store
      :width: 65%


   Once you save the connection, resources can be used inside workflow editor etc. using the above connection.

  .. Note:: Make Sure Sparkflows User Login (Using Key-Pair) should have sufficient privilege of Snowflake resources.

 
Documentation
-----

Reference guide : `Snowflake User Guide Documentation. <https://docs.sparkflows.io/en/latest/snowflake/index.html>`_   
