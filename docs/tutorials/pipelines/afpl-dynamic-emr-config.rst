Configure EMR Cluster dynamically
=================================

This tutorial will guide you through using the Airflow Pipeline feature to configure an EMR Cluster dynamically and add steps to it.

It will cover the following key aspects:

* Defining Sparkflows Global Variable.
* Pipeline creation to create EMR Cluster, and add Steps to it.
* Configuring the Create EMR node using the Global Variable for dynamic configuration.
* Executing and monitoring the pipeline.

Adding Global Variable
^^^^^^^^^^^^^^^^^^^^^^^^

#. Define a **Global Variable** as below. It will be used to set the count of **Worker Nodes** dynamically.

   .. figure:: ../../_assets/tutorials/pipeline/afpl-dynamicemr-variable.png
      :alt: Pipeline Tutorials
      :width: 70%
	  
#. Once added it will be added to the Variables list as below.

   .. figure:: ../../_assets/tutorials/pipeline/afpl-dynamicemr-varlist.png
      :alt: Pipeline Tutorials
      :width: 70%

Pipeline Set Up
^^^^^^^^^^^^^^^^^^^^^^^^

#. Create a Pipeline as shown below. More nodes can be added based on the functionality.

   .. figure:: ../../_assets/tutorials/pipeline/afpl-dynamicemr-pipeline.png
      :alt: Pipeline Tutorials
      :width: 70%

Pipeline Parameters
^^^^^^^^^^^^^^^^^^^^^^^^

#. Add Parameters to the Pipeline as below. They would be used for dynamic configuration.

   .. figure:: ../../_assets/tutorials/pipeline/afpl-dynamicemr-param.png
      :alt: Pipeline Tutorials
      :width: 70%


EMR Node Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

#. Add an **EMR node** to the pipeline and configure it as shown below. This node will create an **EMR cluster running on AWS** based on the provided configuration.

   .. figure:: ../../_assets/tutorials/pipeline/afpl-dynamicemr-emrnode.png
      :alt: Pipeline Tutorials
      :width: 70%

#. Enter the desired values in the required fields as follows:

   * **Cluster Name:** Enter a Cluster Name value or an expression using a Macro. It will be evaluated during the runtime and the Cluster Name will be assigned accordingly.

   * **Release Label:** Enter an EMR Release Label. The Cluster will be created accordingly.

   * **Instance Type:** Enter the Instance Type, which determines the type of instances to be created, as shown below. **EC2 Subnet ID** and **Instance Type** values need to be set as the **Pipeline Parameter**. **Instance Count** needs to be set the **Global Variable** as below.
 
     .. figure:: ../../_assets/tutorials/pipeline/afpl-dynamicemr-emrinsnode.png
        :alt: Pipeline Tutorials
        :width: 70%
		
     .. figure:: ../../_assets/tutorials/pipeline/afpl-dynamicemr-emrinsnode2.png
        :alt: Pipeline Tutorials
        :width: 70%

XML Parser Node Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

#. Add a **XML node** to the pipeline and configure it as shown below. It parses XML Files and would be added as a Step to the **EMR Cluster**

   .. figure:: ../../_assets/tutorials/pipeline/afpl-dynamicemr-xmlparser.png
      :alt: Pipeline Tutorials
      :width: 70%

   .. figure:: ../../_assets/tutorials/pipeline/afpl-dynamicemr-xmlparser2.png
      :alt: Pipeline Tutorials
      :width: 70%

Add Step Node Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

#. Add an **AddStep node** to the pipeline and configure it as shown below. It executes a python file and would be added as a Step to the **EMR Cluster**

   .. figure:: ../../_assets/tutorials/pipeline/afpl-dynamicemr-addstep.png
      :alt: Pipeline Tutorials
      :width: 70%

Pipeline Execution
^^^^^^^^^^^^^^^^^^^^^^^^

#. Click the **Execute** button on the Pipeline to execute it. Upon execution, EMR cluster would be created and would be configured dynamically.

#. Upon successful execution of the pipeline, **EMR Clusters** are listed in the **AWS Console**, as shown below.

   .. figure:: ../../_assets/tutorials/pipeline/afpl-awsconsole-clusterlist.png
      :alt: Pipeline Tutorials
      :width: 70%

#. **EMR Cluster** details can be viewed in the **AWS Console**, as shown below.

   .. figure:: ../../_assets/tutorials/pipeline/afpl-awsconsole-clusterdetail.png
      :alt: Pipeline Tutorials
      :width: 70%

#. Details of the **EMR Step** added using **Workflow** to the **EMR Cluster** can be viewed in the **AWS Console**, as shown below.

   .. figure:: ../../_assets/tutorials/pipeline/afpl-awsconsole-wfstep.png
      :alt: Pipeline Tutorials
      :width: 70%
	  
