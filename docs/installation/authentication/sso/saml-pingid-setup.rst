Ping Identity Setup
========

This documentation describes the steps you need to follow to set up SAML 2.0 with Ping Identity. 

For more detailed information, please refer to the `Ping Identity documentation. <https://docs.pingidentity.com/>`_

Step 1: Get Started with Creating an Account
------

#. Visit the Ping Identity website and create an account in Ping Identity.

   .. figure:: ../../../_assets/authentication/pingid/ping_id.PNG
      :alt: sso
      :width: 40%
   
Step 2 : Sign On to Ping Identity
------

#. Enter the **credentials** to sign on to your Ping Identity Account.

   .. figure:: ../../../_assets/authentication/pingid/ping_id_1.PNG
      :alt: sso
      :width: 40%


Step 3 : Go to Administrators 
------

#. Click on **Administrators** in Environments.

   .. figure:: ../../../_assets/authentication/pingid/pingid_2.PNG
      :alt: sso
      :width: 50%

Step 4 : Go to Connections  
------

#. Click on **Connections**. This will display available options.

   .. figure:: ../../../_assets/authentication/pingid/pingid_3.PNG
      :alt: sso
      :width: 50%

Step 5 : Create new Application
------

#. Select **Applications**.  
#. Click on **+** sign.

   .. figure:: ../../../_assets/authentication/pingid/pingid_4.PNG
      :alt: sso
      :width: 50%

#. Add **Name** and **Description** of the Application.

   .. figure:: ../../../_assets/authentication/pingid/pingid_5.PNG
      :alt: sso
      :width: 50%
   
#. Choose Application Type as **SAML Application**.

   .. figure:: ../../../_assets/authentication/pingid/pingid_6.PNG
      :alt: sso
      :width: 50%
   
#. Provide Application Metadata:
   
   * Click on **Configure** and
   * Choose the method to provide metadata as per your configuration.
   
     .. figure:: ../../../_assets/authentication/pingid/pingid_7.PNG
      :alt: sso
      :width: 50%
   
#. Enter the **ACS URLs** and **Entity ID**. 
#. Click **Save** to save the Application.
  
   .. figure:: ../../../_assets/authentication/pingid/ping_acs.PNG
      :alt: sso
      :width: 50%

Step 6: Update HTTP POST
------

#. Click on **Configure** and update the HTTP POST as ``urn:oasis:names:tc:SAML:2.0:nameid-format:persistent``

   .. figure:: ../../../_assets/authentication/pingid/http_post_1.PNG
      :alt: sso
      :width: 50%

Step 7 : Update Attribute Mappings
------

#. Click on **Attribute Mappings** and update the required details as below: 

   * fireUsername=UserName
   * emailID=EmailID
   * firstName=FirstName
   * samlSubject=saml_subject
   * lastName=LastName

   .. figure:: ../../../_assets/authentication/pingid/attribute_mapping.PNG
      :alt: sso
      :width: 50%

Step 8 : Download Metadata from Application
------

#. Activate the Application and download the Metadata from application. 
   
   This metadata will be used while configuring the Fire Insights.

   .. figure:: ../../../_assets/authentication/pingid/pingid_9.PNG
      :alt: sso
      :width: 50%

.. note::  Make sure to change localhost to your domain name or your IP where Fire Insights is running.
