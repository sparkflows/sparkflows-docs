Fire Insights SAML oneLogin Configuration
====================

Fire Insights can be Configured with SAML 2.0 OneLogin as below.

Go to folder ``conf/sso.saml.properties`` file:

Add below information from newly created application in oneLogin:

1. Enable sso in sparkflows::


    sparkflows.sp.sso.enable=true 
    
2. Create user locally in application if user doesn't exist in Fire Insights, otherwise app will show page 'User not found'::
    
    sparkflows.sp.auto.user.create=true 

3. Metadata url of identity provider.

.. figure:: ../../_assets/authentication/saml_metadata_url.png
   :alt: sso
   :align: left
   :width: 60%

::  
  
    saml2.idp.metadata-url=https://sparkflows-dev.onelogin.com/saml/metadata/5f5d16a1-07d1-4167-a305-489d2ee0b18b
    
4. Identifier of the SP entity  (must be a URI) Audience URI
		        
.. figure:: ../../_assets/authentication/service_provider_entity_id.png
   :alt: sso
   :align: left
   :width: 60%

::

    saml2.sp.entityid=https://localhost:8443/sparkflow/saml/metadata
   
5. Identifier of the IdP entity  (must be a URI)
  
   
.. figure:: ../../_assets/authentication/one_login_entity_id.png
   :alt: sso
   :align: left
   :width: 60%

::

    saml2.idp.entityid=https://app.onelogin.com/saml/metadata/5f5d16a1-07d1-4167-a305-489d2ee0b18b

6. Algorithm that the toolkit will use on signing process.

  
.. figure:: ../../_assets/authentication/saml_signature.png
   :alt: sso
   :align: left
   :width: 60%  

::

    saml2.security.signature_algorithm=http://www.w3.org/2001/04/xmldsig-more#rsa-sha1

 

.. note::  Make sure to change localhost to your domain name or your ip







