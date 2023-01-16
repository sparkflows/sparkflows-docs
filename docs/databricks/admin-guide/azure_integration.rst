Azure Integration
=================

ADLS Passthrough
---------------

https://docs.microsoft.com/en-us/azure/databricks/security/credential-passthrough/adls-passthrough

Creating Tables
---------------

https://docs.microsoft.com/en-us/azure/databricks/data/tables

Managed or Unmanaged tables can be created.

CREATE TABLE <example-table>(id STRING, value STRING) USING org.apache.spark.sql.parquet OPTIONS (PATH "<your-storage-path>")

dataframe.write.option('path', "<your-storage-path>").saveAsTable("<example-table>")

// Create managed table as select
dataframe.write.mode(SaveMode.Overwrite).partitionBy("id").saveAsTable("<example-table>")

// Create unmanaged/external table as select
dataframe.write.mode(SaveMode.Overwrite).option("path", "<file-path>").saveAsTable("<example-table>")

