SSL Certificate Setup
=====================

This document outlines the steps to use a trusted SSL certificate for the fire server, which uses a ``keystore.jks`` to manage certificates. 

By default, Fire Insights uses a self-signed certificate, which can lead to certificate validation issues when accessing it via HTTPS in a browser. To resolve this, you can configure Fire Insights to use a valid certificate.

Pre-Requisites
---------

In order to configure a valid certificate in Fire Insights, the following pre-requisites are needed:

#. Valid Certificate in JKS format
#. Keystore Password
#. Server Keystore Alias



1. Obtain a Trusted SSL Certificate
---------------------------------------

You will need to obtain an SSL certificate from a trusted Certificate Authority (CA). You can choose a free CA like **Let's Encrypt**.

Once you have obtained the certificate, you will have the following files:

- Certificate (``your_domain.crt`` or ``your_domain.pem``)
- Private Key (``your_domain.key``)
- CA Bundle or Intermediate Certificate (if provided by your CA, typically ``ca_bundle.crt``)

2. Convert Certificate to PKCS12 Format
--------------------------------------------

The following command will convert your certificate and private key into a PKCS12 keystore:

.. code-block:: bash

    openssl pkcs12 -export \
      -in your_domain.crt \
      -inkey your_domain.key \
      -out keystore.p12 \
      -name your_alias \
      -CAfile ca_bundle.crt \
      -caname root

This command will generate a ``keystore.p12`` file containing your certificate, private key, and CA bundle.

3. Convert PKCS12 to JKS Keystore
---------------------------------------

Next, we'll have to convert the PKCS12 keystore into Java Keystore (JKS) format. Run the following command:

.. code-block:: bash

    keytool -importkeystore \
      -deststorepass your_password \
      -destkeypass your_password \
      -destkeystore keystore.jks \
      -srckeystore keystore.p12 \
      -srcstoretype PKCS12 \
      -alias your_alias

This will create a new ``keystore.jks`` that includes the trusted SSL certificate. Replace this in the ``conf/`` folder of the home directory of the Fire installation.

4. Update keystore.properties File
----------------------------------------

Update the ``conf/keystore.properties`` file to reflect the path and password of the newly generated ``keystore.jks``:

.. code-block:: properties

    keystore.path=./conf/keystore.jks
    keystore.password=your_password

5. Update sso.saml.properties
--------------

.. code-block:: properties

    server.keystore.alias=alias name
    server.keystore.password=keystore_password
    server.keystore.location=./conf/keystore.jks
    



Conclusion
----------

After completing these steps, the SSL certificate is ready to be used.

