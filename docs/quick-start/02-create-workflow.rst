Step 4 : Create Workflow
------------

After you have created the datasets you want to process, you can start to build a workflow to process it. 

A typical workflow will take one or more dataset, clean them and join them to created an enrighed dataset. After the enriched dataset is created, the workflow can perform steps to build machine learning models.

At at highlevel,creating a workflow involves the following steps:

- *Open the Application where you want to create your workflow*
- *Click on "Workflows" tab*
- *Click on "Create" button and choose the kind of workflow you want to create*
- *Click on the processors on the left hand side pane to add them in the Workflow Canvas*
- *Configure and connect the processors to route data from one processor to another*
- *Name the workflow and save it*

Go to Application Page
=======================

.. figure:: ../_assets/tutorials/quickstart/8.PNG
   :alt: Quicstart
   :align: center



Go to Workflow Listings Page
============================

.. figure:: ../_assets/tutorials/quickstart/7.PNG
   :alt: Quicstart
   :align: center

Click on Create Workflow
========================

Click on ``Create Workflow`` for creating a new workflow. It would take you to the Workflow Designer Page.

In the Workflow Designer Page, give a ``Name, Category and Description`` to the Workflow.

- **NAME** : Name of the New Workflow
- **CATEGORY** : Category is used to group various workflows. For example if we have various Workflows for Customer Reports, the Category could be ``Customer Reports``.
- **DESCRIPTION** : Description of the New Workflow
- **PARAMETERS** : Parameter of the Workflow


Create the Workflow
===================

Click on the nodes in the LHS to create them. Connect them with Links. Links can be connected between 2 Nodes by clicking on the yellow box in the first node, dragging the mouse and connecting to the second Node.

.. figure:: ../_assets/tutorials/quickstart/9.PNG
   :alt: Quickstart
   :align: center




Save the Workflow
=================

Finally Save the Workflow by clicking on the ``Save`` button.

Each time the workflow is saved with new values, a new version of the Workflow gets created.





