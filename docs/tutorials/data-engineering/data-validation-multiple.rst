Data Validation II
===============

This workflow performs multiple validations on each incoming record.

It also:

* Records which pass validation are output into the first edge.
* Records which fail validation are output into the seconds edge.

Validations
-----------
* Ensures that field is greater than or equal to specified string value.
* Ensures that field is less than or equal to specified string value.
* Ensures that field matches given datePattern.
* Ensures that the email is valid.
* Ensures field length is greater than or equal to specified length.

Workflow
--------

The below workflow:

* Reads data from a CSV File.
* Performs specific validation on specific columns.

.. figure:: ../../_assets/tutorials/data-engineering/data-validation-multiple/1.PNG
   :alt: Data Validation Multiple
   :width: 65%
   
Reading from CSV File
---------------------

``DatasetCSV`` Processor reads data from a CSV file. 

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-validation-multiple/2.PNG
   :alt: Data Validation Multiple
   :width: 85%
   
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-validation-multiple/3.PNG
   :alt: Data Validation Multiple
   :width: 85%

String Functions
----------------
``StringFunctions`` Processor performs specified operation on the selected column (i.e. trim function for column 'name' in this case).

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-validation-multiple/4.PNG
   :alt: Data Validation Multiple
   :width: 85%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-validation-multiple/5.PNG
   :alt: Data Validation Multiple
   :width: 85%
   

Performing Validation
---------------------

``ValidationMultiple`` Processor performs different validation on different columns.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-validation-multiple/6.PNG
   :alt: Data Validation Multiple
   :width: 85%   

   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-validation-multiple/7.PNG
   :alt: Data Validation Multiple
   :width: 90% 

Prints the Valid Records
------------------

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-validation-multiple/8.PNG
   :alt: Data Validation Multiple
   :width: 90%  


Prints the Invalid Records
------------------

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-validation-multiple/9.PNG
   :alt: Data Validation Multiple
   :width: 90%  

