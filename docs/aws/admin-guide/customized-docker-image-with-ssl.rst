Customize Docker Image for SSL Configuration
============================================

Sparkflows uses SSL keystore for configuring the HTTPS in Spring boot application. In order to provide a custom keystore, we need to import the SSL Certificate into the keystore using the Java keytool and then add them in conf directory, while building the docker image.

Below are the required steps:


Step 1 : Import Existing Certificate into Keystore
----------------------

#. The following OpenSSL command combines the keys in privkey.pem and the certificate in the fullchain.pem file into the sparkflows.pkcs12 file::

        $ openssl pkcs12 -inkey privkey.pem -in fullchain.pem -export -out sparkflows.pkcs12
        
   Note: This is not going to work with publicly managed AWS certificates, as AWS doesn’t expose the private keys which are required for importing into the keystore. 

#. If you have a chain of certificates, because your CA is an intermediary, build the PKCS12 file as follows::

        $ cat example.crt intermediate.crt [intermediate2.crt] ... rootCA.crt > fulchain.pem
        $ openssl pkcs12 -export -inkey privkey.pem -in fullchain.pem -out sparkflows.pkcs12

#. OpenSSL asks for an export password. A non-empty password is required to make the next step work. Load the resulting PKCS12 file into a JSSE keystore   with keytool::

        $ keytool -importkeystore -srckeystore sparkflows.pkcs12 -srcstoretype PKCS12 -destkeystore keystore.jks

#. If you imported the key and certificate originally using the PKCS12 method, use an alias of "1" rather than "sparkflows", because that is the alias the     PKCS12 process enters into the keystore::


            keytool -import -trustcacerts -alias <Name of Cert> -file /path/to/certificate.crt -keystore /path/to/keystore.jks -storepass <KEYSTORE_PASSWORD>
            
#. Finally make sure you've updated the sso.saml.properties file , as below::
    
         server.keystore.alias=1


#. Store this new keystore in the conf directory of the Docker context.

Step 2 : Build Image
----------------

#. Build the image using the following command: ::

    docker build --build-arg SPARK_VERSION=3.2.1 \
    --build-arg FIRE_VERSION=3.1.0 \
    -t sparkflows/sparkflows

Step 3 : Set Environment Variable
------------------
#. Set the environment variable, with the correct keystore password while running the container using the below: ::

    docker run -p 8080:8080 -p 9443:9443 \
    -e KEYSTORE_PASSWORD=<keystore_password> \
    -e FIRE_HTTP_PORT=8080 \
    -e FIRE_HTTPS_PORT=9443 \
    -e FIRE_VERSION=${FIRE_VERSION} \
    sparkflows/fire:py_${SPARK_VERSION}_${RELEASE_VERSION}
