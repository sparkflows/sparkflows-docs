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

Also make sure that below configuration is passed in Livy Connection:

::

    --conf spark.hadoop.mapreduce.fileoutputcommitter.algorithm.version=2
    --conf spark.hadoop.mapreduce.fileoutputcommitter.cleanup-failures.ignored=true
    --conf spark.hadoop.mapreduce.fileoutputcommitter.cleanup-succeed.enabled=true
    --conf spark.hadoop.fs.s3a.committer.name=directory
    --conf spark.hadoop.fs.s3a.committer.magic.enabled=true

