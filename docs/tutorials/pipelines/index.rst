Pipelines
=========

Multiple workflows can be stitched together with the help of a **Pipeline**. 

**Pipeline** helps in orchestrating execution of workflows to achieve a business function. 

Individual workflow can help to cater to a specific business implementation such as Data Ingestion, Data Preparation, Features Identification, Model Building, Model Prediction and so on. **Pipeline** helps to execute these jobs as a single unit. 

With pipelines, multiple workflows can be scheduled to be executed sequentially.


.. panels::
    :container: container-lg pb-3
    :column: text-center col-lg-6 col-md-6 col-sm-6 col-xs-12 p-2

    :doc:`pipeline-tutorials-cs-pipeline`

    ---

    :doc:`afpl-add-wf-as-emr-step`

    Airflow Pipeline Tutorials - Adding a workflow as an EMR Step

    ---

    :doc:`afpl-create-emr-cluster`

    Airflow Pipeline Tutorials - EMR Cluster Creation, Execute a Workflow and Termination of Cluster

    ---

    :doc:`afpl-dynamic-emr-config`

    Airflow Pipeline Tutorials - Dynamically configuring EMR Cluster

    ---

    :doc:`dbpl-execnotebk`

    Databricks Pipeline Tutorials - Executing Databricks Notebook

.. toctree::
   :hidden:

   pipeline-tutorials-cs-pipeline.rst
   afpl-add-wf-as-emr-step.rst
   afpl-create-emr-cluster.rst
   afpl-dynamic-emr-config.rst
   dbpl-execnotebk.rst

