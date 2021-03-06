
Configuring Azure Key Vault in Fire Insights
===========================

You can configure Azure Key Vault in Fire Insights.

Below are the steps for configuring Azure Key Vault.

Go to Administration/Credential Store
-------------

Login to Fire Insights application as an admin user. Go to Administration and select Credential Store.

.. figure:: ../../_assets/credential_store/1.PNG
   :alt: Azure Key Vault
   :width: 90%


Add Credential Store
------------------

Click on the ADD CREDENTIAL STORE button


.. figure:: ../../_assets/credential_store/2.PNG
   :alt: Credential Store
   :width: 90%

Add Credential Store Parameters
--------------------------

.. list-table:: Credential Store
   :widths: 20 80
   :header-rows: 1

   * - Title
     - Description
   * - STORE TYPE
     - Select Azure Key Vault
   * - STORE NAME
     - Add any unique name
   * - CLIENT ID
     - Add Client Id for Azure account which has access to Key Vault
   * - SECRET KEY
     - Add Secret Key
   * - STORE URL
     - Azure KeyVault URI
   * - DESCRIPTION
     - Add any description
     

.. figure:: ../../_assets/credential_store/3_a.PNG
   :alt: Credential Store
   :width: 90%     

After Adding the above parameters, you can Click on TEST CREDENTIAL STORE CONNECTION.


.. figure:: ../../_assets/credential_store/4.PNG
   :alt: Credential Store
   :width: 90%     

.. figure:: ../../_assets/credential_store/5.PNG
   :alt: Credential Store
   :width: 90%     

Credential Store Created
------------------------

Once the Credential store has been created you can view it in the list of Credential Stores.

.. figure:: ../../_assets/credential_store/6.PNG
   :alt: Credential Store
   :width: 90%   
   

