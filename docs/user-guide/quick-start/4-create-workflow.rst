Step 4 : Create Workflow
------------

A typical workflow takes one or more datasets, cleans them, joins them and creates an enriched dataset. After the enriched dataset is created, you can add additional processors to build machine learning models.

The steps invoved in creating a workflow are: 

* Go to Workflows Page.
* Create an empty workflow.
* Add, configure and connect processors.
* Save the workflow.


Step 1 : Go to Workflows Page
============================

#. **Open** the **Project** where you want your workflow to reside.
#. Click **Workflows** tab in the upper-middle bar of the Project page.
   
   *Note: The Workflows page displays already created workflows list. It will be empty if no workflows have been created in the project.*
   
   .. figure:: ../../_assets/tutorials/quickstart/Create-Workflows/CreateWorkflow-1.png
      :alt: Quickstart
      :width: 60%


Step 2 : Create an Empty Workflow
========================

#. Click **Create** on the **Workflows Page**.
#. Select the **type** of workflow you want to create from the **drop-down** list. Fire offers:
      
      * Spark
      * PySpark

#. Give a **Name** and **Category** to your workflow on the **Workflows Editor Page**.
      
   *Note: The category is used to group various workflows. For instance, if you have several workflows for customer reports, you can group them by specifying the category as *Customer Reports*.*
    
#. Click **Save** to save the empty workflow.


Step 3 : Add, Configure and Connect Processors 
===================

#. Click the **processor name** in the **Processor Repository** located on the left-hand side pane of the Workflows Editor Page to make processor(s) appear on the Canvas.
   
   Note: You can use the **Search Panel** located on top of the Processor Repository to add processors.

#. After adding all the processors, **double-click** each **processor** to open the **configuration window** and configure them as per your need.
#. **Connect** two processors by drawing an **edge** between them. To draw an edge:
   
   * **Hover** the cursor over **Grey Square Icon** present on the processor and **click**.
   * While clicking **drag** the cursor and **drop** it on the processor to which you want to establish a connection.
     
   An edge between the processors is successfully drawn and they are now connected.
      
  .. figure:: ../../_assets/tutorials/quickstart/Create-Workflows/CreateWorkflow-2.png
   :alt: Quickstart
   :width: 60%

Step 4 : Save the Workflow
=================

Click **Save** after you finish building your pipline of processors. Now, you are ready to process your dataset.
   
*Note: Each time the workflow is saved, a new version of the workflow is created.*

.. note:: Only CSV and Snowflake dataset is supported to be used in workflow as of today.


