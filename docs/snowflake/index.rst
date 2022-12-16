
Snowflake Guide
=========

Fire Insights jobs can read from and write to Snowflake.

Data from Snowflake is read into a Dataframe. This dataframe can be transformed and also joined with data read from other sources. Final result Dataframe can be written back to Snowflake.

Fire Insights also incorporates pushdown into Snowflake. The various nodes of the workflow push down processing into Snowflake. Hence it is entirely prossible that the whole processing happens in Snowflake.


Snowflake Spark Connector
---------------

Fire Insights uses the Snowflake Spark connector for reading from and writing to Snowflake.

https://docs.snowflake.com/en/user-guide/spark-connector.html

.. panels::
    :container: container-lg pb-3
    :column: text-center col-lg-6 col-md-6 col-sm-6 col-xs-12 p-2
    
    :doc:`/snowflake/creating-snowflake-connection`
    
    Creating a snowflake connection in fire insights
    
    ---
    
    :doc:`/snowflake/reading-snowflake`
    
    Reading data from snowflake in fire insights
    
    ---
    
    :doc:`/snowflake/writing-snowflake`
    
    Writing data to snowflake in fire insights
    
    ---
    
    :doc:`/snowflake/browse-snowflake-tables`
    
    Browsing snowflake tables in fire insights

.. toctree::
   :hidden:

   creating-snowflake-connection.rst
   reading-snowflake.rst
   writing-snowflake.rst
   browse-snowflake-tables.rst
   
   
   
   
   

   
   
   
   

   
   
