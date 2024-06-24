Mount ADLS to DBFS
===============

You can Mount ADLS to DBFS and access using Fire Insights application using DBFS.

Run the following in your notebook to authenticate and create a mount point.

Python
+++++

::

    configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": "<application-id>",
          "fs.azure.account.oauth2.client.secret": dbutils.secrets.get(scope="<scope-name>",key="<service-credential-key-name>"),
          "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/<directory-id>/oauth2/token"}

   # Optionally, you can add <directory-name> to the source URI of your mount point.
   dbutils.fs.mount(
   source = "abfss://<container-name>@<storage-account-name>.dfs.core.windows.net/",
   mount_point = "/mnt/<mount-name>",
   extra_configs = configs)

.. Note:: Make sure to change **<application-id>, <scope-name>, <service-credential-key-name>, <directory-id>, <container-name>, <storage-account-name> & <mount-name>** with actual value.


Scala
+++++

::

    val configs = Map(
    "fs.azure.account.auth.type" -> "OAuth",
    "fs.azure.account.oauth.provider.type" -> "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
    "fs.azure.account.oauth2.client.id" -> "<application-id>",
    "fs.azure.account.oauth2.client.secret" -> dbutils.secrets.get(scope="<scope-name>",key="<service-credential-key-name>"),
    "fs.azure.account.oauth2.client.endpoint" -> "https://login.microsoftonline.com/<directory-id>/oauth2/token")
   // Optionally, you can add <directory-name> to the source URI of your mount point.
   dbutils.fs.mount(
   source = "abfss://<container-name>@<storage-account-name>.dfs.core.windows.net/",
   mount_point = "/mnt/<mount-name>",
   extra_configs = configs)

.. Note:: Make sure to change **<application-id>, <scope-name>, <service-credential-key-name>, <directory-id>, <container-name>, <storage-account-name> & <mount-name>** with actual value.


`Click here <https://learn.microsoft.com/en-us/azure/databricks/dbfs/mounts>`_ to get more details on mounting adls to dbfs.

   
