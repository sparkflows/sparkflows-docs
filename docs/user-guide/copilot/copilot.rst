Copilot
====

This document outlines how to configure, use, and manage Copilot in Sparkflows to create workflows, projects, and queries using Natural Language capabilities.

Prerequisites
-----------

1. Ensure that the configuration setting **module.enableCopilot** is enabled to access Copilot.

  .. figure:: ../../_assets/user-guide/copilot/copilot_configuration.png
     :alt: copilot configuration
     :width: 60%

2. Gen AI connection is required for making queries.

Add Copilot
-----------
1. After logging into Fire Insights, navigate to **Administration -> Copilot**.

  .. figure:: ../../_assets/user-guide/copilot/copilot_administration.png
    :alt: copilot_administration
    :width: 60%

2. Click on **Add Copilot** button and enter details such as the Copilot Name and Gen AI Connection required for making queries. Then click on **Save** button.

  .. figure:: ../../_assets/user-guide/copilot/create_copilot.png
    :alt: create_copilot
    :width: 60%

3. Once created, you can **update** the Copilot details by clicking the **Edit Details** icon (pen icon) in **Actions** column in the table.

  .. figure:: ../../_assets/user-guide/copilot/update_copilot.png
    :alt: update_copilot
    :width: 60%

Copilot on Workflow
-----------

1. Once the Copilot is created, you can use it in the workflow designer by clicking the **Copilot button**.

  .. figure:: ../../_assets/user-guide/copilot/wf-copilot-btn.png
      :alt: copilot_workflow
      :width: 60%

  .. figure:: ../../_assets/user-guide/copilot/copilot_workflow.png
    :alt: copilot_workflow
    :width: 60%

2. Once the workflow is generated based on your query, you can move it to the main designer using the **Select** option.

  .. figure:: ../../_assets/user-guide/copilot/wf_copilot_move_to_editor.png
    :alt: copilot_move_to_editor
    :width: 60%

 .. figure:: ../../_assets/user-guide/copilot/wf_copilot_after_click_select.png
    :alt: copilot_move_to_editor
    :width: 60%

Copilot on Pipeline
-----------

1. Once the Copilot is created, you can use it in the pipeline designer by clicking the **Copilot button**.

  .. figure:: ../../_assets/user-guide/copilot/pipeline-copilot-btn.png
      :alt: copilot_workflow
      :width: 60%

  .. figure:: ../../_assets/user-guide/copilot/copilot_pipeline.png
    :alt: copilot_workflow
    :width: 60%

2. Once the pipeline is generated based on your query, you can move it to the main designer using the **Select** option.

  .. figure:: ../../_assets/user-guide/copilot/pipeline_copilot_move_to_editor.png
    :alt: copilot_move_to_editor
    :width: 60%

 .. figure:: ../../_assets/user-guide/copilot/pipeline_copilot_after_click_select.png
    :alt: copilot_move_to_editor
    :width: 60%


Copilot on Nodes
---------------

1. By double-clicking a node, you can access the Copilot for easy Natural Language Query (NLQ) writing. For example, in the image below, a prompt is provided and the Copilot generated the appropriate query.

  .. figure:: ../../_assets/user-guide/copilot/copilot_nodes.png
    :alt: copilot_nodes
    :width: 60%

Copilot on Project
------------------

1. Fire Insights allows you to create projects using Natural Language Queries (NLQ) with the help of Copilot.

  .. figure:: ../../_assets/user-guide/copilot/copilot_project.png
    :alt: copilot_project
    :width: 60%

2. On clicking **Create Using Natural Language** option, a popup will appear for creating a project.

  .. figure:: ../../_assets/user-guide/copilot/copilot_project_create.png
    :alt: copilot_project_create
    :width: 60%

  The **project description** will be used as the prompt for creating the project. 
 
  The **Data Directory Location** specifies where all data files for datasets will be stored, and the selected Copilot will be used to perform queries.

3. Once you click **Submit**, Copilot will create a project along with a set of datasets and workflows based on your description.

  .. figure:: ../../_assets/user-guide/copilot/copilot_dataset_created.png
    :alt: copilot_dataset_created
    :width: 60%

  .. figure:: ../../_assets/user-guide/copilot/copilot_workflow_created.png
    :alt: copilot_workflow_created
    :width: 60%







