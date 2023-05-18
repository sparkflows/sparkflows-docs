Snowflake
=========

In Fire Insights, connections can be made to Snowflake so that users can access and manage data files stored in the Snowflake database. This is done with the help of Snowflake connection nodes that can be used in workflows to read and write data from and to Snowflake database.

Creating Connection
-------------------

**Who can create?**
+++++
A snowflake connection can be created either a by an Administrator or other users.

**Types of connection:**
+++++++
It can be created at various levels depending on the need:

#. **Global Level Connection**: which is accessible to everyone.
#. **Group Level Connection**: which is accessible only to the members of specified group.
#. **Project Level Connection**: which is accessible only to the project owner and members of the group with which the project has been shared. 

**Steps to create connection**
+++++

**Create Global and Group Connections:**

#. **Login** to Fire Insights.
#. From the Dashboard page, click **Administration** tab in the top-bar.
#. From the Administration page, click **Global Connections**.

   .. figure:: ../../../_assets/connections/admin-page.png
      :alt: snowflake
      :width: 70%
#. From Connections List page, click **Add Connection** and choose a type from the drop-down list:
   
   - **Add Connection For All**: to create a global level connection.
   - **Add Connection For Group**: to create a group level connection.
   
   .. figure:: ../../../_assets/connections/add-connection-page.png
      :alt: snowflake
      :width: 70%

#. In the Add Connection dialog box, specify all the parameters e.g. SQL Server Username, Password, JDBC URL, etc.

   For more details on configuration parameters read about :ref:`how to create a Snowflake connection.<Create Snowflake Connection>`

   .. figure:: ../../../_assets/connections/snowflake_connection.PNG
      :alt: snowflake
      :width: 70%

#. Click on **Test Connection** to test your connection.
#. After successful test completion, click **Save** to save your connection.

**Create Project Connection:**

#. Open the **Project** for which you want to create a connection.
#. Click **Settings** tab in upper-middle bar.
#. Click **Connections** on the LHS.
#. Click **Add Connection or Add new connection**.

   .. figure:: ../../../_assets/connections/add-connection-project.png
      :alt: snowflake
      :width: 70%

#. In the Add Connection dialog box, fill in all the parameters as above.
   
   Follow the rest of the process as mentioned above for global connection.


Using Connection
------

**Read from Snowflake**
+++++
Now, you are ready to start using the Snowflake Connection in Fire Insights.

- Fire, now, enables you to read data from snowflake using **Read From Snowflake** node.

- A list of all created snowflake connections will be listed and users can choose to read data from any of the connections.

- Add all required details e.g. SF DATABASE, SF SCHEMA, SF WAREHOUSE, SF TABLE. 

- Refresh schema before continuing further.

  .. figure:: ../../../_assets/connections/snowflake_read.PNG
     :alt: snowflake
     :width: 70%

**Write to Snowflake**
++++++

- Fire, now, enables you to write data to snowflake using **Write To Snowflake** node.

- A list of all created snowflake connections will be listed and user can choose to read data from any of the connections.

- Add all required details e.g. SF DATABASE, SF SCHEMA, SF WAREHOUSE, SF TABLE. 

  .. figure:: ../../../_assets/connections/snowflake_write.PNG
     :alt: snowflake
     :width: 70%
     
For detailed information on nodes usage read, :ref:`how to read from and write to Snowflake.<Snowflake>`    
