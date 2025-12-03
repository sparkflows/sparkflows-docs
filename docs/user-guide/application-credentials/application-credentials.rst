Application Credentials
============================

Sparkflows enables you to create Application Credentials. These credentials store a Key and its associated Value, which are linked to Local Store Type Credential Stores. The values of these credentials can be used during the Create or Update process of an Application Connection through Macros.

Follow the steps below for creating an Application Credential.

Step 1 : Navigate to the Credential Store
-------------

#. **Log in** to Sparkflows. 
#. Go to the **Administration** page and click on the **Credential Store** card, as shown below to access the Credential Store section.

   .. figure:: ../../_assets/credential_store/local-credential-store/credential-store-card.png
      :alt: Credential Store Card
      :width: 45%

Step 2 : Add a New Credential and Configure Credential Details
---------

#. Select the **Credential** tab and click on **Add Credentials** button, as shown below.

   .. figure:: ../../_assets/user-guide/application-credentials/add-application-credential.png
      :alt: Add Credential Store Button
      :width: 70%

#. After clicking, an 'Add Credential' form will open up, as shown below.

   .. figure:: ../../_assets/user-guide/variables-macros/application-connection-macros/application-credential-using-local-store.png
      :alt: Add Credential Store Button
      :width: 70%

#. Configure the Credential by filling the required details in the above fields as follows and click on **Save** button to create the Application Credential.

   * **STORE:** Select the Credential Store previously created of Store Type **Local**.
   * **KEY:** Enter a unique identifier for the selected Local Credential Store.
   * **VALUE:** Enter the associated value (e.g., a password) as here we are creating a postgres related Application Credential as an example. 
   * **TITLE:** Give the credential a meaningful title.
   * **DESCRIPTION:** Optionally, add a relevant description if needed.

   *Note: During the creation of an Application Credential, the 'Key' field has a validation check ensuring that the 'Key' must be unique for the selected Local Credential Store in the dropdown.*

Step 3 : Editing an Application Credential
----------

#. Locate the Application Credential in the list.

#. From the **Actions** column, make the following updates:

   * To update fields such as Store, Key, Title, or Description then click on **Edit Details** icon.
   * To update the Value field click on **Edit Value** icon.

The created Application Credential can now be used with its associated Local Credential Store during the Create/Edit Application Connection process through Credential Store-specific macros.

