Read from Snowflake
======================

Fire Insights has provided two processors for reading data from Snowflake.

1. Read From Snowflake
2. Execute Query In Snowflake

Read From Snowflake Workflow
--------

A user can use this processor to select a single table/view from the Snowflake schema.

**Processor Configuration**
++++++++++++++++++++++++++++++

Below are the processor configuration details:

* ``CONNECTION``  : Connection created for Snowflake.
* ``SF WAREHOUSE`` : Snowflake Warehouse Name.
* ``SF DATABASE`` : Snowflake Database Name.
* ``SF SCHEMA`` : Snowflake Schema Name.
* ``SF TABLE/VIEW`` : Snowflake Table/View Name. 

  .. figure:: ..//_assets/snowflake/ReadProcessorGen.png
     :alt: snowflake
     :width: 60%


**Example Workflow**
+++++++++++++++++++++

The below workflow does the following:

* Reads Snowflake Table/View.
* Prints a few records of the DataFrame.

  .. figure:: ..//_assets/snowflake/wf_read.png
     :alt: snowflake
     :width: 60%

**Reading from Snowflake Table/View**
++++++++++++++++++++++++++++++++++++++++

It reads the table/view using **Read From Snowflake** processor.

Processor Configuration
++++++

Below are the configurations for the Read from Snowflake processor:

  .. figure:: ..//_assets/snowflake/ReadProcessorGen.png
     :alt: snowflake
     :width: 60%

Processor Output
++++

  .. figure:: ..//_assets/snowflake/processor_read.png
     :alt: snowflake
     :width: 60%

Execute Query In Snowflake
--------

A user can use this processor to select multiple tables/views across the Snowflake schema and write subqueries and perform aggregations and use Snowflake specific SQL functions.

**Processor Configuration**
+++++++++++++++++++++++++++++++

Below are the processor configuration details:

* ``CONNECTION`` : Connection created for Snowflake.
* ``SF WAREHOUSE`` : Snowflake Warehouse Name.
* ``SF DATABASE`` : Snowflake Database Name.
* ``SF SCHEMA`` : Snowflake Schema Name.
* ``SF QUERY`` : Write SQL query. 

  .. figure:: ..//_assets/snowflake/EXProcessorGen.png
     :alt: snowflake
     :width: 60%


**Example Workflow**
+++++++++++++++++++++

The below workflow does the following:

* Reads data from Customers & Orders tables to find all pending orders.
* Prints a few records of the DataFrame.

  .. figure:: ..//_assets/snowflake/wf_execute.png
     :alt: snowflake
     :width: 60%

**Execute Query in SnowFlake** 
+++++++++++++++++++++++++++++++++++

It executes a query on the Snowflake tables using **Execute Query In SnowFlake** processor.

Processor Configuration
++++++

Below are the configurations for the Read from Snowflake processor.

  .. figure:: ..//_assets/snowflake/EXProcessorGen.png
     :alt: snowflake
     :width: 60%

Processor Output
++++

  .. figure:: ..//_assets/snowflake/processor_execute.png
     :alt: snowflake
     :width: 60%
