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
   :widths: 15 10 30
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
     - The distinguished name to use as a search base for finding users and groups. This should be similar to ‘dc=hadoop,dc=mycompany,dc=com’.
     - dc=example,dc=com
   * - ldap.UserDn
     - Distinguished name of the user to bind as. This is used to connect to LDAP/AD for searching user and group information. This may be left blank if the LDAP server supports anonymous binds.
     - uid=john,ou=bindusers,dc=example,dc=com
   * - ldap.Password
     - The password of the bind user.
     - xyz
   * - ldap.UserSearchBase
     - User Search Base
     - ou=sparkflows
   * - ldap.UserSearchFilter
     - The base filter for searching for users. For Active Directory, this is typically ‘(objectClass=user)’.
     - (uid={0})
   * - ldap.GroupSearchBase
     - Group Search Base
     - ou=groups
   * - ldap.GroupSearchFilter
     - Group Search Filter
     - member={0}
     
     
     
