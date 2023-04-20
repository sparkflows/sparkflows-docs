Date-Time Field Extract
=============


Workflow
-------

The below workflow:

* Reads data from a dataset.
* It creates a new DataFrame by extracting ``Year``, ``Month``, ``Day of month``, ``Hour``, ``Minute``, ``Second`` fields from **TimeStamp**.
* Prints the result.

.. figure:: ../../_assets/tutorials/data-engineering/date-time-field-extract/date-time-wf.png
   :alt: DateTimeFieldExtract
   :width: 80%
   
Reading from Dataset
---------------------

It reads in the input Dataset file.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/date-time-field-extract/read-config.png
   :alt: DateTimeFieldExtract
   :width: 80%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/date-time-field-extract/read-output.png
   :alt: DateTimeFieldExtract
   :width: 80%
   
   
Date-Time Field Extract
------------

It creates a new DataFrame by extracting the ``year``, ``month``, ``day of month``, ``hour``, ``minute``, ``second``, ``week of the year`` from the **Timestamp Column**.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/date-time-field-extract/date-time-config.png
   :alt: DateTimeFieldExtract
   :width: 80%
   
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/date-time-field-extract/date-time-output.png
   :alt: DateTimeFieldExtract
   :width: 80%
  
  
Prints the Result
------------------

It prints the first few records onto the screen.
