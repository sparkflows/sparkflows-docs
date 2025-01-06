EMR Cluster Creation
=================================

This tutorial will cover how to use Airflow Pipeline feature to create an EMR Cluster, add an existing workflow as a step to it, and finally, terminate the EMR cluster.

It includes steps involved for the following: 

* Setting up the pipeline
* Configuring the **Create EMR** & **EMR Workflow** nodes
* Executing the pipeline

Pipeline Set Up
^^^^^^^^^^^^^^^^^^^^^^^^

#. Create a Pipeline as shown below.

   .. figure:: ../../_assets/tutorials/pipeline/afpl-createemr-pipeline.png
      :alt: Pipeline Tutorials
      :width: 70%

EMR Node Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

#. Add an **EMR node** to the pipeline and configure it as shown below. This node will create an **EMR cluster running on AWS** based on the provided configuration.

   .. figure:: ../../_assets/tutorials/pipeline/afpl-createemr-emrnode.png
      :alt: Pipeline Tutorials
      :width: 70%

#. Enter the desired values in the required fields as follows:

   * **Cluster Name:** Enter a Cluster Name value or an expression using a Macro. It will be evaluated during the runtime and the Cluster Name will be assigned accordingly.

   * **Release Label:** Enter an EMR Release Label. The Cluster will be created accordingly.

   * **Instance Type:** Enter the Instance Type, which determines the type of instances to be created, as shown below.
 
     .. figure:: ../../_assets/tutorials/pipeline/afpl-createemr-emrinsnode.png
        :alt: Pipeline Tutorials
        :width: 70%

EMR Workflow Node Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

#. Add an **EMR Workflow** node to the pipeline and configure it, as shown below. This workflow will be added as a step to the created EMR Cluster.

   .. figure:: ../../_assets/tutorials/pipeline/afpl-createemr-emrwfnode.png
      :alt: Pipeline Tutorials
      :width: 70%

#. Enter the desired values in the required fields as follows:

   * **Workflow ID:** Select a workflow from the dropdown to be added as an EMR step.

   * **Trigger Rule:** This governs whether the node will be executed based on the completion status of the previous node.

   * Enter the values for **Deploy Mode** and **Parameters** as needed.

Pipeline Execution
^^^^^^^^^^^^^^^^^^^^^^^^

#. Click the **Execute** button on the Pipeline to execute it. Upon execution, the selected workflow will be added as a step in the created EMR cluster. On successful completion EMR Cluster will be terminated.

   .. figure:: ../../_assets/tutorials/pipeline/afpl-createemr-plexec.png
      :alt: Pipeline Tutorials
      :width: 70%

#. Upon successful execution of the pipeline the **EMR Clusters** get listed in the **AWS Console**, as shown below.

   .. figure:: ../../_assets/tutorials/pipeline/afpl-awsconsole-clusterlist.png
      :alt: Pipeline Tutorials
      :width: 70%

#. The **EMR Cluster** details can be viewed in the **AWS Console**, as shown below.

   .. figure:: ../../_assets/tutorials/pipeline/afpl-awsconsole-clusterdetail.png
      :alt: Pipeline Tutorials
      :width: 70%

#. Details of the **EMR Step** added using **Workflow** to the **EMR Cluster** can be viewed in the **AWS Console**, as shown below.

   .. figure:: ../../_assets/tutorials/pipeline/afpl-awsconsole-wfstep.png
      :alt: Pipeline Tutorials
      :width: 70%
