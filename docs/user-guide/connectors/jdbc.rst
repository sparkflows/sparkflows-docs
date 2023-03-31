Read from RDBMS
=======================

Fire has JDBC Processors for reading from JDBC sources or writing to JDBC sinks.

In order to connect to a JDBC source like MySQL/Oracle/DB2 etc. the JDBC driver needs to be installed in Fire Insights.

Use the steps given at the following link for installing the corresponding JDBC driver for your RDBMS:

- http://docs.sparkflows.io/en/latest/operating/installing-jdbc-drivers.html


Workflow for reading from MySQL
--------------------------------

Below is a workflow which reads data from MySQL and reads the result from ``Print N Rows`` processor. It reads in the data from the ``Loandata`` table in MySQL.

.. figure:: ../../_assets/user-guide/ReadJDBC_WF.png
   :alt: JDBC Workflowt
   :width: 45%
   
   
JDBC Processor Configuration
----------------------------

Below are the configuration details of the JDBC Processor. It uses the provided user credentials for reading from the MySQL database. On clicking on `Refresh Schema`, Fire gets the schema of the table from MySQL and populates the entries.

.. figure:: ../../_assets/user-guide/JDBCNodeConfiguration1.png
   :alt: JDBC Processor Dialog
   :width: 80%
   
Results of reading from MySQL Table
------------------------------------

The following screenshot displays schema of the table from the MySQL table by Fire.

.. figure:: ../../_assets/user-guide/JDBCShemaRefresh1.png
   :alt: JDBC Get Schema
   :width: 80%

Specifying a Sub-Query
----------------------

In the configuration of the JDBC node for ``DB TABLE``, anything that is valid in a FROM clause of a SQL query can be used. For example, instead of a full table we could also use a subquery.

 
More details are available on the Spark Guide : https://spark.apache.org/docs/1.6.0/sql-programming-guide.html#jdbc-to-other-databases


Executing the processor displays the records read from MySQL Table.

.. figure:: ../../_assets/user-guide/ResultJDBC1.png
   :alt: JDBC Result Output
   :width: 80%
   

JDBC Drivers
-------------

Below are the JDBC URLs for some databases:

* MySQL : com.mysql.jdbc.Driver
* PostgreSQL : org.postgresql.Driver
* Oracle : oracle.jdbc.driver.OracleDriver

Examples of JDBC URL
----------------

Below are some examples of JDBC URLs for reading from relational sources:

* MySQL : jdbc:mysql://localhost:3306/mydb
* PostgreSQL : jdbc:postgresql://localhost:5432/mydb

