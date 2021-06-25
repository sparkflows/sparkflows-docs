Writing to Snowflake
=====================

Fire Insights has a processor for writing to Snowflake.

It would write the incoming Dataframe to Snowflake.

Workflow
--------

The below workflow does the following:

* Reads Housing dataset.
* Write it to Snowflake Table.

.. figure:: ..//_assets/snowflake/4_a.PNG
   :alt: snowflake
   :width: 90%
   
Reading from CSV File
---------------------

It reads Housing data from a CSV File using Read CSV Processor.

Processor Configuration
^^^^^^^^^^^^^^^^^^   

.. figure:: ..//_assets/snowflake/5.PNG
   :alt: snowflake
   :width: 90%
   
Processor Output
^^^^^^

.. figure:: ..//_assets/snowflake/6.PNG
   :alt: snowflake
   :width: 90%
