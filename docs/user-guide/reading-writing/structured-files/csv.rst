CSV
======

Read CSV
------------
This node reads CSV Files.

Below is a sample workflow which contains the Read CSV processor in Fire Insights. It demonstrates the usage of Read CSV File node to read a CSV file.

It does the following processing of data:

*	Reads incoming dataset in CSV Data format using the Read CSV node.
* 	Prints the content of the CSV file using the Print node.

.. figure:: ../../../_assets/user-guide/read-write/read-structured/CSV_WF_1.png
   :alt: readcsv_node_userguide
   :width: 50%
   

**Read CSV Node configuration**

The Read CSV node is configured as below.

#. General Tab

      .. figure:: ../../../_assets/user-guide/read-write/read-structured/CSVConfig_1.png
         :alt: readcsv_node_userguide
         :width: 70%
      
      *	A ``CSV Data File`` needs to be selected in the ``Path``. The ``Browse`` option can be used to browse and select a CSV file from respective filesystem.
      *	A Delimiter or Character used to separate two columns' data needs to be selected in the ``Separator``. In most of the cases ``,`` / comma is used to separate two columns.
      *	``Header`` needs to be selected as ``True`` or ``False`` based on whether data file contains header row that can be used in the imported dataset.
      *  ``Drop Special Character In ColumnName`` needs to be selected as ``True`` or ``False`` based on whether special characters such as ``_ or - or # and so on`` need to be removed from the column name.
      *  ``Whether to Add Input File Name as Column in the Dataframe`` needs to be selected as ``True`` or ``False`` based on whether the file name needs to be added a column to the dataset.

#. Schema Tab

      .. figure:: ../../../_assets/user-guide/read-write/read-structured/CSVConfig_2.png
         :alt: readcsv_node_userguide
         :width: 70%
      
      *	Once a CSV file is selected the ``Refresh Schema`` button needs to be clicked to list Schema defined in the ``CSV Data File``. 

#. Extra Options Tab

      .. figure:: ../../../_assets/user-guide/read-write/read-structured/CSVConfig_3.png
         :alt: readcsv_node_userguide
         :width: 70%
      
      *	``Extra Options`` can be entered in key-value pair. They would be used while reading the CSV file. i.e. Option ``Comment`` can be added to skip comments from the file while reading it.

*	``Okay`` button needs to be clicked to complete the configuration.

**Read CSV node output**

Data read from a CSV Data File is printed as below using the Print node.

.. figure:: ../../../_assets/user-guide/read-write/read-structured/CSVOutput_1.png
   :alt: readcsv_node_userguide
   :width: 70%
   
Save CSV
----------------------------------------
This node saves the incoming dataset as CSV File.

Below is a sample workflow which contains the Save CSV processor in Fire Insights. It demonstrates the usage of Save CSV node to save the incoming dataset in CSV format.

It does the following processing of data:

*	Reads the incoming dataset.
*	Coalesce node is used to define the number of partitions to be created while saving.
*	Saves the incoming dataset in CSV format using  the Save CSV node.

.. figure:: ../../../_assets/user-guide/read-write/save-files/save-csv-wf.png
   :alt: savefiles_userguide
   :width: 50%
   
**Incoming Dataset**

.. figure:: ../../../_assets/user-guide/read-write/save-files/InputData.png
   :alt: savefiles_userguide
   :width: 75%
   
**Save CSV node configuration**

Save CSV node is configured as below.

*	HDFS location where created file needs to be saved is to be selected in the ``Path`` box.
*	Save mode to be selected in the ``Save Mode`` list. It states whether to *Append*, *Overwrite*, *Error out if file exists* or *Ignore* while saving the file.
*	Option to save Header row is to be selected as True/False in the ``Header`` list.
*	In ``Advanced`` tab, set of columns that need to be used to partition data are to be selected in the ``Partition Column Names`` list. One file would be created for each partition.
*	Saves the incoming dataset in CSV format.

.. figure:: ../../../_assets/user-guide/read-write/save-files/CSVGenConfig.png
   :alt: savefiles_userguide
   :width: 75%
   
.. figure:: ../../../_assets/user-guide/read-write/save-files/CSVAdvConfig.png
   :alt: savefiles_userguide
   :width: 75%
   
