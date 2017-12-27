Configuring HTTPS
=================

You can choose to run the FIRE project either on http or https connection. The only difference would be the port used in the url.
 
HTTP
----
 
    http://hostname:8080/login
 
HTTPS
-----
 
    https://hostname:8443/login
 
keystore.jks
------------
 
    Replace the keystore.jks in the conf directory with your newly generated one
 
keystore password
-----------------
 
    The keystore password is in the file conf/keystore.properties
 
 
**When the keystore is updated, the password also has to be updated in case it changes. The Sparkflows web server would also have to be restarted for the changes to take effect.**
 
 
 
 
