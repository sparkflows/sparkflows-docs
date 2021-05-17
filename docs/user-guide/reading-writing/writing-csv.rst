Write csv
==========

Fire Insights enables the user to write a CSV file

Workflow
--------

Below is the workflow. It does the following:

* Reads data from a CSV file.
* save CSV to the specified location.

.. figure:: ../../_assets/user-guide/read-write/4.png
   :alt: readwrite
   :width: 80%

Reading from CSV File
---------------------

It reads data from a CSV file using a Read CSV processor.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/user-guide/read-write/8.png
   :alt: readwrite
   :width: 80%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/user-guide/read-write/9.png
   :alt: readwrite
   :width: 80%

Save CSV file
----------------

It saves CSV file in the specified location, uses the below fields for saving the CSV file


* PATH: Select specified path of CSV file to be saved
* SEPERATOR : CSV separtor
* HEADER: True or false depending on file type

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/user-guide/read-write/5.png
   :alt: readwrite
   :width: 80%
   
Once the workflow executes successfully the CSV file will be saved to the specified location

.. figure:: ../../_assets/user-guide/read-write/6.png
   :alt: readwrite
   :width: 80%
