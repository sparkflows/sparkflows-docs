Date-Time Field Extract
=============


Workflow
-------

The below workflow:

* Reads data from a dataset.
* It creates a new DataFrame by extracting ``Year``, ``Month``, ``Day of month``, ``Hour``, ``Minute``, ``Second`` fields from **TimeStamp**.
* Prints the result.

.. figure:: ../../_assets/tutorials/data-engineering/date-time-field-extract/1.PNG
   :alt: DateTimeFieldExtract
   :width: 65%
   
Reading from Dataset
---------------------

It reads in the input Dataset file.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/date-time-field-extract/2.PNG
   :alt: DateTimeFieldExtract
   :width: 90%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/date-time-field-extract/3.PNG
   :alt: DateTimeFieldExtract
   :width: 90%
   
   
Date-Time Field Extract
------------

It creates a new DataFrame by extracting the ``year``, ``month``, ``day of month``, ``hour``, ``minute``, ``second``, ``week of the year`` from the **Timestamp Column**.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/date-time-field-extract/4.PNG
   :alt: DateTimeFieldExtract
   :width: 90%
   
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/date-time-field-extract/5.PNG
   :alt: DateTimeFieldExtract
   :width: 90%
  
  
Prints the Result
------------------

It prints the first few records onto the screen.
