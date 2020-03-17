Databricks Integration
======================

Fire Insights integrates with Databricks. It submits jobs to the Databricks clusters using the REST API of Databricks and have the results displayed back in Fire Insights.

Fire also fetches the list of Databases and Tables from Databricks, making it easier for the user to build their workflows and execute them. In addition fire displays the list of Databricks clusters running for the user.

Databricks can be running on Azure or on AWS.

* Running Databricks on Azure : https://docs.microsoft.com/en-us/azure/azure-databricks/quickstart-create-databricks-workspace-portal
* Running Databricks on AWS : https://databricks.com/aws


Deployment
-----------

Install Fire Insights on any machine. The machine has to be reachable from the web via a public IP or DNS entry. Then connect Fire Insights to your Databricks Cluster

Upload Fire Core Jar to Databricks
----------------------------------

Fire Insights jar has to be uploaded to Databricks. Fire Insights jobs running on Databricks make use of this jar file.

Upload ``fire-x.y.z/fire-core-lib/fire-spark_2_3-core-3.1.0-jar-with-dependencies.jar`` to Databricks. Upload it under Workspace as a Library on to Databricks.

Login to ``Databricks Cluster``
++++++++++++++++++++++++++++++++

Click on ``workspace`` in the left side pane
++++++++++++++++++++++++++++++++

.. figure:: ../_assets/configuration/azure_workspace.PNG
   :alt: Databricks
   :align: center
   :width: 40%
   
Dropdown ``workspace``, Click on ``Create & Library``
++++++++++++++++++++++++++++++++
 
.. figure:: ../_assets/configuration/library_create.PNG
   :alt: Databricks
   :align: center
   :width: 40%
   
Upload ``fire-spark_2_3-core-3.1.0-jar-with-dependencies.jar`` from localmachine on Clicking on ``Drop JAR here``
++++++++++++++++++++++++++++++++

.. figure:: ../_assets/configuration/uploadlibrary.PNG
   :alt: Databricks
   :align: center
   :width: 40%
   
Once ``fire-spark_2_3-core-3.1.0-jar-with-dependencies.jar`` uploaded, Click on ``Create``
++++++++++++++++++++++++++++++++

.. figure:: ../_assets/configuration/createlibrary.PNG
   :alt: Databricks
   :align: center
   :width: 40%
   
* Check the box with ``Install automatically on all clusters``, Inorder to avoid uploading manually to every cluster.   

.. figure:: ../_assets/configuration/installautomatic.PNG
   :alt: Databricks
   :align: center
   :width: 40%
   
   
Configure the Uploaded Library in Fire Insights
------------------------------------

Configure the path of the uploaded fire core jar library in Databricks in Fire Insights.

This has to be done under Administration/Configuration.


.. figure:: ../_assets/configuration/databricks-configurations.PNG
   :alt: Databricks
   :align: center
   :width: 40%
   
Configure app.postMessageURL
----------------------------

Configure ``app.postMessageURL`` to be the public IP of the machine. It has to be accessible from the Databricks Cluster.

.. figure:: ../_assets/configuration/Fireui_postbackurl.PNG
   :alt: Databricks
   :align: center
   :width: 40%


Install Databricks JDBC Driver
-----------------------------------

Fire needs the Databricks JDBC Driver to be installed. Install it in the ``fire-user-lib`` folder of the Fire installation.

You can download the Databricks JDBC Driver from the Databricks site : 

* https://docs.databricks.com/bi/jdbc-odbc-bi.html
* https://databricks.com/spark/odbc-driver-download

The driver is available as a zip file. eg: ``SimbaSparkJDBC-2.6.3.1003.zip``

* Unzip the downloaded file. It will create a directory like ``SimbaSparkJDBC-2.6.3.1003``
* Copy the jdbc jar file named ``SparkJDBC4.jar`` into ``fire-x.y.z/fire-user-lib`` and ``fire-x.y.z/fire-server-lib``


Create your REST API token in Databricks
--------------

Create your token in Databricks. It would be used in making REST API calls to Databricks from Fire Insights.

Login to your Databricks Account
++++++++++++++++++++++++++++++++

Click on ``Account`` icon in right corner top
++++++++++++++++++++++++++++++++

.. figure:: ../_assets/configuration/usersetting.PNG
   :alt: Databricks
   :align: center
   :width: 40%
   
Click on ``User Settings``
++++++++++++++++++++++++++++++++

.. figure:: ../_assets/configuration/userset.PNG
   :alt: Databricks
   :align: center
   :width: 40%

Click on ``Generate New Token``
++++++++++++++++++++++++++++++++

.. figure:: ../_assets/configuration/generatetoken.PNG
   :alt: Databricks
   :align: center
   :width: 40%

Add ``comment`` & ``Lifetime(days)`` for token expiry & Click on ``Generate``
++++++++++++++++++++++++++++++++

.. figure:: ../_assets/configuration/token_update.PNG
   :alt: Databricks
   :align: center
   :width: 40%

Copy the token generated and Click on ``DONE``
++++++++++++++++++++++++++++++++

.. figure:: ../_assets/configuration/token_generated.PNG
   :alt: Databricks
   :align: center
   :width: 40%



Create Databricks Connection
----------

Create a connection in Fire Insights under your Application for connecting to Databricks.

* Specify your Databricks Token.
* Specify the Databricks JDBC URL of your cluster in Databricks.

.. figure:: ../_assets/configuration/databricks_connection.PNG
   :alt: Databricks
   :align: center
   :width: 40%


Now we are ready to start using the Databricks Connection in workflows etc.
