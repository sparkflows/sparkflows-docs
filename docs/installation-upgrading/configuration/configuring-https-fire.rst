Configuring HTTPS for Fire
==========================

The Fire server can listen on HTTPS. Fire Server comes with a pre-configured keystore.

Below are the steps for configuring Fire with your keystore and certificates.

Generate a Keystore
-------------------

As an example you can use the following command for generating the Keystore:

* keytool ....

Configure Keystore and Password for Fire Server
-----------------------------------------------

Configure it in the file ``fire.conf``


Configure the Certificate into Fire Web Server
----------------------------------------------

Configure the certificate into the Fire Web Server too.

Configure it in ``applications.conf``

