
Configuring Azure Key Vault
===========================

You can configure Azure Key Vault in Fire Insights. Below are the steps for configuring Azure Key Vault:

Step 1 : Navigate to Credential Store
-------------

* Login to **Fire Insights** as an admin user. 
* Go to **Administration** and select **Credential Store**, as shown below.

  .. figure:: ../../_assets/credential_store/admin-credentialstore.PNG
     :alt: Azure Key Vault
     :width: 65%


Step 2 : Add Credential Store
------------------

* On the Credential Store page, click on **Add Credential Store** button. 

  .. figure:: ../../_assets/credential_store/credential-store-page.png
     :alt: Credential Store
     :width: 65%

  An Add Credential Store dialog box will open, as shown below.

   .. figure:: ../../_assets/credential_store/credential_store_1.PNG
      :alt: Credential Store
      :width: 65%     


Step 3 : Add Credential Store Parameters
--------------------------
* Enter the required parameters in the above dialog box referring to the below table:

.. list-table:: **Credential Store**
   :widths: 20 80
   :header-rows: 1

   * - Title
     - Description
   * - STORE TYPE
     - Select Azure Key Vault.
   * - STORE NAME
     - Add any unique name.
   * - CLIENT ID
     - Add Client ID for Azure account which has access to Key Vault.
   * - SECRET KEY
     - Add Secret Key
   * - STORE URL
     - Azure KeyVault URL.
   * - DESCRIPTION
     - Add any description.
     

* After adding the above parameters, you can click on **Test Credential Store Connection** button to verify the connection before saving it.


  .. figure:: ../../_assets/credential_store/credential_store_2.PNG
     :alt: Credential Store
     :width: 65%     

  .. figure:: ../../_assets/credential_store/credential_store_3.PNG
     :alt: Credential Store
     :width: 65%     

Step 4 : View Created Credential Store
------------------------

* Once the credential store has been created, you can view it in the **list** of credential stores, as shown below.

  .. figure:: ../../_assets/credential_store/credential-store-list.png
     :alt: Credential Store
     :width: 65%   
   

