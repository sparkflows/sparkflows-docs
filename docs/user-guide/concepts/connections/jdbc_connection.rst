SQL Server
=========

In Fire Insights, Connections can be made to SQL Server. This helps users to access and manage data files stored in the SQL server database. This is done with the help of JDBC Connection nodes that can be in Workflows to read and write data from and to SQL server database.


Creating Connection
-------------------

**Who can create?**
+++++
A connection to SQL server can be created either a by an Administrator or other users.

**Types of connections**
+++++++
It can be created at various levels depending on the need:

#. ``Global Level Connection``: which is accessible to all users.
#. ``Group Level Connection``: which is accessible only to the members of the specified group.

**Prerequisite**
+++++++

It is necessary to have the **JDBC Driver** installed in Fire Insights before you create a connection. 

This will help in establishing connection to MySQL JDBC source.

Steps to create connection
+++++

#. **Login** to Fire Insights.
#. From the Dashboard page, click **Administration** tab in the top-bar.
#. From the Administration page, click **Global Connections**.
   
   .. figure:: ../../../_assets/connections/admin-page.png
      :alt: Databricks
      :width: 70%

#. From Connections List page, click **Add Connection** and choose a type from the drop-down list:
   
   - **Add Connection For All**: to create a global level connection.
   - **Add Connection For Group**: to create a group level connection.
   
   .. figure:: ../../../_assets/connections/add-connection-page.png
      :alt: Databricks
      :width: 70%

#. In the Add Connection dialog box, specify all the parameters e.g. SQL Server Username, Password, JDBC URL, etc.

   For more details on configuration parameters read :ref:`configuration details.<MySQL Connection>`

   .. figure:: ../../../_assets/connections/sql_connection.PNG
      :alt: Databricks
      :width: 70%

#. Click on **Test Connection** to test your connection.
#. After successful test completion, click **Save** to save your connection.

Using Connection
--------
Now, you are ready to start using the SQL Server Connection in Fire Insights using Read JDBC nodes.

   .. figure:: ../../../_assets/connections/sql_node.PNG
      :alt: Databricks
      :width: 70%
