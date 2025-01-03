Read JDBC - Reading Large Dataset
=================================

.. contents::
   :depth: 3

Read JDBC Overview
-------------------

**Read JDBC** node can be used to read data from the connected JDBC source such as Oracle, Postgres, MySql and so on.

If Database Table contains huge amount of data to be read then performance optimization would be of utmost importance. Read JDBC node can be configured to read and save data in multiple to gain performance benefit. 

Reading Large Dataset Tutorials
-------------------

This tutorial will guide you on how to use **Read JDBC** node in Sparkflows to read large amount of data.

This tutorial covers the steps for configuring **Read JDBC** node and saving the partitioned data.

Oracle Datasource - Partition on Timestamp column
^^^^^^^^^^^^^^^^^^^^^^^^

This section of the Tutorials uses a **Timestamp** column of **Oracle Database Table** to **Partition** the data to get performance benefit.

Data Source: Bank Transactions Oracle Table
++++++++++

* This tutorial uses **Bank Transactions Database Table** from an Oracle database. 
* The table schema includes essential columns like Transaction_ID, Account_ID, Transaction_Type, Amount, Balance_Change, Status, Transaction_Datetime, and Is_Deleted, as shown below.
* **Transaction_Datetime** Timestamp column would be used to Partition the data.
   
  .. figure:: ../../_assets/tutorials/readjdbclds/largeds-banktrans-table.png
     :alt: ReadJDBC Tutorials
     :width: 70%

Workflow
++++++++++

* Create a workflow as below to read the data from the Oracle Table and save it to the Filesystem.
* In this Tutorials we have considered to save data in csv format; however, save the data in the format of your choice.

  .. figure:: ../../_assets/tutorials/readjdbclds/largeds-ts-workflow.png
     :alt: ReadJDBC Tutorials
     :width: 70%


Read JDBC Node Configuration
++++++++++

* Configure **Read JDBC** node as below to read data and create partition.

**1. General Tab**

  .. figure:: ../../_assets/tutorials/readjdbclds/largeds-ts-readjdbc-1.png
     :alt: ReadJDBC Tutorials
     :width: 70%

* Select the **Oracle Database Connection** in **Connection** dropdown.
* Enter the Database Table name i.e. **SPARKFLOWS.BANK_TRANSACTIONS** in the **DB Table** field.

**2. Schema Tab**

  .. figure:: ../../_assets/tutorials/readjdbclds/largeds-ts-readjdbc-2.png
     :alt: ReadJDBC Tutorials
     :width: 70%

* Click on **Refresh Schema** button. It would fetch and list the schema details of the selected table i.e. **SPARKFLOWS.BANK_TRANSACTIONS**.

**3. Properties Tab**

  .. figure:: ../../_assets/tutorials/readjdbclds/largeds-ts-readjdbc-3.png
     :alt: ReadJDBC Tutorials
     :width: 70%

* **Fetch Size:** This governs the size of data to fetched in each round. Enter a value of **1000**
* **Query Timeout:** Enter a value of **3600** so that connection would be invalidated after 1 hour if response is not received.
* **Session Init Statement:** Enter a value as below. This statement would be executed after session has started and before fetching the data. This handles the Oracle Date format. In this Tutorials we are using a Timestamp column for partition; hence, it is needed only for Oracle Database.

	::
	
		ALTER SESSION SET NLS_TIMESTAMP_FORMAT = 'YYYY-MM-DD HH24:MI:SS.FF'

**4. Performance Tab**

  .. figure:: ../../_assets/tutorials/readjdbclds/largeds-ts-readjdbc-4.png
     :alt: ReadJDBC Tutorials
     :width: 70%

* **Partition Column:** Enter **TRANSACTION_DATETIME** in the field i.e. it would be used to partition the data.
* **Lower Bound:** Enter **2025-01-02 18:15:03.656** in the field. Enter this value as per the data values.
* **Upper Bound:** Enter **2025-01-02 19:26:28.952** in the field. Enter this value as per the data values. **Lower Bound** and **Upper Bound** would govern the partition size. They don't filter the data.
* **Num Partitions:** Enter **8** i.e. instructing to create 8 Paritions of data.

**Extra Options Tab can be left blank. Click on Okay Button to save the changes.**

Workflow Execution
++++++++++

* Click on the **Execute** button to execute the workflow.
* On successful execution it would read data from the source database table and save it in **Partitions**.
