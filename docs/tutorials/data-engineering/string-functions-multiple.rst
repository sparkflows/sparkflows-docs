String Functions
================

String functions are useful to tranform strings in your dataframe. The "StringFunction" processors allows you to apply common string operations such as ``trim``, ``upper``, ``lower``, ``lefttrim``, ``righttrim`` etc. to strings.

In the example below, different string functions are applied to input dataset.

Workflow
--------

The example workflow below, reads data from HDFS/Hive and applies different string functions on different columns of the dataset.


.. figure:: ../../_assets/tutorials/etl/string-functions-multiple/6.PNG
   :alt: String Functions Multiple
   :width: 100%
   
Read data from HDFS
-------------------

The "Housing" processor above, reads an existing dataset on HDFS.

Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/etl/string-functions-multiple/7.PNG
   :alt: String Functions Multiple
   :width: 100%

Processor Output
^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/etl/string-functions-multiple/8.PNG
   :alt: String Functions Multiple
   :width: 100%

Apply string Functions
----------------------

The 'StringFunctionMultiple' processor below, converts contents of 'Driveway' column to upper case and trims contents of 'Gashw' column.

Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/etl/string-functions-multiple/9.PNG
   :alt: String Functions Multiple
   :width: 100%
   
Processor Output
^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/etl/string-functions-multiple/10.PNG
   :alt: String Functions Multiple
   :width: 100%
   
   
   
   
