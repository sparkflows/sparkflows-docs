Fire Insights AWS SSO Configuration
====================

Fire Insights can be configured with AWS SSO as below.

1. Enable sso in Fire Insights

::

    sparkflows.sp.sso.enable=true 
    
2. Create user automatically in application if user doesn't exist in Fire Insights, otherwise app will show page 'User not found'

::

    sparkflows.sp.auto.user.create=true 
    
3. Disable the db login for superuser or else you can enable it to login with superuser authentication

::

    sparkflows.sp.db.login.enable=true

4. enable/disable global logout

::

    saml2.global.logout=true
