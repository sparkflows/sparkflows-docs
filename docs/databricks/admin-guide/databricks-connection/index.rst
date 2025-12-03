Databricks Connections
======================

Sparkflows connects to Databricks using Connections.

Connections in Sparkflows can be a various levels:

  * Global Connections
  * Group Level Connections
  * Project Level Connections
  
Global Connections
------------------

The admin users in Sparkflows can configure the global connections. These are available for all the users logged into Sparkflows.


Group Level Connections
-----------------------

The admin users in Sparkflows can configure group level connection. These are available to use to the users belonging to that group.

Project Level Connections
-------------------------

Users of a project can create connections within the Project. These can be used for operations associated with that Project.

Setting Current Connection
--------------------------

A user can set their current connection from the list. Here the user can choose from the global and group level connections. And also from project level connections.


Scenarios
----------

Data/Databricks Clusters
+++++++++++++++

Here the user can choose from global and group level connections. 
When the user lands on this page, the user's current connection is chosen by default.

Data/DBFS
+++++++++++++++

Here the user can choose from global and group level connections.
When the user lands on this page, the user's current connection is chosen by default.


Data/Databricks DB
+++++++++++++++

Here the user can choose from global and group level connections.
When the user lands on this page, the user's current connection is chosen by default.


Workflow Editor
+++++++++++++++

Here the connection is chosen in the following order of priority:

  * Project level connection
  * Group level connection
  * Global connection
  
  
Workflow Execute
+++++++++++++++

Here the connection is chosen in the following order of priority:

  * Current Connection (if it belongs to the same group as the workflow)
  * Project level connection
  * Group level connection
  * Global connection
    
Analytical Apps
+++++++++++++++

Here the connection is chosen in the following order of priority:

  * Project level connection
  * Current Connection (but it cannot be from another Project)
  * Group level connection
  * Global connection
  
  



