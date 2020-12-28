SSO
====

Single sign-on (SSO) enables you to authenticate your users using your organization’s identity provider. If your identity provider supports the SAML 2.0 protocol, you can use Sparkflows SSO to integrate with your identity provider.
   
Below are the steps for configuring SSO with Fire Insights.

Create Users in Fire
--------------------

First create the user in Fire under ``Administration/Users``.

Log into Fire with the ``admin`` user in order to be able to create the New Users.

Enable/Disable single signOn (sso.saml.properties)
------------------------------

Single Sign-on can be enabled or disabled in Fire Insights ::

    sparkflows.sp.sso.enable=true 

Enable/Disable auto user creation
-----------------------------------
 Enable/disable user auto creation in local database. If user is not present in local database and auto creation is true then
 after successful login, one user will get created in local database. If set false and user is not in local database,
 application will not allow to login and it will redirect it to User not found error page.

::

    sparkflows.sp.auto.user.create=false
    
    
Steps for Configuring Identity Provider
------------------------

.. toctree::
   :maxdepth: 2

   saml-onelogin.rst
