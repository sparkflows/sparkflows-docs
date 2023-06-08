OneLogin SAML Setup
==============

Below are steps to setup SAML 2.0 OneLogin:

#. Create an **account** at OneLogin. 
#. **Sign in** to OneLogin.


   .. figure:: ../../../_assets/authentication/oneLoginSignIn.png
      :alt: sso
      :width: 60%
	   
#. Go to **Administrator**. 
#. Click on **Applications** menu.

   .. figure:: ../../../_assets/authentication/applications_menu.png
      :alt: sso
      :width: 60%
	   
4. Add an application.

   .. figure:: ../../../_assets/authentication/addAppButton.png
      :alt: sso
      :width: 60%
   
5. Select an application:

    * Search application **SAML Custom**.
    * Select **Custom Connector (Advanced)**.
      
   .. figure:: ../../../_assets/authentication/search-app.png
      :alt: sso
      :width: 60%
	   
   Note: The SAML Custom Connector (Advanced) is the new name for the SAML Test Connector (Advanced)  

6. Input an application **name** and **save** it.

   .. figure:: ../../../_assets/authentication/saveApp.png
      :alt: sso
      :width: 60%
   
7. Configure the newly created application to add the below information:

    * Audience (EntityID)
    * Recipient
    * ACS (Consumer) URL Validator
    * ACS (Consumer) URL
    * Single Logout URL
    * Login URL
	   
   .. figure:: ../../../_assets/authentication/configuration.png
      :alt: sso
      :width: 60%

.. note::  Make sure to change the localhost to your domain name or your IP, where Fire is Running.
