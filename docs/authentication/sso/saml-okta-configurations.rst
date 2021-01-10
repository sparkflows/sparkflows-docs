Fire Insights SAML Okta Configuration
====================

Fire Insights can be configured with SAML 2.0 Okta as below.

Go to folder ``conf/okta.saml.properties`` file:

Add below information from newly created application in oneLogin:

1. Enable sso in sparkflows::


    sparkflows.sp.sso.enable=true 
    
2. Create user locally in application if user doesn't exist in Fire Insights, otherwise app will show page 'User not found'::
    
    sparkflows.sp.auto.user.create=true 
    
3. Copy Okta config info

::

    # Identifier of the SP entity  (must be a URI) Audience URI
    saml2.sp.entityid=https://localhost:8443/sparkflow/saml/metadata
    # Algorithm that the toolkit will use on signing process
    saml2.security.signature_algorithm=http://www.w3.org/2001/04/xmldsig-more#rsa-sha256

.. figure:: ../../_assets/authentication/okta_identifier.png
   :alt: sso
   :width: 60%

4. Right click on identity provider metadata and select Copy link address

::

    #Metadata url of identity provider
    saml2.idp.metadata-url=https://dev-514411.okta.com/app/exk6sc27dyq4istqO357/sso/saml/metadata
    
    
.. figure:: ../../_assets/authentication/okta_metdata.png
   :alt: sso
   :width: 60%    

5. Capture Issuer url

.. figure:: ../../_assets/authentication/okta_issuer.png
   :alt: sso
   :width: 60% 

.. figure:: ../../_assets/authentication/okta_identifier_url.png
   :alt: sso
   :width: 60% 

.. note::  Make sure to change localhost to your domain name or your ip    
