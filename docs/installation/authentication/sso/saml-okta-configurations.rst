Okta Fire Insights SAML Configuration
====================

Fire Insights can be configured with SAML 2.0 Okta as below:

Go to folder ``conf`` and edit the file ``sso.saml.properties`` in it:

Add/update the below information from newly created application in Okta:

1. Enable SSO in Fire Insights.

::

    sparkflows.sp.sso.enable=true 

2. authentication type - expected value (saml or oauth).

::

    sparkflows.authentication.type=saml 


3. Create user automatically in application, if user doesn't exist in Fire Insights, otherwise app will show page 'User not found'.

::

    sparkflows.sp.auto.user.create=true 
    
4. Disable the DB login for superuser or else you can enable it to login with superuser authentication.

::

    sparkflows.sp.db.login.enable=true

5. Enable/disable global logout.

::

    saml2.global.logout=true
    
    
6. Copy Okta config info.

::

    # Identifier of the SP entity  (must be a URI) Audience URI
    saml2.sp.entityid=https://localhost:8443/sparkflow/saml/metadata
    # Algorithm that the toolkit will use on signing process
    saml2.security.signature_algorithm=http://www.w3.org/2001/04/xmldsig-more#rsa-sha256

.. figure:: ../../../_assets/authentication/okta_identifier.png
   :alt: sso
   :width: 60%

7. Right click on identity provider metadata and select Copy link address.

::

    #Metadata URL of identity provider
    saml2.idp.metadata-url=https://dev-514411.okta.com/app/exk6sc27dyq4istqO357/sso/saml/metadata or file:./conf/saml2-metadata-idp-d717f2ad-aa47-4260-b84e-08094d0dbcd4.xml
    
    
.. figure:: ../../../_assets/authentication/okta_metdata.png
   :alt: sso
   :width: 60%    

.. note::  ``saml2.idp.metadata-url`` can be absolute idp.metadata-url which is accessible from application or saml-metadata.xml file path in conf folder.


8. Capture Issuer URL:

.. figure:: ../../../_assets/authentication/okta_issuer.png
   :alt: sso
   :width: 60% 

.. figure:: ../../../_assets/authentication/okta_identifier_url.png
   :alt: sso
   :width: 60% 

9. Algorithm that the toolkit will use in signing process.

::

  saml2.security.signature_algorithm=http://www.w3.org/2001/04/xmldsig-more#rsa-sha256

10. Application base URL.

::

  saml.sso.metadata-generator.entity-base-url=https://localhost:8443
  
11. Server name.

::

  saml.context.lb.server-name=localhost:8443
  saml.context.lb.scheme=https
  saml.context.lb.contextPath=/  
  
.. note::  Make sure to change localhost to your domain name or your IP.    
