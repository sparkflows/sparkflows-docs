Okta AWS SSO Configuration
==========

Below are  the steps required to create an application with AWS SSO.

1. Login to Okta portal.
2. Browse App Catalog.

.. figure:: ../../../_assets/configuration/aws-sso/browse_app.PNG
   :alt: aws sso
   :width: 60%

3. Search with AWS Single Sign-on.

.. figure:: ../../../_assets/configuration/aws-sso/aws_single_signon.PNG
   :alt: aws sso
   :width: 60%

4. Add General Settings, like Label etc.

.. figure:: ../../../_assets/configuration/aws-sso/aws_add.PNG
   :alt: aws sso
   :width: 80%

5. In Okta, select the Sign On tab for the AWS Single Sign-On SAML app, then click on Edit:

::

    Enter your AWS SSO ACS URL and AWS SSO issuer URL values (you made a copy of these in previous steps) into the corresponding fields.

    Application username format: Select one of the options from the dropdown menu.

    Note: All users in AWS SSO require a unique username, so the mapped value should be unique within your organization.

    Click on Save:
    
.. figure:: ../../../_assets/configuration/aws-sso/aws-acs.PNG
   :alt: aws sso
   :width: 50%
    
Click on Save to complete the configuration.

6. Configuring Automatic Provisioning

Click on Provisioning tab under the AWS SSO Application. Select Enable API Integration. Then copy/paste the values of Base URL (paste the value copied in AWS Single Sign-On Console SCIM endpoint) and API Token (paste the value copied AWS Single Sign-On Console Access token). Please be sure to remove the trailing forward slash(/) at the end of the URL. The URL usually ends in ``scim/v2``.

.. figure:: ../../../_assets/configuration/aws-sso/provisoning.PNG
   :alt: aws sso
   :width: 50%

7. Click on Test API Credentials to verify that everything works as expected. After successful verification click on ``To App`` to enable creation of users, updation of users' attributes and deactivation of users.

.. figure:: ../../../_assets/configuration/aws-sso/provisoning_enabled.PNG
   :alt: aws sso
   :width: 50%

