REST API Read and Parse JSON
=============

This workflow reads in a single record JSON from the given URL. It then parses the dataset and prints the result.

Workflow
-------

Below is the workflow that shows:

* How to read in single record JSON from the given URL and create the DataFrame from it.
* Prints the result.

.. figure:: ../../_assets/tutorials/data-engineering/rest-read-and-parse-json/1.PNG
   :alt: ReadandParse
   :width: 60%
   
Reading from URL And Parsing
---------------------

``DatasetURLSingleRecordJSONReader`` Processor uses the passed URL to download single record JSON, Parse the dataset and create the DataFrame.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/rest-read-and-parse-json/2.PNG
   :alt: ReadandParse
   :width: 75%

  
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/rest-read-and-parse-json/3.PNG
   :alt: ReadandParse
   :width: 75%
   
   
Prints the Result
------------------

It prints the result onto the screen.
