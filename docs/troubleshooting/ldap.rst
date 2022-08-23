LDAP
====

Fire can be configured to authenticate the user with LDAP. Below are some ways to troubleshoot the LDAP configurations.


Testing LDAP connection with ldapsearch
---------------------------------------

It is a good idea to test the ldap environment setup using ldapsearch. This ensures that the machine is setup correctly for LDAP - it can connect to the LDAP server, the LDAP username and passwords are correct, the SSL certificates are good if using LDAPS.

Testing Getting User Details from LDAP
--------------------------------------

* cd to your installation directory
* Create a properties file called ``ldaptestconfig.properties``

Below is an example::

  ldap_attributeUserName=myLdapUsername
  ldap_Order="DB_LDAP";
  ldap_URL="ldap://localhost:10389";
  ldap_base="dc=example,dc=com";
  ldap_userDn="uid=john,ou=bindusers,dc=example,dc=com";
  ldap_password="johnspassword";
  ldap_userSearchBase="ou=sparkflow";
  ldap_userSearchFilter="(uid={0})";
  ldap_groupSearchBase="ou=groups";
  ldap_groupSearchFilter="member={0}";

Fetch the user details for the user ``xyz`` with the following command::

  java -cp app/fire-ui-3.1.0.jar -Dloader.main=fireui.ldap.LDAPTest org.springframework.boot.loader.PropertiesLauncher xyz

What if I get locked out
------------------------

``ldap.Order`` determines the order in which Fire tries to log in the user.
In case you are locked out of Fire and are not able to log in, you can do the following:

* Add the below line to conf/configuration.properties
ldap.Order=DB

* Then restart the fire server. Now you should be able to log in with your admin account.

Once things are back to normal, you can remove the line you added to ``configuration.properties`` and restart the fire server.


Testing Getting User Details from LDAP via Python
-------------------------------------------------

Sample code for the same is as below:

  #! /usr/bin/python3
  import ldap

  # LDAP Attribute User Name-  LDAP Name of the attribute for User Name
  ldap_attributeUserName = "userName"

  # LDAP Url - URL to the ldap Server
  ldap_URL = "ldap://ldap.test.net:389"

  # LDAP Base - The point from where a server will search for users
  ldap_base = "dc=internal,dc=sytelreply,dc=com"

  # LDAP UserDn - A distinguished name of a user that will authenticate to the directory using a BIND request
  ldap_userDn = "uid=tns;ou=Users,dc=internal,dc=sytelreply,dc=com"

  # LDAP Password
  ldap_password = "password"

  # LDAP User Search Base - The location in the directory where the search for a particular directory object begins
  ldap_userSearchBase = "ou=Users"

  # LDAP User Search Filter - Define search criteria and provide more efficient and effective searches
  ldap_userSearchFilter = "(uid={0})"

  # LDAP Group Search Base
  ldap_groupSearchBase = "ou=Users"

  # LDAP Group Search Filter
  ldap_groupSearchFilter = "member={0}"



  def initLdapConnection():
      print('initialize ldap connection')
      conn = ldap.initialize(ldap_URL)
      try:
          conn.protocol_version = ldap.VERSION3
          conn.simple_bind_s(ldap_userDn, ldap_password)
          criteria = "(&(objectClass=account)(uid=*))"

          res = conn.search_s(ldap_base, ldap.SCOPE_SUBTREE)
          for dn, entry in res:
              print(dn)
              print(entry)

      except Exception as error:
          print(error)

  if __name__ == '__main__':
      initLdapConnection()
