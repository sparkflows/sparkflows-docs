Customize Docker Image for SSL Configuration
============================================

Sparkflows uses SSL keystore for configuring the HTTPS in Spring boot application. In order to provide a custom keystore, we need to import the SSL Certificate into the keystore using the Java keytool and then add them in conf directory, while building the docker image.

Steps
--------

* **Import the existing certificate into the keystore.** ::

    keytool -import -trustcacerts -alias <Name of Cert> -file /path/to/certificate.crt -keystore /path/to/keystore.jks -storepass <KEYSTORE_PASSWORD>


* **Store this new keystore in the conf directory of the Docker context.**

* **Build the image using the following command.** ::

    docker build --build-arg SPARK_VERSION=3.2.1 \
    --build-arg FIRE_VERSION=3.1.0 \
    -t sparkflows/sparkflows


* **Set the environment variable, with the correct keystore password while running the container.** ::

    docker run -p 8080:8080 -p 9443:9443 \
    -e KEYSTORE_PASSWORD=<keystore_password> \
    -e FIRE_HTTP_PORT=8080 \
    -e FIRE_HTTPS_PORT=9443 \
    -e FIRE_VERSION=${FIRE_VERSION} \
    sparkflows/fire:py_${SPARK_VERSION}_${RELEASE_VERSION}
