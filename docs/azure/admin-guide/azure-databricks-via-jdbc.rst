Azure Databricks via JDBC using OAuth (Azure AD)
====

This document provides a step-by-step guide to configuring Azure Databricks via JDBC using OAuth (Azure AD) authentication with a **Client ID** and **Client Secret**. It outlines the process of creating an Azure App Registration in Microsoft Entra ID (Azure Active Directory) to obtain the required credentials.

Pre-requisites
----

Before you begin, ensure you have the following:

**1. Azure App Registration (in Entra ID / Azure AD)**

  * Client ID (Application ID)

  * Client Secret

  * Tenant ID (Directory ID)

**2. Databricks Workspace on Azure Databricks**

You’ll need these values later for Databricks OAuth or JDBC configurations.

Step-by-Step Instructions
----
**Create an Azure App Registration (Service Principal)**
++++

Follow the steps below to create an Azure App Registration in Microsoft Entra ID (Azure AD) to get your Client ID, Client Secret, and Tenant ID for Databricks using OAuth.


**1. Sign in to the Azure Portal**

  * Go to https://portal.azure.com.
  * Use an account with Admin or Application Administrator permissions.

**2. Open Microsoft Entra ID (Azure AD)**

  * In the left sidebar or search bar, search for “Microsoft Entra ID” (previously called Azure Active Directory).

  * Click **Microsoft Entra ID** to open your directory’s overview page.

**3. Register a New Application**

  * In the sidebar, select **App registrations**.

  * Click **+ New registration** and fill out the form as follows:

  .. list-table::
     :widths: 30 70
     :header-rows: 1
  
     * - Field
       - Input
     * - Name
       - Any name (e.g., databricks-oauth-app).
     * - Supported account types
       - Usually select Accounts in this organizational directory only.
     * - Redirect URI (Optional)
       - Leave empty (for service-to-service use).


  * Then click on **Register**.

**4. Copy the Client ID and Tenant ID**

  * Once registered, you’ll land on the app’s Overview page where you will see the below:

    * Application (client) ID → This is your Client ID

    * Directory (tenant) ID → This is your Tenant ID

  * Copy and store both values securely — you’ll need them for your JDBC OAuth setup.

**5. Create a Client Secret**

   Now generate the secret (used like a password for your app):

    * In the app sidebar, click Certificates & secrets.

    * Under Client secrets, click + New client secret.

    * Add a description (e.g., databricks-secret).

    * Choose an expiration period (e.g., 6 months, 1 year, 2 years).

    * Click Add.

.. Note:: Copy the Value immediately — this is your Client Secret. Once you leave the page, it cannot be viewed again.



**6. Assign Azure Role Permissions (Optional)**

   If the app will access resources (like Databricks, Storage, etc.), you must assign permissions.

  * For accessing Databricks APIs:

    * Go to your Databricks workspace resource in the Azure Portal.

    * Click Access control (IAM) → + Add role assignment.

    * Assign Contributor or Reader (depending on your need).

    * Select your App Registration under Members.

  * For accessing Azure Storage, SQL, or other services:

    * Repeat the above steps under each resource’s Access control (IAM) page.


**7. Verify Setup**
                                     
   To confirm your app is ready:

  * Go to **App registrations → Your App → Overview**.

  * Verify that you have the following:

    * Application (client) ID

    * Directory (tenant) ID

    * Client Secret (Value)


Reference Document
----
* `Microsoft Learn: Quickstart - Register an application <https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app>`_

* You can now plug these into your Databricks JDBC or OAuth configuration in Sparkflows.

  `Databricks Connection using OAuth <https://docs.sparkflows.io/en/latest/user-guide/connection/compute-connection/databricks.html>`_
                                   









