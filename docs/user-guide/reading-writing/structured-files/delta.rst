DELTA
======
This document provides an overview of the Read Delta and Save Delta nodes in Fire Insights, explaining their configurations and functionalities for reading from and writing to Delta Lake.

Read Delta
------------
This node reads files from a Delta Lake.

Below is a sample workflow which contains the Read Delta processor in Fire Insights. It demonstrates the usage of Read Delta node to read data from a Delta Lake.

  .. figure:: ../../../_assets/user-guide/read-write/read-delta/read-delta-wf-1.png
     :alt: read-delta-wf
     :width: 50%

It does the following processing of data:

*	Reads the data located in the Delta Lake using the Read Delta node.
* 	Prints the content of the file using the Print node.



**Read Delta Node Configuration**
++++++++++++++++++++++++++++++++++++

To configure this node, follow the steps below:

**Step 1 : Configuring the General Tab**

Enter the required details in the General Tab fileds, as shown below:

   .. figure:: ../../../_assets/user-guide/read-write/read-delta/read-delta-processor-1.png
      :alt: read-delta-processor
      :width: 70%
      
* **PATH:** Select the path to the **Delta file**. Use the **Browse** option to navigate and select a Delta file path from the configured file system.

**Step 2 : Configuring the Schema Tab**

*	Once the Delta file is selected, click the **Refresh Schema** button to list Schema defined in the **Delta File**, as shown below.

      .. figure:: ../../../_assets/user-guide/read-write/read-delta/read-delta-processor-2.png
         :alt: read-delta-processor
         :width: 70%

      
**Step 3 : Configuring the Extra Options Tab**

* The extra options can be added in key-value pairs, as shown below. These will be used when reading Delta files.

 .. figure:: ../../../_assets/user-guide/read-write/read-delta/read-delta-processor-3.png
      :alt: read-delta-processor
      :width: 70%
      
     
* To complete the configuration, click on **Okay** button.


|
**Read Delta Node Output**
++++++++++++++++++++++++++++++

The data read from the Delta Lake file is printed using the Print node, as shown below.

 .. figure:: ../../../_assets/user-guide/read-write/read-delta/read-delta-output-1.png
    :alt: read-delta-output
    :width: 70%


|
  
Save Delta
----------------------------------------
This node saves the incoming dataset to a Delta Lake location in Delta format.

Below is a sample workflow which contains the Save Delta processor in Fire Insights. It demonstrates the usage of Save Delta node to save the incoming dataset to a Delta Lake in Delta format.

 .. figure:: ../../../_assets/user-guide/read-write/Save-Delta/save-delta-workflow-1.png
    :alt: save-delta-lake
    :width: 50%

It does the following processing of data:

*	Reads the incoming dataset.
*	Partitions and Saves the incoming dataset using the Save Delta node.


   
**Save Delta Node Configuration**
++++++++++++++++++++++++++++++++++++++

To configure the Save Delta node follow the steps below:

**Step 1 : Configuring the General Tab**

Enter the required details in General Tab fields, as shown below:

 .. figure:: ../../../_assets/user-guide/read-write/Save-Delta/save-delta-general.png
         :alt: save-delta-general
         :width: 75%
      
* **PATH:** Enter the Delta Lake location where created file needs to be saved or select it by using the **Browse File System** option.
* **SAVE MODE:** Select the appropriate option from the dropdown, which determines whether to **Append**, **Overwrite**, **Error out if file exists** or **Ignore** while saving the file.

**Step 2 : Configuring the Advanced Tab**

Enter the required details in the Advanced Tab fields, as shown below.

   .. figure:: ../../../_assets/user-guide/read-write/Save-Delta/save-delta-advanced-1.png
         :alt: save-delta-general
         :width: 75%

   .. figure:: ../../../_assets/user-guide/read-write/Save-Delta/save-delta-advanced-1a.png
         :alt: save-delta-general
         :width: 75%

*	**PARTITION COLUMN NAMES:** Select the set of columns from the list that need to be used for partitioning data. A separate file is created for each partition.
*	**MERGE SCHEMA:** By default, it is **false**, indicating that the schema of the new data must match the existing Delta table schema. If there are any schema differences, the merge operation will fail.
*	**OVERWRITE SCHEMA:** This option when enabled allows schema overwriting. By default, it is **false**, indicating that the schema of the data being written must match the existing schema of the Delta table. If there are any schema differences, the write operation will fail.
*	**OPTIMIZE WRITE:** This option when enabled, optimizes file sizes during the write operation. By default it is **false**, indicating that Delta Lake will not optimize file sizes during the write operation, potentially leading to many small files.
*	**OVERWRITE PARTITION PREDICATE:** This option allows you to selectively overwrite specific partitions in a Delta table based on partition values, providing flexibility in updating and managing partitioned data.

**Step 3 : Configuring the Extra Options Tab**

*	The extra options can be added in key-value pairs, as shown below. These will be used while saving Delta Files.

   .. figure:: ../../../_assets/user-guide/read-write/Save-Delta/save-delta-extoptions-1.png
      :alt: save-delta-general
      :width: 75%

* To complete the configuration, click on **Okay** button.

      
**Save Delta - Execution Success Message**
+++++++++++++++++++++++++++++++++++++++++++

Once data is successfully saved in Delta Lake, a success message is displayed as shown below:

 .. figure:: ../../../_assets/user-guide/read-write/Save-Delta/save-delta-savesuccess-1.png
    :alt: save-delta-advanced
    :width: 75%
   
