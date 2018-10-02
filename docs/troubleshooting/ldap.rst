LDAP
====

Fire can be configured to authenticate the user with LDAP.


Testing LDAP connection with ldapsearch
---------------------------------------

It is a good idea to test the ldap environment setup using ldapsearch.

What if I get locked out
------------------------

``ldap.Order`` determines the order in which Fire tries to log in the user.
In case you are locked out of Fire and are not able to log in, you can do the following:

* Add the below line to conf/configuration.properties
ldap.Order=DB

* Then restart the fire server. Now you should be able to log in with your admin account.

Once things are back to normal, you can remove the line you added to ``configuration.properties`` and restart the fire server.

