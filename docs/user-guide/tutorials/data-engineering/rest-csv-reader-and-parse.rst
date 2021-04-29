REST - CSV Reader & Parse
=============

This workflow reads in a dataset from URL. It then parses the dataset and prints the results.

Workflow
-------

Below is the workflow. It does the following:

* Reads data from the URL and creates a DataFrame
* Prints few records
* Splits the string of the input column using the delimiter
* Creates a new DataFrame containing rows satisfying the provided condition
* Prints the result

.. figure:: ../../_assets/tutorials/data-engineering/rest-csv-reader-and-parse/Capture1.PNG
   :alt: ReadandParse
   :align: center
   :width: 60%
   
Reading from URL
---------------------

``DatasetURLTextFileReader`` processor uses the passed URL to download the data and create the DataFrame.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/rest-csv-reader-and-parse/Capture2.PNG
   :alt: ReadandParse
   :align: center
   :width: 60%

  
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/rest-csv-reader-and-parse/Capture3.PNG
   :alt: ReadandParse
   :align: center
   :width: 60%   
   
Prints the Records
------------------

It prints the first few records onto the screen.
   
   
Parsing the DataFrame
------------

``FieldSplitter`` processor parses and creates new DataFrame by splitting the string of the input column using the delimiter as shown below:

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/rest-csv-reader-and-parse/Capture4.PNG
   :alt: ReadandParse
   :align: center
   :width: 60%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/rest-csv-reader-and-parse/Capture5.PNG
   :alt: ReadandParse
   :align: center
   :width: 60%
   
Row Filter by Index
-------------

``RowFilterByIndex`` processor creates a new DataFrame containing required rows as shown below:


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/rest-csv-reader-and-parse/Capture6.PNG
   :alt: ReadandParse
   :align: center
   :width: 60%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/rest-csv-reader-and-parse/Capture7.PNG
   :alt: ReadandParse
   :align: center
   :width: 60%
     
  
Prints the Results
------------------

It prints the result onto the screen.
