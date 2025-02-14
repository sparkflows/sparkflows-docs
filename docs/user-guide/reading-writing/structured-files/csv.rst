CSV
======
This document provides a guide for the Read CSV and Save CSV nodes in Fire Insights, explaining their configuration, functionality, and usage in workflows.

Read CSV
------------
This node reads CSV Files.

Below is a sample workflow which contains the Read CSV processor in Fire Insights. It demonstrates the usage of Read CSV File node to read a CSV file.

 .. figure:: ../../../_assets/user-guide/read-write/read-structured/CSV_WF_1.png
    :alt: readcsv_node_userguide
    :width: 50%

It does the following processing of data:

*	Reads incoming dataset in CSV Data format using the Read CSV node.
* 	Prints the content of the CSV file using the Print node.

   

**Read CSV Node Configuration**
+++++++++++++++++++++++++++++++++

To configure the Read CSV node follow the steps below:

**Step 1 : General Tab Configurations**

      .. figure:: ../../../_assets/user-guide/read-write/read-structured/CSVConfig_1.png
         :alt: readcsv_node_userguide
         :width: 70%

      Enter the desired values in the above fields as follows:
      
      *	**PATH:** Select a CSV Data File. The **Browse** option can be used to browse and select a CSV file from respective filesystem.
      *	**SEPARATOR:** Select a Delimiter or Character used to separate two columns' data. In most of the cases comma(' **,** ') is used to separate two columns.
      *	**HEADER:** Select it to **True** or **False** based on whether data file contains header row that can be used in the imported dataset.
      *  **DROP SPECIAL CHARACTER IN COLUMN NAME:** Select it to **True** or **False** based on whether special characters such as **_ or - or # and so on** need to be removed from the column name.
      *  **WHETHER TO ADD FILE NAME AS COLUMN IN THE DATAFRAME** needs to be selected as **True** or **False** based on whether the file name needs to be added as column to the dataset.

**Step 2 : Schema Tab Configurations**
_______________________________________

      Once a CSV file is selected click on **Refresh Schema** button to list Schema defined in the CSV Data File, as shown below.

      .. figure:: ../../../_assets/user-guide/read-write/read-structured/CSVConfig_2.png
         :alt: readcsv_node_userguide
         :width: 70%
      
      
**Step 3 : Extra Options Tab Configurations**

*	Enter extra options in key-value pair. They can be used while reading the CSV file. For e.g. Option **comment** can be added to skip comments from the file while reading it, as shown below.

     .. figure:: ../../../_assets/user-guide/read-write/read-structured/CSVConfig_3.png
        :alt: readcsv_node_userguide
        :width: 70%
      
      

* To complete the configurations, click on **Okay** button.

**Read CSV node output**
+++++++++++++++++++++++++++++++

 Using the Print node Data read from a CSV Data File is printed as shown below.

 .. figure:: ../../../_assets/user-guide/read-write/read-structured/CSVOutput_1.png
     :alt: readcsv_node_userguide
     :width: 70%
   
Save CSV
----------------------------------------
This node saves the incoming dataset as CSV File.

Below is a sample workflow which contains the Save CSV processor in Fire Insights. It demonstrates the usage of Save CSV node to save the incoming dataset in CSV format.

 .. figure:: ../../../_assets/user-guide/read-write/save-files/save-csv-wf.png
    :alt: savefiles_userguide
    :width: 50%

It does the following processing of data:

*	Reads the incoming dataset.
*	Coalesce node is used to define the number of partitions to be created while saving.
*	Saves the incoming dataset in CSV format using the Save CSV node.


   
**Incoming Dataset**
+++++++++++++++++++++++

 .. figure:: ../../../_assets/user-guide/read-write/save-files/InputData.png
    :alt: savefiles_userguide
    :width: 75%
   
**Save CSV node Configuration**
+++++++++++++++++++++++++++++++++++

To configure Save CSV node follow the steps below:

 
**Step 1 : General Tab Configurations**

Enter the required details in the fileds shown below as follows:

 .. figure:: ../../../_assets/user-guide/read-write/save-files/CSVGenConfig.png
    :alt: savefiles_userguide
    :width: 75%

* **PATH:** Select HDFS location where created file needs to be saved.
* **SAVE MODE:** Select a save mode from the dropdown. It states whether to **Append, Overwrite, Error out if file exists or Ignore** while saving the file.
* **HEADER:** Select **True or False** from the dropdown to save the Header row. 

**Step 2 : Advanced Tab Configurations**

Enter the required details in the fileds shown below as follows:
 
 .. figure:: ../../../_assets/user-guide/read-write/save-files/CSVAdvConfig.png
    :alt: savefiles_userguide
    :width: 75%

*	**PARTITION COLUMN NAMES:** Select the set of columns in the list, that need to be used to partition data. One file would be created for each partition.
*	After selecting columns, click on **Okay** button. It saves the incoming dataset in CSV format.


   

   
