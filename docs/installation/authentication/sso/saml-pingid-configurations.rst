Ping Identity Fire Insights SAML Configuration
====================

Fire Insights can be configured with SAML 2.0 Ping Identity as below:

Go to folder ``conf`` and edit the file ``sso.saml.properties`` in it:

Add/update the below information from newly created application in Okta:

1. Enable SSO in Fire Insights.

::

    sparkflows.sp.sso.enable=true 
    
2. Create user automatically in application if user doesn't exist in Fire Insights, otherwise application will show page 'User not found'.

::

    sparkflows.sp.auto.user.create=true 
    
3. Disable the DB login for superuser or else you can enable it to login with superuser authentication.

::

    sparkflows.sp.db.login.enable=true

4. Enable/disable global logout.

::

    saml2.global.logout=true
    
    
5. Copy Ping Identity config info.

::

    # Metadata URL of identity provider
    saml2.idp.metadata-url=https://auth.pingone.asia/fa405895-689d-4ced-9a0e-6d940667583b/saml20/metadata/46240920-e6a9-4d2f-b2ce-ddb7d00e4087

   #  Identifier of the SP entity  (must be a URI) Audience URI
   saml2.sp.entityid=https://localhost:8443/sparkflow/saml/metadata

  # Identifier of the IdP entity  (must be a URI)
  saml2.idp.entityid=https://auth.pingone.asia/fa405895-689d-4ced-9a0e-6d940667583b
  
  # Algorithm that the toolkit will use on signing process. Options:
  saml2.security.signature_algorithm=http://www.w3.org/2001/04/xmldsig-more#rsa-sha256
  
6. Application base URL.

::

  saml.sso.metadata-generator.entity-base-url=https://localhost:8443
  
7. Server name.

::

  saml.context.lb.server-name=localhost:8443
  saml.context.lb.scheme=https
  saml.context.lb.contextPath=/  
  
.. note::  Make sure to change localhost to your domain name or your ip.   
