Azure AD SAML Setup
========

This documentation describes the steps you need to follow to set up SAML with Azure AD. 

For more detailed information, please refer to the `Azure AD SAML documentation. <https://learn.microsoft.com/en-us/azure/active-directory/manage-apps/migrate-adfs-saml-based-sso>`_

Step 1: Get Started with Creating an Account
------

#. Visit the Azure website and create an account in Azure, if you donot have.

   .. figure:: ../../../_assets/authentication/azure-ad/azure_signin.PNG
      :alt: sso
      :width: 40%
   
Step 2 : Sign On to Azure
------

#. Enter the **credentials** to sign on to your Azure Account.

   .. figure:: ../../../_assets/authentication/azure-ad/azure_signin.PNG
      :alt: sso
      :width: 40%


Step 3 : Go to Azure AD 
------

#. Click on **Enterprise applications**.

   .. figure:: ../../../_assets/authentication/azure-ad/azure_ad.PNG
      :alt: sso
      :width: 50%

Step 4 : Click on **New application**.
------

#. Click on **New application**.

   .. figure:: ../../../_assets/authentication/azure-ad/azure_app_register.PNG
      :alt: sso
      :width: 50%

Step 5 : Create your own application
------

#. Select **Integrate any other application you don't find in the gallery (Non-gallery)**.  
#. Add **Name** of the Application.
#. Click on **create**.

   .. figure:: ../../../_assets/authentication/azure-ad/azure_app_register.PNG
      :alt: sso
      :width: 50%

Step 6 : Create your Single sign-on
------

 #. Click on **Single sign-on**.

   .. figure:: ../../../_assets/authentication/azure-ad/azure_single_signon.PNG
      :alt: sso
      :width: 50%
   
#. Select **SAML**.
   
       
   .. figure:: ../../../_assets/authentication/azure-ad/azure_saml_page.PNG
      :alt: sso
      :width: 50%
   
#. Enter the **ACS URLs** and **Entity ID**. 

  
   .. figure:: ../../../_assets/authentication/azure-ad/azure_single_signon.PNG
      :alt: sso
      :width: 50%
      
#. Click **Save** to save the Application.     


Step 7 : Add Users and groups
------

#. Click on **Add Users and groups** and add users and group which need to have access of the application: 
       
   .. figure:: ../../../_assets/authentication/azure-ad/azure_adduser_group.PNG
      :alt: sso
      :width: 50%
 
   
Step 8 : Download Metadata from Application
------

#. Download the Metadata from application. 
   
   This metadata will be used while configuring the Fire Insights.

   .. figure:: ../../../_assets/authentication/azure-ad/azure_metadata.PNG
      :alt: sso
      :width: 50%

.. note::  Make sure to change the sparkflows_dns to your domain name or your IP where Fire Insights is running.
