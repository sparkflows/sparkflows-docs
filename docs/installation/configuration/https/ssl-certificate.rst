SSL Certificate Setup
=====================

This guide outlines the steps to configure a trusted SSL certificate for the Fire Server, which uses keystore.jks to manage certificates. By default, Fire Insights ships with a self-signed certificate, which can lead to browser warnings when accessed via HTTPS. To avoid these issues, you can replace the self-signed certificate with a trusted one.

Pre-Requisites
---------

In order to configure a valid certificate in Fire Insights, the following pre-requisites are needed:

#. Valid Certificate in JKS format
#. Keystore Password
#. Server Keystore Alias



1. Obtain a Trusted SSL Certificate
---------------------------------------

To secure Fire Insights with HTTPS, you need an SSL certificate from a trusted Certificate Authority (CA), such as Let's Encrypt or a commercial CA. Once obtained, you should have the following files:

- Certificate (``your_domain.crt`` or ``your_domain.pem``)
- Private Key (``your_domain.key``)
- CA Bundle or Intermediate Certificate (if provided by your CA, typically ``ca_bundle.crt``)

2. Convert Certificate to PKCS12 Format
--------------------------------------------

Use the following command to convert your certificate and private key into a PKCS12 keystore format, which Java supports:

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

Update the ``conf/sso.saml.properties`` file to reflect the alias, path and password of the newly generated ``keystore.jks``:


.. code-block:: properties

    server.keystore.alias=alias name
    server.keystore.password=keystore_password
    server.keystore.location=./conf/keystore.jks
    



Conclusion
----------

After following these steps, Fire Insights will be configured to use your trusted SSL certificate. You can now access the application via HTTPS without certificate validation warnings in browsers.

