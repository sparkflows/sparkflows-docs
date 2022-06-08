Fire Insights SAML Ping Identity Configuration
====================

Fire Insights can be configured with SAML 2.0 Ping Identity as below.

Go to folder ``conf`` and edit the file ``sso.saml.properties`` in it:

Add/update the below information from newly created application in Okta:

1. Enable sso in Fire Insights

::

    sparkflows.sp.sso.enable=true 
    
2. Create user automatically in application if user doesn't exist in Fire Insights, otherwise app will show page 'User not found'

::

    sparkflows.sp.auto.user.create=true 
    
3. Disable the db login for superuser or else you can enable it to login with superuser authentication

::

    sparkflows.sp.db.login.enable=true

4. enable/disable global logout

::

    saml2.global.logout=true
    
    
5. Copy Ping Identity config info

::

    # Identifier of the SP entity  (must be a URI) Audience URI
    saml2.sp.entityid=https://localhost:8443/sparkflow/saml/metadata
    # Algorithm that the toolkit will use on signing process
    saml2.security.signature_algorithm=http://www.w3.org/2001/04/xmldsig-more#rsa-sha256
