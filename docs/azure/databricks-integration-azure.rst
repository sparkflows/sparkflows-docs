Azure Databricks Integration Steps
======================

Fire Insights integrates with Databricks. It submits jobs to the Databricks clusters using the REST API of Databricks and have the results displayed back in Fire Insights.

Fire also fetches the list of Databases and Tables from Databricks, making it easier for the user to build their workflows and execute them. In addition Fire displays the list of Databricks clusters running for the user.

* Running Databricks on Azure : https://docs.microsoft.com/en-us/azure/azure-databricks/quickstart-create-databricks-workspace-portal

Below are the steps for Integrating Fire Insights with your Databricks Clusters.

Install Fire Insights
-----------

Install Fire Insights on any machine. The machine has to be reachable from the Databricks cluster.

Upload Fire Core Jar to Databricks
----------------------------------

Upload Fire Insights jar to Databricks. Fire Insights jobs running on Databricks make use of this jar file.

Upload ``fire-x.y.z/fire-core-lib/fire-spark_2_4-core-3.1.0-jar-with-dependencies.jar`` to Databricks. Upload it under Workspace as a Library on to Databricks.

1. Login to ``Databricks Cluster``
++++++++++++++++++++++++++++++++

2. Click on ``workspace`` in the left side pane
++++++++++++++++++++++++++++++++

   .. figure:: ../_assets/configuration/azure_workspace.PNG
      :alt: Databricks
      :width: 40%
   
3. Create a new Library
++++++++++++++++++++++++++++++++
 
   .. figure:: ../_assets/configuration/library_create.PNG
      :alt: Databricks
      :width: 40%
   
4. Upload ``fire-spark_2_4-core-3.1.0-jar-with-dependencies.jar`` from your machine by Clicking on ``Drop JAR here``
++++++++++++++++++++++++++++++++

   .. figure:: ../_assets/configuration/uploadlibrary.PNG
      :alt: Databricks
      :width: 40%
   
5. Once ``fire-spark_2_4-core-3.1.0-jar-with-dependencies.jar`` is uploaded, click on ``Create``
++++++++++++++++++++++++++++++++

   .. figure:: ../_assets/configuration/createlibrary.PNG
      :alt: Databricks
      :width: 40%
   
* Check the box with ``Install automatically on all clusters``, in order to avoid installing it manually to every cluster.   
+++++++++++++++++++++++

   .. figure:: ../_assets/configuration/installautomatic.PNG
      :alt: Databricks
      :width: 40%
   
   
Configure the Uploaded Library in Fire Insights
------------------------------------

Configure the path of the uploaded fire core jar library in Databricks in Fire Insights.

This has to be done under Administration/Configuration.


.. figure:: ../_assets/configuration/databricks-configurations.PNG
   :alt: Databricks
   :width: 40%
   
   
Configure app.postMessageURL in Fire Insights
----------------------------

Configure ``app.postMessageURL`` to be the IP of the machine on which Fire Insights is installed. Jobs running on Databricks would post back results to Fire Insights using this URL.

.. figure:: ../_assets/configuration/Fireui_postbackurl.PNG
   :alt: Postback URL
   :width: 40%


Install Databricks JDBC Driver
-----------------------------------

Fire needs the Databricks JDBC Driver to be installed. Install it in the ``fire-user-lib`` and ``fire-server-lib`` folder of the Fire installation.

You can download the Databricks JDBC Driver from the Databricks site : 

* https://docs.databricks.com/bi/jdbc-odbc-bi.html
* https://databricks.com/spark/odbc-driver-download

The driver is available as a zip file. eg: ``SimbaSparkJDBC-2.6.3.1003.zip``

* Unzip the downloaded file. It will create a directory like ``SimbaSparkJDBC-2.6.3.1003``
* Copy the jdbc jar file named ``SparkJDBC4.jar`` into ``fire-x.y.z/fire-user-lib`` and ``fire-x.y.z/fire-server-lib``


Create your REST API token in Databricks
--------------

Create your token in Databricks. It would be used in making REST API calls to Databricks from Fire Insights.

1. Login to your Databricks Account
++++++++++++++++++++++++++++++++

2. Click on ``Account`` icon in right corner top
++++++++++++++++++++++++++++++++

.. figure:: ../_assets/configuration/usersetting.PNG
   :alt: Databricks
   :width: 40%
   
3. Click on ``User Settings``
++++++++++++++++++++++++++++++++

.. figure:: ../_assets/configuration/userset.PNG
   :alt: Databricks
   :width: 40%

4. Click on ``Generate New Token``
++++++++++++++++++++++++++++++++

.. figure:: ../_assets/configuration/generatetoken.PNG
   :alt: Databricks
   :width: 40%

5. Add ``comment`` & ``Lifetime(days)`` for token expiry & Click on ``Generate``
++++++++++++++++++++++++++++++++

.. figure:: ../_assets/configuration/token_update.PNG
   :alt: Databricks
   :width: 40%

6. Copy the token generated. Click on ``DONE``
++++++++++++++++++++++++++++++++

.. figure:: ../_assets/configuration/token_generated.PNG
   :alt: Databricks
   :width: 40%



Create Databricks Connection in Fire Insights
-----------------------------------

Create a connection in Fire Insights to Databricks. 

It can be created by the Administrator under Administration/Global Connections. These connections are available for everyone to use.

It can also be created by any user with their Application. In this case, it is only available to the Application and its users.

* Specify your Databricks Token.
* Specify the Databricks JDBC URL of your cluster in Databricks.

.. figure:: ../_assets/configuration/databricks_connection.PNG
   :alt: Databricks Connection
   :width: 40%


Now we are ready to start using the Databricks Connection in Fire Insights to:

* Browse DBFS
* View your Databricks Clusters
* Browse your Databricks Databases & Tables
* Create Workflows which Read from and Write to Databricks
