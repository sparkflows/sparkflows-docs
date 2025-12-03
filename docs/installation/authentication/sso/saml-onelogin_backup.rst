SAML Authentication with One Login
====================

Sparkflows supports SAML Authentication.


Configuring SAML
-----------------
Add  identity provider configuration information in sso.saml.properties file:

1. Metadata url of identity provider 

Right click on SAML Metadata menu and copy link address and add it in config properties file like below:

.. figure:: ../../_assets/authentication/saml_metadata_url.png
   :alt: sso
   :align: center
   :width: 60%

::  
  
    saml2.idp.metadata-url=https://sparkflows-dev.onelogin.com/saml/metadata/5f5d16a1-07d1-4167-a305-489d2ee0b18b
    
2. Identifier of the SP entity  (must be a URI) Audience URI::


.. figure:: ../../_assets/authentication/service_provider_entity_id.png
   :alt: sso
   :align: center
   :width: 60%

::

    saml2.sp.entityid=https://localhost:8443/sparkflow/saml/metadata
   
3. Identifier of the IdP entity  (must be a URI)::

    
.. figure:: ../../_assets/authentication/one_login_entity_id.png
   :alt: sso
   :align: center
   :width: 60%

::

    saml2.idp.entityid=https://app.onelogin.com/saml/metadata/5f5d16a1-07d1-4167-a305-489d2ee0b18b

4. Signature algorithm::

 
.. figure:: ../../_assets/authentication/saml_signature.png
   :alt: sso
   :align: center
   :width: 60%  

::

    saml2.security.signature_algorithm=http://www.w3.org/2001/04/xmldsig-more#rsa-sha1

5. Make it sure that recepient url start with /saml/SSO


.. figure:: ../../_assets/authentication/one_login_recipient.png
   :alt: sso
   :align: center
   :width: 60% 
 

.. note::  Make sure to change localhost to your domain name or your ip
