AWS Credential Store
=======================

Sparkflows allows users to securely access AWS resources by configuring the AWS Credential Store. Below are the steps to configure AWS Credential Store.

Prerequisites
----

- The private key must be stored in AWS Secrets Manager, following the format illustrated in the image below.

  .. figure:: ../../..//_assets/credential_store/snowflake-aws-secret-manager-file.png
      :alt: Azure Key Vault Private Key Format
      :width: 35%

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


Step 1 : Access Credential Store
-------------

* Login to **Sparkflows** as an admin user. 
* Navigate to **Administration -> Credential Store**, as shown below.

  .. figure:: ../../../_assets/credential_store/credentialstore-admin-page.PNG
     :alt: AWS Credential Store
     :width: 65%


Step 2 : Add Credential Store
------------------

* From the credential store page, click on **ADD CREDENTIAL STORE** button, as shown below.
  
  .. figure:: ../../../_assets/credential_store/add-credentialstore-button.png
     :alt: Credential Store
     :width: 65%

* Now select the option **Add Credential Store For All** from the dropdown. An Add Credential Store dialog box will open, as shown below.

  .. figure:: ../../../_assets/credential_store/aws-credential-store/aws_add_credentials_new.png
     :alt: aws-credential-store
     :width: 65%     
  

  .. Note:: Credential Stores can be added at both the **Global** and **Group** levels. To add a global Credential Store, select **Add Credential Store For All**. For group-level configuration, select **Add Credential Store For Group**.

Step 3 : Add Credential Store Parameters
--------------------------
* Enter the configuration details for Credential Store, as shown below, referring to the table for guidance. 

  .. figure:: ../../../_assets/credential_store/aws-credential-store/aws_add_credentials_tested.png
     :alt: aws-credential-store
     :width: 65%     

.. list-table:: Credential Store
   :widths: 20 80
   :header-rows: 1

   * - Parameter
     - Description
   * - STORE TYPE
     - Select AWS Secret Manager
   * - STORE NAME
     - Add any unique name.
   * - AWS ROLE ARN
     - Assume role ARN to access resources
   * - SECRET KEY
     - Secret Key (For Test Connection)
     

* After entering the parameters, click on **TEST CREDENTIAL STORE CONNECTION** button to verify the connection before saving it.




Step 4 : Save and View the Credential Store
------------------------
* Once the test is successful, click on **Save** button to save the configuration.

* Once the credential store has been created, you can view it in the list of credential stores, as shown below.

  .. figure:: ../../../_assets/credential_store/aws-credential-store/aws_add_credentials_list.png
     :alt: aws-credential-store
     :width: 65%  

Step 5 : Update the Credential Store (if Required)
------------------------

* Once the credential store for AWS Secrets Manager has been created, click on **edit (pen)** icon in the **Actions** column of the list.
* Modify the necessary fields in the dialog box shown below and click on **Update** button to save the changes.

  .. figure:: ../../../_assets/credential_store/aws-credential-store/aws_add_credentials_update.png
     :alt: aws-credential-store
     :width: 65%  
