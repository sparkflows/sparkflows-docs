Snowflake Key-Pair Authentication
=======

Sparkflows provides the capability to create Snowflake Connection and use the connection to access various resources using **Key-Pair Authentication** with credentials stores like **AWS Secrets Manager** and **Azure Key Vault**.

Prerequisites
-------------
When using AWS Secrets Manager Credential Store
++++
- The private key is stored in AWS Secrets Manager. 
- The configured ARN must have the **secretsmanager:GetSecretValue** permission to retrieve the secret.
- Sparkflows machine would have access to ARN.

The ARN should have below permission:

::

    {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue",
                "secretsmanager:ListSecrets",
                "secretsmanager:DescribeSecret"
            ],
            "Resource": "arn:aws:secretsmanager:us-east-1:xxxxxx:secret:snowflake_key-*"
        }
    ]
  }

When using Azure Key Vault Credential Store
++++
- The private key is stored in Azure Key Vault.

The following formats are supported for storing private keys in Azure Key Vault :

**Format 1 -** If the key must includes the lines **-----BEGIN PRIVATE KEY-----** and **-----END PRIVATE KEY-----** ,then make sure to place key strictly between them on separate lines.

.. figure:: ../../../..//_assets/credential_store/sf-azure-key-valut-key-format-1.png
      :alt: Azure Key Vault Private Key Format
      :width: 35%

**Format 2 -** The key can also be added in the format where the lines **-----BEGIN PRIVATE KEY-----** and **-----END PRIVATE KEY-----** are not included, and only the key content is provided.

.. figure:: ../../../..//_assets/credential_store/sf-azure-key-valut-key-format-2.png
      :alt: Azure Key Vault Private Key Format
      :width: 35%

How to create private key and configure it in snowflake
---------------------------------------

Snowflake supports using key pair authentication for enhanced authentication security as an alternative to basic authentication, such as username and password.

Reference guide : `Configuring key-pair authentication in Snowflake. <https://docs.snowflake.com/en/user-guide/key-pair-auth>`_   


Configuring Credential Store 
-------------
**For AWS Secrets Manager**
++++++++++++++++++++++++++++++++

- If a user wants to configure AWS Secrets Manager for Snowflake authentication, they need to create a credential store and configure it in the connection settings.
- If the user wants to test and use a different ARN for accessing the Secrets Manager, they can configure it in the credentials store.
- By default, the ARN configured at the user group level will be used to fetch AWS secrets.


  .. figure:: ../../../..//_assets/credential_store/create-snowflake-connection/snowflake_credential_store.png
      :alt: Credential Store
      :width: 65%

Reference guide : `AWS Credentials Store Creation Documentations. <https://docs.sparkflows.io/en/latest/installation/credential-store/aws/index.html>`_

**For Azure Key Vault**
++++++++++++++++++++++++++

- If a user wants to configure Azure Key Vault for Snowflake authentication, they need to create a credential store and then select that credential store during connection creation.

  .. figure:: ../../../../_assets/credential_store/credential_store_2.PNG
      :alt: Credential Store
      :width: 65%  

  .. figure:: ../../../../_assets/credential_store/credential_store_3.PNG
      :alt: Credential Store
      :width: 65%  

Reference guide : `Configuring Azure Key Vault Credential Store. <https://docs.sparkflows.io/en/latest/installation/credential-store/azure-keyvault.html>`_ 


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
        - Enter the Secret Key Name for the selected connection in the format **$mysecret**


**Using AWS Secret Manager Credential Store** 

In the below image, a snowflake connection of type key-pair has been configured and is having the credential store of AWS Secrets Manager.

.. figure:: ../../../..//_assets/credential_store/create-snowflake-connection/snowflake_key_pair_auth.png
         :alt: Credential Store
         :width: 65%

**Using Azure Key Vault Credential Store**

In the below image, a snowflake connection of type key-pair has been configured and is having the credential store of Azure Key Vault.

.. figure:: ../../../..//_assets/credential_store/create-snowflake-connection/Snowflake-KeyPair-AzureKeyVault-Conn.png
         :alt: Credential Store
         :width: 65%
 


Step 4 : Test and Save the connection
------

#. After adding the parameters, click on **Test Connection** button to verify the connection.
#. Once the success notification is received, click on **Save** button to store the connection details.

   **For AWS Secret Manager Credential Store** 

   .. figure:: ../../../..//_assets/credential_store/create-snowflake-connection/sf-connection-test.png
      :alt: Credential Store
      :width: 65%

   **For Azure Key Vault Credential Store**

   .. figure:: ../../../..//_assets/credential_store/create-snowflake-connection/Snowflake-KeyPair-AzureKeyVault-Test.png
     :alt: Credential Store
     :width: 65%

   Once you save the connection, resources can be used inside workflow editor for snowflake nodes, in snowflake db editor, etc. using the above connection.

  .. Note:: 1. Please ensure that the Snowflake URL is accessible from the Sparkflows machine.

       2. Please ensure that the Sparkflows user login (using key-pair authentication) has sufficient privileges to access the required Snowflake resources.

       3. Please ensure that for the selected execution mode, the Snowflake key pair is accessible to the compute environment being used — such as Amazon EMR or any other specific compute engine.


 
Documentation
-----

Reference guide : `Snowflake User Guide Documentation. <https://docs.sparkflows.io/en/latest/snowflake/index.html>`_   
