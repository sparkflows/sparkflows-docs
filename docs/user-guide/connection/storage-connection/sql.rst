SQL Server Connection
================

In Fire Insights, Connections can be made to SQL Server. This helps users to access and manage data files stored in the SQL server database. This is done with the help of JDBC Connection nodes that can be used in workflows to read and write data from and to SQL server database.

  * Download MSSQL JDBC Driver
  * Install the JDBC Driver
  * Restart Fire Insights
  * Create the MSSQL Connection

Download MSSQL JDBC Driver
-------------

- SQL JDBC Driver can be downloaded directly from maven repository : https://mvnrepository.com/artifact/com.microsoft.sqlserver/mssql-jdbc/12.10.0.jre11
- Ensure that the JDBC JAR file is available in the directory.
- Use the JAR file (mssql-jdbc-12.10.0.jre11.jar) for installation in the Fire.

Install the JDBC Driver
--------

In order to install the JDBC driver copy the driver jdbc jar file into ``fire-user-lib`` and ``fire-server-lib`` directories under the Fire installation home directory.

Restart Fire Server
------------

Once you have copied the JDBC driver into the required folder, restart the Fire server with ``./run-fire-server.sh restart`` for it to register the new driver.

This will restart the Fire services automatically.

Creating Connection
-------------------

* **Who can create?**

  A connection to SQL server can be created either a by an Administrator or other users.

* **Types of connections**

  It can be created at various levels depending on the need:

  - **Global Level Connection**: which is accessible to all users.
  - **Group Level Connection**: which is accessible only to the members of the specified group.
  - **Project Level Connection**: which is accessible only to the project owner and members of the group with which the project has been shared. 

**Steps to create connection**
+++++

**Create Global and Group Connections:**

#. **Login** to Fire Insights.
#. From the Dashboard page, click **Administration** tab in the top-bar.
#. From the Administration page, click **Global Connections**.
   
   .. figure:: ../../../_assets/connections/admin-page.png
        :alt: SQL Server
        :width: 70%

#. From Connections List page, click **Add Connection** and choose a type from the drop-down list:
   
   - **Add Connection For All**: to create a global level connection.
   - **Add Connection For Group**: to create a group level connection.
   
   .. figure:: ../../../_assets/connections/add-connection-page.png
        :alt: SQL Server
        :width: 70%

#. In the Add Connection dialog box, specify all the parameters e.g. SQL Server Username, Password, JDBC URL, etc.

   For more details on configuration parameters read about :ref:`configuration details.<Configuration Details>`

   .. figure:: ../../../_assets/connections/sql_connection.PNG
        :alt: SQL server
        :width: 55%

#. Click on **Test Connection** to test your connection.
#. After successful test completion, click **Save** to save your connection.

**Create Project Connection:**

#. Open the **Project** for which you want to create a connection.
#. Click **Settings** tab in upper-middle bar.
#. Click **Connections** on the LHS.
#. Click **Add Connection or Add new connection**.

   .. figure:: ../../../_assets/connections/add-connection-project.png
        :alt: SQL Server
        :width: 70%

#. In the Add Connection dialog box, fill in all the parameters as above.
   
   Follow the rest of the process as mentioned above for global connection.

Using Connection
--------
Now, you are ready to start using the SQL Server Connection in Fire Insights using Read JDBC nodes.

   .. figure:: ../../../_assets/connections/sql_node.PNG
      :alt: SQL Server
      :width: 70%

