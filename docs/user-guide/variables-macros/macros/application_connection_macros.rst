Macros in Application Connection
==================

**Macros** can also be accessed by the Sparkflows Application Connections. They can be added to any field during the Add/Edit process of a connection. These macros are specifically associated to the Credential Store of type '**Local**' only.

Macros that Sparkflows Supports for Application Connection
++++++++++++++++++++++++++++++

.. list-table:: 
   :widths: 30 70
   :header-rows: 1

   * - Macro
     - Description
   * - ${cs.StoreName.CredentialKey}
     - It returns the credential value set for the **CredentialKey** that is associated to the Local Credential Store named **StoreName**. When using this macro, 
       then during the creation of application connection, we can either select the Local Credential Store as **StoreName** or choose '**Do not use Credential 
       Store**' from the Credential Store field dropdown. 
   * - ${cs.CredentialKey}
     - It returns the credential value set for the **CredentialKey**. When using this macro, then during the creation of application connection, we must select 
       the Local Credendial Store to which the CredentialKey is associated from the Credential Store field dropdown. Otherwise, an error message '**Please select 
       the credential store**' will appear.

To use macros in Sparkflows Application Connection, follow the steps given below:

Step 1 : Create a Credential Store of Type 'Local'
++++++++++

#. Navigate to **Administration** page and click on **Credential Store** card. 

#. Create a new Credential Store with the 'Store Type' set to **Local**, as shown below. Here, we have given the store name as **Store** which will be used while creating an Application Credential. This credential will then be used for establishing an Application Connection for PostgreSQL.

   .. figure:: ../../../_assets/user-guide/variables-macros/application-connection-macros/local-credential-store.png
      :alt: local-credential-store
      :width: 60%

Step 2 : Add Credentials to the Credential Store
+++++++

#. Once the Credential Store of type Local is created, navigate to the **Credentials** tab on the Credential Store page and click on **Add Credential** button.

#. Now add the details for the Credential as shown below:

   .. figure:: ../../../_assets/user-guide/variables-macros/application-connection-macros/application-credential-using-local-store.png
      :alt: application-credential-using-local-store
      :width: 60%

 * Select the Credential Store created in Step 1 (i.e. **Store**).
 * Provide a Key (e.g., **postgresPass**).
 * Enter the Password for the PostgreSQL connection as the Value.
 * Add a Title and optionally a Description, as shown above. Then click on **Save** button.

Step 3 : Using Macros in Application Connections
+++++++++++++

(A) Using the macro ${cs.StoreName.CredentialKey}
------------------

#. Navigate to **Administration** and click on the **Global/Group Connections** card.
#. Click on **Add Connection** and an 'Add Connection' form will be displayed as shown below.

   .. figure:: ../../../_assets/user-guide/variables-macros/application-connection-macros/macro-without-selecting-store.png
      :alt: macro-without-selecting-store
      :width: 60%

#. Enter the details in the required fields as follows and click on **Test Connection** button.

   * **Category:** Select the Category as **Storage**.
   * **Connection Type:** Select **PostgreSQL** as the Connection Type and fill in the required details for the PostgreSQL connection.
   * **Password:** Use the macro **${cs.Store.postgresPass}** for password, based on the Credential Store and Key created in Step 1 and Step 2.

   *Note: In this macro format we can either select the 'Credential Store' whose Credential Key we are using or we can set it to 'Do not use Credential Store'.*

#. After clicking the **Test Connection** button, if the password is set correctly in the macro used, a **Successfully Connected** message will appear on the form, as shown below. 

   .. figure:: ../../../_assets/user-guide/variables-macros/application-connection-macros/test-connection-without-store.png
     :alt: test-connection-without-store
     :width: 60%

(B) Using the macro ${cs.CredentialKey}
------------------

#. Navigate to **Administration** and click on **Global/Group Connections** card.
#. Click on **Add Connection** and an 'Add Connection' form will be displayed as shown below.

   .. figure:: ../../../_assets/user-guide/variables-macros/application-connection-macros/macro-with-selecting-store.png
      :alt: macro-without-selecting-store
      :width: 60%

#. Enter the details in the required fields as follows and click on **Test Connection** button.

   * **Category:** Select the Category as **Storage**.
   * **Connection Type:** Select **PostgreSQL** as the Connection Type and fill in the required details for the PostgreSQL connection.
   * **Password:** Use the macro **${cs.postgresPass}** for password.

   *Note: In this macro format, we must select the 'Credential Store' whose Credential Key we are using else an error message 'Please select the credential store' will appear.*

#. After clicking the **Test Connection** button, if the password is set correctly in the macro used, a **Successfully Connected** message will appear on the form, as shown below.

   .. figure:: ../../../_assets/user-guide/variables-macros/application-connection-macros/test-connection-with-store.png
      :alt: test-connection-without-store
      :width: 60%

Now this connection containing macros can be used seamlessly throughout Sparkflows. 

By following the steps above, you can seamlessly incorporate dynamic macros into your application connections. This allows the connections to adapt to changing conditions or input data, enhancing their flexibility and overall usability.
