Redshift Connection
================

Fire Insights provides the capability to create a "Redshift connection" and use it for reading from and writing to Amazon Redshift tables. Below are the steps for creating a Redshift connection in Fire Insights:

.. Note:: you can use jdbc connection type to create Redshift connection too and use it in read jdbc and Save jdbc node.

Connections can be at various levels:

  * Global  : Everyone has access to these connections.
  * Group   : Users belonging to the group have access to these connections.
  * Project : The owner of the project and the groups with which the project has been shared with have access to the project level connections.

This page shows how to create a "Redshift Connection" in Fire Insights.

Create the Redshift Connection
-----

Create the Redshift Connection at Global, Group or Project level.

Connection Details
++++

Enter the configuration details with the help of table given below and click on ``Add Connection``.

   .. figure:: ../../../_assets/connections/redshift_1.PNG
      :alt: redshift
      :width: 60%

   
   .. figure:: ../../../_assets/connections/redshift_2.PNG
      :alt: redshift
      :width: 60%

Connection Field Details
----------------------

   .. list-table:: 
      :widths: 25 25 50
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
        - Choose Postgres as Connection Type
      * - Connection Name
        - Connection Name
        - Add an unique Connection Name
      * - Username 
        - Username
        - Username for Redshift
      * - Password
        - Password
        - Password of Redshift
      * - Title 
        - Title for selected Connection
        - Add an unique Title
      * - Description
        - Connection Description
        - Add some Connection Description
      * - Url
        - Url for Redshift
        - JDBC Url for Redshift
      * - Driver Class
        - Driver Class Name for Redshift
        - com.amazon.redshift.jdbc42.Driver (by default)


Test Connection and Save
+++++

Once you have entered the connection details, click on "Test Connection". If the connection is successful,  click on "Save" to save the connection. 

Now, you are ready to start using the Connection in workflows.


.. Note:: Make sure that Redshift URL should be accessible from Sparkflows web server URL.


Run Workflows and Pipelines
-----------------

Now you can use the connection in Read jdbc Node to run the workflows/pipelines.
