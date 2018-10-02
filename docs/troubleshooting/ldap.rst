LDAP
====

Fire can be configured to authenticate the user with LDAP.


Testing LDAP connection with ldapsearch
---------------------------------------

It is a good idea to test the ldap environment setup using ldapsearch.

Testing Getting User Details from LDAP
--------------------------------------

Create a properties file called ``ldaptestconfig.properties``

Below is an example:

ldap_attributeUserName=myLdapUsername
ldap_Order = "DB";
ldap_URL = "ldap://localhost:10389";
ldap_base = "dc=example,dc=com";
ldap_userDn = "uid=john,ou=bindusers,dc=example,dc=com";
ldap_password = "johnspassword";
ldap_userSearchBase = "ou=sparkflow";
ldap_userSearchFilter = "(uid={0})";
ldap_groupSearchBase = "ou=groups";
ldap_groupSearchFilter = "member={0}";

Fetch some user details with the following command:

- java -cp app/fire-ui-3.1.0.jar fireui.ldap.LDAPTest username


What if I get locked out
------------------------

``ldap.Order`` determines the order in which Fire tries to log in the user.
In case you are locked out of Fire and are not able to log in, you can do the following:

* Add the below line to conf/configuration.properties
ldap.Order=DB

* Then restart the fire server. Now you should be able to log in with your admin account.

Once things are back to normal, you can remove the line you added to ``configuration.properties`` and restart the fire server.

