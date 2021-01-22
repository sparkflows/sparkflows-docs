Admin user
===========

Fire Insights come up with Admin access role which have below privilege

.. list-table:: 
   :widths: 10 20 
   :header-rows: 1

   * - Title
     - Description
   * - users.manage
     - create, modify permission & disable user
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
     
     
.. figure:: ..//_assets/security/admin_priv.PNG
   :alt: security
   :width: 60%
     
   * - apps.execute
     - execute analytics application
   * - apps.view
     - view analytics application

.. note:: apart from that admin user can do below functionality

- Diagnostics
Using it, he can view detail informations about Fire Insights Machine environments.

.. figure:: ..//_assets/security/diagnostic.PNG
   :alt: security
   :width: 60%

- Usage Statistics
Using it, he can view Total Users, Groups, Roles, Projects, Workflows & Workflows Executions

.. figure:: ..//_assets/security/usgae_satatistics.PNG
   :alt: security
   :width: 60%
   
- Runtime Statistics
Using it, he can view Total Logged In User, Total Fire Spark Process, Total Fire Pyspark Process & Total Running Jobs

.. figure:: ..//_assets/security/runtime.PNG
   :alt: security
   :width: 60%
   
- Sample Projects
- Global Connections
- Server Logs
- Cleanup Data

