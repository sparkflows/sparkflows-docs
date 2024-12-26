Airflow Pipeline Tutorials - Adding a workflow as an EMR Step
=================================

This tutorial will cover how to use Airflow Pipeline feature to add an existing workflow as an step to an existing EMR cluster.

This tutorial covers steps involved in setting up the pipeline, configuring the **EMR Workflow** node and execution of the pipeline.

EMR Workflow Node Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

Add a **EMR Workflow** node to the pipeline and configure it as below. 

   .. figure:: ../../_assets/tutorials/pipeline/afpl-wfaddtoemr-emrwfnode.png
      :alt: Pipeline Tutorials
      :width: 70%

**Cluster ID:** Enter the ID of an existing EMR Cluster.

**Workflow ID:** Select a workflow from the dropdown that needs to be added as an EMR step.

Enter values for **Deploy Mode** and **Parameters** as needed.

Pipeline Execution
^^^^^^^^^^^^^^^^^^^^^^^^

Click on **Execute** Button on the Pipeline to execute it. On execution the selected workflow would get added as an step in the select EMR cluster.

   .. figure:: ../../_assets/tutorials/pipeline/afpl-wfaddtoemr-plexec.png
      :alt: Pipeline Tutorials
      :width: 70%
