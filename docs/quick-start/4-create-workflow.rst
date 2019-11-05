Step 4 : Create Workflow
------------

After you have created the datasets, you can start building workflows to process them. 

A typical workflow takes one or more dataset, cleans them and joins them, and creates an enriched dataset. After the enriched dataset is created, you can add additional processors to build machine learning models.

At a high level,creating a workflow involves the following steps:

- *Open the Application where you want to create your workflow*
- *Click "Workflows" tab*
- *Create empty workflow*
- *Add processors*
- *Save workflow*

Application
=======================
Open the application where you want to create your new workflow.

.. figure:: ../_assets/tutorials/quickstart/8.PNG
   :alt: Quicstart
   :align: center



Workflows Tab
============================
Click "Workflows" tab to view the list of workflows already in the application. The workflow list will be empty if no workflows have been created earlier. 

.. figure:: ../_assets/tutorials/quickstart/7.PNG
   :alt: Quicstart
   :align: center

Create Empty Workflow
========================

Click "Create" button and choose the type of workflow you want to create. In the "Create Workflow" page, enter a name, category and description of the workflow. Category is used to group various workflows. For instance, if you have several workflows for customer reports, you can group them by specifying "Customer Reports" category.

Click "Save" to save the empty workflow.


Add Processors
===================

After you have saved the empty workflow, you can start adding processors to process the datasets that you had defined earlier. Click on the processors on the left hand side pane. This will make the processor appear on the workflow canvas. Add other procesors,configure and connect them as needed.  Two processors can be connected by clicking on the yellow box in the first processor and dragging it to the second processor. 

.. figure:: ../_assets/tutorials/quickstart/9.PNG
   :alt: Quickstart
   :align: center



Save Workflow
=================

Once you are satisfied with your workflow, save the workflow by clicking on 'Save' button.

Each time the workflow is saved, a new version of workflow is created.





