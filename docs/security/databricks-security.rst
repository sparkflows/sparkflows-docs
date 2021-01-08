Databricks Security
===================

Users in Fire Insights access Databricks via Databricks Tokens.

Whenever users interact with Databricks in Fire Insights, they have the access which is assigned to the token in Databricks.

Below diagrams show the integration of Fire Insights with Databricks.

---image---

Viewing DB/Tables
-----------------

In Fire Insights users can view the databases and tables. They are accessed via JDBC from Databricks cluster using the token.

The same applies if users chose to execute a query to view a few records from the table.


Executing Workflows
-------------------

When users execute workflows in Fire Insights, they are submitted to the Databricks cluster view the REST API using the Databricks token.



