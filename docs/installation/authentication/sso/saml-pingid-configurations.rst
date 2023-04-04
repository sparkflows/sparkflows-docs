Ping Identity Fire Insights SAML Configuration
====================

Fire Insights can be configured with SAML 2.0 Ping Identity as below:

Go to folder ``conf`` under Fire Insights installation directory and edit the file ``sso.saml.properties`` in it:

Add/update the below information from newly created application in Ping Identity:

1. Enable SSO in Fire Insights

::

    sparkflows.sp.sso.enable=true 
    
2. Create user automatically in application if user doesn't exist in Fire Insights, otherwise application will show page 'User not found'.

::

    sparkflows.sp.auto.user.create=true 
    
3. Enable the superuser to be able to log in with DB login

::

    sparkflows.sp.db.login.enable=true

4. Enable or disable global logout as needed

::

    saml2.global.logout=true
    
    
5. Update Ping Identity config information

::

  # Metadata URL of identity provider
  saml2.idp.metadata-url=https://auth.pingone.asia/fa405895-689d-4ced-9a0e-6d940667583b/saml20/metadata/46240920-e6a9-4d2f-b2ce-ddb7d00e4087

  #  Identifier of the SP (Service Provider) entity  (must be a URI) Audience URI
  saml2.sp.entityid=https://<sparkflows-dns>:8443/sparkflows/saml/metadata

  # Identifier of the IdP entity  (must be a URI)
  saml2.idp.entityid=https://auth.pingone.asia/fa405895-689d-4ced-9a0e-6d940667583b
  
  # Algorithm that the toolkit will use on signing process. Options:
  saml2.security.signature_algorithm=http://www.w3.org/2001/04/xmldsig-more#rsa-sha256
  
6. Configure Application Base URL

::

  saml.sso.metadata-generator.entity-base-url=https://<sparkflows-dns>:8443
  
7. Configure Server Name in case Load Balancer is being used

The below is needed only when load balancer is being used. 

::

  saml.context.lb.server-name=<sparkflows-dns>:8443
  saml.context.lb.scheme=https
  saml.context.lb.contextPath=/  
  
.. note::  Make sure to change localhost to your domain name or your IP.
