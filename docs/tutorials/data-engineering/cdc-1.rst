CDC With AutoIncrement Node
======================
Sparkflows provide the support for incremental load of changes in relation table with workflow and summary page.

Once CDC is enabled in Administration -> Configurations -> Module tab, in each project CDC module is visible where details of the incremental data pull is captured.

.. figure:: ../../_assets/tutorials/cdc/cdc-page-in-project.png
   :alt: cdc
   :width: 60%

Create the workflow with **AutoIncrement Node** by selecting the connection to mysql, postgress, oracle, etc. and configure the database, table, keycolumn name & key column type.

Currently key column type **timestamp** and **index** only supported.

.. figure:: ../../_assets/tutorials/cdc/node-configuration.png
   :alt: cdc
   :width: 60%

CDC summary page after the first execution of the workflow with above configuration.

.. figure:: ../../_assets/tutorials/cdc/after-first-run.png
   :alt: cdc
   :width: 60%

After the second run summary page details.

.. figure:: ../../_assets/tutorials/cdc/after-second-run.png
   :alt: cdc
   :width: 60%

Workflow:

Read the incremental changes from relation source and save it any file system. Later merge the incremental changes with original data (Update, Delete and Insert).

.. figure:: ../../_assets/tutorials/cdc/auto-increment-wf.png
   :alt: cdc
   :width: 60%




