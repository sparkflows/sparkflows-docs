DELTA
======

Read DELTA
------------
This node reads files from a Delta Lake.

Below is a sample workflow which contains the Read Delta processor in Fire Insights. It demonstrates the usage of Read Delta node to read a file from a Delta Lake.

It does the following processing of data:

*	Reads the file located in the Delta Lake using the Read Delta node.
* 	Prints the content of the file using the Print node.
* 	Prints the summary profile of the read table.

.. figure:: ../../../_assets/user-guide/read-write/read-delta/read-delta-wf.png
   :alt: read-delta-wf
   :width: 60%
   
|
**Read Delta Node configuration**

The Read Delta node is configured as below.

*	A ``Delta File`` needs to be selected in the ``Path``. The ``Browse File System`` option can be used to browse and select a Delta file from the configured File System.
*	Once the Delta file is selected the ``Refresh Schema`` button needs to be clicked to list Schema defined in the ``Delta File``. 
*	``OK`` button needs to be clicked to complete the configuration.

.. figure:: ../../../_assets/user-guide/read-write/read-delta/read-delta-processor.png
   :alt: read-delta-processor
   :width: 70%
|
**Read Delta node Output**

Data read from the Delta Lake file is printed as below using the Print node.

.. figure:: ../../../_assets/user-guide/read-write/read-delta/read-delta-output.png
   :alt: read-delta-output
   :width: 70%
