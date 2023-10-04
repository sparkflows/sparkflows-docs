Azure AD Fire Insights SAML Configuration
====================

Fire Insights can be configured with SAML 2.0 Ping Identity as below:

Go to folder ``conf`` under Fire Insights installation directory and edit the file ``sso.saml.properties`` in it:

Add/update the below information from newly created application in Azure AD:

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
  saml2.idp.metadata-url=https://login.microsoftonline.com/95d882cb-76e3-4dee-94d8-6e2dffbb1a5d/federationmetadata/2007-06/federationmetadata.xml?appid=b937756f-6ebe-472f-9069-15dc88f6dec7 or ./conf/sparkflows-test.xml

  #  Identifier of the SP (Service Provider) entity  (must be a URI) Audience URI
  saml2.sp.entityid=https://<sparkflows-dns>:8443/sparkflow/saml/metadata

  # Identifier of the IdP entity  (must be a URI)
  saml2.idp.entityid=https://sts.windows.net/95d882cb-76e3-4dee-94d8-6e2dffbb1a5d/
  
  # Algorithm that the toolkit will use on signing process. Options:
  saml2.security.signature_algorithm=http://www.w3.org/2001/04/xmldsig-more#rsa-sha256

.. note::  ``saml2.idp.metadata-url`` can be absolute idp.metadata-url which is accessible from application or saml-metadata.xml file path in conf folder.

``saml2.idp.entityid`` should be the Issuer ID of Ping Identity application.

6. Configure Application Base URL

::

  saml.sso.metadata-generator.entity-base-url=https://<sparkflows-dns>:8443
  
7. Configure Server Name

If application is running behind load balancer, one needs to configure the below. Update the Fire Insights application URI. 

::

  saml.context.lb.server-name=<sparkflows-dns>
  saml.context.lb.scheme=https
  saml.context.lb.contextPath=/  
  
.. note::  Make sure to change <sparkflows-dns> to your domain name or your IP.
