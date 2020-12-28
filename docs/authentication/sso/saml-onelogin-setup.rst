OneLogin setup
==============

Below are steps to setup OneLogin

1. Create an account at one Login 
2. SignIn into oneLogin


.. figure:: ../../_assets/authentication/oneLoginSignIn.png
   :alt: sso
   :align: center
   :width: 60%
	   
   3. Go to administrator >> Click on applications menu >> 
       <image: applications_menu>
	   
   3. Add an app
      <image: addAppButton> 
   4. Select an application
      a) Search application 'SAML Test Connector'
	  b) Select the application SAML Test Connector (Advanced).
	    <Image: searchApp>
    5. Input an application name and save it.
	   <image: saveApp>
	6. Configure the newly created app and add below information:
	   a) Audience (EntityID)
	   b) Recipient
	   c) ACS (Consumer) URL Validator*
	   d) ACS (Consumer) URL*
	   e) Single Logout URL
	   f) Login URL
	     <Image: configuration>
