Execute CRUD Statement in Snowflake
=====

Sparkflows provides a node to execute prepared statements for Snowflake, supporting **CRUD operations** such as INSERT, UPDATE, and DELETE.

The **Execute CRUD Stmt In Snowflake** node allows execution of INSERT, UPDATE, and DELETE prepared statements. The node can be added at the **start**, **middle**, or **end** of a workflow.

Configuration Steps
----

1. Set Auth-Type and Connection Details
++++

  Configure the following:

 
  * ``Auth Type``: Select **KeyPair** from the dropdown.
  * ``Connection``: Select **SNOWFLAKE_KEYPAIR** from the dropdown.
  * ``Warehouse``: Select the required **Snowflake Warehouse** by using browse button.
  * ``Database``: Select the required **Snowflake Database** by using browse button.
  * ``Schema``: Select the required **Snowflake Schema** by using browse button. 


  .. figure:: ../../_assets/user-guide/utilities/crud-stmt-config-general.png
     :alt: CRUD Operation
     :width: 80%
  



2. CRUD Statement Configuration
++++

  Add the prepared statement along with corresponding input types and values.

  **Example Usage**

  In the example below, an **INSERT** statement is executed with **three input values**.


  .. figure:: ../../_assets/user-guide/utilities/crud-stmt-config-example.png
     :alt: CRUD Operation
     :width: 80%

















