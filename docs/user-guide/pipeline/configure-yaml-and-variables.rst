Configure Yml files and Variables
==================================


Fire Insights provides a node using which yml files and airflow variables can be configured.

YML File Configuration
----------------------

1. Upload Yml configuration files from Node UI

.. figure:: ../../_assets/user-guide/pipeline/pipeline_upload_config_files.PNG
   :alt: Upload Yml Config files in Node
   :width: 30%

2. Add additional Yml files in Airflow Variables UI (Optional)

.. figure:: ../../_assets/user-guide/pipeline/pipeline_define_config_yml_in_airflow.PNG
   :alt: Specify Yml Content in Airflow Variable UI
   :width: 30%

3. Note that the merged content of Yml files will be displayed in Airflow Variables UI as follows.

.. figure:: ../../_assets/user-guide/pipeline/pipeline_merged_yml_in_airflow.PNG
   :alt: Update Merged Yml Content in Airflow Variable UI
   :width: 30%

The merged Yml is stored inside a variable having the same name as the DAG file.

If user updates the merged Yml content in Airflow Variable UI, then it will take precedence over the files uploaded from the Sparkflows Pipeline Node UI.

Variable Definition
-----------------------

1. First define the Key variables in Airflow which are parent Nodes in the Yml file.

For example,
::
    ENV prod
    LOCATION  us-east1

.. figure:: ../../_assets/user-guide/pipeline/pipeline_define_config_yml_in_airflow.PNG
   :alt: Specify Variables in Airflow
   :width: 30%

2. Next allow users to define custom variable in the Node

For example, following variable `s3_bucket_path` shows how to specify the Airflow Variables (ENV, LOCATION)
and a YML Config file variable (s3_bucketname).
::
    s3_bucket_path {{ENV}}.{{LOCATION}}.s3_bucketname


.. figure:: ../../_assets/user-guide/pipeline/pipeline_define_node_variable.PNG
   :alt: Specify Variables in Airflow
   :width: 30%

MACRO Usage
-------------------

Specify predefined Airflow Macros by following this document https://airflow.apache.org/macros.html#default-variables

For example, `{{ execution_date }}` is an example of specifying a macro inside a value as follows "s3://fre-sample-data/change-health/outputIngestion/{{ execution_date }}".
