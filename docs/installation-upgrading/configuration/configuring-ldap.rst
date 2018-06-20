Configuring LDAP
================

Sparkflows can be configured to authenticate the user against LDAP.

The following configurations have to be set appropriately.


.. figure:: ../../_assets/installation/ldap-order.png
   :scale: 100%
   :alt: Sparkflows Ldap Order
   :align: center
   

LDAP Parameters
---------------


.. list-table:: LDAP Parameters
   :widths: 10 30 15
   :header-rows: 1

   * - Name of Parameter
     - Description
     - Example
   * - ldap.Order
     - Order in which to authenticate the user. Possible values are DB, LDAP_DB, DB_LDAP.
     - 
   * - ldap.URL
     - The URL of the LDAP server. The URL must be prefixed with ldap:// or ldaps://. The URL can optionally specify a custom port, for example: ldaps://ldap_server.example.com:1636.
     - ldap://localhost:10389
   * - ldap.Base
     - The distinguished name to use as a search base for finding users and groups. This should be similar to ‘dc=sparkflows,dc=com’.
     - dc=sparkflows,dc=com
   * - ldap.UserDn
     - Distinguished name of the user to bind as. This is used to connect to LDAP/AD for searching user and group information. This may be left blank if the LDAP server supports anonymous binds.
     - uid=john,ou=development,dc=sparkflows,dc=com
   * - ldap.Password
     - The password of the bind user.
     - xyz
   * - ldap.UserSearchBase
     - User Search Base
     - ou=development
   * - ldap.UserSearchFilter
     - The base filter for searching for users. For Active Directory, this is typically ‘(objectClass=user)’.
     - For Active Directory : (objectClass=user)     Other Example : (uid={0})
   * - ldap.GroupSearchBase
     - Group Search Base
     - ou=groups
   * - ldap.GroupSearchFilter
     - Group Search Filter
     - For Active Directory : (objectClass=group)     Other Example : (member={0})
     
Note
----

For ``ldap.UserSearchFilter`` we can use strings like ``(uid={USERNAME})``  
In this case {USERNAME} would be replaced by the real username of the user when searching in LDAP during ``Add User``.
     
Importing a user from LDAP into Sparkflows
------------------------------------------

Once LDAP is enabled in Sparkflows, users can be imported into Sparkflows from LDAP.

* Go to Administration/User
* Click on Add/Sync User
* Enter the username and click on Search
* User details are fetched from LDAP
* Click on Add User to create the user in Sparkflows

User Login
----------

Once LDAP is enabled in Sparkflows, all the authentication for login in Sparkflows are done against LDAP.

Search Order
-----

Sparkflows would search in LDAP and then in its DB. Search order is determined by the parameter ldap.Order.

If it is set to LDAP_DB, it would first search for the User in LDAP and then in its own DB. This allows having the admin user in the Sparkflows DB if needed, so that all users are not locked out of the system in case LDAP goes down or ends up with invalid Configurations.

Reference
---------

Below are some great links for reference:

* Active Directory Search Filter Syntax : https://msdn.microsoft.com/en-us/library/aa746475(v=vs.85).aspx


Notes
-----

* Search strings are not case sensitive

