CDC Tutorials - Employee Master (Using Index Column)
=================================

.. contents::
   :depth: 3

CDC Overview
-------------------

**CDC (Change Data Capture)** is used to identify and track changes in a connected data table, including data insertions, updates, and deletions. 

It facilitates efficient incremental data loading and ensures seamless integration of these changes into the dataset. 

CDC (Change Data Capture) Tutorials
-------------------

This tutorial will guide you on how to use Sparkflows CDC to capture changes in employee master data stored in an Postgres Database. The **AutoIncrement node** in Sparkflows is utilized for tracking these changes. It is configured to track changes based on the new Index Column data (Employee_ID).

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

Data Source: Employee Master Postgres Table
^^^^^^^^^^^^^^^^^^^^^^^^

* This tutorial uses **Employee Master Database Table** from an Postgres database to capture changes. 
* The table schema includes essential columns like Employee_ID, First_Name, Last_Name, Department, Salary, Join_Date, Update_Timestamp,  and IS_DELETED, as shown below.
   
  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-empmaster-table.png
     :alt: CDC Tutorials
     :width: 70%

CDC Workflow
^^^^^^^^^^^^^^^^^^^^^^^^

* Create a CDC Workflow using the **AutoIncrement** and **DeltaMerge nodes**.

  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-id-workflow.png
      :alt: CDC Tutorials
      :width: 70%

AutoIncrement Node Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

* The **AutoIncrement Node** needs to be configured as shown below. It will be used to capture changes in the data based on the values in the **Key Column**.

  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-id-autoincrement.png
      :alt: CDC Tutorials
      :width: 70%

* To configure the **AutoIncrement Node**, enter appropriate values in the required fields as follows and click the **Okay** button.
	  
  **Connection:** Select the **Postgres Connection** from the dropdown.

  **Database Name:** Enter the Database name.

  **Table Name:** Specify the Database Table name(**Employee_Master**).

  **Key Column Name:** Enter the name of the column that will be used to capture changes(**Employee_ID**).

  **Key Column Type:** Select the datatype of the Key Column from the dropdown(**Index**).

  **Key Column Format:** It can be left blank.
	  
DeltaMerge Node Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

* **DeltaMerge Node** needs to be configured as shown below. It will be used to merge changes from the source data to the target location in Delta format.

  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-id-deltamerge.png
      :alt: CDC Tutorials
      :width: 70%

* To configure the **DeltaMerge Node**, enter appropriate values in the required fields as follows and click the **Okay** button.
	  
  **TargetPath:** Provide the Delta file path for merging changes.

  **Source Alias:** Enter an alias for the Source Dataset. It will be used in the joining conditions.

  **Target Alias:** Enter an alias for the Target Dataset. It will be used in the joining conditions.

  **Merge Condition:** Enter the condition **source.employee_id = target.employee_id** to join Source and Target datasets.
	  
Execute Workflow
^^^^^^^^^^^^^^^^^^^^^^^^

* Click the **Execute** Button on the workflow to execute it. It will perform **Initial Loading** of data from the Source (EMPLOYEE_MASTER database table) and merge it into the Target Location. 

* The output of the execution will be displayed as shown below. It will merge all the records during the first run i.e. Initial Loading.

  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-id-initload.png
      :alt: CDC Tutorials
      :width: 70%
	  
* **CDC Tab** on the Project Dashboard will be updated as shown below. It will update the **End Value** as the max **Key Column (Employee_ID)** value.
	  
  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-id-endvalinitload.png
     :alt: CDC Tutorials
     :width: 70%
	  	  
Handling New Employees
^^^^^^^^^^^^^^^^^^^^^^^^

* Over time new employees will be added to the **EMPLOYEE_MASTER** table, as shown below. The highlighted records represent the new ones.

  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-id-newtrans.png
      :alt: CDC Tutorials
      :width: 70%
	  
* Click the **Execute** Button on the workflow to fetch new employees, as shown below.
	  
  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-id-newtransfetched.png
     :alt: CDC Tutorials
     :width: 70%
	  
* The **CDC Tab** on the Project Dashboard will be updated as shown below. It will update the **End Value** as the max **Key Column (Employee_ID)** value. The **Start Value** will display the previously fetched max value.
	  
  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-id-endvalnewtrans.png
     :alt: CDC Tutorials
     :width: 70%
		  
* New Employee will be merged into the Delta File at the location shown below.
	  
  .. figure:: ../../_assets/tutorials/cdc/cdc-tutorials-id-mergednewtrans.png
     :alt: CDC Tutorials
     :width: 70%
