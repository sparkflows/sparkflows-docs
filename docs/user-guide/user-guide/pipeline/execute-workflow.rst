Execute Workflow
================

Fire Insights provides a node using which another workflow can be executed.

Using this node enables creating a dag of workflows.

Overview
--------

The `Execute Worklow` node sends a message to Fire Insights to execute a specific workflow. The workflow has to be within the same project. The workflow gets executes with the user who execute the original workflow, you can pass even some workflow parameters too.

Below are the steps on how to Execute a specific workflow in Fire Insights.

Create Workflow
--------------------

Click on 'Create New Workflow' and search 'Execute Workflow' Node in Left pane and drag to editor.

Add below parameters in 'Execute Workflow' Node.

.. list-table:: 
   :widths: 10 20 
   :header-rows: 1

   * - Title
     - Value
   * - WORKFLOW
     - The workflow to execute
   * - isEnabled
     - isEnabled true execute the selected workflow
   * - KEY VALUE ARRAY
     - PARAMETER NAME and PARAMETER VALUE if want to pass workflow parameters

.. figure:: ../../../_assets/user-guide/wfe_node/wfe_node.PNG 
   :alt: Execute Workflow
   :width: 80%



