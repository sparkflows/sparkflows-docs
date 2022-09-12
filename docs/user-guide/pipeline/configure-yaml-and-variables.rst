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

For example, you can define these variables in Airflow.
::
    ENV prod
    LOCATION  us-east1

for a multi-level yml config file like this one.

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

2. Next allow users to define custom variable in the Node

For example, following variable `s3_bucket_path` shows how to specify the Airflow Variables (ENV, LOCATION)
and a YML Config file variable (s3_bucketname).
::
    s3_bucket_path {{ENV}}.{{REGION}}.s3_bucketname


.. figure:: ../../_assets/user-guide/pipeline/pipeline_define_node_variable.PNG
   :alt: Specify Variables in Airflow
   :width: 30%

MACRO Usage
-------------------

Specify predefined Airflow Macros by following this document https://airflow.apache.org/macros.html#default-variables

For example, `{{ execution_date }}` is an example of specifying a macro inside a value as follows "s3://fre-sample-data/change-health/outputIngestion/{{ execution_date }}".

Default Variables
-----------------
The Airflow engine passes a few variables by default that are accessible
in all templates

=====================================   ====================================
Variable                                Description
=====================================   ====================================
``{{ ds }}``                            the execution date as ``YYYY-MM-DD``
``{{ ds_nodash }}``                     the execution date as ``YYYYMMDD``
``{{ prev_ds }}``                       the previous execution date as ``YYYY-MM-DD``
                                        if ``{{ ds }}`` is ``2018-01-08`` and ``schedule_interval`` is ``@weekly``,
                                        ``{{ prev_ds }}`` will be ``2018-01-01``
``{{ prev_ds_nodash }}``                the previous execution date as ``YYYYMMDD`` if exists, else ``None``
``{{ next_ds }}``                       the next execution date as ``YYYY-MM-DD``
                                        if ``{{ ds }}`` is ``2018-01-01`` and ``schedule_interval`` is ``@weekly``,
                                        ``{{ next_ds }}`` will be ``2018-01-08``
``{{ next_ds_nodash }}``                the next execution date as ``YYYYMMDD`` if exists, else ``None``
``{{ yesterday_ds }}``                  the day before the execution date as ``YYYY-MM-DD``
``{{ yesterday_ds_nodash }}``           the day before the execution date as ``YYYYMMDD``
``{{ tomorrow_ds }}``                   the day after the execution date as ``YYYY-MM-DD``
``{{ tomorrow_ds_nodash }}``            the day after the execution date as ``YYYYMMDD``
``{{ ts }}``                            same as ``execution_date.isoformat()``. Example: ``2018-01-01T00:00:00+00:00``
``{{ ts_nodash }}``                     same as ``ts`` without ``-``, ``:`` and TimeZone info. Example: ``20180101T000000``
``{{ ts_nodash_with_tz }}``             same as ``ts`` without ``-`` and ``:``. Example: ``20180101T000000+0000``
``{{ execution_date }}``                the execution_date (`pendulum.Pendulum`_)
``{{ prev_execution_date }}``           the previous execution date (if available) (`pendulum.Pendulum`_)
``{{ prev_execution_date_success }}``   execution date from prior succesful dag run (if available) (`pendulum.Pendulum`_)
``{{ prev_start_date_success }}``       start date from prior successful dag run (if available) (`pendulum.Pendulum`_)
``{{ next_execution_date }}``           the next execution date (`pendulum.Pendulum`_)
``{{ dag }}``                           the DAG object
``{{ task }}``                          the Task object
``{{ macros }}``                        a reference to the macros package, described below
``{{ task_instance }}``                 the task_instance object
``{{ end_date }}``                      same as ``{{ ds }}``
``{{ latest_date }}``                   same as ``{{ ds }}``
``{{ ti }}``                            same as ``{{ task_instance }}``
``{{ params }}``                        a reference to the user-defined params dictionary which can be overridden by
                                        the dictionary passed through ``trigger_dag -c`` if you enabled
                                        ``dag_run_conf_overrides_params` in ``airflow.cfg``
``{{ var.value.my_var }}``              global defined variables represented as a dictionary
``{{ var.json.my_var.path }}``          global defined variables represented as a dictionary
                                        with deserialized JSON object, append the path to the
                                        key within the JSON object
``{{ task_instance_key_str }}``         a unique, human-readable key to the task instance
                                        formatted ``{dag_id}_{task_id}_{ds}``
``{{ conf }}``                          the full configuration object located at
                                        ``airflow.configuration.conf`` which
                                        represents the content of your
                                        ``airflow.cfg``
``{{ run_id }}``                        the ``run_id`` of the current DAG run
``{{ dag_run }}``                       a reference to the DagRun object
``{{ test_mode }}``                     whether the task instance was called using
                                        the CLI's test subcommand
=====================================   ====================================
