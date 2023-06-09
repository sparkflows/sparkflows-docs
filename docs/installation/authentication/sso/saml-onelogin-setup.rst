OneLogin SAML Setup
==============

Below are the steps required to setup SAML 2.0 OneLogin.

For more detailed information, please refer to the `OneLogin documentation. <https://developers.onelogin.com/>`_

Step 1 : Get Started with Creating an Account
--------

#. Visit OneLogin official website and create an account at OneLogin.

Step 2 : Sign In to OneLogin 
--------

#. Enter the credentials to sign in to your OneLogin account.

   .. figure:: ../../../_assets/authentication/oneLoginSignIn.png
      :alt: sso
      :width: 60%
	   
Step 3 : Go to Administration and Open Applications
------

#. Click on **Administration**.
#. Click on **Applications**.

   .. figure:: ../../../_assets/authentication/applications_menu.png
      :alt: sso
      :width: 60%
	   
Step 4 : Add an Application
---------

#. Click on **Add App** to reach Application finder.
   
   .. figure:: ../../../_assets/authentication/addAppButton.png
      :alt: sso
      :width: 60%
   
Step 5 : Search and Select an Application
---------

#. Search for : **SAML Custom**
#. Select **Custom Connector (Advanced)**.
   
   Note: The SAML Custom Connector (Advanced) is the new name for the SAML Test Connector (Advanced).  
   
   .. figure:: ../../../_assets/authentication/search-app.png
      :alt: sso
      :width: 60%
	   
   

Step 6 : Input an Applictaion Name
-------------

#. Enter the desired **name** for the Application in the Display Name box.
#. Click on **Save** to save the application.

   .. figure:: ../../../_assets/authentication/saveApp.png
      :alt: sso
      :width: 60%
   
Step 7 : Configure the Application
----------

#. Configure to add the below information to the newly created Application:

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
