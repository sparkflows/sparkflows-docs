
Configuration Steps
===========

Below are the configuration steps to configure AWS SSO:

Step 1 : Login to the AWS Management Console
--------------------
#. Access the AWS Management Console using your credentials.

Step 2 : Navigate to AWS Single Sign-On
----------------

#. Go to the Security, Identity, & Compliance section and select AWS Single Sign-On.

   .. figure:: ../../../_assets/configuration/aws-sso/service_aws.PNG
      :alt: aws sso
      :width: 60%
   
Step 3 :  Enable AWS SSO
-------------------
#. Click on **Enable AWS SSO** to initiate the setup process.

   .. figure:: ../../../_assets/configuration/aws-sso/aws_sso.PNG
      :alt: aws sso
      :width: 60%

Step 4 : Select Settings
-------------------

#. Under the AWS SSO dashboard, choose **Settings** to configure your preferences.

   .. figure:: ../../../_assets/configuration/aws-sso/aws_setting.PNG
      :alt: aws sso
      :width: 60%


Step 5 : Change Identity Source
----------------------
#. Navigate to the **Identity source** section.
#. Select **Change** to specify your preferred identity source.

   .. figure:: ../../../_assets/configuration/aws-sso/aws_identity.PNG
      :alt: aws sso
      :width: 60%

Step 6 : Configure External Identity Provider
-----------------------------------
#. Select **External identity provider**.
#. Click on  **Show individual metadata values**.
    
   .. figure:: ../../../_assets/configuration/aws-sso/aws_external.PNG
      :alt: aws sso
      :width: 60%

Step 7 : Capture Metadata Values
------------
#. Make copies of **AWS SSO Sign-in URL**, **AWS SSO ACS URL**, and **AWS SSO issuer URL** as these values will be used at a later stage.
#. Save **IdP SAML metadata** as **metadata.xml** and then upload it into AWS.
    
   .. figure:: ../../../_assets/configuration/aws-sso/aws_validation.PNG
      :alt: aws sso
      :width: 60%

Step 8 : Review and Confirm Identity Source Change
----------------------
#. Click on **Next: Review** to review the list of changes.
#. Once you are ready to proceed, type **CONFIRM** and then click on **Change Identity source**.    

   .. figure:: ../../../_assets/configuration/aws-sso/aws_change_identity.PNG
      :alt: aws sso
      :width: 60%
