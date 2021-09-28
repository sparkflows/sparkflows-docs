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
     - Select the workflow to execute
   * - isEnabled
     - isEnabled true to execute the selected workflow
   * - KEY VALUE ARRAY
     - PARAMETER NAME and PARAMETER VALUE if want to pass workflow parameters

.. figure:: ../../../_assets/user-guide/wfe_node/wfe_node.PNG 
   :alt: Execute Workflow
   :width: 80%

Execute Workflow
------------

Once the above workflow got configured with needed details, you can Execute the workflow now.

when it will be executed, you will see in workflow execution page the workflow selected in Execute Workflow Node is also executed and you can see their result etc.

.. figure:: ../../../_assets/user-guide/wfe_node/wf_triggered.PNG 
   :alt: Execute Workflow
   :width: 80%
 
 Results after passing workflow parameters
 
.. figure:: ../../../_assets/user-guide/wfe_node/parameter.PNG 
   :alt: Execute Workflow
   :width: 80%   

