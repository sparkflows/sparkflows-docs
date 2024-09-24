
CDC with AutoIncrement Node
======================
Sparkflows supports the incremental loading of changes in relational tables through workflows and the summary page.

This document outlines steps to set up Change Data Capture (CDC) using the AutoIncrement Node in Sparkflows.

Step 1 : Enable CDC in the Module Configuration
----------------------------------------------

#. Navigate to **Administration -> Configurations -> Module**.
#. Enable the CDC (Change Data Capture) module.

Once enabled, the CDC module will appear in each project, allowing you to track incremental data pulls.

.. figure:: ../_assets/cdc/cdc-page-in-project.png
   :alt: cdc
   :width: 60%

Step 2 : Create a Workflow with AutoIncrement Node
-------------------------------------------------
#. Start by creating a new workflow.
#. Add the **AutoIncrement Node** to the workflow.
#. Configure the connection details by selecting your database (e.g., MySQL, PostgreSQL, Oracle).
   
   Provide the following information:

   * Database Name
   * Table Name
   * Key Column Name (the column that identifies unique rows)
   * Key Column Type (Currently, only timestamp and index key types are supported)


   .. figure:: ../_assets/cdc/node-configuration.png
      :alt: cdc
      :width: 60%

Step 3 : Run the Workflow
--------------------------

#. Execute the workflow after configuration. After the first run, the CDC Summary Page will display details of the initial data pull

   .. figure:: ../_assets/cdc/after-first-run.png
      :alt: cdc
      :width: 60%

Step 4 : View Summary After Subsequent Runs
-----------------------------------------------

#. After executing the workflow for a second time, the summary page will display details of the incremental data pulled during the second run.

   .. figure:: ../_assets/cdc/after-second-run.png
      :alt: cdc
      :width: 60%

Step 5 : Save and Merge Incremental Changes
-------------------------------------------
#. The workflow reads the incremental changes from the relational source and saves them to your preferred file system. You can later merge these incremental changes with the original data to perform updates, deletions, and insertions as required.

   .. figure:: ../_assets/cdc/auto-increment-wf.png
      :alt: cdc
      :width: 60%

