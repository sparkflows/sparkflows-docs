Date-Time Field Extract
=============


Workflow
-------

The below workflow:

* Reads data from a dataset.
* It creates a new DataFrame by extracting "Year"," Month"," Day of month", "Hour", "Minute"," Second"  fields from "TimeStamp"
* Prints the result.

.. figure:: ../../_assets/tutorials/data-engineering/date-time-field-extract/Capture1.PNG
   :alt: DateTimeFieldExtract
   :width: 65%
   
Reading from Dataset
---------------------

It reads in the input Dataset File.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/date-time-field-extract/Capture2.PNG
   :alt: DateTimeFieldExtract
   :width: 90%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/date-time-field-extract/Capture3.PNG
   :alt: DateTimeFieldExtract
   :width: 90%
   
   
Date-Time Field Extract
------------

It creates a new DataFrame by extracting the "year", "month", "day of month", "hour"," minute", "second",: week of the year" from the Timestamp Column.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/date-time-field-extract/Capture4.PNG
   :alt: DateTimeFieldExtract
   :width: 90%
   
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/date-time-field-extract/Capture5.PNG
   :alt: DateTimeFieldExtract
   :width: 90%
  
  
Prints the Result
------------------

It prints the first few records onto the screen.
