Admin user
===========

Fire Insights support variety of permissions for Roles. Each user can be assigned one more more Roles.

Permissions supported by Fire Insights
----------------------

Below are the permissions supported by Fire Insights.

.. figure:: ..//_assets/security/admin_priv.PNG
   :alt: security
   :width: 60%
     
     
.. list-table:: 
   :widths: 10 20 
   :header-rows: 1

   * - Title
     - Description
   * - users.manage
     - create, modify & disable user
   * - groups.manage
     - Create, modify & delete the group
   * - roles.manage
     - Create, modify & delete the roles  
   * - projects.manage
     - Create, modify & delete the projects
   * - configurations.manage
     - modify diiferent configurations 
   * - connections.manage
     - add & modify diifferent connections  
   * - datasets.view
     - view dataset in specified project
   * - datasets.modify
     - modify datasets in specified project
   * - workflows.view
     - view workflows in specified project
   * - workflows.modify
     - modify workflows in specified project
   * - workflows.execute
     - execute workflow in specified project
   * - apps.modify
     - modify analytics application 
   * - apps.execute
     - execute analytics application
   * - apps.view
     - view analytics application
     
Permissions for Admin User
-------------

In Fire Insights generally the below permissions are associated with Admin features

- users.manage
- groups.manage
- roles.manage
- configurations.manage

An admin user in Fire Insights is one who has users.manage permission.

Admin User Rights
-----------------

The Admin user gets the following rights.

Operating Fire Insights
++++++++++++++++++++++++

In Fire Insights an admin user can do the following administration tasks:

- Configure Fire Insights
- Run Diagnostics
- Manage Users, Groups, Permissions
- Load Sample Projects
- View Server Logs
- Cleanup Data

Projects/Data etc
+++++++++++++++++

As regards to data, the Admin user can do the following:

- Can the Admin user view other users projects? : NO
- Can the Admin user view the execution of Projects/workflows they are not part of? NO

- Onboarding Analytics Apps for a Customer
    - Who creates that Project which will hold the Analytics App? Admin user. Now the admin user becomes the owner of that Project and be able to see everything.
    - Who shares that project with the Group of the Customer? Admin user.
    
- Can a user be deleted? Can all the data associated with a user be deleted? : NO
- Can a group be deleted? : NO
    - If a group is deleted, all the projects who share with that group, the sharing entries should be deleted.
- Can an Admin user who is not part of a Project, share that Project with other Groups? : NO


     
Details on the Admin user rights
--------------------

Diagnostics
++++++++++

The admin user can view detailed informations about Machine environments.

.. figure:: ..//_assets/security/diagnostic.PNG
   :alt: security
   :width: 60%

Usage Statistics
++++++++++++++

The admin user can view Total Users, Groups, Roles, Projects, Workflows & Workflows Executions

.. figure:: ..//_assets/security/usgae_satatistics.PNG
   :alt: security
   :width: 60%
   
Runtime Statistics
++++++++++++++

The admin user can view Total Logged In Users, Total Fire Spark Processes, Total Fire Pyspark Processes & Total Running Jobs

.. figure:: ..//_assets/security/runtime.PNG
   :alt: security
   :width: 60%
   
Sample Projects
+++++++++++++

The admin user can RELOAD SAMPLE PROJECTS, as by default Fire Insights comes with sample projects containing different types of workflows & datasets

.. figure:: ..//_assets/security/reload_sample.PNG
   :alt: security
   :width: 60%

Global Connections
+++++++++++++++++++

The admin user can Add Connections which everyone can use and also connections at the Group Level.

.. figure:: ..//_assets/security/connection.PNG
   :alt: security
   :width: 60%

Server Logs
++++++++

The admin user can view Fire Server Logs, Fire Logs, Fire Exception Logs & Fire Pyspark Logs

.. figure:: ..//_assets/security/logs.PNG
   :alt: security
   :width: 60%
   
Cleanup Data
+++++++++++

The admin user can Delete old workflow executions for cleaning the DB which is Older than  Last 7 days, Older than  Last 30 days, Older than  Last 90 days & Delete All Executions

.. figure:: ..//_assets/security/cleanup.PNG
   :alt: security
   :width: 60%
