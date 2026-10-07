Connecting to Data
==================

Sparkflows provides a number of Processors for reading and writing data from various sources.


Connector Processors in Sparkflows
----------------------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Title
     - Description
   * - Read JDBC
     - It reads the data from a JDBC source.
   * - Save JDBC
     - It saves the data to a JDBC source.
   * - Read Cassandra
     - It reads the data from Apache Cassandra.
   * - Save Cassandra
     - It saves the rows of the incoming DataFrame into Apache Cassandra.
   * - Read Databricks Table
     - It reads a table from Databricks.
   * - Save Databricks Table
     - It saves the data to a Databricks table.
   * - Read Elastic Search
     - It reads the data from ElasticSearch.
   * - Save ElasticSearch
     - It stores the rows of the incoming DataFrame into Elastic Search.
   * - Read HIVE Table
     - It reads the data from Apache HIVE table and creates a DataFrame from it.
   * - Save As Hive Table
     - It saves the processed data as a Hive table in a database.
   * - Insert Into Hive Table
     - It inserts data into a Hive table.
   * - Run HiveQL
     - It executes a SQL statement against a Hive table.
   * - Hive Incremental
     - It reads incremental data from a Hive table.
   * - Read MongoDB
     - It reads the data from MongoDB.
   * - Save MongoDB
     - It saves the incoming DataFrame into MongoDB.
   * - Read Redshift-AWS
     - It reads the data from Redshift using JDBC.
   * - Save Redshift-AWS
     - It saves the data to Redshift using JDBC.
   * - Read Salesforce
     - It reads the data from Salesforce.
   * - Save Salesforce
     - It saves the data to Salesforce.
   * - Read Shopify
     - It reads the data from a Shopify resource.
   * - Read From SnowFlake
     - It reads a table from Snowflake.
   * - Write To SnowFlake
     - It saves the rows of the incoming DataFrame into Snowflake.
   * - Execute Query In SnowFlake
     - It executes the query in the Snowflake.
   * - Read SFTP
     - It reads from SFTP.
   * - Sharepoint Data Extraction
     - It extracts data from Sharepoint.

.. toctree::
   :hidden:

   cassandra.rst
   databricks.rst
   elasticsearch.rst
   hive.rst
   jdbc.rst
   mongodb.rst
   mysql.rst
   redshift.rst
   salesforce.rst
   sap/index.rst
   sharepoint.rst
   shopify.rst
   snowflake.rst
   sftp.rst
