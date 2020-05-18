Troubleshooting Fire/Databricks Integration
===========================================


When the workflow is executed, nothing shows up in Fire
-----------------------------------------

One problem might be that the ``postbackURL`` is not configured right in Fire Insights under Administration/Configuration.

The other problem can be that the machine running Fire Insights is not accessible from the Databricks Cluster. Test connectivity to the Fire Insights machine from Databricks.

Connectiving from Databricks to Fire postbackURL can be done in Databricks via Notebooks.

.. figure:: ../_assets/configuration/databricks_ping.PNG
   :alt: Databricks
   :align: center
   :width: 60%
   

When accessing most Databricks page in Fire, it gives Simba JDBC error
-----------------------------------------

The probably reason for it is that the Databricks Simba JDBC jar file is not deployed in Fire.

https://docs.sparkflows.io/en/latest/databricks/databricks-installation.html#install-databricks-jdbc-driver


