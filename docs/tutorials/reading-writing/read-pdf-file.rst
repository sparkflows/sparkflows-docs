Reading PDF File
=============

This workflow reads PDF file from the given location. It then parses its content, creates DataFrame and then prints the result.

Workflow
-------

The below workflow shows:

* How to read in PDF file from the given location and create the DataFrame from it
* Prints the result

.. figure:: ../../_assets/tutorials/read-write/read-pdf-file/1.PNG
   :alt: ReadandParse
   :width: 90%
   
Reading And Parsing PDF File
---------------------

``DatasetPDF`` processor uses the passed location to download PDF file, parse its content into string and create the DataFrame.


Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/read-write/read-pdf-file/2.PNG
   :alt: ReadandParse
   :width: 90%

  
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/read-write/read-pdf-file/3.PNG
   :alt: ReadandParse
   :width: 90%   
   
   
Prints the Result
------------------

It prints the result onto the screen.
