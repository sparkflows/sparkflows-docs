AI Assistant on Pipeline
========================

This section explains how to use **AI Assistant** within the **Pipeline Designer** in Sparkflows.

Prerequisites
-------------

Before using AI Assistant in the Pipeline Designer, ensure that a AI Assistant has already been added.

The steps for adding a AI Assistant are provided in the following document:

https://docs.sparkflows.ai/en/latest/user-guide/copilot/copilot.html

Steps to Use AI Assistant in Pipeline Designer
----------------------------------------------

1. Navigate to the **Pipelines** page within any **Project**.
2. Click on the **Create** button.
3. To use AI Assistant, click on the **AI Assistant** button.

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Pipeline/Copilot-Button-Pipeline-Page.PNG
     :alt: copilot configuration
     :width: 60%



4. On clicking the AI Assistant button, the **AI Assistant** opens. The previously created AI Assistant will be selected by default in the dropdown, as shown below.

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Pipeline/Copilot-Pipeline-Assistant-Conn-Selected.PNG
     :alt: copilot configuration
     :width: 60%



5. A prompt can now be entered to create a pipeline. AI Assistant generates a response based on the prompt, as shown below.

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Pipeline/Copilot-Pipeline-Generate-Response.PNG
    :alt: copilot configuration
    :width: 60%




6. Once the Pipeline JSON is generated based on the submitted query, click on the **Show More** button.

   This allows you to preview the complete generated Pipeline JSON.

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Pipeline/Copilot-ShowMore-Preview-Pipeline-JSON.PNG
     :alt: copilot configuration
     :width: 60%



   You can also preview the generated **Pipeline**.

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Pipeline/Copilot-ShowMore-Preview-Pipeline.PNG
     :alt: copilot configuration
     :width: 60%


7. Clicking the **Confirm** button on the Preview Pipeline popup will move the generated pipeline to the **Pipeline Designer**.

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Pipeline/Copilot-Pipeline-Preview-Confirm.PNG
     :alt: copilot configuration
     :width: 60%


   You can also directly preview the generated pipeline by clicking the **Preview** icon seen in the AI Assistant response.

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Pipeline/Copilot-Pipeline-Direct-Preview.PNG
     :alt: copilot configuration
     :width: 60%

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Pipeline/Copilot-ShowMore-Preview-Pipeline.PNG
     :alt: copilot configuration
     :width: 60%



   You can also directly add the generated pipeline to the Pipeline Designer by clicking the **Add** icon in the response.

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Pipeline/Copilot-Pipeline-Direct-Add.PNG
     :alt: copilot configuration
     :width: 60%

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Pipeline/Copilot-Pipeline-Preview-Confirm.PNG
     :alt: copilot configuration
     :width: 60%



Additional Features for AI Assistant in Pipeline Designer
---------------------------------------------------------

In addition to generating pipelines, AI Assistant in Pipeline provides additional features that help users explore **sample prompts, track AI Assistant activities, and review historical interactions** for better visibility and reuse.

**Sample Prompts**
+++++++++++++++++++++

A set of **Sample Prompts** is provided and can be copied and used directly.

1. Click the **Sample Prompts** button under the AI Assistant to view them.

  .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Workflow/Copilot-WF-Sample-Prompts.PNG
     :alt: copilot configuration
     :width: 60%



2. Click the **Copy** icon to copy a sample prompt and use it to generate a pipeline.

  .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Pipeline/Copilot-Pipeline-Sample-Prompts-List.PNG
     :alt: copilot configuration
     :width: 60%


**AI Assistant Activities**
+++++++++++++++++++++++++++

1. To view captured **AI Assistant Activities** or **Events**, click the **Activities** button under the AI Assistant.

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Workflow/Copilot-WF-Activities.PNG
     :alt: copilot configuration
     :width: 60%


2. A table listing all events is displayed. These events are captured for the current user of the current selected project for the AI Assistant on which the prompt was submitted.

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Pipeline/Copilot-Pipeline-Activities-List.PNG
     :alt: copilot configuration
     :width: 60%



3. To view details of a specific event, click on the **Event Detail** entry. A popup displays the following information:

  - First 10–15 words of the submitted prompt
  - Type of AI Assistant used
  - Step-by-step interaction with the LLM
  - Input and Output token count for each step

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Pipeline/Copilot-Pipeline-Activities-View.PNG
     :alt: copilot configuration
     :width: 60%


**AI Assistant History**
++++++++++++++++++++++++

1. To view the captured **AI Assistant History**, click the **AI Assistant History** button under the AI Assistant.

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Workflow/Copilot-WF-History.PNG
     :alt: copilot configuration
     :width: 60%


   A table is displayed showing all prompts submitted. The history is captured for the current user of the current selected project for the AI Assistant on which the prompt was submitted. 

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Pipeline/Copilot-Pipeline-History-List.PNG
     :alt: copilot configuration
     :width: 60%

2. Click the **View** icon under the **Action** column to see:

  - The User Prompt
  - The LLM-generated Prompt

   These prompts can also be copied for future use.

   .. figure:: ../../_assets/user-guide/copilot/Copilot-On-Pipeline/Copilot-Pipeline-History-View.PNG
     :alt: copilot configuration
     :width: 60%

