Troubleshooting Fire/Databricks Integration
===========================================


When the workflow is executed, nothing shows up in Fire
-----------------------------------------

One problem might be that the ``postbackURL`` is not configured right in Fire Insights under Administration/Configuration.

The other problem can be that the machine running Fire Insights is no accessible from the Databricks Cluster. Test connectivity to the Fire Insights machine from Databricks.

Test connectiving from Databricks to Fire postbackURL.

.. figure:: ../_assets/configuration/databricks_ping.PNG
   :alt: Databricks
   :align: center
   :width: 60%
   
