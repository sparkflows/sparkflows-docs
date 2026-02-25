Azure Databricks via JDBC using OAuth (Databricks Managed Service Principal)
====

This document provides a step-by-step guide to configuring Azure Databricks via JDBC using OAuth (Databricks Managed Service Principal) authentication with a **Client ID** and **Client Secret**. 

Step-by-Step Instructions
----

**1. Create Service Principal (Account Console)**


* Go to Databricks Account Console

     https://accounts.cloud.databricks.com


* Navigate to:

    User Management → Service Principals


* Click Add service principal

    Provide:

    Name (example): databricks-sp

    Click Create

**2. Generate Client Secret**

* Open the created Service Principal

    Go to Secrets

    Click Generate Secret

    Copy:

    Client ID

    Client Secret

    ⚠️ Secret value is shown only once.

.. note:: Make sure to use same Client ID and Client Secret in Databricks Connection and it should be accessible from Sparkflows application.

Reference Document
----

* `Microsoft Learn: Quickstart - Secret management <https://learn.microsoft.com/en-us/azure/databricks/security/secrets/>`_

* You can now plug these into your Databricks JDBC or OAuth configuration in Sparkflows.

  `Databricks Connection using OAuth <https://docs.sparkflows.io/en/latest/user-guide/connection/compute-connection/databricks.html>`_
                                   









