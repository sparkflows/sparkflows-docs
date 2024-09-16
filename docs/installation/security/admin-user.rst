Superuser and Admin Users
===========

Superusers and Admin users have special permissions and rights.

Superuser
---------

A user in Fire Insights can be marked to be a super-user. A Super user has the below permissions:

#. **Project Sharing:** Share or unshare any project with any group.
#. **User Privileges:** Designate other users as Superusers.
#. **Group Management:** Create, update, or delete groups.
#. **User Management:** Create or update users.
#. **Roles Management:** Create, update, or delete roles.
#. **Operational Permissions:** Access tasks such as viewing server logs, updating configurations, etc.



Admin Role
---------

Fire Insights comes with a Role called Admin. This Role has the permissions to manage users, groups, roles and to also operate Fire Insights. This permissions associated with this role can also be updated.

Users who would be administrating Fire Insights would have the Admin Role assigned to them.

Below are the permissions for managing users, groups and roles:

* users.manage - Manage users

* groups.manage - Manage groups

* roles.manage - Manage roles

Below are the permission for administrating Fire Insights:

* **System Configuration:** Configure Fire Insights settings.
* **Diagnostics:** Run system diagnostics.
* **Usage Statistics:** View platform usage statistics.
* **YARN Applications:** Monitor YARN applications running on the Spark cluster.
* **Sample Projects:** Load sample projects that come with Fire Insights.
* **Global Connections:** Manage global and group-level connections.
* **Server Logs:** View Fire server logs, exception logs, and PySpark logs.
* **Data Cleanup:** Delete old workflow executions based on time ranges (e.g., older than 7, 30, or 90 days).
* **Audit Report:** View and download audit reports for user activities like logins, logouts, and workflow modifications.
* **Credential Store:** Manage credential stores for securely retrieving usernames, passwords, etc., when creating connections.
* **LDAP Testing:** Test LDAP configuration to ensure it's set up correctly (only when the LDAP properties file is updated).
* **Database Backup:** Backup the database if running on H2 DB.
* **Runtime Statistics:** View total logged-in users, active Fire Spark processes, and PySpark processes, along with running jobs.
* **Scheduler Statistics:** Monitor the status of scheduled jobs.
* **Cache Statistics:** View cache statistics for logged-in users and data sources like Snowflake and Databricks.

Operating Fire Insights
-----

There are certain tasks to be performed for operating Fire Insights. It is recommended to give the below permissions to the Admin for performing the operational tasks in Fire Insights.



.. figure:: ../../_assets/security/admin_user/admin_user.PNG
   :alt: security
   :width: 70%

.. figure:: ../../_assets/security/admin_user/admin_operations.PNG
   :alt: security
   :width: 70%

Projects/Data
+++++++++++++++++

As for projects, the admin user can do the following:

* View all the projects to which the admin user belongs.
* View the executions of all workflows to which the admin user belongs.
* View the executions of all analytical apps to which the admin user belongs.
* Create analytics apps in projects to which the admin user belongs.

Deleting Users/Groups
++++++++++++++++++++

* **User Deactivation:** In Fire Insights, users cannot be deleted but can be made inactive.
* **Group Deletion:** Groups can be deleted as needed.




Diagnostics
++++++++++

The admin user can view detailed informations about machine environments.

.. figure:: ../../_assets/security/admin_user/admin_diagnostic_1.PNG
   :alt: security
   :width: 70%

.. figure:: ../../_assets/security/admin_user/admin_diagnostic_2.PNG
   :alt: security
   :width: 70%
   
.. figure:: ../../_assets/security/admin_user/admin_diagnostic_3.PNG
   :alt: security
   :width: 70%

Usage Statistics
++++++++++++++

The admin user can view the total number of users, groups, roles, projects, workflows, and workflow executions.


.. figure:: ../../_assets/security/admin_user/admin_usage_statistics.PNG
   :alt: security
   :width: 70%
   

YARN APPLICATIONS
++++++++++++++

The admin user can view YARN applications if they are running on a Spark cluster with YARN.

.. figure:: ../../_assets/security/admin_user/admin_yarn_application.PNG
   :alt: security
   :width: 70%

Sample Projects
+++++++++++++

The admin user can reload sample projects, as Fire Insights, by default, comes with sample projects containing various types of workflows and datasets.

.. figure:: ../../_assets/security/admin_user/admin_sample_project.PNG
   :alt: security
   :width: 70%

.. figure:: ../../_assets/security/admin_user/admin_sample_project_1.PNG
   :alt: security
   :width: 70%

Global Connections
+++++++++++++++++++

The admin user can add connections which everyone can use and also connections at the group level.

.. figure:: ../../_assets/security/admin_user/admin_global.PNG
   :alt: security
   :width: 70%

Server Logs
++++++++

The admin user can view Fire server logs, Fire logs, Fire exception logs, and Fire PySpark logs.

.. figure:: ../../_assets/security/admin_user/admin_logs.PNG
   :alt: security
   :width: 70%
   
Cleanup Data
+++++++++++

The admin user can delete old workflow executions from the database that are older than the last 7 days, 30 days, or 90 days, as well as delete all executions.


.. figure:: ../../_assets/security/admin_user/admin_cleanup_1.PNG
   :alt: security
   :width: 70%

The admin user can delete old pipeline executions from the database that are older than the last 7 days, 30 days, or 90 days, as well as delete all executions.

.. figure:: ../../_assets/security/admin_user/admin_cleanup_2.PNG
   :alt: security
   :width: 70%

The admin user can clean audit logs from the database that are older than 7 days, 30 days, or 90 days, as well as delete all logs.


.. figure:: ../../_assets/security/admin_user/admin_cleanup_3.PNG
   :alt: security
   :width: 70%

Audit Report
++++++++++++

The admin user can view and download audit reports of user logins, logouts, and workflow modifications.

.. figure:: ../../_assets/security/admin_user/admin_audit.PNG
   :alt: security
   :width: 70%

Credential Store
+++++++++++++++++

The admin user can add credentials to the credential store. When creating connections, values such as usernames and passwords can be fetched from the credential store.

.. figure:: ../../_assets/security/admin_user/admin_credentials.PNG
   :alt: security
   :width: 70%

TEST LDAP
+++++++++++++++++

The admin user can test LDAP configuration to ensure it is configured correctly (only when the LDAP properties file has been updated).

.. figure:: ../../_assets/security/admin_user/admin_ldap.PNG
   :alt: security
   :width: 70%

Backup DB
+++++++++++++++++

The admin user can back up the database (only if the application is running on H2 DB) to a configured location.


.. figure:: ../../_assets/security/admin_user/admin_bkp.PNG
   :alt: security
   :width: 70%

Runtime Statistics
++++++++++++++

The admin user can view the total number of logged-in users, Fire Spark processes, Fire PySpark processes, and running jobs.


.. figure:: ../../_assets/security/admin_user/admin_statistics.PNG
   :alt: security
   :width: 70%

Scheduler Statistics
++++++++++++++

The admin user can view the statistics of scheduled jobs.

.. figure:: ../../_assets/security/admin_user/admin_scheduler_statistics.PNG
   :alt: security
   :width: 70%

Cache Statistics
++++++++++++++

The admin user can view cache statistics for logged-in users and data sources such as Snowflake and Databricks.

.. figure:: ../../_assets/security/admin_user/admin_cache_statistics.PNG
   :alt: security
   :width: 70%
