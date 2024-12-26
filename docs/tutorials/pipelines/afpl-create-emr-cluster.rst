EMR Cluster Creation
=================================

This tutorial will cover how to use Airflow Pipeline feature to create an EMR Cluster, add an existing workflow as an step to it and finally terminate the EMR cluster.

This tutorial covers steps involved in setting up the pipeline, configuring the **Create EMR** & **EMR Workflow** nodes and execution of the pipeline.

Pipeline
^^^^^^^^^^^^^^^^^^^^^^^^

Create a Pipeline as below.

   .. figure:: ../../_assets/tutorials/pipeline/afpl-createemr-pipeline.png
      :alt: Pipeline Tutorials
      :width: 70%

EMR Node Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

Add a **EMR** node to the pipeline and configure it as below. It would create an EMR cluster running on AWS as per the configuration provided.

   .. figure:: ../../_assets/tutorials/pipeline/afpl-createemr-emrnode.png
      :alt: Pipeline Tutorials
      :width: 70%

**Cluster Name:** Enter a Cluster Name value or an expression using a Macro. It would be evaluated during the runtime and Cluster Name would be assigned accordingly.

**Release Label:** Enter a EMR Release Label. Cluster would be created accordingly.

   .. figure:: ../../_assets/tutorials/pipeline/afpl-createemr-emrinsnode.png
      :alt: Pipeline Tutorials
      :width: 70%

		**Instance Type:** Enter the Instance Type governing the type of instances to be created.


EMR Workflow Node Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

Add a **EMR Workflow** node to the pipeline and configure it as below. This workflow would be added as an step to the created EMR Cluster.

   .. figure:: ../../_assets/tutorials/pipeline/afpl-createemr-emrwfnode.png
      :alt: Pipeline Tutorials
      :width: 70%

**Workflow ID:** Select a workflow from the dropdown that needs to be added as an EMR step.

**Trigger Rulw:** It governs whether this node is to be executed or not based on the completion status of previous node.

Enter values for **Deploy Mode** and **Parameters** as needed.

Pipeline Execution
^^^^^^^^^^^^^^^^^^^^^^^^

Click on **Execute** Button on the Pipeline to execute it. On pipeline execution the selected workflow would get added as an step in the created EMR cluster. On successful completion EMR Cluster would be terminated.

   .. figure:: ../../_assets/tutorials/pipeline/afpl-createemr-plexec.png
      :alt: Pipeline Tutorials
      :width: 70%

