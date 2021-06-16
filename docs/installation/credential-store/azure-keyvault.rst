
Fire Insights is integrated with Azure KeyVault. Once configured you can use the Keyvault for accessing secret key from it.
Below are the steps for configuring Fire Insights with Azure KeyVault and using it for application connection.

Create Azure Key Vault at Azure portal
======================================

Create a Key Vault at Azure portal if you don't have any.

.. figure:: ../../_assets/credential_store/azure-keyvault-list.PNG
   :alt: Azure Key Vault
   :width: 90%

.. figure:: ../../_assets/credential_store/azure-keyvault-create.PNG
   :alt: Azure Key Vault
   :width: 90%

Add Secret Key in Key Vault
---------------
 Click on Generate/Import

.. figure:: ../../_assets/credential_store/azure-keyvault-secret-list.PNG
   :alt: Azure Key Vault
   :width: 90%

Add Secret Key and its Value.

.. figure:: ../../_assets/credential_store/azure_keyvault-create-secret.PNG
   :alt: Azure Key Vault
   :width: 90%

Configuring Azure Key Vault in Fire Insights
===========================

You can configure Azure Key Vault in Fire Insights.

Below are the steps for configuring Azure Key Vault.

Go to Administration/Credential Store
-------------

Login to Fire Insights application, Go to Administration and select Credential Store.

.. figure:: ../../_assets/credential_store/1.PNG
   :alt: Azure Key Vault
   :width: 90%

.. figure:: ../../_assets/credential_store/1.PNG
   :alt: Azure Key Vault
   :width: 90%

Add Credential Store
------------------

Click on ADD CREDENTIAL STORE tab


.. figure:: ../../_assets/credential_store/2.PNG
   :alt: Credential Store
   :width: 90%

Add Credential Store Parameter
--------------------------

.. list-table:: Credential Store
   :widths: 20 80
   :header-rows: 1

   * - Title
     - Description
   * - STORE TYPE
     - Select Connection Type from Drop down ie Azure KeyVault.
   * - STORE NAME
     - Add any unique name.
   * - CLIENT ID
     - Add Client Id for Azure account having access of KeyVault.
   * - SECRET KEY
     - Add Secret Key
   * - STORE URL
     - Azure KeyVault URI.
   * - DESCRIPTION
     - Add any description.
     

.. figure:: ../../_assets/credential_store/3_a.PNG
   :alt: Credential Store
   :width: 90%     

After Adding the above parameter, you can Click on TEST CREDENTIALSTORE CONNECTION, It will shows connected to Azure KeyVault and after saving it will show in Credential Store LIst.

.. figure:: ../../_assets/credential_store/4.PNG
   :alt: Credential Store
   :width: 90%     

.. figure:: ../../_assets/credential_store/5.PNG
   :alt: Credential Store
   :width: 90%     

.. figure:: ../../_assets/credential_store/6.PNG
   :alt: Credential Store
   :width: 90%   
   

