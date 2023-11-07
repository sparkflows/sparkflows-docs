Troubleshooting Databricks Integration
===========================================


Nothing is Displayed in Fire Insights after Workflow Execution
-----------------------------------------

* This problem may arise due to incorrect configuration of the postback URL in Fire Insights under Administration/Configuration.

* Another possible issue is the inaccessibility of the machine running Fire Insights from the Databricks Cluster. 

  It is recommended to verify connectivity between Databricks and the Fire Insights machine. Connectivity from Databricks to Fire postback URL can be done in Databricks via Notebooks using the telnet command.

  .. figure:: ../../_assets/configuration/databricks_ping.PNG
     :alt: Databricks
     :width: 60%
   
* Another reason might be that you are using the Databricks **High Concurrency** cluster. Ensure that you connect Fire to Databricks **Standard** cluster or have enabled scala in the high concurrency cluster. 

When accessing most of the Databricks pages in Fire, it gives Simba JDBC error
-----------------------------------------

* The reason for it is that the Databricks Simba JDBC JAR file is not deployed in Fire. Follow the installation guidelines at `Databricks JDBC Driver Installation Guide <https://docs.sparkflows.io/en/latest/databricks/databricks-installation.html#install-databricks-jdbc-driver>`_


Workflow Editor Gives 'Cannot connect to Fire' Error
-------------------

* To resolve this issue, ensure that **app.runOnCluster** under **Administration/Configuration** is set to **false**.


Checking Cluster Logs in Databricks
-------------------

* When running Fire with Databricks, it can be beneficial to review cluster logs in Databricks.

  The following logs under **Driver Logs** are useful:

  - log4j-active.log

  Search for **WorkflowExecuteDatabricks** in the logs to view if the Fire Insights Job is running in Databricks.


Getting (java.lang.Exception) Error
--------------------------------

* If you receive the error **java.lang.Exception: An error occurred while initializing the REPL**, it may be due to conflicting Scala libraries or JARs attached to the cluster such as Scala 2.11 libraries attached to Scala 2.10 cluster (or vice-versa).

  Ensure that the Scala libraries match the cluster's version to resolve the conflict.


Getting (DatabricksILoop.scala:98) Error
-------------------------------
* If you encounter the error **at com.databricks.backend.daemon.driver.DatabricksILoop$class.initSpark(DatabricksILoop.scala:98)**, it's likely because you are running the Spark 2.3 version of Fire with a Spark 2.4 cluster on Databricks. 

  To resolve this issue, consider upgrading Fire to the Spark 2.4 version or create a Databricks cluster compatible with Spark 2.3.   



Databricks Cluster Versions Support
------------------------------------
.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Databricks Runtime Version 
     - Spark Version    
     - Scala Version
   * - 7.3 
     - 3.0.1 
     - 2.12
   * - 6.2 
     - 2.4.4   
     - 2.11
   * - 6.3  
     - 2.4.4 
     - 2.11
   * - 6.4  
     - 2.4.5 
     - 2.11
   * - 6.5      
     - 2.4.5    
     - 2.11
   




