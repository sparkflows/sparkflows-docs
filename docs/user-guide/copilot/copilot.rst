Add Copilot
====

This document outlines how to configure, use, and manage Copilot in Sparkflows to create workflows, projects, and queries using Natural Language capabilities.

Prerequisites
-----------

1. Ensure that the configuration setting **module.enableCopilot** is enabled to access Copilot.

   .. figure:: ../../_assets/user-guide/copilot/copilot_configuration.png
     :alt: copilot configuration
     :width: 60%

2. Gen AI connection is required for making queries.

Steps for Adding Copilot
-----------
1. After logging into Sparkflows, navigate to **Administration -> Copilot**.

   .. figure:: ../../_assets/user-guide/copilot/copilot_administration.png
    :alt: copilot_administration
    :width: 60%

2. Click on **Add Copilot** button and enter the following details. such as the Copilot Name and Gen AI Connection required for making queries. Then click on **Save** button to create the Copilot.

   .. figure:: ../../_assets/user-guide/copilot/add_copilot_button.png
    :alt: create_copilot
    :width: 60%

  * **Name (mandatory):** Enter a unique and meaningful name for the Copilot.
  * **Description (Optional):** Provide a short description of what the Copilot will be used for.
  * **Gen AI Connection (mandatory):** Select an existing Gen AI Connection (e.g., OpenAI, Azure OpenAI, Bedrock, etc.) from the dropdown. Ensure the selected connection is already configured and active.
  * **MCP Connection (Optiona):** Select one or more MCP Connections from the dropdown, if required. This is optional and depends on whether your Copilot needs MCP-based tools or integrations.



   .. figure:: ../../_assets/user-guide/copilot/create_copilot.png   
     :alt: create_copilot
     :width: 60%

3. Once the copilot is created, you can **update** the Copilot details by clicking the **Edit Details** icon (pen icon) in **Actions** column in the copilot list, as shown below.

   .. figure:: ../../_assets/user-guide/copilot/copilot_edit_details.png
    :alt: create_copilot
    :width: 60%

   .. figure:: ../../_assets/user-guide/copilot/update_copilot.png
    :alt: update_copilot
    :width: 60%








