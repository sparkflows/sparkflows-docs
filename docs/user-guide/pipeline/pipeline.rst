Overview
========

Fire Insights supports Pipelines. Pipelines allow running multiple workflows in a defined order.

Fire Insights can be executed Pipelines in below ways :

1. It Can run workflows on Compute engine configured.
2. It can run them via Airflow. The nodes available in the Pipeline depends on whether Airflow is configured or not.

Pipeline List
-------------

``Pipeline`` tab under a Project displays list of all Pipelines created under the selected project. Pipelines can be grouped together under several Categories. 

.. figure:: ../../_assets/user-guide/pipeline-list-new.png
   :alt: Pipeline List

Creating a Pipeline
--------------------

Following steps can be taken to create a Pipeline:

*	A Pipeline can be created under a Project by navigating to the ``Pipeline`` tab and clicking on ``Create Pipeline`` button.
*	Add ``Nodes`` to the new Pipeline canvas. Enter ``Pipeline Name`` and ``Pipeline Category`` and click on ``Save`` button to save the new Pipeline.

Various ``Nodes`` can be added to a Pipeline. Some of them are listed below:

*	``Workflow`` node can be added to a Pipeline to execute a Workflow. A ``Workflow`` node can be connected to another ``Workflow`` node thus forming a series of workflows that can be executed one after another.
*	``Shell Commands`` node can be used to execute a shell command.
*	``Create EMR Cluster`` node can be used to create an EMR cluster based on the parameters passed.
* 	``XML Parser`` node can be used to parse an XML file.

Below is an example a Pipeline with multiple Workflows.

.. figure:: ../../_assets/user-guide/pipeline-new.png
   :alt: Pipeline
   
   
Executing a Pipeline
--------------------

Pipelines can be executed in the similar way as Workflow execution. When a Pipeline is executed, its tasks are submitted to Airflow.

The Pipeline tab displays the list of Pipelines for the current Application.

.. figure:: ../../_assets/user-guide/pipeline-list-new.png
   :alt: Pipeline List
   
Clicking on the ``Execute`` Action button from ``Pipeline`` list or in the ``Pipeline`` page opens the ``Pipeline Execute`` Page.

.. figure:: ../../_assets/user-guide/pipeline-execute-new.png
   :alt: Pipeline Execute
   
Pipeline Execution
------------------

Once a Pipeline is submitted for execution, its execution details can be viewed in the ``Pipeline Executions`` tab.

.. figure:: ../../_assets/user-guide/pipeline-execution-new.png
   :alt: Pipeline Execution
   
