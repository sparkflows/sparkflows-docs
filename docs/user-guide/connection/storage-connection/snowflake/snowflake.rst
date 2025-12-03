Snowflake Basic Connection
=======

Sparkflows provides the capability to create "Snowflake Connection" and use the connection to access various resources, using User Credentials.

Below are the steps for creating the Snowflake Connection.

Step 1 : Navigate to Connections Page
-------------

#. Login to **Sparkflows** using your credentials.
#. From the dashboard page, Go to **Administration** and select **Global/Group Connections**, as shown below.

   .. figure:: ../../../..//_assets/credential_store/create-snowflake-connection/fire_admin_page.PNG
      :alt: Credential Store
      :width: 65%

Step 2 : Add Connection
-----------
#. From the connections page, click on **Add Connection** button located at the top right corner of the page.
#. Choose either **Add Connection For All** or **Add Connection For Group** from the dropdown based on your requirements, as shown below. An 'Add Connection' dialog box will open.

   .. figure:: ../../../..//_assets/credential_store/create-snowflake-connection/connections-add.png
      :alt: Credential Store
      :width: 65%

Step 3 : Add Connection Parameter
--------------------------
#. In 'Add Connection' dialog box, choose the category as **Storage** and connection type as **Snowflake**.

   .. figure:: ../../../..//_assets/credential_store/create-snowflake-connection/choose-snowflake.png
      :alt: Credential Store
      :width: 65%

#. Add the connection parameters using the table below:


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

   .. figure:: ../../../../_assets/credential_store/create-snowflake-connection/SFbasic-connection-parameter.png
      :alt: Credential Store
      :width: 50%       

   
  

Step 4 : Test and Save the Connection
-------------------------
#. After adding the parameters, click on **Test Connection** button to verify the connection.
#. Once the success notification is received, click on **Save** button to store the connection details.

   .. figure:: ../../../../_assets/credential_store/create-snowflake-connection/snowflake-basic.PNG
      :alt: Credential Store
      :width: 50%       

   After saving, the connection will be displayed on the connections list page as shown below.

   .. figure:: ../../../../_assets/credential_store/create-snowflake-connection/SF-connection.PNG
      :alt: Credential Store
      :width: 65%


   Once you save the connection, resources can be used inside workflow editor etc. using the above connection.

Documentation
-----

Reference guide : https://docs.sparkflows.io/en/latest/snowflake/index.html
