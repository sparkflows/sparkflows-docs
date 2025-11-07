Adding a workflow as an EMR Step
=================================

This tutorial will guide you through using the Airflow Pipeline feature to add an existing workflow as a step into an existing EMR cluster.

It will cover the following key aspects:

* Setting up the Airflow pipeline.
* Configuring the EMR Workflow node.
* Executing and monitoring the pipeline.

Pipeline Set Up
^^^^^^^^^^^^^^^^^^^^^^^^

#. Create a Pipeline with a single step, as shown below. More nodes can be added based on the functionality.

   .. figure:: ../../../_assets/tutorials/pipeline/afpl-wfaddtoemr-pipeline.png
      :alt: Pipeline Tutorials
      :width: 70%

EMR Workflow Node Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

#. Add an **EMR Workflow** node to the pipeline and configure it, as shown below. 

   .. figure:: ../../../_assets/tutorials/pipeline/afpl-wfaddtoemr-emrwfnode.png
      :alt: Pipeline Tutorials
      :width: 70%

#. Enter the desired values in the required fields as follows:

   * **Cluster ID:** Enter the ID of an existing EMR Cluster.

   * **Workflow ID:** Select a workflow from the dropdown that needs to be added as an EMR step.

#. Enter the values for **Deploy Mode** and **Parameters** as needed.

Pipeline Execution
^^^^^^^^^^^^^^^^^^^^^^^^

#. Click the **Execute** button on the Pipeline to execute it. Upon execution, the selected workflow will be added as a step in the chosen EMR cluster.

   .. figure:: ../../../_assets/tutorials/pipeline/afpl-wfaddtoemr-plexec.png
      :alt: Pipeline Tutorials
      :width: 70%

#. Upon successful execution of the pipeline, **EMR Clusters** are listed in the **AWS Console**, as shown below.

   .. figure:: ../../../_assets/tutorials/pipeline/afpl-awsconsole-clusterlist.png
      :alt: Pipeline Tutorials
      :width: 70%

#. **EMR Cluster** details can be viewed in the **AWS Console**, as shown below.

   .. figure:: ../../../_assets/tutorials/pipeline/afpl-awsconsole-clusterdetail.png
      :alt: Pipeline Tutorials
      :width: 70%

#. Details of the **EMR Step** added using **Workflow** to the **EMR Cluster** can be viewed in the **AWS Console**, as shown below.

   .. figure:: ../../../_assets/tutorials/pipeline/afpl-awsconsole-wfstep.png
      :alt: Pipeline Tutorials
      :width: 70%
