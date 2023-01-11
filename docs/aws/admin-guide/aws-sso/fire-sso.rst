Fire Insights AWS SSO Configuration
====================

Fire Insights can be configured with AWS SSO as below.

1. Enable sso in Fire Insights.

::

    sparkflows.sp.sso.enable=true 
    
2. Create user automatically in application if user doesn't exist in Fire Insights, otherwise app will show page 'User not found'.

::

    sparkflows.sp.auto.user.create=true 
    
3. Disable the database login for superuser or else you can enable it to login with superuser authentication.

::

    sparkflows.sp.db.login.enable=true

4. Enable/disable global logout.

::

    saml2.global.logout=true
    
5. Copy AWS SSO config info.

::

    #Metadata URL of identity provider.
    saml2.idp.metadata-url=./conf/fire_custom.xml

    #  Identifier of the SP entity  (must be a URI) Audience URI.
    saml2.sp.entityid=https://localhost:8443/saml/metadata

   # Identifier of the IdP entity  (must be a URI).
   saml2.idp.entityid=https://portal.sso.us-east-1.amazonaws.com/saml/assertion/xxxxxxxxxxxxxxxxxxx

6. Algorithm that the toolkit will use in signing-in process.

::

    saml2.security.signature_algorithm=http://www.w3.org/2001/04/xmldsig-more#rsa-sha25    

7. Application base URL.

::

  saml.sso.metadata-generator.entity-base-url=https://localhost:8443
  
8. ACS URL.

::

    saml.sso.acs-url=https://localhost:8443/saml/SSO  
  
9. Server Name.

::

  saml.context.lb.server-name=localhost:8443
  saml.context.lb.scheme=https
  saml.context.lb.contextPath=/  
  
10. Once the above configuration added and when started the Fire Server, you will able to Login through Fire Insights page.

.. figure:: ../../../_assets/configuration/aws-sso/login.PNG
   :alt: aws sso
   :width: 60%
  
.. note::  Make sure to change the localhost to your domain name or your IP.
