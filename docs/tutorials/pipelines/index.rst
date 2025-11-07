Pipelines
=========

Multiple workflows can be stitched together with the help of a **Pipeline**. 

**Pipeline** helps in orchestrating execution of workflows to achieve a business function. 

Individual workflow can help to cater to a specific business implementation such as Data Ingestion, Data Preparation, Features Identification, Model Building, Model Prediction and so on. **Pipeline** helps to execute these jobs as a single unit. 

With pipelines, multiple workflows can be scheduled to be executed sequentially.


.. panels::
    :container: container-lg pb-3
    :column: text-center col-lg-6 col-md-6 col-sm-6 col-xs-12 p-2

    :doc:`tutorials/pipelines/sparkflows_pipelines`

    Sparkflows Pipeline Tutorials
    
    ---

    :doc:`tutorials/pipelines/airflow_pipelines`

    Airflow Pipeline Tutorials

    ---

    :doc:`dbpl-create-cluster`

    Databricks Pipeline Tutorials - Create Cluster

    ---

    :doc:`dbpl-execnotebk`

    Databricks Pipeline Tutorials - Executing Databricks Notebook

    ---

    :doc:`dbpl-execute-job`

    Databricks Pipeline Tutorials - Executing Databricks Jobs

    ---

    :doc:`dbpl-exec-workflow`

    Databricks Pipeline Tutorials - Executing Workflow

    ---

    :doc:`snowflake-sp-execution`

    Snowflake Stored Procedure Execution - Using Airflow & EMR



.. toctree::
   :hidden:

   sparkflows_pipelines/index.rst
   airflow_pipelines/index.rst
   dbpl-create-cluster.rst
   dbpl-execnotebk.rst
   dbpl-execute-job.rst
   dbpl-exec-workflow.rst
   snowflake-sp-execution.rst

