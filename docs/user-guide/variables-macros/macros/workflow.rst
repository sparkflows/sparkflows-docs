Macros in Workflows
==================
cros in Workflows
==================

**Macros** are runtime variables that can be accessed by the Sparkflows workflows. They can be defined in the format such as **${fire.ds}** to access **Current Date** value or they can defined as an expression i.e. **${fire.macros.ts_add(ts, days)}** to add number of days to the **Current Timestamp** value. They are evaluated during the runtime. 

They can be used in Sparkflows nodes such as **Add Columns**, **Read CSV** & other read nodes, **Save** Nodes, **Expression** Nodes, **Filter** Nodes and so on.

Some of the scenarios where they can be used are listed below:

* Adding Workflow Executor Username, Workflow ID, Datetime Values, Pipeline Executor details.
* Reading data from files created for past dates. In this scenarios files are either saved in Date-Valued folders or files have date parts. Expression **${fire.macros.ts_add(ts, days)}** can be used to get past days and can be used to read specific files.
* To get Date Part values at runtime.
* They can also be used as workflow parameters.
* To filter data in SQL Node.

Some of the macros that can be used in Sparkflows are listed below:

@@ -30,14 +28,6 @@ Macros that Sparkflows supports
     - Returns the Current execution date as YYYYmmDD
   * - ${fire.ts}
     - Returns the Current execution Timestamp as YYYY-mm-DD HH-MM-SS
   * - ${fire.wf.name}
     - Returns the Current Workflow Name, e.g. (01-Read-Macros)
   * - ${fire.wf.id}
     - Returns the Current Workflow ID, e.g. 631
   * - ${fire.wfe.id}
     - Returns the Current Workflow Execution ID, e.g. 362
   * - ${fire.wfe.username}
     - Returns the Username by whom the workflow has been executed, e.g. admin
   * - ${fire.pl.name}
     - Returns the Current Pipeline Name, e.g. EndToEnd_Pipeline
   * - ${fire.pl.id}
@@ -187,212 +177,85 @@ Macros related to Timestamp
     - 2024-11-19 14:19:44, s,YYYY-mm-DD HH-MM-SS,-1
     - 2024-11-19 14:19:43

Usage of Macros in the Workflow Node
++++++++++++++++++++++++++++++++++++

.. figure:: ../../../_assets/user-guide/variables-macros/node.png
   :alt: macros
   :width: 60%


Usage of Macros on the Workflow Execution Page
+++++++++++++++++++++++++++++++++++++++++++++
.. figure:: ../../../_assets/user-guide/variables-macros/execution.png
   :alt: macros
   :width: 60%


Usage of Macros in Add Columns Advanced Node to fetch Current Date and Time values
+++++++++++++++++++++++++++++++++++++++++++++
.. figure:: ../../../_assets/user-guide/variables-macros/macros_addcols_node_1.png
   :alt: macros
   :width: 60%

It would add new columns with Date and Time values as below:

.. figure:: ../../../_assets/user-guide/variables-macros/macros_addcols_node_1_op.png
   :alt: macros
   :width: 60%


Usage of Macros to extract Date parts
+++++++++++++++++++++++++++++++++++++++++++++
.. figure:: ../../../_assets/user-guide/variables-macros/macros_addcols_node_2.png
   :alt: macros
   :width: 60%

It would add new columns with Date and Time values as below:

.. figure:: ../../../_assets/user-guide/variables-macros/macros_addcols_node_2_op.png
   :alt: macros
   :width: 60%

.. list-table:: 
   :widths: 50 50
   :header-rows: 1

   * - Value
     - Macro
   * - Current Year
     - ${fire.macros.ds_format(ds,y, YYYY,0)}
   * - Previous Year
     - ${fire.macros.ds_format(ds,y, YYYY,-1)}
   * - Next Year
     - ${fire.macros.ds_format(ds,y, YYYY,1)}
   * - Current Month
     - ${fire.macros.ds_format(ds,m, MM,0)}
   * - Current Day
     - ${fire.macros.ds_format(ds,d, DD,0)}
   * - Current Date in DD-MM-YYYY format
     - ${fire.macros.ds_format(ds,d, DD-MM-YYYY,0)}
   * - Current Date in DD-MMM-YYYY format
     - ${fire.macros.ds_format(ds,d, DD-MMM-YYYY,0)}

Usage of Macros to extract Time parts
+++++++++++++++++++++++++++++++++++++++++++++
.. figure:: ../../../_assets/user-guide/variables-macros/macros_addcols_node_3.png
   :alt: macros
   :width: 60%

It would add new columns with Date and Time values as below:

.. figure:: ../../../_assets/user-guide/variables-macros/macros_addcols_node_3_op.png
   :alt: macros
   :width: 40%

.. list-table:: 
   :widths: 50 50
   :header-rows: 1

   * - Value
     - Macro
   * - Full Timestamp
     - ${fire.macros.ts_format(ts,y, YYYY-mm-DD HH-MM-SS,0)}
   * - Current Hour
     - ${fire.macros.ts_format(ts,d, HH,0)}

Usage of Macros to add Workflow and Pipeline details to dataframe
+++++++++++++++++++++++++++++++++++++++++++++
.. figure:: ../../../_assets/user-guide/variables-macros/macros_addcols_node_4.png
   :alt: macros
   :width: 60%

It would add new columns with Workflow values as below:

.. figure:: ../../../_assets/user-guide/variables-macros/macros_addcols_node_4_op.png
   :alt: macros
   :width: 60%

It would add new columns with Pipeline values as below. Pipeline values would be added only when workflow is triggered from a pipeline:

.. figure:: ../../../_assets/user-guide/variables-macros/macros_addcols_node_4_op1.png
   :alt: macros
   :width: 60%

Usage of Macros in Workflow Parameter
+++++++++++++++++++++++++++++++++++++++++++++
.. figure:: ../../../_assets/user-guide/variables-macros/macros_addcols_node_5.png
   :alt: macros
   :width: 60%

Above Parameter can be used in Add Columns Advanced node as below:

.. figure:: ../../../_assets/user-guide/variables-macros/macros_addcols_node_5_1.png
   :alt: macros
   :width: 60%

It would add new columns as below:

.. figure:: ../../../_assets/user-guide/variables-macros/macros_addcols_node_5_op.png
   :alt: macros
   :width: 60%


Usage of Macros in Read CSV Node to read data from Date Folders
+++++++++++++++++++++++++++++++++++++++++++++

If **Datafiles** are placed in **Date Folders** as below

.. figure:: ../../../_assets/user-guide/variables-macros/macros_addcols_node_6.png
   :alt: macros
   :width: 60%

.. figure:: ../../../_assets/user-guide/variables-macros/macros_addcols_node_6_1.png
   :alt: macros
   :width: 60%

If suppose **Current Date** is **29-Nov-2024** and data needs to be read for **26-Nov-2024** then **Read CSV** Node needs to be configured as below:

.. figure:: ../../../_assets/user-guide/variables-macros/macros_addcols_node_6_2.png
   :alt: macros
   :width: 60%

Path in the **Read CSV** needs to be set as below:

::

   s3a://sparkflows/TestMacros/input-data-datefolder/${fire.macros.ds_format(ds,d, DD,-3)}-${fire.macros.ds_format(ds,m, MMM,0)}-${fire.macros.ds_format(ds,y, YYYY,0)}/

It would fetch data from the **26-Nov-2024** folder as below:

.. figure:: ../../../_assets/user-guide/variables-macros/macros_addcols_node_6_3.png
   :alt: macros
   :width: 60%

Usage of Macros in Read CSV Node to read data from Date Files
+++++++++++++++++++++++++++++++++++++++++++++

If **Datafiles** are placed in the same folder and files have **Date Part** in the name as below

.. figure:: ../../../_assets/user-guide/variables-macros/macros_addcols_node_7.png
   :alt: macros
   :width: 60%

If suppose **Current Date** is **29-Nov-2024** and data needs to be read for **27-Nov-2024** then **Read CSV** Node needs to be configured as below:

.. figure:: ../../../_assets/user-guide/variables-macros/macros_addcols_node_7_1.png
   :alt: macros
   :width: 60%

Path in the **Read CSV** needs to be set as below:

::

   s3a://sparkflows/TestMacros/input-data-datefiles/bank-trans-${fire.macros.ds_format(ds,d, DD,-2)}-${fire.macros.ds_format(ds,m, MMM,0)}-${fire.macros.ds_format(ds,y, YYYY,0)}.csv

It would fetch data from the **27-Nov-2024** file as below:

.. figure:: ../../../_assets/user-guide/variables-macros/macros_addcols_node_7_2.png
   :alt: macros
   :width: 60%

Usage of Macros in Read JDBC Node
+++++++++++++++++++++++++++++++++++++++++++++

While reading data from a **Oracle Database Table** if data needs to be read using certain condition then **Macro** can be used as below:
In this scenario we are trying to fetch employees who joined in last one year. Assuming **Current Date** is **29-Nov-2024**.

Define a **Workflow Parameter** as below:

.. figure:: ../../../_assets/user-guide/variables-macros/macros_addcols_node_8.png
   :alt: macros
   :width: 60%

Parameter needs to be defined as below:

::

   '${fire.macros.ds_add(ds, -365)}'

**Read JDBC** Node needs to be configured as below:

.. figure:: ../../../_assets/user-guide/variables-macros/macros_addcols_node_8_1.png
   :alt: macros
   :width: 60%

It would fetch employees who joined in last one year as below:

.. figure:: ../../../_assets/user-guide/variables-macros/macros_addcols_node_8_2.png
   :alt: macros
   :width: 60%


