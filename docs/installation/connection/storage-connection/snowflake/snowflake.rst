Snowflake Basic Connection
=======

Sparkflows provides the capability to create "Snowflake Connection" and use the connection to access various resources, using User Credentials.

Below are the steps for creating the Snowflake Connection.

Step 1 : Navigate to Administration/Global Connections
-------------
#. **Login** to Fire Insights application.
#. Go to **Administration** and select **Global Connections**.

   .. figure:: ../../../..//_assets/credential_store/create-snowflake-connection/admin-page.png
      :alt: Credential Store
      :width: 65%

Step 2 : Add Connection
-----------
#. Click on **ADD CONNECTION**.
#. Choose either **Add Connection For All** or **Add Connection For Group** based on your requirements.

   .. figure:: ../../../..//_assets/credential_store/create-snowflake-connection/connection-type.png
      :alt: Credential Store
      :width: 65%

Step 3 : Add Connection Parameter
--------------------------
Add connection parameters using the below table:


   .. list-table:: 
      :widths: 10 20 20
      :header-rows: 1


      * - Title
        - Description
        - Value
      * - Credential Store  
        - Select the Credential Store from drop-down
        - Choose specific Credential Store from drop-down or Select Do not use Credential Store
      * - Select Category
        - Select Category of Connection Type
        - Select Storage Connection
      * - Connection Type 
        - Select the Connection type from drop-down
        - Choose Snowflake as Connection Type
      * - Authentication Type 
        - Select the USER_CREDENTIAL or OAUTH
        - Choose USER_CREDENTIAL as Authentication Type
      * - Connection Name
        - Connection Name
        - Add an unique Connection Name
      * - Username 
        - Username
        - Username for Snowflake
      * - Password
        - Password
        - Password of Snowflake
      * - Title 
        - Title for selected Connection
        - Add an unique Title
      * - Warehouse 
        - Warehouse
        - Type Warehouse name which have access
      * - Description
        - Connection Description
        - Add some Connection Description
      * - Url
        - Url for Snowflake
        - Url for Snowflake

   .. figure:: ../../../../_assets/installation/connection/snowflake_storage.PNG

      :alt: connection
      :width: 60%  

Step 4 : Test and Save Connection
-------------------------
#. After adding the parameters, click on **TEST CONNECTION** to verify the connection.
#. Once the success notification is received, click **Save** to store the connection details.

   .. figure:: ../../../../_assets/credential_store/create-snowflake-connection/connection-parameters.png
      :alt: Credential Store
      :width: 50%       

   After saving, the connection would display on the connections list page as shown below.

   .. figure:: ../../../../_assets/credential_store/create-snowflake-connection/connection-list.png
      :alt: Credential Store
      :width: 65%


   Once you save the connection, resouces can be used inside workflow editor etc. using the above connection.

Documentation
-----

Reference guide : https://docs.sparkflows.io/en/latest/snowflake/index.html
