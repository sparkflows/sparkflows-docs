Password Reset
=====


The **Reset Password** feature allows an admin user to reset the password for any user in the system. This ensures secure management of user credentials by enabling admin to initiate a password change and notify the user via email.

Purpose
-------
This functionality is designed to provide admin with a convenient way to assist users to reset their passwords or require a reset for security reasons.

Steps to Enable and Use the Reset Password Feature
--------------------------------------------------

1. **Enable the Reset Password Option**

   Navigate to:   ``Administration → Config → Module``
    


   Search for the configuration key: ``module.enableResetPassword``
                                                                                                                                                                 

   It is set to ``false`` by default, change it to ``true`` to enable the feature.

   **Reference Image**

   .. figure:: ../../../_assets/Reset_Passwords/Module_Reset.png
      :width: 60%
      :alt: Reset Password Config Module

2. **Verify the Feature in User Management**

   Go to:  ``Administration → User Management``
     

   Under the **Users** tab, locate the **Actions** section.


   There would be a **Reset Password** icon  for each user entry.
   
   **Reference Image**

   .. figure:: ../../../_assets/Reset_Passwords/password_users_page.png
      :width: 60%
      :alt: Reset Password UsersTab


3. **Reset a User’s Password**

   Click on the **Reset Password** icon next to the user for whom the password needs to be changed.


   Enter the new password in the provided input field.

   **Reference Image**

   .. figure:: ../../../_assets/Reset_Passwords/Reset_Password.png
      :width: 60%
      :alt: Reset Password UsersTab

4. **Password Notification**

   The new password will be automatically sent to the user’s registered email address.


   The user can then log in to the system using the newly generated password.

Notes
--------------------------------------------------

- Ensure that the email configuration is correctly set up in the application for successful delivery of reset credentials.


