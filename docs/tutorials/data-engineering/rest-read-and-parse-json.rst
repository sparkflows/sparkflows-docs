REST Read And Parse JSON
=============

This workflow reads in single record JSON from the given URL. It then parses the dataset and prints the results.

Workflow
-------

Below is the workflow that shows:
* How to read in single record JSON from the given URL and create the DataFrame from it
* Prints the result

.. figure:: ../../_assets/tutorials/data-engineering/rest-read-and-parse-json/Capture1.PNG
   :alt: ReadandParse
   :align: center
   :width: 60%
   
Reading from URL And Parsing
---------------------

``DatasetURLSingleRecordJSONReader`` processor uses the passed URL to download single record JSON, parse the dataset and create the DataFrame.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/rest-read-and-parse-json/Capture2.PNG
   :alt: ReadandParse
   :align: center
   :width: 60%

  
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/data-engineering/rest-read-and-parse-json/Capture3.PNG
   :alt: ReadandParse
   :align: center
   :width: 60%   
   
   
Prints the Results
------------------

It prints the result onto the screen.
