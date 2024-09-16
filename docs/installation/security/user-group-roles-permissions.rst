User/Group/Role/Permission
==========================

Fire Insights supports users, groups, roles, and permissions. A user can belong to multiple groups and have multiple roles. Each role can have multiple permissions associated with it.

Groups
------

There can be multiple groups in Fire Insights. A user can belong to one or more groups.

.. figure:: ../../_assets/security/group_list.PNG
   :alt: security
   :width: 60%

Below are further details associated with each group

* **Name:** The name of the group.
* **Properties:** Key-value pairs you need to pass.
* **AWS Role ARN:** S3 locations that the users of the group can browse and view. Associated with each S3 location is also the IAM role to be assumed.
* **S3 Access Key:** The credential used to authenticate and authorize access to Amazon Web Services (AWS) resources, such as S3 buckets.
* **S3 Secret Key:** The credential secret key. Together with the access key, it is used to authenticate and authorize access to AWS resources, such as S3 buckets.
* **S3 Endpoint URL:** The S3 endpoint URL used to access Amazon S3 (Simple Storage Service).

.. figure:: ../../_assets/security/group_creation.PNG
   :alt: security
   :width: 60%

Users
-----

Fire Insights supports multiple users. Each user can belong to multiple groups and have multiple roles.

.. figure:: ../../_assets/security/user_list.PNG
   :alt: security
   :width: 60%

.. figure:: ../../_assets/security/user_detail.PNG
   :alt: security
   :width: 60%

Permissions
-----------

Fire Insights supports the following permissions, which are associated with roles:

.. list-table:: 
   :widths: 10 20 
   :header-rows: 1

   * - Title
     - Description
   * - users.manage
     - Create, modify, and disable users.
   * - groups.manage
     - Create, modify, and delete groups.
   * - roles.manage
     - Create, modify, and delete roles.
   * - projects.manage
     - Create, modify, and delete projects.
   * - configurations.manage
     - Modify different configurations.
   * - enable.projectShare
     - Enable project sharing permissions.
   * - connections.manage
     - Manage connections.
   * - credentialstores.manage
     - Manage credential stores.
   * - enable.tokenGeneration
     - Manage token generation.
   * - datasets.view
     - View datasets in specified projects.
   * - datasets.modify
     - Modify datasets in specified projects.
   * - dashboard.view
     -View dashboards.
   * - dashboard.modify
     - Modify dashboards.
   * - workflows.view
     - View workflows in specified projects.
   * - workflows.modify
     - Modify workflows in specified projects.
   * - workflows.execute
     - Execute workflows in specified projects.
   * - enable.automl
     - Enable AutoML.
   * - apps.modify
     - Modify analytics applications.
   * - apps.execute
     - Execute analytics applications.
   * - apps.view
     - View analytics applications.
   * - data.view
     - View data.
   * - data.write
     - Write and read data.
   * - report.view
     - View report.
   * - report.modify
     - Modify report.
   * - usage.statistics.manage
     - View usage statistics.
   * - runtime.statistics.manage
     - View runtime statistics.
   * - scheduler.statistics.manage
     - View scheduler statistics.
   * - cache.statistics.manage
     - View cache statistics.
   * - sampleProject.manage
     - Reload sample projects.
   * - cleanup.data.manage
     - Clean up data.
   * - audit.report.manage
     - View, export, and delete audit reports.
   * - serverLogs.view
     - View server logs.
   * - yarn.application.view
     - View and search YARN applications.
   * - diagnostics.manage
     - Run diagnostics.
   * - test.ldap.manage
     - Test LDAP configurations.
   * - database.backup.manage
     - Backup the database and schedule backups.
   * - enable.tokenGeneration
     - Enable token generation.
   * - pipelines.view
     - View pipelines. 
   * - pipelines.modify
     - Create, modify, and delete pipelines.
   * - pipelines.execute
     - Execute pipelines. 



Role's Permissions
----------------

A role has a set of permissions associated with it. A new role can be created, and an existing role can be edited.

Out of the box, Fire Insights comes with three roles: ADMIN, ANALYST, and BUSINESS ASSOCIATE.

.. figure:: ../../_assets/security/role_permissions.PNG
   :alt: security
   :width: 60%



User/Roles
-----

A user can have multiple roles. The actions a user can perform depend on the roles they belong to.


.. figure:: ../../_assets/security/role_list1.PNG
   :alt: security
   :width: 60%





