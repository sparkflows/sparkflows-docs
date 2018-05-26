Configuring HTTPS for Fire
==========================

The Fire server can listen on HTTPS. Fire Server comes with a pre-configured keystore.

Below are the steps for configuring Fire with your keystore and certificates.

Generate a Keystore
-------------------

You can use the following command for generating the Keystore:

keytool -genkeypair -alias sparkflows -keyalg RSA -validity 365 -keystore keystore.jks

You will be prompted with the following questions and enter something similar to the SAMPLE answers:

Enter keystore password: fireServer2018
Re-enter new password: fireServer2018
What is your first and last name?
  [Unknown]:  Ashok Rajan
What is the name of your organizational unit?
  [Unknown]:  BigData on AWS
What is the name of your organization?
  [Unknown]:  SparkFlows.io
What is the name of your City or Locality?
  [Unknown]:  Austin
What is the name of your State or Province?
  [Unknown]:  Texas
What is the two-letter country code for this unit?
  [Unknown]:  TX
Is CN=Ashok Rajan, OU=BigData on AWS, O=SparkFlows.io, L=Austin, ST=Texas, C=TX correct?
  [no]:  yes

Enter key password for <sparkflows>
        (RETURN if same as keystore password): Press the return key or Type and note down the password

Copy the keystore into Fire project
----------------------------------------------

Copy the generated keystore.jks file into the src folder and place it in a classpath to reference it from the .java server or client codes.

Server Code is available in the package file fire.httpserver.ssl.FireHttpsServer. Recommend to place the keystore file under this package for easy reference from the server code. This location of keystore can also be externalized in a config file so that in production scenarios, the keystore from customers can be used. Use the following command to run the SSL based FireServer:

java FireHttpsServer fire.httpserver.service.HadoopService /hadoop 

The client side of code to create a SSL communication is available in fire.httpserver.ssl.HttpsClient. 

Its recommended to modularize the code into a separate class that implements IService, similar to fire.httpserver.service.HadoopService and use the implementation class in the Server code to keep the Server code de-coupled from business logic.

