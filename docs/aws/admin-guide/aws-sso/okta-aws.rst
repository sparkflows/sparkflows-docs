Okta AWS SSO Configuration
==========
This document provides comprehensive guide for setting up AWS Single Sign-On (SSO) with Okta, ensuring a smooth integration process. 

Below are  the steps required to create an application with AWS SSO.


Step 1 : Log in to Okta Portal
-------------------
#. Access the Okta portal using your credentials to initiate the AWS SSO configuration process.

Step 2 : Browse App Catalog
-----------------
#. Navigate to the App Catalog within Okta to begin creating an application for AWS Single Sign-On.

   .. figure:: ../../../_assets/configuration/aws-sso/browse_app.PNG
      :alt: aws sso
      :width: 60%

Step 3 : Search with AWS Single Sign-on
---------------
#. Locate the AWS Single Sign-On SAML app within the App Catalog.

   .. figure:: ../../../_assets/configuration/aws-sso/aws_single_signon.PNG
      :alt: aws sso
      :width: 60%

Step 4 : Add General Settings
---------------------
#. Configure general settings, such as the label, for the AWS SSO application within Okta.

   .. figure:: ../../../_assets/configuration/aws-sso/aws_add.PNG
      :alt: aws sso
      :width: 80%

Step 5 : Edit AWS SSO SAML App Settings
---------------------
#. In Okta, go to the **Sign On** tab for the AWS Single Sign-On SAML app, and click on **Edit**. 
#. Enter **AWS SSO ACS URL and issuer URL values** (you made a copy of these in previous steps) into the corresponding fields.
#. Select an **Application username format** from the dropdown menu.
#. Click on **Save** to confirm and complete the AWS SSO application configuration.

   .. figure:: ../../../_assets/configuration/aws-sso/aws-acs.PNG
      :alt: aws sso
      :width: 50%
    
Step 6 : Configure Automatic Provisioning
----------------------
#. Click on **Provisioning** tab under the AWS SSO Application. 
#. Select **Enable API Integration**. 
#. Copy/paste the values of **Base URL** (paste the value copied in AWS Single Sign-On Console SCIM endpoint) and **API Token** (paste the value copied AWS Single Sign-On Console Access token). 

   .. Note:: Make sure to delete the trailing slash (/) at the end of the URL, commonly ending with **scim/v2**.

   .. figure:: ../../../_assets/configuration/aws-sso/provisoning.PNG
      :alt: aws sso
      :width: 50%

Step 7 : Test and Enable Provisioning
----------------------------

#. Click on **Test API Credentials** to verify that everything works as expected. 
#. After successful verification, click on **To App** to enable the creation, updating, and deactivation of users.

   .. figure:: ../../../_assets/configuration/aws-sso/provisoning_enabled.PNG
      :alt: aws sso
      :width: 50%

