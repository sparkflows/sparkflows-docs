Databricks Workspace Connection
=====

Sparkflows enables you to create Databricks Workspace connection and use the connection to sync to Airflow and use it in pipelines.

Connections can be at various levels:

  * Global : Everyone has access to these connections.
  * Group  : Users belonging to the group have access to these connections.
 
Below are the steps required to create Databricks Workspace connection:

Step 1 : Go to Connections Page
----------

#. **Login** to Sparkflows web server URL as an **Admin**.
#. Navigate to **ADMINISTRATION** Page from the top bar.
#. Click **Global Connections** from the Administration Page.

   .. figure:: ../../_assets/installation/connection/databricks-admin.png
      :alt: connection
      :width: 60%

   **Note :** Global Connections are available for everyone to use.

Step 2 : Open Add Connection Window
-----------------------

#. Click **Add Connection** button located on the top-right corner of the Connections Page.

   .. figure:: ../../_assets/installation/connection/databricks-connection.png
      :alt: connection
      :width: 60%

Step 3 : Enter Parameter Details
----------------
#. Enter parameter details in the Add Connection window.

   For more details refer the following tables and images:

   **GENERAL Tab:**

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
        - Select Category as Workspace
        - Select Workspace
      * - CONNECTION TYPE 
        - Default Workspace Databricks
        - by Default Workspace Databricks would be selected
      * - CONNECTION NAME
        - Connection Name
        - Add an unique Connection Name
      * - TOKEN 
        - Token
        - Add token generated
      * - TITLE 
        - Title for selected Connection
        - Add an unique Title
      * - DESCRIPTION
        - Connection Description
        - Add some Connection Description
      * - URL
        - URL for Databricks Workspace
        - Add Databricks Workspace Url from the Databricks. Example: https://xxxxxxxx.databricks.net

   .. figure:: ../../_assets/installation/connection/databricks_general.PNG
      :alt: connection
      :width: 60%    

   
   **WORKSPACE DATABRICKS Tab:**

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
     
   .. figure:: ../../_assets/installation/connection/databricks_other.PNG
      :alt: connection
      :width: 60%
