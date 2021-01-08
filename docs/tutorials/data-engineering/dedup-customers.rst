Dedup Customers
=============

Data deduplication refers to a technique for eliminating redundant data in a data set. 
In the process of deduplication, extra copies of the same data are deleted, leaving only one copy to be stored.


Workflow
-------

Below is the workflow. This workflow does the following:


* Finds matching records between 2 given datasets. It first joins them with the column "State".
* Then it applies distance algorithms on a few fields to find the distance between the records.


.. figure:: ../../_assets/tutorials/data-engineering/dedup-customers/capture1.png
   :alt: DedupCustomers
   :width: 60%
   
Input Datasets
---------------------

There are 2 input datasets in this case "Dedup Master Dataset" & "Dedup Error Dataset" as shown below,

DataFrame 1:
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/dedup-customers/capture3.png
   :alt: DedupCustomers
   :width: 80%
   
   
DataFrame 2:
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/dedup-customers/capture5.png
   :alt: DedupCustomers
   :width: 80%
   
   
Join input DataFrames
------------

``JoinUsingColumn`` processors joins the incoming DataFrames on a joinCol "State" and ``ColumnFilter`` processor is used to filter the columns and get the required DataFrame as shown below:


.. figure:: ../../_assets/tutorials/data-engineering/dedup-customers/capture9.png
   :alt: DedupCustomers
   :width: 80%
   
Data Deduplication
------------

``Dedup`` is used for the problems like entity resolution or data matching.
Entity resolution or data matching is the problem of finding and linking different mentions of the same entity in a single data source or across multiple data sources. Here Levenshtein Algorithm is used for data Deduplication.

``Dedup`` Processor Configuration 
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/dedup-customers/capture10.png
   :alt: DedupCustomers
   :width: 80%
   
   
``Dedup`` Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/dedup-customers/capture11.png
   :alt: DedupCustomers
   :width: 80%
   

Prints the Results
------------------

It prints the first few records onto the screen.
