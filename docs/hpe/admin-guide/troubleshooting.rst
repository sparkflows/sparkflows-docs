Troubleshooting
=========

1. Facing Issues while saving to Data Fabric
------
**Problem**
++++++

I see below error:

::

    An error occurred while calling o114.csv.
    org.apache.spark.SparkException- Job aborted.
    at org.apache.spark.sql.errors.QueryExecutionErrors$.jobAbortedError(QueryExecutionErrors.scala-651)
    at org.apache.spark.sql.execution.datasources.FileFormatWriter$.write(FileFormatWriter.scala-288)
    at org.apache.spark.sql.execution.datasources.InsertIntoHadoopFsRelationCommand.run(InsertIntoHadoopFsRelationCommand.scala-186)
    at org.apache.spark.sql.execution.command.DataWritingCommandExec.sideEffectResult$lzycompute(commands.scala-113)
    at org.apache.spark.sql.execution.command.DataWritingCommandExec.sideEffectResult(commands.scala-111)
    at org.apache.spark.sql.execution.command.DataWritingCommandExec.executeCollect(commands.scala-125)
    at org.apache.spark.sql.execution.QueryExecution$$anonfun$eagerlyExecuteCommands$1.$anonfun$applyOrElse$1(QueryExecution.scala-98)


**Solution**
++++++++++

Do check in the logs for exceptions and the root cause. The log files can be analysed from Livy url.

Also make sure that below configuration is passed in Livy Connection inside ``Conf`` value:

::

    spark.hadoop.mapreduce.fileoutputcommitter.algorithm.version=2
    spark.hadoop.mapreduce.fileoutputcommitter.cleanup-failures.ignored=true
    spark.hadoop.mapreduce.fileoutputcommitter.cleanup-succeed.enabled=true
    spark.hadoop.fs.s3a.committer.name=directory
    spark.hadoop.fs.s3a.committer.magic.enabled=true

or you can pass below parameter from workflow execute page too

::

    --conf spark.hadoop.mapreduce.fileoutputcommitter.algorithm.version=2
    --conf spark.hadoop.mapreduce.fileoutputcommitter.cleanup-failures.ignored=true
    --conf spark.hadoop.mapreduce.fileoutputcommitter.cleanup-succeed.enabled=true
    --conf spark.hadoop.fs.s3a.committer.name=directory
    --conf spark.hadoop.fs.s3a.committer.magic.enabled=true



2. Facing Issues with running h2o with AutoML on Livy
------
**Problem**
++++++

I see below error:

::

    Could not establish link to the H2O cloud http-//sandbox-datafabric.internal.cloudapp.net-54323 after 5 retries\n[46-21.68] H2OConnectionError- Timeout after 3.010s\n[46-24.89] H2OConnectionError- Timeout after 3.013s\n[46-28.10] H2OConnectionError- Timeout after 3.010s\n[46-31.33] H2OConnectionError- Timeout after 3.021s\n[46-34.54] H2OConnectionError- Timeout after 3.010s



**Solution**
++++++++++

Do check in the logs for exceptions and the root cause. The log files can be analysed from Livy url.

Also make sure that below configuration is passed in Livy Connection inside ``Conf`` value:

::

    spark.h2o.backend:internal,spark.executor.memory:4g,spark.executor.cores:2


3. Facing Issues with running h2o workflow on Livy
------
**Problem**
++++++

I see below error:

::

    ai.h2o.sparkling.backend.exceptions.RestApiNotReachableException: H2O node http://10.2.0.10:54321 is not reachable.


**Solution**
++++++++++

Do check in the logs for exceptions and the root cause. The log files can be analysed from Livy url.

Also make sure that below configuration is passed in Livy Connection inside ``Conf`` value:

::

    spark.h2o.backend:internal,spark.executor.memory:4g,spark.executor.cores:2
