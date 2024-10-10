Variables
==========

Fire Insights allows you to define and use variables in various ways.

  * Variables can be defined at the project, group and global level
  * Variables can be defined during workflow execution
  * Variables can be added using a scala node
  * Variables can be defined at the pipeline level
  * Variables can be used in the Pyspark node

When a variable is used in a node, below is the order of precedence:

  * Lowest precedence is variables defined at the project level, then group level & Lowest precedence is variables defined at the global level
  * Variables defined during execution override the variables at the workflow level
  * Variables defined in Scala/Pyspark node override the previous variables

.. panels::
    :container: container-lg pb-3
    :column: text-center col-lg-6 col-md-6 col-sm-6 col-xs-12 p-2

    :doc:`/user-guide/variables/global_or_group-variable`

    ---

    :doc:`/user-guide/variables/project-variablel`

    ---


    :doc:`/user-guide/variables/workflow`

    ---

    :doc:`/user-guide/variables/node`

    ---

    :doc:`/user-guide/variables/pipeline`

    ---

    :doc:`/user-guide/variables/spark-configuration`



.. toctree::
   :hidden:
   global_or_group-variable.rst
   project.rst
   workflow.rst
   node.rst
   pipeline.rst
   spark-configuration.rst
