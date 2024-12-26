CDC Tutorials - Bank Transactions
=================================

.. contents::
   :depth: 3

CDC Overview
-------------------

**CDC (Change Data Capture)** helps in the identification and tracking of changes made to the connected Data Table. It tracks changes made by Insertion, Update and Deletion of data.

It facilitates incremental load of data and merging of changes made to the dataset.

CDC (Change Data Capture) Tutorials
-------------------

This tutorial will cover how to use Sparkflows CDC to capture changes made to the Bank Transactions data. It is maintained in a Oracle Database. **Sparkflows AutoIncrement** node is used to capture the changes.

This tutorial covers steps involved in CDC Setup, configuring AutoIncrement node, creation of the respective workflow, and To merge changes made to a Delta file.

CDC Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

Enable **CDC** by navigating to **Administration > Configuration > Modules** as shown below.

   .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-config.png
      :alt: CDC Tutorials
      :width: 70%

**Enable CDC** needs to be set to **true**
	
**CDC Tab** on Project Dashboard would get enabled as below.
	
   .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-tab.png
      :alt: CDC Tutorials
      :width: 70%

Bank Transactions Oracle DataTable
^^^^^^^^^^^^^^^^^^^^^^^^

This tutorials uses **Bank Transactions Database Table** to capture changes. It has below schema and intial data looks as below.

   .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-banktrans-table.png
      :alt: CDC Tutorials
      :width: 70%

CDC Workflow
^^^^^^^^^^^^^^^^^^^^^^^^

**CDC Workflow** needs to be created as below using **AutoIncrement** and **DeltaMerge** nodes.

   .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-workflow.png
      :alt: CDC Tutorials
      :width: 70%

AutoIncrement Node Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

**AutoIncrement Node** needs to be configured as below. It would be used to capture changes in the data based on the value in the Key Column.

   .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-autoincrement.png
      :alt: CDC Tutorials
      :width: 70%
	  
**Connection:** Select the **Oracle Connection** from the dropdown.

**Database Name:** Enter the Database name.

**Table Name:** Enter the Database Table name i.e. **Bank_Transactions**

**Key Column Name:** Enter the name the column which would be used to capture changes i.e. **Transaction_Datetime**

**Key Column Type:** Select the datatype of the Key Column from the dropdown i.e. **Timestamp**

**Key Column Format:** Enter the data format for the Key Column i.e. **YYYY-MM-DD HH24:MI:SS:FF**
	  
DeltaMerge Node Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

**DeltaMerge Node** needs to be configured as below. It would be used to merge the changes in the source data to the target location in Delta format.

   .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-deltamerge.png
      :alt: CDC Tutorials
      :width: 70%
	  
**TargetPath:** Enter Delta File Path. It would be merged with the changed data.

**Source Alias:** Enter the alias for the Source Dataset. It would be used in the joining conditions.

**Target Alias:** Enter the alias for the Target Dataset. It would be used in the joining conditions.

**Merge Condition:** Enter the condition to join Source and Target datasets i.e. source.TRANSACTION_ID = target.TRANSACTION_ID
	  
Execute Workflow
^^^^^^^^^^^^^^^^^^^^^^^^

Click on **Execute** Button on the workflow to execute it. It would perform **Initial Loading** of data from the Source (BANK_TRANSACTIONS database table) and merge it the Target Location. 

Output of the execution would be as below. It would merge all the records during the first run i.e. Initial Loading.

   .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-initload.png
      :alt: CDC Tutorials
      :width: 70%
	  
**CDC Tab** on the Project Dashboard would be updated as below. **End Value** would get updated as the max **Key Column (Transaction_Datetime)** value.
	  
   .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-endvalinitload.png
		  :alt: CDC Tutorials
		  :width: 70%
	  	  
Handling New Transactions
^^^^^^^^^^^^^^^^^^^^^^^^

During the course of time new transactions would be done and new records would be added to the **BANK_TRANSACTIONS** table as below. Highlighted records are the new ones.

  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-newtrans.png
      :alt: CDC Tutorials
      :width: 70%
	  
Click on the **Execute** Button on the workflow to fetch new transactions as below.
	  
	.. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-newtransfetched.png
		  :alt: CDC Tutorials
		  :width: 70%
	  
**CDC Tab** on the Project Dashboard would be updated as below. **End Value** would get updated as the max **Key Column (Transaction_Datetime)** value. **Start Value** would display the previous fetched max value.
	  
	.. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-endvalnewtrans.png
		  :alt: CDC Tutorials
		  :width: 70%
		  
New Transactions would get merged to the Delta File at the location as below.
	  
	 .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-mergednewtrans.png
		  :alt: CDC Tutorials
		  :width: 70%

Handling Updated Transactions
^^^^^^^^^^^^^^^^^^^^^^^^

During the course of time some of the transactions would get updated in the **BANK_TRANSACTIONS** table as below. Highlighted record is the one which has been updated i.e. Amount and Balance_Change values have been changed from 250 to 500. Transaction_Datetime would get updated to the Update Timestamp value.

  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-updtrans.png
      :alt: CDC Tutorials
      :width: 70%
	  
Click on the **Execute** Button on the workflow to fetch the updated transaction as below.
	  
	.. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-updtransfetched.png
		  :alt: CDC Tutorials
		  :width: 70%
	  
**CDC Tab** on the Project Dashboard would be updated as below. **End Value** would get updated as the max **Key Column (Transaction_Datetime)** value i.e. as per the Updated Timestamp value. **Start Value** would display the previous fetched max value.
	  
	.. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-endvalupdtrans.png
		  :alt: CDC Tutorials
		  :width: 70%
		  
Updated Transaction would get merged to the Delta File at the location as below.
	  
	.. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-mergedupdtrans.png
		  :alt: CDC Tutorials
		  :width: 70%

Handling Deleted Transactions
^^^^^^^^^^^^^^^^^^^^^^^^

**BANK_TRANSACTIONS** table contains a column **IS_DELETED**. It gets upddated to **Y** whenever any transaction is deleted at the source else it would be updated as **N** by default. 

Suppose a transaction at the source gets deleted and flag gets updated as below. Transaction_Datetime would get updated to the Update Timestamp value reflecting the deleted timestamp value.

  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-deltrans.png
      :alt: CDC Tutorials
      :width: 70%
	  
**DeltaMerge** node need to be configured to handled deleted transactions as below.
	  
	.. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-deltransconfig.png
		  :alt: CDC Tutorials
		  :width: 70%
	  
Click on the **Execute** Button on the workflow to handle deleted transaction as below.
	  
	.. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-deltransfetched.png
		  :alt: CDC Tutorials
		  :width: 70%
	  
**CDC Tab** on the Project Dashboard would be updated as below. **End Value** would get updated as the max **Key Column (Transaction_Datetime)** value i.e. as per the Deleted Timestamp value. **Start Value** would display the previous fetched max value.
	  
	.. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-endvaldeltrans.png
		  :alt: CDC Tutorials
		  :width: 70%
		  
Deleted Transaction would get merged to the Delta File at the location as below. **IS_DELETED** flag would get updated for the deleted transaction.
	  
	.. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-mergeddeltrans.png
		  :alt: CDC Tutorials
		  :width: 70%
