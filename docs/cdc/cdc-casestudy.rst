CDC - Case Study
======================
Sparkflows supports the incremental loading of changes in relational tables through workflows and the summary page.

This document outlines the **Change Data Capture (CDC) - Case Studies** using the **AutoIncrement** and **DeltaMerge** Nodes in Sparkflows.

Case Study-Initial Load
----------------------------------------------

1. Table Creation
----------------------------------------------

* a. Create a **EMPLOYEE_MASTER** Oracle table as below:

.. figure:: ../_assets/cdc/cdc-cs-createtable.png
   :alt: cdc
   :width: 60%

* b. Add following rows to the table:

.. figure:: ../_assets/cdc/cdc-cs-addrows.png
   :alt: cdc
   :width: 60%

2. Workflow creation and execution
----------------------------------------------

* a. Create a workflow as below:

.. figure:: ../_assets/cdc/cdc-cs-workflow.png
   :alt: cdc
   :width: 60%

* b. Configure Autoincrement node as below:

.. figure:: ../_assets/cdc/cdc-cs-autoinc.png
   :alt: cdc
   :width: 60%

* c. Configure DeltaMerge node as below:

.. figure:: ../_assets/cdc/cdc-cs-deltamerge.png
   :alt: cdc
   :width: 60%

3. With this configuration execute the workflow and output would be as followings:
----------------------------------------------

* a. Print Node

.. figure:: ../_assets/cdc/cdc-cs-printop.png
   :alt: cdc
   :width: 60%

* b. CDC Tab displaying the End Value

.. figure:: ../_assets/cdc/cdc-cs-cdcop.png
   :alt: cdc
   :width: 60%
   
* c. Entire data from the dataset would get merged to the Targetpath as a part of Initial Load. Data from the TargetPath is as below

.. figure:: ../_assets/cdc/cdc-cs-mergeop.png
   :alt: cdc
   :width: 60%

Case Study-New Row Merge
----------------------------------------------

1. New Row Addition
----------------------------------------------

* a. Add a new rows to EMPLOYEE_MASTER Oracle table as below:

.. figure:: ../_assets/cdc/cdc-cs1-newrows.png
   :alt: cdc
   :width: 60%

2. Workflow execution
----------------------------------------------

* a. Execute the CDC workflow that was created earlier

.. figure:: ../_assets/cdc/cdc-cs-workflow.png
   :alt: cdc
   :width: 60%

3. With this configuration execute the workflow and output would be as followings:
----------------------------------------------

* a. Print Node

Two newly added rows would be printed by the Print Node

.. figure:: ../_assets/cdc/cdc-cs1-printop.png
   :alt: cdc
   :width: 60%

* b. CDC Tab displaying the Start Value as per the last fetch Update_Timestamp value and End Value as per the latest Max Updae_Timestamp

.. figure:: ../_assets/cdc/cdc-cs1-cdcop.png
   :alt: cdc
   :width: 60%
   
* c. New rows added to the Table got merged to the Targetpath. Data from the TargetPath is as below

.. figure:: ../_assets/cdc/cdc-cs1-mergeop.png
   :alt: cdc
   :width: 60%

Case Study-Update Data Merge
----------------------------------------------

1. Update Data
----------------------------------------------

* a. Update Data in EMPLOYEE_MASTER Oracle table as below:

Salary and Update_Timestamp has been updated for Employee_ID = 4

.. figure:: ../_assets/cdc/cdc-cs2-update.png
   :alt: cdc
   :width: 60%

2. Workflow execution
----------------------------------------------

* a. Execute the CDC workflow that was created earlier

.. figure:: ../_assets/cdc/cdc-cs-workflow.png
   :alt: cdc
   :width: 60%

3. With this configuration execute the workflow and output would be as followings:
----------------------------------------------

* a. Print Node

Updated row would be printed by the Print node based on the update in the Update_Timestamp column (which is the CDC column in Autoincrement node)

.. figure:: ../_assets/cdc/cdc-cs2-printop.png
   :alt: cdc
   :width: 60%

* b. CDC Tab displaying the Start Value as per the last fetch Update_Timestamp value and End Value as per the latest Max Updae_Timestamp

.. figure:: ../_assets/cdc/cdc-cs2-cdcop.png
   :alt: cdc
   :width: 60%
   
* c. Data updates (Salary and Update_Timestamp values for the Employee_ID = 4) reflect the merged data at the Targetpath. Data from the TargetPath is as below

.. figure:: ../_assets/cdc/cdc-cs2-mergeop.png
   :alt: cdc
   :width: 60%

Case Study-Delete Data Merge
----------------------------------------------

1. Update Delete Flag Data
----------------------------------------------

* a. Update Data in EMPLOYEE_MASTER Oracle table as below:

Is_Deleted and Update_Timestamp has been updated for Employee_ID = 3. Is_Deleted flag has been set to ‘True’ marking it as deleted.

.. figure:: ../_assets/cdc/cdc-cs3-delete.png
   :alt: cdc
   :width: 60%

2. Workflow execution
----------------------------------------------

* a. Configure DeltaMerge node as below:

.. figure:: ../_assets/cdc/cdc-cs3-deltamerge.png
   :alt: cdc
   :width: 60%
   
.. figure:: ../_assets/cdc/cdc-cs3-deltamerge1.png
   :alt: cdc
   :width: 60%
   
.. figure:: ../_assets/cdc/cdc-cs3-deltamerge2.png
   :alt: cdc
   :width: 60%

* b. Execute the CDC workflow that was created earlier

.. figure:: ../_assets/cdc/cdc-cs-workflow.png
   :alt: cdc
   :width: 60%

3. With this configuration execute the workflow and output would be as followings:
----------------------------------------------

* a. Print Node

Updated row would be printed by the Print node based on the update in the Update_Timestamp column (which is the CDC column in Autoincrement node). Deleted row would be printed.

.. figure:: ../_assets/cdc/cdc-cs3-printop.png
   :alt: cdc
   :width: 60%

* b. CDC Tab displaying the Start Value as per the last fetch Update_Timestamp value and End Value as per the latest Max Updae_Timestamp

.. figure:: ../_assets/cdc/cdc-cs3-cdcop.png
   :alt: cdc
   :width: 60%
   
* c. Row that was marked as deleted (Employee_ID = 3) has been removed from the Targetpath after merge. Data from the TargetPath is as below

.. figure:: ../_assets/cdc/cdc-cs3-mergeop.png
   :alt: cdc
   :width: 60%
