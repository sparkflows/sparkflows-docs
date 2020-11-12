ADLS Integration
================

Fire Insights integrated with azure data lake filesystem, once configured you can use the filesystem for accessing data from it.

Below are the steps to Configured adls using managed identity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Managed identity allow the users to access the azure resources without hardcoding any credentials in code.

- System identity is enabled on vm where Fire Insights is running.
- In storage account, add the role to provide the access to Azure-VM with below role.

