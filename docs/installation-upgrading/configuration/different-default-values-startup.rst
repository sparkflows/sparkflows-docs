Different Default Values on Startup
===================================

Administration / Configuration
===============================

 
Fire has a number of properties under Administration / Configuration.

If you would like to populate these with different default values on initial install, the below steps can be followed:

 * Update the file **conf/configuration.properties** with the new values
 * Run **create-h2-db.sh or create-mysql-db.sh after that**

**(Please note that the file has to be updated with the new values before running the db creation script)**


Now the default values are populated with the values provided in configuration.properties.

Fire comes with a conf/configuration.properties file. It has minimal values in it.

