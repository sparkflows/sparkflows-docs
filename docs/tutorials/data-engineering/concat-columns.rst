
Concatenate Columns
==============

This sample workflow concats columns in the input dataset with the specified separator.


Workflow
--------

The below workflow:

* Reads data from a file present on HDFS.
* Concats the selected columns with specified separator.

.. figure:: ../../_assets/tutorials/data-cleaning/concat-columns/6.PNG
   :alt: Concat Columns
   :width: 60%
   
Reading from HDFS File
---------------------

It reads data from a file present on HDFS. 

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/concat-columns/7.PNG
   :alt: Concat Columns
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/concat-columns/8.PNG
   :alt: Concat Columns
   :width: 60%
   
Concating columns
-----------------

It concatenates the specified columns using the specified separator.

Processor Configuration
^^^^^^^^^^^^^^^^^^

We need to provide all the desired columns to be concatenated without any separator or space, like Name,Sex, Age, etc.
Columns would get concatenated in same order defined in configuration like Name then Sex then Age.

.. figure:: ../../_assets/tutorials/data-cleaning/concat-columns/9.PNG
   :alt: Concat Columns
   :width: 60%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-cleaning/concat-columns/10.PNG
   :alt: Concat Columns
   :width: 60%
