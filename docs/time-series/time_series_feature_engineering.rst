Time Series Feature Engineering
------------------------------

Fire Insights provides a number of Processors for Feature Engineering of Time Series Data. These include:

 
.. list-table:: Update New features where needed
   :widths: 10 40
   :header-rows: 1

   * - Features
     - Description
   * - DateTimeFieldExtract
     - Extracts year, month, day of month, hour, minute, second and week of year from timestamp/date columns.
   * - Days to holiday
     - day remaining for next holiday
   * - Days from holiday
     - Days passed after holiday
   * - Time-segmentation
     - Divide data in morning, afternoon, evening, night to get more idea about time based pattern
   * - MovingWindowingFunctions
     - Calculates the moving values using the given function.
   * - WindowingAnalytics
     - Window Analytics Functions



DateTimeFieldExtract
====================

Below is the sample workflows which contains ``DateTimeFieldExtract`` processor in Fire Insights.

It reads the JetRail Train dataset & use DateTimeFieldExtract processor which create New DataFrame by extracting Date & Time field and print the result.

.. figure:: ../_assets/ml_userguide/datetime_field.PNG
   :alt: ml_userguide
   :align: center
   :width: 60%
   
DateTimeFieldExtract processor Configuration:

.. figure:: ../_assets/ml_userguide/datetime_configuration.PNG
   :alt: ml_userguide
   :align: center
   :width: 60%

Output result of ``DateTimeFieldExtract`` processor:

.. figure:: ../_assets/ml_userguide/datetime_output_result.PNG
   :alt: ml_userguide
   :align: center
   :width: 60%

MovingWindowingFunctions
========================

Below is the sample workflows which contains ``MovingWindowingFunctions`` processor in Fire Insights.

It reads the ticker dataset, concatenate the input column, casting specified column to new data type, use MovingWindowingFunctions processor which calculates the moving value of selected function of input column and print the result. 

.. figure:: ../_assets/ml_userguide/windowsfn.PNG
   :alt: ml_userguide
   :align: center
   :width: 60%

MovingWindowingFunctions processor Configuration:

.. figure:: ../_assets/ml_userguide/windows_configuartion.PNG
   :alt: ml_userguide
   :align: center
   :width: 60%

Output result of ``MovingWindowingFunctions`` processor:

.. figure:: ../_assets/ml_userguide/output-result.PNG
   :alt: ml_userguide
   :align: center
   :width: 60%

