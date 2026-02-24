Databricks Connection
=======

Sparkflows enables you to create Databricks connection and use the connection to submit job on respective Databricks cluster. 

Connections can be at various levels:

  * Global : Everyone has access to these connections.
  * Group  : Users belonging to the group have access to these connections.
  * Project : The owner of the project and the groups with which the Project has been shared with have access to the Project level connections.

Below are the steps required to create Databricks connection:

Step 1 : Go to Connections Page
----------

#. **Login** to Sparkflows web server URL as an **Admin**.
#. Navigate to **ADMINISTRATION** Page from the top bar.
#. Go to  **Administration -> Configurations -> Connection**.
#. Enable Databricks connection by setting the below parameter to **true** and save the configuration.

   ::
  
      connection.databricks.enabled : true
#. Click **Global/Group Connections** from the Administration Page.

   .. figure:: ../../_assets/installation/connection/databricks-admin1.png
      :alt: connection
      :width: 60%

   **Note :** Global Connections are available for everyone to use.

Step 2 : Open Add Connection Window
-----------------------
#. Click **Add Connection** button located on the top-right corner of the Connections Page.
#. These connections are available for everyone to use if defined at Global level or for a particular Group if defined at the Group level.

   .. figure:: ../../_assets/installation/connection/databricks_selgrp_global.png
    :alt: connection
    :width: 60%

Step 3 : Add Connection Details
-----

#. Make selection in the **Add Connection** dialog box as shown below, to create **Databricks Compute** connection.

   .. figure:: ../../_assets/installation/connection/databricks_sel_type.png
    :alt: connection
    :width: 60%    

#. After selecting Databricks connection, the connection configuration page will appear with two tabs: **General** and **Databricks**, as shown below.

   .. figure:: ../../_assets/installation/connection/databricks_general_uc1.png
    :alt: connection
    :width: 60% 

Step 4 : Configure the Connection
----------------
#. Based on the **Authentication Type** selected, the fields will vary. Choose between **User Credential** and **OAuth**.

#. To configure the connection, refer the following tables for filling required details for ``General`` Tab and ``Databricks`` Tab:

   **GENERAL Tab (User Credential):**

   .. list-table:: 
      :widths: 10 20 20
      :header-rows: 1

      * - Title
        - Description
        - Value
      * - CREDENTIAL STORE  
        - Select the Credential Store from drop-down
        - Choose specific Credential Store from drop-down or Select Do not use Credential Store
      * - Select Category
        - Select Category of Connection Type
        - Select Compute Connection
      * - CONNECTION TYPE 
        - Select the Connection type from drop-down
        - Choose Databricks as Connection Type
      * - CONNECTION NAME
        - Connection Name
        - Add an unique Connection Name
      * - Auth Type
        - Select the Authentication Type
        - Select the appropriate option as ``User Credential``
      * - TOKEN 
        - Token
        - Add token generated from your Databricks workspace under User Settings → Access Tokens.
      * - POSTBACK URL
        - Sparkflows Post Back URL
        - Add Sparkflows Post Back URL
      * - TITLE 
        - Title for selected Connection
        - Add a unique Title
      * - DESCRIPTION
        - Connection Description
        - Add some Connection Description
      * - URL
        - Jdbc url for databricks connection
        - Add JDBC Url from the Databricks cluster. Example: ``jdbc:spark://HOST_NAME:443/default;transportMode=http;ssl=1;httpPath=sql/protocolv1/o/7174905206826341/0109-043115-vc4yc9ai;AuthMech=3;UID=token;PWD=<personal-access-token>``

   .. figure:: ../../_assets/installation/connection/databricks_general_uc1.png
    :alt: connection
    :width: 60%   

   **GENERAL Tab (OAUTH):**

   .. list-table:: 
      :widths: 10 20 20
      :header-rows: 1
   
      * - Title
        - Description
        - Value
      * - CREDENTIAL STORE  
        - Select the Credential Store from drop-down
        - Choose specific Credential Store from drop-down or Select Do not use Credential Store
      * - Select Category
        - Select Category of Connection Type
        - Select Compute Connection
      * - CONNECTION TYPE 
        - Select the Connection type from drop-down
        - Choose Databricks as Connection Type
      * - CONNECTION NAME
        - Connection Name
        - Add an unique Connection Name
      * - Auth Type
        - Select the Authentication Type
        - Select the appropriate option as ``OAUTH``
      * - POSTBACK URL
        - Sparkflows Post Back URL
        - Add Sparkflows Post Back URL
      * - Client ID 
        - Client ID for the connection
        - Enter Client ID for the connection.  Reference guide : `Azure Databricks via JDBC using OAuth Documentation. <https://docs.sparkflows.io/en/latest/azure/admin-guide/azure-databricks-via-jdbc.html>`_
      * - Client Secret 
        - Client Secret for the connection
        - Enter Client Secret for the connection.  Reference guide : `Azure Databricks via JDBC using OAuth Documentation. <https://docs.sparkflows.io/en/latest/azure/admin-guide/azure-databricks-via-jdbc.html>`_
      * - TITLE 
        - Title for selected Connection
        - Add an unique Title
      * - DESCRIPTION
        - Connection Description
        - Add some Connection Description
      * - URL
        - Jdbc url for databricks connection
        - Add Jdbc Url for Databricks Connection. Example: ``jdbc:databricks://HOST_NAME:443/default;transportMode=http;ssl=1;httpPath=sql/protocolv1/o/7174905206826341/0109-043115-vc4yc9ai;AuthMech=3;UID=token;PWD=<personal-access-token>``
   
   
   
   .. figure:: ../../_assets/installation/connection/databricks_general_oa2.png
       :alt: connection
       :width: 60%

   **DATABRICKS Tab:**

   .. list-table:: 
      :widths: 10 20 20
      :header-rows: 1

      * - Title
        - Description
        - Value
      * - Fire core JAR
        - Path of Fire core JAR dependencies
        - Absolute path of Fire core JAR  
      * - Python file
        - Path of Pyspark main file
        - Absolute path of Pyspark main file
      * - Fire PySpark libraries
        - Path of Fire pyspark libraries
        - Absolute path of Fire PySpark libraries
      * - DBFS Scratch directory
        - Scratch directory on DBFS where it has Read/Write/Delete Permissions.
        - Scratch directory on DBFS where it has Read/Write/Delete Permissions. (User can update absolute DBFS path).


   .. figure:: ../../_assets/installation/connection/databricks_other1.png
      :alt: connection
      :width: 60%    


Step 5 : Test and Save Connection
---------------

#. Click **TEST CONNECTION**. You will get a success notification.
#. Click **SAVE** to save the connection.

   Once you save the connection, it can be used for submitting the job on specific Databricks cluster.

.. note:: Make sure to add a POSTBACK URL through which jobs running on Databricks will post back results to Sparkflows. Otherwise, it will use the URL specified in app.postMessageURL in the configuration.

More details on creating these connections can be found here : `Create Databricks Connection <https://docs.sparkflows.io/en/latest/user-guide/connection/compute-connection/databricks.html>`_


Setting Current Connection
------------------

A user can set their current connection from the list. Here, the user can choose from among the global, group level, or project level connections.


**Data or Databricks Clusters:**

Here, the user can choose between the global and group level connections. 

When the user lands on this page, the user's current connection is chosen by default.

**Data or DBFS:**

Here, the user can choose between the global and group level connections.

When the user lands on this page, the user's current connection is chosen by default.


**Data or Databricks Database:**

Here, the user can choose between the global and group level connections.

When the user lands on this page, the user's current connection is chosen by default.


**Workflow Editor:**

Here, the connection is chosen in the following order of priority:

  * Project level connection
  * Group level connection
  * Global connection
  
  
**Workflow Execute:**

Here, the connection is chosen in the following order of priority:

  * Current Connection (if it belongs to the same group as the workflow)
  * Project level connection
  * Group level connection
  * Global connection
    
**Analytical Apps:**

Here, the connection is chosen in the following order of priority:

  * Project level connection
  * Current Connection (but it cannot be from another Project)
  * Group level connection
  * Global connection
  
  



