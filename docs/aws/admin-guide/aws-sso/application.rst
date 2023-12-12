Application
=======

Since, you have successfully configured both the AWS SSO and Okta in the previous steps so now, you can configure single sign-on (SSO) access to Fire Insights applications as it supports identity federation with SAML 2.0.

This document guides you through the process of configuring single sign-on (SSO) access to Fire Insights applications using AWS SSO and Okta. Below are the steps involved in it:

Step 1 : Login to Aws Console
------------------------
#. Access the AWS Console with your credentials. 

Step 2 : Open AWS SSO and Access Applications
-----------------------
#. Within the AWS Single Sign-On service, navigate to the **Applications** section.

   .. figure:: ../../../_assets/configuration/aws-sso/aws_sso_app.PNG
      :alt: aws sso
      :width: 60%

Step 3 : Add Custom SAML 2.0 Application
----------------
#. Add a custom SAML 2.0 application, providing essential details for configuration as below:
   
   ::

      Display name : Custom SAML 2.0 application Name
      Description : Any Specific description

   .. figure:: ../../../_assets/configuration/aws-sso/aws_details.PNG
      :alt: aws sso
      :width: 60%

#. AWS SSO metadata:

   Cloud application may require the following certificate and metadata details to recognize AWS SSO as the identity provider.

   .. figure:: ../../../_assets/configuration/aws-sso/aws_metdata.PNG
      :alt: aws sso
      :width: 60%

#. Application metadata:

   AWS SSO requires specific metadata about your cloud application before it can trust this application. 

   You can type this metadata manually or upload a metadata exchange file.

   ::

      Application ACS URL : The Assertion Consumer Service (ACS) URL is used to identify the location from where the service provider accepts SAML assertions.
      Application SAML audience: Application SAML URL

      .. figure:: ../../../_assets/configuration/aws-sso/aws_acs.PNG
         :alt: aws sso
         :width: 60%    

