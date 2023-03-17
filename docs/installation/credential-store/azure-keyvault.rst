
Configuring Azure Key Vault
===========================

You can configure Azure Key Vault in Fire Insights. Below are the steps for configuring Azure Key Vault:

Go to Administration -> Credential Store
-------------

Login to Fire Insights application as an admin user. Go to ``Administration`` and select ``Credential Store``.

.. figure:: ../../_assets/credential_store/credential_store_5.PNG
   :alt: Azure Key Vault
   :width: 65%


Add Credential Store
------------------

Click on the ``ADD CREDENTIAL STORE`` button.


.. figure:: ../../_assets/credential_store/credential_store_6.PNG
   :alt: Credential Store
   :width: 65%

Add Credential Store Parameters
--------------------------

.. list-table:: Credential Store
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
     

.. figure:: ../../_assets/credential_store/credential_store_1.PNG
   :alt: Credential Store
   :width: 65%     

After adding the above parameters, you can click on ``TEST CREDENTIAL STORE CONNECTION`` to verify the connection before saving it.


.. figure:: ../../_assets/credential_store/credential_store_2.PNG
   :alt: Credential Store
   :width: 65%     

.. figure:: ../../_assets/credential_store/credential_store_3.PNG
   :alt: Credential Store
   :width: 65%     

Credential Store Created
------------------------

Once the credential store has been created, you can view it in the list of credential stores.

.. figure:: ../../_assets/credential_store/credential_store_4.PNG
   :alt: Credential Store
   :width: 65%   
   

