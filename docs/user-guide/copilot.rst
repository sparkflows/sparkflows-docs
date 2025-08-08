Copilot
====
Prerequisites
-----------

1. Ensure that the configuration setting **module.enableCopilot** is enabled to access Copilot.

  .. figure:: ../_assets/user-guide/copilot/copilot_configuration.png
     :alt: copilot configuration
     :width: 60%
2. Gen AI connection required for making queries.

Add Copilot
-----------
1. After logging into Fire Insights, navigate to **Administration -> Copilot**.

  .. figure:: ../_assets/user-guide/copilot/copilot_administration.png
    :alt: copilot_administration
    :width: 60%

2. Click on **Add Copilot** button and enter details such as the Copilot name and Gen AI connection required for making queries.

  .. figure:: ../_assets/user-guide/copilot/create_copilot.png
    :alt: create_copilot
    :width: 60%

3. Once created, the user can update the Copilot details by clicking the pen icon in the table.

  .. figure:: ../_assets/user-guide/copilot/update_copilot.png
    :alt: update_copilot
    :width: 60%

Copilot on Workflow
-----------

1. Once the Copilot is created, the user can use it in the workflow designer by clicking the Copilot icon.

  .. figure:: ../_assets/user-guide/copilot/copilot_workflow.png
    :alt: copilot_workflow
    :width: 60%

2. Once the workflow is generated based on the user query, the user can move it to the main designer using the **Move to Editor** option.

  .. figure:: ../_assets/user-guide/copilot/copilot_move_to_editor.png
    :alt: copilot_move_to_editor
    :width: 60%

Copilot on Nodes
---------------

1. By double-clicking on a node, the user can access the Copilot for easy Natural Language Query (NLQ) writing. For example, in the image below, the user provided a prompt and the Copilot generated the appropriate query.

  .. figure:: ../_assets/user-guide/copilot/copilot_nodes.png
    :alt: copilot_nodes
    :width: 60%

Copilot on Project
------------------

1. Fire Insights allows users to create projects using Natural Language Queries (NLQ) with the help of Copilot.

  .. figure:: ../_assets/user-guide/copilot/copilot_project.png
    :alt: copilot_project
    :width: 60%

2. When the Create Using Natural Language button is clicked, a popup will appear for creating a project.

  .. figure:: ../_assets/user-guide/copilot/copilot_project_create.png
    :alt: copilot_project_create
    :width: 60%

  The project description will be used as the prompt for creating the project. 
  The data directory location specifies where all data files for datasets will be stored, and the selected Copilot will be used to perform queries.

3. Once the user clicks Save, Copilot will create a project along with a set of datasets and workflows based on the description provided by the user.

  .. figure:: ../_assets/user-guide/copilot/copilot_dataset_created.png
    :alt: copilot_dataset_created
    :width: 60%

  .. figure:: ../_assets/user-guide/copilot/copilot_workflow_created.png
    :alt: copilot_workflow_created
    :width: 60%







