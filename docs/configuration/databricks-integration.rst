Databricks Integration
======================

Fire integrates with Databricks. Fire can submit jobs to the Databricks clusters.

Deployment
-----------

Install Fire on any machine. Then connect it to your Databricks Cluster

Configuration
-------------

Create a connection in your Application for connecting to Databricks.

In the workflow use the processor 'Read from Databricks'. It will allow you to read tables from Databricks.

Then use the other processors in Fire for processing things.

Databricks JDBC Driver Installation
-----------------------------------

Fire need the Databricks JDBC Driver to be installed. Install it in the fire-core-lib folder of the Fire installation.
