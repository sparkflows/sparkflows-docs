Variables
===============

Overview
--------

Fire Insights allows you to define and use variables in various ways.

  * Variables can be defined at workflow level
  * Variables can be defined during workflow execution
  * Variables can be added using a scala node
  * Variables can be defined at the pipeline level
  * Variables can be used in the Pyspark node
  * Variables can be used in Application Connection
  * Variables can be defined at the project, group and global level
  * Variables can be imported using a INI or JSON file

Order of Precedence
-----------

When a variable is used in a node, below is the order of precedence:

  * Variables defined during execution override the variables at the workflow level
  * Variables defined in Scala/Pyspark node override the previous variables  
  * Variables defined at the project level, then group level and lowest precedence is variables defined at the global level


.. panels::
    :container: container-lg pb-3
    :column: text-center col-lg-6 col-md-6 col-sm-6 col-xs-12 p-2


    :doc:`/user-guide/variables-macros/variables/workflow`

    ---

    :doc:`/user-guide/variables-macros/variables/node`

    ---

    :doc:`/user-guide/variables-macros/variables/pipeline`

    ---

    :doc:`/user-guide/variables-macros/variables/spark-configuration`

    ---

    :doc:`/user-guide/variables-macros/variables/application_connection`

    ---

    :doc:`/user-guide/variables-macros/variables/global_or_group-variable`

    ---

    :doc:`/user-guide/variables-macros/variables/project-variable`

    ---

    :doc:`/user-guide/variables-macros/variables/import-variables`



.. toctree::
   :hidden:

   workflow.rst
   node.rst
   pipeline.rst
   spark-configuration.rst
   application_connection.rst
   global_or_group-variable.rst
   project-variable.rst
   import-variables.rst
