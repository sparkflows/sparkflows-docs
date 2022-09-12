Configure Yaml files and Variables
==================================


Sparkflows provides a node using which yaml files and airflow variables can be configured.

Yaml File Configuration
----------------------

1. Upload yaml configuration files from Node UI

.. figure:: ../../_assets/user-guide/pipeline/pipeline_upload_config_files.PNG
   :alt: Upload yaml Config files in Node
   :width: 30%

2. Add additional yaml files in Airflow Variables UI (Optional)

.. figure:: ../../_assets/user-guide/pipeline/pipeline_define_config_yml_in_airflow.PNG
   :alt: Specify yaml Content in Airflow Variable UI
   :width: 30%

3. Note that the merged content of yaml files will be displayed in Airflow Variables UI as follows.

.. figure:: ../../_assets/user-guide/pipeline/pipeline_merged_yml_in_airflow.PNG
   :alt: Update Merged yaml Content in Airflow Variable UI
   :width: 30%

The merged yaml is stored inside a variable having the same name as the DAG file.

If user updates the merged yaml content in Airflow Variable UI, then it will take precedence over the files uploaded from the Sparkflows Pipeline Node UI.

Variable Definition
-----------------------

1. First define the Key variables in Airflow which are parent Nodes in the yaml file.

For example, you can define these variables in Airflow.
::
    ENV prod
    LOCATION  us-east1

for a multi-level yaml config file like this one.

.. code-block:: bash

    prod:
       us-east1:
           s3_bucketname: biz-pipeline
           role: admin
    dev:
       us-west1:
           bucketname: biz-pipeline
           role: admin
 
.. figure:: ../../_assets/user-guide/pipeline/pipeline_define_config_yml_in_airflow.PNG
   :alt: Specify Variables in Airflow
   :width: 30%

2. Next allow users to define yaml variable in the Node

For example, following variable `s3_bucket_path` shows how to specify the Airflow Variables (ENV, REGION)
and a yaml Config file variable (s3_bucketname).
::
    s3_bucket_path {{ENV}}.{{REGION}}.s3_bucketname


   Then use the above variable in the fields with single curly bracket.  ex: ``s3://{s3_bucket_path}``
   
   
.. figure:: ../../_assets/user-guide/pipeline/pipeline_define_node_variable.PNG
   :alt: Specify Variables in Airflow
   :width: 30%


