Read from Snowflake
======================

Fire Insights has provided two processors for reading data from Snowflake.

1. Read From SnowFlake
2. Execute Query In SnowFlake

1. Read From SnowFlake Workflow
--------

Using this processor, a user can select a single table/view from the Snowflake schema.

Processor Configuration
----------

.. figure:: ..//_assets/snowflake/ReadProcessorGen.PNG
   :alt: snowflake
   :width: 90%

* CONNECTION  : Connection created for Snowflake.
* SF WAREHOUSE : Snowflake Warehouse Name.
* SF DATABASE : Snowflake Database Name.
* SF SCHEMA : Snowflake Schema Name.
* SF TABLE/VIEW : Snowflake Table/View Name 


Example Workflow
--------

The below workflow does the following:

* Reads Snowflake Table/View.
* Prints a few records of the DataFrame.

.. figure:: ..//_assets/snowflake/wf_read.PNG
   :alt: snowflake
   :width: 40%

Reading from Snowflake Table/View
^^^^^^^^^^^^^^^^^^

It reads the table/view using ``Read From Snowflake`` processor.

Processor Configuration
++++++

Below are the configurations for the Read from Snowflake processor.

.. figure:: ..//_assets/snowflake/ReadProcessorGen.PNG
   :alt: snowflake
   :width: 90%

Processor Output
++++

.. figure:: ..//_assets/snowflake/processor_read.PNG
   :alt: snowflake
   :width: 90%

2. Execute Query In SnowFlake
--------

Using this processor, a user can select multiple tables/views across the Snowflake schema amd write subqueries and perform aggregations and use Snowflake specific SQL functions .

Processor Configuration
----------

.. figure:: ..//_assets/snowflake/EXProcessorGen.PNG
   :alt: snowflake
   :width: 90%

* CONNECTION  : Connection created for Snowflake.
* SF WAREHOUSE : Snowflake Warehouse Name.
* SF DATABASE : Snowflake Database Name.
* SF SCHEMA : Snowflake Schema Name.
* SF QUERY : Write SQL query. 


Example Workflow
--------

The below workflow does the following:

* Reads data from Customers & Orders tables to find all pending orders .
* Prints a few records of the DataFrame.

.. figure:: ..//_assets/snowflake/wf_execute.PNG
   :alt: snowflake
   :width: 40%

Execute Query in SnowFlake 
^^^^^^^^^^^^^^^^^^

It executes a query on the Snowflake tables using ``Execute Query In SnowFlake`` processor.

Processor Configuration
++++++

Below are the configurations for the Read from Snowflake processor.

.. figure:: ..//_assets/snowflake/EXProcessorGen.PNG
   :alt: snowflake
   :width: 90%

Processor Output
++++

.. figure:: ..//_assets/snowflake/processor_execute.PNG
   :alt: snowflake
   :width: 90%
