Create Snowflake Connection
=============================

In order to read from or write to Snowflake, we need to first create a Snowflake Connection in Fire Insights.

Below are the steps for creating the Snowflake Connection.

Step 1 : Navigate to Administration/Global Connections
-------------
#. **Login** to Fire Insights application.
#. Go to **Administration** and select **Global Connections**.

   .. figure:: ..//_assets/credential_store/create-snowflake-connection/admin-page.png
      :alt: Credential Store
      :width: 65%

Step 2 : Add Connection
-----------
#. Click on **ADD CONNECTION**.
#. Choose either **Add Connection For All** or **Add Connection For Group** based on your requirements.

   .. figure:: ..//_assets/credential_store/create-snowflake-connection/connection-type.png
      :alt: Credential Store
      :width: 65%


Step 3 : Add Connection Parameter
--------------------------
#. Add connection parameters using the below table:

   .. list-table:: 
      :widths: 20 80
      :header-rows: 1

      * - Title
        - Description
      * - CREDENTIAL STORE
        - Select Credential Store Listed in dropdown or else choose Do not use Credential Store.
      * - SELECT CATEGORY
        - Select Storage Connection.   
      * - CONNECTION TYPE
        - Select Connection type as Snowflake, it can be `Databricks, MySql, MOngo DB, Sql Server, HIve, Redshift and Snowflake.`
      * - CONNECTION NAME
        - Add a Connection Name.
      * - USERNAME
        - Username for the selected Snowflake Connection. 
      * - PASSWORD
        - Password for selected Snowflake Connection.
      * - TITLE
        - Add a unique title.
      * - WAREHOUSE
        - A comma seperated list of default Warehouse that users can acess via this connection. If the field is left blank, it will list all the warehourses.
      * - DESCRIPTION
        - Add description.
      * - URL
        - URL for selected Snowflake Connection.
     
     
   .. figure:: ..//_assets/credential_store/create-snowflake-connection/connection-dialog.png
      :alt: Credential Store
      :width: 50%     

Step 4 : Test and Save Connection
-------------------------
#. After adding the parameters, click on **TEST CONNECTION** to verify the connection.
#. Once the success notification is received, click **Save** to store the connection details.

   .. figure:: ..//_assets/credential_store/create-snowflake-connection/connection-parameters.png
      :alt: Credential Store
      :width: 50%       

   After saving, the connection would display on the connections list page as shown below.

   .. figure:: ..//_assets/credential_store/create-snowflake-connection/connection-list.png
      :alt: Credential Store
      :width: 65%


.. note::  Now, you can use above Snowflake connection in Read From SnowFlake, Write To SnowFlake & Execute Query In SnowFlake Processor in workflow editor.
