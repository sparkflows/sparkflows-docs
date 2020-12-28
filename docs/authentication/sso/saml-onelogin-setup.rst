SAML OneLogin setup
==============

Below are steps to setup SAML 2.0 OneLogin

1. Create an account at one Login 
2. SignIn into oneLogin


.. figure:: ../../_assets/authentication/oneLoginSignIn.png
   :alt: sso
   :align: center
   :width: 60%
	   
3. Go to administrator >> Click on applications menu >> 

.. figure:: ../../_assets/authentication/applications_menu.png
   :alt: sso
   :align: center
   :width: 60%
	   
4. Add an app

.. figure:: ../../_assets/authentication/addAppButton.png
   :alt: sso
   :align: center
   :width: 60%
   
5. Select an application
      a) Search application 'SAML Test Connector'
      b) Select the application SAML Test Connector (Advanced).
      
.. figure:: ../../_assets/authentication/searchApp.png
   :alt: sso
   :align: center
   :width: 60%
	    
6. Input an application name and save it.

.. figure:: ../../_assets/authentication/saveApp.png
   :alt: sso
   :align: center
   :width: 60%
   
7. Configure the newly created app and add below information:
	   a) Audience (EntityID)
	   b) Recipient
	   c) ACS (Consumer) URL Validator*
	   d) ACS (Consumer) URL*
	   e) Single Logout URL
	   f) Login URL
	   
.. figure:: ../../_assets/authentication/configuration.png
   :alt: sso
   :align: center
   :width: 60%
