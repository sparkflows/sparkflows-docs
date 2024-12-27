CDC Tutorials - Bank Transactions
=================================

.. contents::
   :depth: 3

CDC Overview
-------------------

**CDC (Change Data Capture)** is used to identify and track changes in a connected data table, including data insertions, updates, and deletions. 

It facilitates efficient incremental data loading and ensures seamless integration of these changes into the dataset. 

CDC (Change Data Capture) Tutorials
-------------------

This tutorial will guide you on how to use Sparkflows CDC to capture changes in bank transaction data stored in an Oracle Database. The **AutoIncrement node** in Sparkflows is utilized for tracking these changes.

This tutorial covers the steps for CDC setup, configuring the AutoIncrement node, creating the workflow, and merging the captured changes into a Delta file.

CDC Configuration
^^^^^^^^^^^^^^^^^^^^^^^^
The steps to set up CDC are as follows:

#. Navigate to **Administration > Configuration > Modules.**
#. **Enable CDC** by setting Enable CDC to **true**.

   .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-config.png
      :alt: CDC Tutorials
      :width: 70%

#. The CDC Tab on the Project Dashboard will now be visible as shown below.

   .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-tab.png
      :alt: CDC Tutorials
      :width: 70%

Data Source: Bank Transactions Oracle Table
^^^^^^^^^^^^^^^^^^^^^^^^

* This tutorial uses **Bank Transactions Database Table** from an Oracle database to capture changes. 
* The table schema includes essential columns like Transaction_ID, Transaction_Datetime, Amount, Balance_Change, and IS_DELETED, as shown below.
   
  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-banktrans-table.png
     :alt: CDC Tutorials
     :width: 70%

CDC Workflow
^^^^^^^^^^^^^^^^^^^^^^^^

* Create a CDC Workflow using the **AutoIncrement** and **DeltaMerge nodes**.

  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-workflow.png
      :alt: CDC Tutorials
      :width: 70%

AutoIncrement Node Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

* The **AutoIncrement Node** needs to be configured as shown below. It will be used to capture changes in the data based on the values in the **Key Column**.

  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-autoincrement.png
      :alt: CDC Tutorials
      :width: 70%

* To configure the **AutoIncrement Node**, enter appropriate values in the required fields as follows and click the **Okay** button.
	  
  **Connection:** Select the **Oracle Connection** from the dropdown.

  **Database Name:** Enter the Database name.

  **Table Name:** Specify the Database Table name(**Bank_Transactions**).

  **Key Column Name:** Enter the name of the column that will be used to capture changes(**Transaction_Datetime**).

  **Key Column Type:** Select the datatype of the Key Column from the dropdown(**Timestamp**).

  **Key Column Format:** Enter the data format **YYYY-MM-DD HH24:MI:SS:FF** for the Key Column.
	  
DeltaMerge Node Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

* **DeltaMerge Node** needs to be configured as shown below. It will be used to merge changes from the source data to the target location in Delta format.

  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-deltamerge.png
      :alt: CDC Tutorials
      :width: 70%

* To configure the **DeltaMerge Node**, enter appropriate values in the required fields as follows and click the **Okay** button.
	  
  **TargetPath:** Provide the Delta file path for merging changes.

  **Source Alias:** Enter an alias for the Source Dataset. It will be used in the joining conditions.

  **Target Alias:** Enter an alias for the Target Dataset. It will be used in the joining conditions.

  **Merge Condition:** Enter the condition **source.TRANSACTION_ID = target.TRANSACTION_ID** to join Source and Target datasets.
	  
Execute Workflow
^^^^^^^^^^^^^^^^^^^^^^^^

* Click the **Execute** Button on the workflow to execute it. It will perform **Initial Loading** of data from the Source (BANK_TRANSACTIONS database table) and merge it into the Target Location. 

* The output of the execution will be displayed as shown below. It will merge all the records during the first run i.e. Initial Loading.

  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-initload.png
      :alt: CDC Tutorials
      :width: 70%
	  
* **CDC Tab** on the Project Dashboard will be updated as shown below. It will update the **End Value** as the max **Key Column (Transaction_Datetime)** value.
	  
  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-endvalinitload.png
     :alt: CDC Tutorials
     :width: 70%
	  	  
Handling New Transactions
^^^^^^^^^^^^^^^^^^^^^^^^

* Over time new transactions will occur and new records will be added to the **BANK_TRANSACTIONS** table, as shown below. The highlighted records represent the new ones.

  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-newtrans.png
      :alt: CDC Tutorials
      :width: 70%
	  
* Click the **Execute** Button on the workflow to fetch new transactions, as shown below.
	  
  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-newtransfetched.png
     :alt: CDC Tutorials
     :width: 70%
	  
* The **CDC Tab** on the Project Dashboard will be updated as shown below. It will update the **End Value** as the max **Key Column (Transaction_Datetime)** value. The **Start Value** will display the previously fetched max value.
	  
  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-endvalnewtrans.png
     :alt: CDC Tutorials
     :width: 70%
		  
* New Transactions will be merged into the Delta File at the location shown below.
	  
  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-mergednewtrans.png
     :alt: CDC Tutorials
     :width: 70%

Handling Updated Transactions
^^^^^^^^^^^^^^^^^^^^^^^^

* Over time, some transactions may be updated in the **BANK_TRANSACTIONS** table as shown below. The highlighted record indicates an update, where the Amount and Balance_Change values have changed from 250 to 500. The **Transaction_Datetime** will be updated to reflect the updated timestamp value.

  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-updtrans.png
      :alt: CDC Tutorials
      :width: 70%
	  
* Click the **Execute** Button on the workflow to fetch the updated transaction as shown below.
	  
  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-updtransfetched.png
     :alt: CDC Tutorials
     :width: 70%
	  
* The **CDC Tab** on the Project Dashboard will be updated as shown below. It will update the **End Value** as the max **Key Column (Transaction_Datetime)** value i.e. as per the Updated Timestamp value. The **Start Value** will display the previously fetched max value.
	  
  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-endvalupdtrans.png
     :alt: CDC Tutorials
     :width: 70%
		  
* The Updated Transaction will be merged into the Delta File at the location shown below.
	  
  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-mergedupdtrans.png
     :alt: CDC Tutorials
     :width: 70%

Handling Deleted Transactions
^^^^^^^^^^^^^^^^^^^^^^^^

* The **BANK_TRANSACTIONS** table contains a column **IS_DELETED**. This column is updated to **Y** whenever a transaction is deleted at the source; otherwise, it remains **N** by default.

* If a transaction at the source is deleted, the flag is updated as shown below. The **Transaction_Datetime** will also be updated to reflect the deletion timestamp. 

  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-deltrans.png
      :alt: CDC Tutorials
      :width: 70%
	  
* The **DeltaMerge** node needs to be configured to handle deleted transactions as shown below.
	  
  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-deltransconfig.png
     :alt: CDC Tutorials
     :width: 70%
	  
* Click the **Execute** Button on the workflow to handle deleted transactions as shown below.
	  
  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-deltransfetched.png
     :alt: CDC Tutorials
     :width: 70%
	  
* The **CDC Tab** on the Project Dashboard will be updated as shown below. It will update the **End Value** as the max **Key Column (Transaction_Datetime)** value to reflect the Deleted Timestamp value. The **Start Value** will display the previously fetched max value.
	  
  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-endvaldeltrans.png
     :alt: CDC Tutorials
     :width: 70%
		  
* The Deleted Transaction will be merged into the Delta File at the location shown below. The **IS_DELETED** flag will be updated for the deleted transaction.
	  
  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-mergeddeltrans.png
     :alt: CDC Tutorials
     :width: 70%
