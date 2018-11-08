Configuring HTTPS for Fire
==========================

The Fire server can listen on HTTPS. Fire Server comes with a pre-configured keystore.

Below are the steps for configuring Fire with your keystore and certificates.

Generate a Keystore
-------------------

You can use the following command for generating the Keystore::

    keytool -genkeypair -alias sparkflows -keyalg RSA -validity 365 -keystore keystore.jks

You will be prompted with the following questions and enter something similar to the SAMPLE answers::

    Enter keystore password: 
    Re-enter new password: 
    What is your first and last name?
      [Unknown]:  John Smith
    What is the name of your organizational unit?
      [Unknown]:  BigData
    What is the name of your organization?
      [Unknown]:  MyOrg
    What is the name of your City or Locality?
      [Unknown]:  San Francisco
    What is the name of your State or Province?
      [Unknown]:  California
    What is the two-letter country code for this unit?
      [Unknown]:  CA
    Is CN=John Smith, OU=BigData, O=MyOrg, L=San Francisco, ST=California, C=CA correct?
      [no]:  yes
    Enter key password for <sparkflows>
            (RETURN if same as keystore password): Press the return key or Type and note down the password

Copy the keystore into the Fire installation directory
----------------------------------------------

Copy the generated ``keystore.jks`` file into the ``conf`` folder of your installation.




