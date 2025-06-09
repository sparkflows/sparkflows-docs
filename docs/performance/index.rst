
Performance Tuning
==================

Performance is the cornerstone of any Big Data Processing. Fire is extremely optimized for best performance. Each of the Processors are written for extreme performance, the engine is optimized for the best performance.

There are certain things which need to be taken into account for any Spark job. Fire makes it extremely easy to apply them to a workflow.

.. panels::
    :container: container-lg pb-3

    :doc:`/performance/caching-level`

    Setting the right caching level of the dataset outputs of the nodes is very important for performance in Apache Spark.

    ---

    :doc:`/performance/runtime-resources`

    When running Apache Spark jobs, we can define the number of executors, executor memory and number of vCores per executor.

    ---  

    :doc:`/performance/repartition`

    Repartioning splits the datasets into the specified number of partitions.

    ---

    :doc:`/performance/debug-mode`

    Run the workflow in Debug mode which helps to know which Processor is exactly taking more time.

    ---

    :doc:`/performance/joins`

    Joins generally tend to be expensive operations. So it is important to tune them for performance.

.. toctree::
   :hidden:

   caching-level.rst
   runtime-resources.rst
   repartition.rst
   debug-mode.rst
   joins.rst
   
