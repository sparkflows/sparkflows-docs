Databricks Security
===================

Users in Fire Insights access Databricks via **Databricks Tokens**. Whenever users interact with Databricks in Fire Insights, they have access according to the permissions assigned to the token in Databricks. The following diagrams show the integration of Fire Insights with Databricks:

.. figure:: ../../_assets/security/databricks-integration.png
   :alt: security
   :width: 60%
   
   
.. figure:: ../../_assets/security/databricks-api.png
   :alt: security
   :width: 60%   

Viewing DB/Tables
-----------------

In Fire Insights, users can view databases and tables. These are accessed via **JDBC** from the Databricks cluster using the token. The same applies if users choose to execute a query to view records from the table.

.. figure:: ../../_assets/security/databricks-table.PNG
   :alt: security
   :width: 60% 

Executing Workflows
-------------------

When users execute workflows in Fire Insights, they are submitted to the Databricks cluster via the **REST API** using the Databricks token. These jobs post messages back to Fire Insights. They use a token generated specifically for the job to post back the messages.


Databricks Connections
-----------------------

The Databricks cluster details and token are specified in a connection. Users use these connections when interacting with Databricks. Connections can be at the global level or the project level. Global-level connections are created by the admin user, while project-level connections are created by project users. Fire Insights also supports defining group-level connections.

.. figure:: ../../_assets/security/databricks-connection.PNG
   :alt: security
   :width: 60% 


