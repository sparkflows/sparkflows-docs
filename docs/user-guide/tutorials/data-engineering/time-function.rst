Time Function
=============

There are many instances when you want to do time-series analysis. Fire Insights provides Date-Time features with TimeFunctions operator.

Creating additional features from the timestamp column helps you to know more about the data and run modeling algorithms on them. Fire Insights has NodeTimeFunctions for creating these time series features.

Dataset
--------

Let us take a Transaction Dataset which is in CSV format on HDFS. The dataset has a "DATE" column.

.. figure:: ../../_assets/tutorials/dataset/28.PNG
   :alt: Dataset
   :align: center
   :width: 60%
   
Workflow for applying TimeFunctions
-----------------------------------

In the example workflow below, additional date time features are being created from the date column.

.. figure:: ../../_assets/tutorials/dataset/29.PNG
   :alt: Dataset
   :align: center
   :width: 60%
   
In the above workflow: 

- The 'CSV' processor reads in the CSV data from HDFS.
- The 'StringToDate' processor converts the column Date, which is in string format to 'timestamp'. 
- The 'TimeFunctions' processor takes in the timestamp column and then applies various timefunctions to it to generate additional output columns.

The diagram below shows the dialog box for the TimeFunctions processor. Timestamp column was selected as input, and various time functions were applied to it.

.. figure:: ../../_assets/tutorials/dataset/30.PNG
   :alt: Dataset
   :align: center
   :width: 60%
   
   
Workflow Execution
------------------

When the example workflow is executed, additional columns are produced for the various time functions that were selected.

.. figure:: ../../_assets/tutorials/dataset/31.PNG
   :alt: Dataset
   :align: center
   :width: 60%




