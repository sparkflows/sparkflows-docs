Databricks Connections
======================

Fire Insights connects to Databricks using Connections.

Connections in Fire Insights can be at various levels:

  * Global Connections
  * Group Level Connections
  * Project Level Connections
  
Global Connections
------------------

The admin users in Fire Insights can configure the global connections. These connections are available for all the users logged into Fire Insights.


Group Level Connections
-----------------------

The admin users in Fire Insights can configure group level connection. These connections are available for use to the users belonging to that group.

Project Level Connections
-------------------------

Users of a project can create connections within the Project. These connections can be used for operations associated with that Project.

Setting Current Connection
--------------------------

A user can set their current connection from the list. Here, the user can choose from among the global, group level, or project level connections.
----------

Data or Databricks Clusters
+++++++++++++++

Here, the user can choose between the global and group level connections. 
When the user lands on this page, the user's current connection is chosen by default.

Data or DBFS
+++++++++++++++

Here, the user can choose between the global and group level connections.
When the user lands on this page, the user's current connection is chosen by default.


Data or Databricks Database
+++++++++++++++

Here, the user can choose between the global and group level connections.
When the user lands on this page, the user's current connection is chosen by default.


Workflow Editor
+++++++++++++++

Here, the connection is chosen in the following order of priority:

  * Project level connection
  * Group level connection
  * Global connection
  
  
Workflow Execute
+++++++++++++++

Here, the connection is chosen in the following order of priority:

  * Current Connection (if it belongs to the same group as the workflow)
  * Project level connection
  * Group level connection
  * Global connection
    
Analytical Apps
+++++++++++++++

Here, the connection is chosen in the following order of priority:

  * Project level connection
  * Current Connection (but it cannot be from another Project)
  * Group level connection
  * Global connection
  
  



