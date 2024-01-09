Workflow Execution
==================

How does Apache Spark's distributed execution affect the number of output files, and what method ensures saving the result in only one file?
--------------

Apache Spark runs distributed. As a result the data is partitioned across multiple process/machines.

When any of the **Save nodes** is used to write the output to files, the number of files created is dependent on the number of partitions of the data in the Spark Job.

If you want to write out the result to only one file, use the **Coalesce node** to convert the DataFrame to just one partition, before using the Save node.
