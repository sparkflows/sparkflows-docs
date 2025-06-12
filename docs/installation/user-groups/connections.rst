Connections
-----------

Connections enable access to various resources and can be established at different levels:

* **Global:** Everyone has access to these connections.
* **Group:** Users belonging to the group have access to these connections.
* **Project:** The owner of the project and the groups with which the project has been shared have access to the project-level connections.
 
Sparkflows offers following types of connections:

#. Compute Connection 
#. Storage Connection 
#. GenAI Connection
#. Vector Databse Connections

In Sparkflows, **Compute Connection** enables the following: 

  * Databricks 
  * Glue 
  * Livy
  * Spark Submit

In Sparkflows, **Storage Connection** enables the following:

  * Cassandra
  * Hive
  * BigQuery
  * Incorta
  * InfluxDB
  * JDBC
  * Mongo DB
  * MySQL
  * PostgreSQL
  * Red Shift
  * Oracle
  * SFTP
  * SQL Server
  * Snowflake
  * Trino
  * SeviceNow
  * Confluence
  * Sharepoint

In Sparkflows, **GenAI Connection** enables the following:

  * Azure OpenAI
  * OpenAI
  * Gemini
  * Databricks LLM
  * Vertex Palm API
  * Bedrock connection
  
In Sparkflows, **Vector DB Connection** enables the following:

  * Pinecone

Job Execution
--------------

Single Group Assignment
++++++++

* When a **User** is assigned to a single **User Group** in the **Fire Insights** then the connection associated to the **User Group** would be used for the Job Execution.

* When a **Project** is shared with multiple **Groups** however, **Logged-In User** is assigned only to a single **Group** then connections associated with that **User Group** would be used for the Job Executions.

Multiple Group Assignment
++++++++

* When a **User** is assigned to multiple **User Groups** in the **Fire Insights** and Project is shared with only one **User Group** i.e. X then the connection associated to **User Group-X** would be used for the Job Execution.

* When a **User** is assigned to multiple **User Groups** in the **Fire Insights** and Project is also shared with mutiple **User Groups**. In this scenario the Job Execution would use a connection from the Group having **ID** value of **1**.

Connection Creation Privileges
--------------

For All Or For A Group
++++++++

* A **User** with **users.manage** and **connections.manage** permissions can create connections for **For All Or For A Group**

* **For All Or For A Group** connections can be created by navigating to **Administration -> Global/Group Connections**. Corresponding card would be displayed only when a **User** has above permissions.

For A Project
++++++++

* A **User** with only **connections.manage** permission and no **users.manage** permission can create connections only at the **Project** level.

* **Project** connections can be created by navigating to **Project Dashboard -> Connections**.
