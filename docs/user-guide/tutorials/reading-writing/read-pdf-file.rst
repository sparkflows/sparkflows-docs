Read PDF File
=============

This workflow reads in PDF file from the given location. It then parses its content and creates DataFrame then prints the results.

Workflow
-------

Below is the workflow that shows:

* How to read in PDF file from the given location and create the DataFrame from it
* Prints the result

.. figure:: ../../_assets/tutorials/read-write/read-pdf-file/Capture1.PNG
   :alt: ReadandParse
   :align: center
   :width: 60%
   
Reading And Parsing PDF File
---------------------

``DatasetPDF`` processor uses the passed location to download PDF file, parse its content into string and create the DataFrame.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/read-write/read-pdf-file/Capture2.PNG
   :alt: ReadandParse
   :align: center
   :width: 60%

  
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/read-write/read-pdf-file/Capture3.PNG
   :alt: ReadandParse
   :align: center
   :width: 60%   
   
   
Prints the Results
------------------

It prints the result onto the screen.
