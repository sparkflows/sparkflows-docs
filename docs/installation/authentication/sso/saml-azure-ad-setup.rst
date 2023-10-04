Azure AD SAML Setup
========

This documentation describes the steps you need to follow to set up SAML 2.0 with Azure AD. 

For more detailed information, please refer to the `Ping Identity documentation. <https://learn.microsoft.com/en-us/azure/active-directory/manage-apps/migrate-adfs-saml-based-sso>`_

Step 1: Get Started with Creating an Account
------

#. Visit the Azure website and create an account in Azure, if you donot have.

   .. figure:: ../../../_assets/authentication/pingid/ping_id.PNG
      :alt: sso
      :width: 40%
   
Step 2 : Sign On to Azure
------

#. Enter the **credentials** to sign on to your Azure Account.

   .. figure:: ../../../_assets/authentication/pingid/ping_id_1.PNG
      :alt: sso
      :width: 40%


Step 3 : Go to Administrators 
------

#. Click on **Administrators** in Environments.

   .. figure:: ../../../_assets/authentication/pingid/pingid_2.PNG
      :alt: sso
      :width: 50%

Step 4 : Go to Connections  
------

#. Click on **Connections**. This will display available options.

   .. figure:: ../../../_assets/authentication/pingid/pingid_3.PNG
      :alt: sso
      :width: 50%

Step 5 : Create new Application
------

#. Select **Applications**.  
#. Click on **+** sign.

   .. figure:: ../../../_assets/authentication/pingid/pingid_4.PNG
      :alt: sso
      :width: 50%

#. Add **Name** and **Description** of the Application.

   .. figure:: ../../../_assets/authentication/pingid/pingid_5.PNG
      :alt: sso
      :width: 50%
   
#. Choose Application Type as **SAML Application**.

   .. figure:: ../../../_assets/authentication/pingid/pingid_6.PNG
      :alt: sso
      :width: 50%
   
#. Provide Application Metadata:
   
    * Click on **Configure** and
    * Choose the method to provide metadata as per your configuration.
   
   .. figure:: ../../../_assets/authentication/pingid/pingid_7.PNG
      :alt: sso
      :width: 50%
   
#. Enter the **ACS URLs** and **Entity ID**. 

  
   .. figure:: ../../../_assets/authentication/pingid/ping_acs.PNG
      :alt: sso
      :width: 50%
      
#. Click **Save** to save the Application.     

Step 6: Update HTTP POST
------

#. Click on **Configure**.
#. Update the HTTP POST as ``urn:oasis:names:tc:SAML:2.0:nameid-format:persistent``

   .. figure:: ../../../_assets/authentication/pingid/http_post_1.PNG
      :alt: sso
      :width: 50%

Step 7 : Update Attribute Mappings
------

#. Click on **Attribute Mappings** and update the required details as below: 
   
    * fireUsername=UserName
    * emailID=EmailID
    * firstName=FirstName
    * samlSubject=saml_subject
    * lastName=LastName

 
   .. figure:: ../../../_assets/authentication/pingid/attribute_mapping.PNG
      :alt: sso
      :width: 50%
 
   
Step 8 : Download Metadata from Application
------

#. Activate the Application and download the Metadata from application. 
   
   This metadata will be used while configuring the Fire Insights.

   .. figure:: ../../../_assets/authentication/pingid/pingid_9.PNG
      :alt: sso
      :width: 50%

.. note::  Make sure to change the localhost to your domain name or your IP where Fire Insights is running.
