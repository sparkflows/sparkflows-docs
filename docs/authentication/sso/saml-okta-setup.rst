SAML okta setup
==============

Below are steps to setup SAML 2.0 okta

1. Create an account at okta

.. figure:: ../../_assets/authentication/okta_signin_url.png
   :alt: sso
   :align: left
   :width: 60%
   
2. SignIn into okta

.. figure:: ../../_assets/authentication/okta_sigin_credential.PNG
   :alt: sso
   :align: left
   :width: 60%
   
3. After login go to home and Click on Admin   

.. figure:: ../../_assets/authentication/okta_admin.png
   :alt: sso
   :align: left
   :width: 60%

4. Click on Developer Console

.. figure:: ../../_assets/authentication/okta_app.png
   :alt: sso
   :align: left
   :width: 60%
   
5. Add an app:

.. figure:: ../../_assets/authentication/okta_addapp.png
   :alt: sso
   :align: left
   :width: 60%

6. Create New App:

.. figure:: ../../_assets/authentication/okta_add_app.png
   :alt: sso
   :align: left
   :width: 60%

7. Select SAML 2.0

.. figure:: ../../_assets/authentication/okta_saml.png
   :alt: sso
   :align: left
   :width: 60%
   
8. Input app name and click next:

.. figure:: ../../_assets/authentication/okta_config.png
   :alt: sso
   :align: left
   :width: 60%

9. Click finish:

.. figure:: ../../_assets/authentication/okta_finish.png
   :alt: sso
   :align: left
   :width: 60%

10. Configure the newly created app and add below information

::

    # Identifier of the SP entity  (must be a URI) Audience URI
    saml2.sp.entityid=https://localhost:8443/sparkflow/saml/metadata
    # Algorithm that the toolkit will use on signing process
    saml2.security.signature_algorithm=http://www.w3.org/2001/04/xmldsig-more#rsa-sha256

.. figure:: ../../_assets/authentication/okta_identifier.png
   :alt: sso
   :align: center
   :width: 60%

