Snowflake
=========

In Fire Insights, Connections can be made to Snowflake. This can be used in the Snowflake nodes in the Workflow Editor for reading and writing data to Snowflake.


Creating Connection
-------------------
Create a connection in Fire Insights for Snowflake.

It can be created by the Administrator under Administration/Global Connections. These connections are available for everyone to use.

It can also be created by any user with their Application. In this case, it is only available to the Application and its users.

Specify your Snowflake Username, Password, and URL and save the details.

.. figure:: ../../../_assets/connections/snowflake_connection.PNG
   :alt: snowflake
   :width: 50%

We can also test the specified connection before saving the connection details. 

Now we are ready to start using the Snowflake Connection in Fire Insights.


Read Snowflake Node
-------------------
Fire, now, enables you to read data from snowflake using this node.

Lists of all created snowflake connections will be listed and users can choose to read data from any of the connections.

Add all required details e.g. SF DATABASE, SF SCHEMA, SF WAREHOUSE, SF TABLE. 

Refresh schema before continuing further.

.. figure:: ../../../_assets/connections/snowflake_read.PNG
   :alt: snowflake
   :width: 70%

Write Snowflake Node
--------------------
Fire, now, enables you to write data to snowflake using this node.

A list of all created snowflake connections will be listed and user can choose to read data from any of the connections.

Add all required details e.g. SF DATABASE, SF SCHEMA, SF WAREHOUSE, SF TABLE. 

For e.g. can read data from CSV and write to the snowflake.

.. figure:: ../../../_assets/connections/snowflake_write.PNG
   :alt: snowflake
   :width: 70%
