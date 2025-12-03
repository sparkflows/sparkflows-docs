Sharing Projects
================

Overview
--------

A project can be shared with multiple groups. A project is visible only to users who belong to the groups with which it has been shared.

Below is a project shared with the **DEFAULT** group:

.. figure:: ../../_assets/security/project_share.PNG
   :alt: security
   :width: 60%

The following permissions can be granted to a group when sharing the project:

.. figure:: ../../_assets/security/project_group.PNG
   :alt: security
   :width: 60%

All users belonging to the group receive the associated permissions for the project.


AWS ARN Role
------------

Each group has associated ARN Roles. They get used when accessing files on S3. This is done by Sparkflows by assuming the ARN Role specified in the group of the user.

If a Project is shared with one group, then the ARN role of that group gets used.

If a user is a member of multiple groups with IDs (1, 2, 3) in Sparkflows, AWS ARN Role will pick the group with ID 1. The group is selected by ID in ascending order.

.. note:: Sparkflows supports one AWS ARN role for every user and it fetches the role based on ID in ascending order.


Connections
-----------

Connections can be a Global, Group and Project levels.

If a Project is shared with a Group, then all the connections associated with that group are available to the users when building the workflows.

If a Project is shared with multiple Groups - say X and Y, and a user belongs to only Group Y, then the user would see all the Connections belonging to the Y group.




