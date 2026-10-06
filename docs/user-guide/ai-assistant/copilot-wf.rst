AI Assistant on Workflow
========================

This section explains how to use **AI Assistant** within the **Workflow Designer** in Sparkflows.

Prerequisites
-------------

Before using AI Assistant in the Workflow Designer, ensure that an AI Assistant has already been added.

The steps for adding an AI Assistant are provided in the following document:

:doc:`/user-guide/ai-assistant/copilot`

Steps to Use AI Assistant in Workflow Designer
----------------------------------------------

1. Navigate to the **Workflows** page within any **Project**.
2. Click on the **Create** button.
3. To use AI Assistant, click on the **AI Assistant** button.

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Workflow/Copilot-Button-WF-Page.PNG
     :alt: copilot configuration
     :width: 60%



4. On clicking the AI Assistant button, the **AI Assistant** opens. The previously created AI Assistant will be selected by default in the dropdown, as shown below.

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Workflow/Copilot-WF-Assistant-Conn-Selected.PNG
     :alt: copilot configuration
     :width: 60%



5. A prompt can now be entered to create a workflow. AI Assistant generates a response based on the prompt, as shown below.

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Workflow/Copilot-WF-Generate-Response.PNG
    :alt: copilot configuration
    :width: 60%




6. Once the Workflow JSON is generated based on the submitted query, click on the **Show More** button.

   This allows you to preview the complete generated Workflow JSON.

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Workflow/Copilot-ShowMore-Preview-WF-JSON.PNG
     :alt: copilot configuration
     :width: 60%



   You can also preview the generated **Workflow**.

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Workflow/Copilot-ShowMore-Preview-Workflow.PNG
     :alt: copilot configuration
     :width: 60%


7. Clicking the **Confirm** button on the Preview Workflow popup will move the generated workflow to the **Workflow Designer**.

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Workflow/Copilot-WF-Preview-Confirm.PNG
     :alt: copilot configuration
     :width: 60%


   You can also directly preview the generated workflow by clicking the **Preview** icon seen in the AI Assistant response.

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Workflow/Copilot-WF-Direct-Preview.PNG
     :alt: copilot configuration
     :width: 60%

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Workflow/Copilot-ShowMore-Preview-Workflow.PNG
     :alt: copilot configuration
     :width: 60%



   You can also directly add the generated workflow to the Workflow Designer by clicking the **Add** icon in the response.

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Workflow/Copilot-WF-Direct-Add.PNG
     :alt: copilot configuration
     :width: 60%

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Workflow/Copilot-WF-Preview-Confirm.PNG
     :alt: copilot configuration
     :width: 60%



Additional Features for AI Assistant in Workflow Designer
---------------------------------------------------------

In addition to generating workflows, AI Assistant in Workflow provides additional features that help users explore **sample prompts, track AI Assistant activities, and review historical interactions** for better visibility and reuse.

**Sample Prompts**
+++++++++++++++++++++

A set of **Sample Prompts** is provided and can be copied and used directly.

1. Click the **Sample Prompts** button under the AI Assistant to view them.

  .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Workflow/Copilot-WF-Sample-Prompts.PNG
     :alt: copilot configuration
     :width: 60%



2. Click the **Copy** icon to copy a sample prompt and use it to generate a workflow.

  .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Workflow/Copilot-WF-Sample-Prompts-List.PNG
     :alt: copilot configuration
     :width: 60%


**AI Assistant Activities**
+++++++++++++++++++++++++++

1. To view captured **AI Assistant Activities** or **Events**, click the **Activities** button under the AI Assistant.

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Workflow/Copilot-WF-Activities.PNG
     :alt: copilot configuration
     :width: 60%


2. A table listing all events is displayed. These events are captured for the current user of the current selected project for the AI Assistant on which the prompt was submitted.

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Workflow/Copilot-WF-Activities-List.PNG
     :alt: copilot configuration
     :width: 60%



3. To view details of a specific event, click on the **Event Detail** entry. A popup displays the following information:

  - First 10–15 words of the submitted prompt
  - Type of AI Assistant used
  - Step-by-step interaction with the LLM
  - Input and Output token count for each step

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Workflow/Copilot-WF-Activities-View.PNG
     :alt: copilot configuration
     :width: 60%


**AI Assistant History**
++++++++++++++++++++++++

1. To view the captured **AI Assistant History**, click the **AI Assistant History** button under the AI Assistant.

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Workflow/Copilot-WF-History.PNG
     :alt: copilot configuration
     :width: 60%


   A table is displayed showing all prompts submitted. The history is captured for the current user of the current selected project for the AI Assistant on which the prompt was submitted. 

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Workflow/Copilot-WF-History-List.PNG
     :alt: copilot configuration
     :width: 60%

2. Click the **View** icon under the **Action** column to see:

  - The User Prompt
  - The LLM-generated Prompt

   These prompts can also be copied for future use.

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Workflow/Copilot-WF-History-View.PNG
     :alt: copilot configuration
     :width: 60%

