Databricks Integration
======================

Fire integrates with Databricks. Fire can submit jobs to the Databricks clusters.

Deployment
-----------

Install Fire on any machine. Then connect it to your Databricks Cluster

Upload Fire Core Jar to Databricks
----------------------------------

Upload fire-x.y.z/fire-core-lib/fire-spark_2_1-core-3.1.0-jar-with-dependencies.jar to Databricks. Upload it under Workflows as a Library.

Specify the Uploaded Library in Fire
------------------------------------

Specify the uploaded fire core jar library in Databricks in Fire Insights.

This has to be done under Administration/Configuration.

Connection
----------

Create a connection in your Application for connecting to Databricks.

Read Databricks tables in Fire Insights
------------------------------------------

In the workflow use the processor 'Read from Databricks'. It will allow you to read tables from Databricks.

Then use the other processors in Fire for processing things.

Databricks JDBC Driver Installation
-----------------------------------

Fire needs the Databricks JDBC Driver to be installed. Install it in the fire-core-lib folder of the Fire installation.

You can download the Databricks JDBC Driver from the Databricks site : 

* https://docs.databricks.com/bi/jdbc-odbc-bi.html
* https://databricks.com/spark/odbc-driver-download


