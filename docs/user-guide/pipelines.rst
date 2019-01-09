Pipeline
========

Fire supports Pipelines. Pipelines allow running workflows in defined order.

Configuring Pipelines
---------------------

Fire uses Apache Airflow for executing Pipelines. Hence Airflow has to be installed on the same machine as Fire.

Below are the configurations needed in Fire.

.. figure:: ../_assets/user-guide/pipelines-configuration.png
   :alt: Pipelines Configuration
   :align: center

Creating a Pipeline
--------------------

Each Application now allows creating Pipelines.

Below is an example Pipeline with 3 Workflows.

.. figure:: ../_assets/user-guide/pipeline.png
   :alt: Pipeline
   :align: center
   
   
Executing a Pipeline
--------------------

Pipelines can be executed like workflows. When a Pipeline is executed, its execution is submitted to Airflow.

The Pipeline tab displays the list of Pipelines for the current Application.

.. figure:: ../_assets/user-guide/pipeline-list.png
   :alt: Pipeline List
   :align: center
   
Clicking on the ``Execute`` Action icon opens the Pipeline Execute Page.

.. figure:: ../_assets/user-guide/pipeline-execute.png
   :alt: Pipeline Execute
   :align: center
   
Airflow Installation
--------------------

It explain the steps involved in installing airflow on Centos and RHEL.

- Login to machine
  - ssh -i xyz.pem sparkflows@x.y.z.w
  
