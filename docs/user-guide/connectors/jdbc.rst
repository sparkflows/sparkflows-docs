JDBC
=======================

Fire has JDBC Processors for reading from or writing to JDBC sources.

In order to connect to a JDBC source like PostgreSQL/MySQL/Oracle/DB2 etc. the JDBC driver needs to be installed in Fire Insights.

Use the steps given at the following link for installing the corresponding JDBC driver for your RDBMS and creating the Connection.

- https://docs.sparkflows.io/en/latest/user-guide/connectors/jdbc.html


Workflow for reading from an RDBMS
--------------------------------

Below is a workflow which reads data from PostgreSQL using a JDBC Connection and prints the result using the ``Print N Rows`` processor. It reads in the data from the ``housing`` table in PostgreSQL.

.. figure:: ../../_assets/user-guide/jdbc_wf.PNG
   :alt: JDBC Workflow
   :width: 60%
   
   
JDBC Processor Configuration
----------------------------

Below are the configuration details of the ReadJDBC Processor. It uses the provided JDBC Connection for reading from the PostgreSQL database. On clicking on `Refresh Schema`, Fire Insights gets the schema of the table from PostgreSQL and populates the entries.

.. figure:: ../../_assets/user-guide/jdbc_config.PNG
   :alt: JDBC Processor Dialog
   :width: 60%
   
Results of reading from PostgreSQL Table
------------------------------------

The following screenshot displays schema of the table from the PostgreSQL table by Fire.

.. figure:: ../../_assets/user-guide/jdbc_output.PNG
   :alt: JDBC Get Schema
   :width: 60%

Specifying a Sub-Query
----------------------

In the configuration of the ReadJDBC node for ``DB TABLE``, anything that is valid in a FROM clause of a SQL query can be used. For example, instead of a full table we could also use a subquery.

 
More details are available on the Spark Guide : https://spark.apache.org/docs/1.6.0/sql-programming-guide.html#jdbc-to-other-databases


Executing the processor displays the records read from PostgreSQL Table.

.. figure:: ../../_assets/user-guide/jdbc_output.PNG
   :alt: JDBC Result Output
   :width: 60%
   

