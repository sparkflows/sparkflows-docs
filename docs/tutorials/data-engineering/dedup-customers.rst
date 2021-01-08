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
   :width: 90%
   
Input Datasets
---------------------

There are 2 input datasets in this case "Dedup Master Dataset" & "Dedup Error Dataset" as shown below,

Dataset 1:
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/dedup-customers/capture3.png
   :alt: DedupCustomers
   :width: 80%
   
   
Dataset 2:
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/dedup-customers/capture5.png
   :alt: DedupCustomers
   :width: 80%
   
   
Join input DataFrames
------------

``JoinUsingColumn`` processor joins the incoming DataFrames on a join column "State". ``ColumnFilter`` processor filters the columns to get the required DataFrame as shown below:


.. figure:: ../../_assets/tutorials/data-engineering/dedup-customers/capture9.png
   :alt: DedupCustomers
   :width: 80%
   
Data Deduplication
------------

``Dedup`` is used for the problems like entity resolution or data matching.
Entity resolution or data matching is the problem of finding and linking different mentions of the same entity in a single data source or across multiple data sources. Here Levenshtein Algorithm is used for data Deduplication. There are more options for Algorithms that can be used:

* Full matching: Full matching makes use of all individuals in the data by forming a series of matched sets in which each set has either 1 treated individual and multiple comparison individuals or 1 comparison individual and multiple treated individuals

* Levenshtein: It counts the number of edits (insertions, deletions, or substitutions) needed to convert one string to the other.

* Jaro-Winkler: The Jaro–Winkler distance is a string metric measuring an edit distance between two sequences. Jaro-Winkler are suited for comparing smaller strings like words and names.

* Jaccard (3 gram) : This takes consecutive words and group them as a single object. A 3-gram is a consecutive set of 3 words. Used for emails or small documents.

* Longest Common Subsequence : If a set of sequences are given, the longest common subsequence problem is to find a common subsequence of all the sequences that is of maximal length used in revision control systems, such as SVN and Git, for reconciling multiple changes made to a revision-controlled collection of files.

* Date Difference: Calculates the number of days between two dates.

* Notional Distance



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
