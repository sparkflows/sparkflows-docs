Databricks Security
===================

Users in Fire Insights access Databricks via Databricks Tokens.

Whenever users interact with Databricks in Fire Insights, they have the access which is assigned to the token in Databricks.

Below diagrams show the integration of Fire Insights with Databricks.

.. figure:: ..//_assets/security/databricks-integration.png
   :alt: security
   :width: 60%
   
   
.. figure:: ..//_assets/security/databricks-api.png
   :alt: security
   :width: 60%   

Viewing DB/Tables
-----------------

In Fire Insights users can view the databases and tables. They are accessed via JDBC from Databricks cluster using the token.

The same applies if users chose to execute a query to view a few records from the table.

.. figure:: ..//_assets/security/databricks-table.PNG
   :alt: security
   :width: 60% 

Executing Workflows
-------------------

When users execute workflows in Fire Insights, they are submitted to the Databricks cluster view the REST API using the Databricks token. These jobs post back messages to Fire Insights. They use a token generated specifically for the job to post back the messages.


Databricks Connections
-----------------------

The Databricks cluster details and token are specified in a Connection. The user uses the connections when talking to Databricks.

Connections can be at the global level or at the Project level. Global level connections are created by the admin user. Project level connections are created by the Project users.

Fire Insights would also support defining Group level connections.

.. figure:: ..//_assets/security/databricks-connection.PNG
   :alt: security
   :width: 60% 


