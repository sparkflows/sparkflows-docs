Troubleshooting Databricks Integration
===========================================

1. No Data Displayed in Fire Insights after Workflow Execution
-------------------------------------------------

Problem
+++++++

Nothing is Displayed in Fire Insights after Workflow Execution.

Solution
+++++++++

* This problem may arise due to incorrect configuration of the postback URL in Fire Insights with the Databricks connection you will be using.

* Another possible issue is the inaccessibility of the machine running Fire Insights from the Databricks Cluster. 

  It is recommended to verify connectivity between Databricks and the Fire Insights machine. Connectivity from Databricks to Fire postback URL can be done in Databricks via Notebooks using the telnet command.

  .. figure:: ../../_assets/configuration/databricks_ping.PNG
     :alt: Databricks
     :width: 60%
   
* Another reason might be that you are using the Databricks **High Concurrency** cluster. Ensure that you connect Fire to Databricks **Standard** cluster or have enabled scala in the high concurrency cluster. 


2. Simba JDBC Error When Accessing Databricks Pages in Fire
-----------------------------------------------------------

Problem
+++++++++++

When accessing most of the Databricks pages in Fire, it gives Simba JDBC error.

Solution
++++++++

The reason for it is that the Databricks Simba JDBC JAR file is not deployed in Fire. 


3. Checking Cluster Logs in Databricks
--------------------------------------

Problem
++++++++

Troubleshooting Fire with Databricks may necessitate the review of cluster logs in Databricks. Users may find it challenging to locate relevant logs for Fire Insights jobs within Databricks.

Solution
++++++++++++

When running Fire with Databricks, it can be beneficial to review cluster logs in Databricks.

  The following logs under **Driver Logs** are useful:

  - Log4j output.log

  Search for **workflowexecutecloud** in the logs to view if the Fire Insights Job is running in Databricks.

4. Java.lang.Exception Error Occurrence
-----------------------------------------

Problem
+++++++++

Getting (java.lang.Exception) Error.

Solution
+++++++++++++

If you receive the error **java.lang.Exception: An error occurred while initializing the REPL**, it may be due to conflicting Scala libraries or JARs attached to the cluster such as Scala 2.11 libraries attached to Scala 2.10 cluster (or vice-versa).

Ensure that the Scala libraries match the cluster's version to resolve the conflict.

5. DatabricksILoop.scala Error
----------------------------------

Problem
++++++++++++

Getting (DatabricksILoop.scala:98) Error.

Solution
++++++++

If you encounter the error **at com.databricks.backend.daemon.driver.DatabricksILoop$class.initSpark(DatabricksILoop.scala:98)**, it's likely because you are running the Spark 3.0.1 version of Fire with a Spark 3.2.1 cluster on Databricks. 

To resolve this issue, consider upgrading Fire to the Spark 2.4 version or create a Databricks cluster compatible with Spark 2.3.   

Databricks Cluster Versions Support
------------------------------------
.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Databricks Runtime Version 
     - Spark Version    
     - Scala Version
   * - 10.4 
     - 3.2.1 
     - 2.12
   * - 7.3 
     - 3.0.1 
     - 2.12
      




