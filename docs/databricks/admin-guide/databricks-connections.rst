Databricks Connection
=======

Sparkflows enables you to create Databricks connection and use the connection to submit job on respective Databricks cluster. 

Connections can be at various levels:

  * Global : Everyone has access to these connections.
  * Group  : Users belonging to the group have access to these connections.
  * Project: The owner of the project and the groups with which the Project has been shared with have access to the Project level connections.

Below are the steps required to create Databricks connection:

Step 1 : Go to Connections Page
----------

#. **Login** to Sparkflows web server URL as an **Admin**.
#. Navigate to **ADMINISTRATION** Page from the top bar.
#. Click **Global Connections** from the Administration Page.

   Note : Global Connections are available for everyone to use.

Step 2 : Open Add Connection Window
-----------------------
#. Click **Add Connection** button located on the top-right corner of the Connections Page.

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
        - Select Category of Connection Type
        - Select Compute Connection
      * - CONNECTION TYPE 
        - Select the Connection type from drop-down
        - Choose Databricks as Connection Type
      * - CONNECTION NAME
        - Connection Name
        - Add an unique Connection Name
      * - TOKEN 
        - Token
        - Add token generated
      * - POSTBACK URL
        - Fire Insights Post Back URL
        - Add Fire Insights Post Back URL
      * - TITLE 
        - Title for selected Connection
        - Add an unique Title
      * - DESCRIPTION
        - Connection Description
        - Add some Connection Description
      * - URL
        - Jdbc url for databricks connection
        - Add Jdbc Url for Databricks Connection

   .. figure:: ../../_assets/installation/connection/databricks_general.PNG
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
        - Scratch directory on DBFS where it have Read/Write/Delete Permissions.
        - Scratch directory on DBFS where it have Read/Write/Delete Permissions(User can update absolute dbfs path).
     
   .. figure:: ../../_assets/installation/connection/databricks_other.PNG
      :alt: connection
      :width: 60%    


Step 4 : Test and Save Connection
---------------

#. Click **TEST CONNECTION**. You will get a success notification.
#. Click **SAVE** to save the connection.

   Once you save the connection, it can be used for submitting the job on specific Databricks cluster.

.. note:: Make sure to add a POSTBACK URL through which jobs running on Databricks will post back results to Sparkflows. Otherwise, it will use the URL specified in app.postMessageURL in the configuration.


Documentation
--------

For more details read `Databricks User Guide <https://docs.sparkflows.io/en/latest/databricks-user-guide/index.html>`_




Setting Current Connection
------------------

A user can set their current connection from the list. Here, the user can choose from among the global, group level, or project level connections.


Data or Databricks Clusters
+++++++++++++++

Here, the user can choose between the global and group level connections. 

When the user lands on this page, the user's current connection is chosen by default.

Data or DBFS
+++++++++++++++

Here, the user can choose between the global and group level connections.

When the user lands on this page, the user's current connection is chosen by default.


Data or Databricks Database
+++++++++++++++

Here, the user can choose between the global and group level connections.

When the user lands on this page, the user's current connection is chosen by default.


Workflow Editor
+++++++++++++++

Here, the connection is chosen in the following order of priority:

  * Project level connection
  * Group level connection
  * Global connection
  
  
Workflow Execute
+++++++++++++++

Here, the connection is chosen in the following order of priority:

  * Current Connection (if it belongs to the same group as the workflow)
  * Project level connection
  * Group level connection
  * Global connection
    
Analytical Apps
+++++++++++++++

Here, the connection is chosen in the following order of priority:

  * Project level connection
  * Current Connection (but it cannot be from another Project)
  * Group level connection
  * Global connection
  
  



