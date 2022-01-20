Reading from Snowflake
======================

Fire Insights has a processor for reading data from Snowflake.

Workflow
--------

The below workflow does the following:

* Reads Snowflake Table
* Prints a few records of the dataframe

.. figure:: ../../_assets/snowflake/1.PNG
   :alt: snowflake
   :width: 70%

Reading from Snowflake Table
-------------------

It reads Table using Read From Snowflake processor.

* CONNECTION  : Connection created for Snowflake
* SF DATABASE : Snowflake Database name
* SF SCHEMA : Snowflake Schema Name
* SF WAREHOUSE : Snowflake Warehouse Name
* SF TABLE : Snowflake Table Name

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/snowflake/2.PNG
   :alt: snowflake
   :width: 90%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/snowflake/3.PNG
   :alt: snowflake
   :width: 90%

Prints the Results
------------------

It prints the first few records of the dataframe
   



