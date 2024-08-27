Connecting to Data
==========

Fire Insights provides a number of Processors for reading and writing data from various sources.


Connector Processors in Fire Insights
----------------------------------------


.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Title
     - Description
   * - Read JDBC
     - It reads the data from a JDBC source.
   * - Read Cassandra
     - It reads the data from Apache Cassandra.
   * - Read Databricks Table
     - It reads a table from Databricks.
   * - Save Databricks table
     - It saves the data to a Databricks table.
   * - Read From SnowFlake
     - It reads a table from Snowflake. 
   * - Read Elastic Search
     - It reads the data from ElasticSearch.
   * - Read HIVE Table
     - It reads the data from Apache HIVE table and creates a DataFrame from it.
   * - Read MongoDB
     - It reads the data from MongoDB.
   * - Read Redshift-AWS
     - It reads the data from Redshift using JDBC.
   * - Read Salesforce.
     - It reads the data from Salesforce.
   * - Reads JDBC
     - It reads the data from Salesforce using cdata JDBC Driver. 
   * - Save Cassandra
     - It saves the rows of the incoming DataFrame into Apache Cassandra.
   * - Save ElasticSearch
     - It stores the rows of the incoming DataFrame into Elastic Search.
   * - Save MongoDB
     - It saves the incoming Dataframe into MongoDB.
   * - Save Redshift-AWS
     - It saves the data to Redshift using JDBC.
   * - Saves Salesforce
     - It saves the data to Salesforce.
   * - Write To SnowFlake
     - It saves the rows of the incoming DataFrame into Snowflake.
   * - Execute Query In SnowFlake
     - It executes the query in the Snowflake.

.. toctree::
   :hidden:

   jdbc.rst
   mysql.rst
   snowflake.rst
   hive.rst
   redshift.rst
   databricks.rst
   salesforce.rst
   elasticsearch.rst
   mongodb.rst
   save-cassandra.rst
   sap/index.rst

   
   
   
   
   
   
   

