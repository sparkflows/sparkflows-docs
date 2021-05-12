Reading CSV File
=================

Fire Insights enables you to Read CSV files.

Workflow
--------

Below is the workflow. It does the following:

* Reads data from a CSV file
* Prints a few records of the dataframe

.. figure:: ../../_assets/user-guide/read-write/1_1.png
   :alt: readwrite
   :width: 60%

Reading from CSV File
---------------------

It reads data from a CSV file using Read CSV processor.

* PATH : Path of csv file
* SEPARATOR : CSV separator
* HEADER : Whether the CSV file has a header line
* DROP MALFORMED : Whether malformed records would be dropped or an error raised

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/user-guide/read-write/2.png
   :alt: readwrite
   :width: 100%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/user-guide/read-write/3.png
   :alt: readwrite
   :width: 100%

Prints the Results
------------------

It prints the first few records of the dataframe
