Time Functions
=============

There are many instances when you want to do time-series analysis. Fire Insights provides Date-Time features with TimeFunctions operator.

Creating additional features from the Timestamp Column helps you to know more about the data and run modeling algorithms on them. Fire Insights has NodeTimeFunctions for creating these time series features.

  
Workflow for applying TimeFunctions
-----------------------------------

In the sample workflow below, additional Date Time features are being created from the date column.

.. figure:: ../../_assets/tutorials/data-cleaning/convert-to-timestamps/timefun-wf.png
   :alt: Convert To Timestamps
   :width: 80%
   
In the above workflow: 

- The **CSV** processor reads in the CSV data from HDFS.
- The **StringToDate** processor converts the column Date, which is in string format to **Timestamp**. 
- The **TimeFunctions** processor takes in the **Timestamp Column** and then applies various TimeFunctions to it to generate additional output columns.

Reading from Dataset
---------------------

It reads sample Dataset file.

Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/convert-to-timestamps/read-config.png
   :alt: Convert To Timestamps
   :width: 80%
   
Processor Output
^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/convert-to-timestamps/read-output.png
   :alt: Convert To Timestamps
   :width: 80%
   
Prints the sample Dataset Result
---------------------------------

It prints the result of the sample dataset available.

   
Convert To Timestamps
---------------------

It converts to Timestamps using **StringToDate** Node.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/convert-to-timestamps/timefun-config.png
   :alt: Convert To Timestamps
   :width: 80% 

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/convert-to-timestamps/timefun-output.png
   :alt: Convert To Timestamps
   :width: 90%
   
Prints the Result
------------------

It prints the result after converting to Timestamps.







