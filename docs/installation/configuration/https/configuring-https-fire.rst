Configuring HTTPS for Fire
==========================

Fire server can listen on HTTPS. Fire server comes with a pre-configured Keystore.

Below are the steps for configuring Fire with your Keystore and certificates:

Generate Keystore
-------------------

You can use the following command for generating the Keystore::

 keytool -genkey -keyalg RSA -alias sparkflows -keystore keystore.jks -validity 365 -keysize 2048 -ext san=ip:< host machine ip address>

You will be prompted with the following questions where you can enter something similar to the below sample answers::

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

Copy Keystore to Installation Directory
----------------------------------------------

Copy the generated ``keystore.jks`` file into the ``conf`` folder of Fire installation directory. 

Update Keystore Password
----------------------------

Update keystore.properties to udpdate the password of the new keystore.jks file::

    keystore.password=123456

Configuring Port Number
-----------

Fire by default listens on port 8443 for HTTPS.

This is configured in the file ``conf/application.properties``::

  #Configure http and https port numbers : Default 8080 for http and 8443 for https
  http.port=8080
  https.port=8443

Restart Fire Server
-------------------------------

Finally, restart the Fire server for the changes to take effect::

  ./run-fire-server.sh stop
  ./run-fire-server.sh start


Configuring with PFX file
-------------------------

* Place the PFX file into the conf folder.
* Edit keystore.properties to update the field keystore.path and keystore.password
* Edit sso.saml.properties to update the field server.keystore.location, server.keystore.alias, server.keystore.password

* Run the below command to get the certificate details::
  
  ./run-fire-server.sh stop
  ./run-fire-server.sh start






