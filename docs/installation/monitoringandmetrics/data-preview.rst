Data Preview
==============

Sparkflows provides a **Data Preview** feature that allows users to inspect data at various stages of a workflow execution.

The Data Preview feature allows users to:

- View row count
- View column count
- View sample data
- Inspect the schema

Follow the steps below to use Data Preview in a workflow:

Step 1: Enable Data Preview Options
-------------------------------------

1. In each node, users can enable one or more 'Data Preview' options and execute the workflow in **Debug Mode**.

   **Example:** In the workflow below, the **Create Dataset** and **Row Filter** nodes have the following options enabled:

  - Row count enabled
  - Column count enabled
  - Sample data preview enabled

  .. figure:: ../../_assets/installation/metrics/data-preview-options-in-nodes.png
       :alt: metrics
       :width: 60%

Step 2: Execute in Debug Mode
----------------------------

1. After enabling the required options, execute the workflow in **Debug Mode**.

2. Using these options, users can:

  - Validate row counts after transformations
  - Verify column structure changes
  - Inspect sample data for correctness
  - Confirm schema consistency

Step 3: Execution in Higher Environments
------------------------------------------

1. After validation in Debug Mode:

  - The same workflow can be promoted to higher environments (QA/Prod).
  - Debug Mode can be disabled.
  - The workflow runs without preview overhead, ensuring better performance.

Step 4: View Execution Results
------------------------------

1. Once executed in Debug Mode, the **Execution Result** page displays:

  - Row count for each enabled node
  - Column count details
  - Sample data preview
  - Schema information

  This enables users to validate data correctness at each transformation stage before final deployment.

  .. figure:: ../../_assets/installation/metrics/data-preview-node-wise-result.png
      :alt: metrics
      :width: 60%


