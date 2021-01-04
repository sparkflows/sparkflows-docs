Data Wrangling
=============

Data wrangling is the process of gathering, selecting, and transforming data to answer an analytical question.  Also known as data cleaning or “munging”.
This workflow reads in a dataset. It then wrangles the dataset based on provided conditions and prints the results.

Workflow
-------

Below is the workflow. It does the following:

* Reads data from a dataset
* It then create new DataFrame based on the rules provided
* Prints the results

.. figure:: ../../_assets/tutorials/data-engineering/data-wrangling/Capture1.PNG
   :alt: data-wrangling
   :align: center
   :width: 60%
   
Reading from Dataset
---------------------

``DatasetStructured`` processor creates a Dataframe of your dataset by reading data from HDFS, HIVE etc. which had been defined earlier in Fire by using the Dataset feature.

  
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-wrangling/Capture2.PNG
   :alt: data-wrangling
   :align: center
   :width: 60%   
   
   
Data Wrangling
------------

``DataWrangling`` processor creates new DataFrame after applying the provided rules

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-wrangling/Capture3.PNG
   :alt: data-wrangling
   :align: center
   :width: 60%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-wrangling/Capture4.PNG
   :alt: data-wrangling
   :align: center
   :width: 60%
  
  
Prints the Results
------------------

It prints the first few records onto the screen.




