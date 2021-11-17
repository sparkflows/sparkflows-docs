Data Preparation
=============

Data preparation is the process of cleaning and transforming raw data prior to processing and analysis. 
It is an important step prior to processing and often involves reformatting data, making corrections to data and the combining of data sets to enrich data.


Workflow
-------

Below is the workflow. It does the following:

* Reads data from the dataset
* converts a string column to date using the given date/time format
* Sets values for the column "State" based on conditions
* Creates a new DataFrame containing only rows satisfying given condition
* Prints the results of few records


.. figure:: ../../_assets/tutorials/data-engineering/data-preparation-1/1.PNG
   :alt: DataPreparation
   :width: 90%
   
Reading from Dataset
---------------------

It reads in the input Dataset File.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-preparation-1/Capture2.PNG
   :alt: DataPreparation
   :width: 90%
   
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-preparation-1/Capture3.PNG
   :alt: DataPreparation
   :width: 90%  
   
   
Convert String to Date
------------

``MultiStringToDate`` converts a string column to date using the given date/time format.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-preparation-1/Capture4.PNG
   :alt: DataPreparation
   :width: 90%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-preparation-1/Capture5.PNG
   :alt: DataPreparation
   :width: 90%
  

Settings values for required Column
------------

``CaseWhen`` sets values for the required column based on conditions as shown in example below:

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-preparation-1/Capture6.PNG
   :alt: DataPreparation
   :width: 90%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-preparation-1/Capture7.PNG
   :alt: DataPreparation
   :width: 90%
   
Creating DataFrame with required rows
------------

``RowFilter`` creates a new DataFrame containing only rows required.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-preparation-1/Capture8.PNG
   :alt: DataPreparation
   :width: 90%
   
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/data-preparation-1/Capture9.PNG
   :alt: DataPreparation
   :width: 90%
   

Prints the Results
------------------

It prints the first few records onto the screen.
