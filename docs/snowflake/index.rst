
Snowflake Guide
=========

Fire Insights jobs can read from and write to Snowflake.

Data from Snowflake is read into a DataFrame. This DataFrame can be transformed and also joined with data read from other sources. Final result of DataFrame can be written back to Snowflake.

Fire Insights also incorporates pushdown into Snowflake. The various nodes of the workflow push down processing into Snowflake. Hence, it is entirely possible that the whole processing happens in Snowflake.


Snowflake Spark Connector
---------------

Fire Insights uses the Snowflake Spark connector for reading from and writing to Snowflake.

For more details, read `Snowflake Documentation. <https://docs.snowflake.com/en/user-guide/spark-connector.html>`_

.. panels::
    :container: container-lg pb-3
    :column: text-center col-lg-6 col-md-6 col-sm-6 col-xs-12 p-2
    
    :doc:`/snowflake/creating-snowflake-connection`
    
    Create a Snowflake connection
    
    ---
    
    :doc:`/snowflake/reading-snowflake`
    
    Read data from Snowflake
    
    ---
    
    :doc:`/snowflake/writing-snowflake`
    
    Write data to Snowflake
    
    ---
    
    :doc:`/snowflake/browse-snowflake-tables`
    
    Browse Snowflake tables

.. toctree::
   :hidden:

   creating-snowflake-connection.rst
   reading-snowflake.rst
   writing-snowflake.rst
   browse-snowflake-tables.rst
   
  
