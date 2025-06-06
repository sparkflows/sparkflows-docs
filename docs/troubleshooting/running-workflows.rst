Running Workflows
=================

1. Error : Impersonation Exception for User
-----------------

**Problem**
+++++++++

Getting Exception: ::

 User: ec2-user is not allowed to impersonate ec2-user.

**Solution**
+++++

Sparkflows impersonates the logged in user when submitting the jobs onto the Cluster.

So, the user with which Sparkflows is running has to be configured on HDFS as a proxy user.

Details for allowing the Sparkflows user to impersonate other users can be updated in spark-submit connection.

For more information, `Read Sparkflows Documentation. <https://docs.sparkflows.io/en/latest/user-guide/connection/compute-connection/spark-submit.html>`_

2. Spark Cluster Workflow Execution: No Browser Results
------------------------------

**Problem**
++++++
When running the workflows on my Spark Cluster, results are not showing up in the Browser

**Solution**
+++++++++

This is probably because there is some configuration error. Sparkflows uses spark-submit to submit the jobs to the cluster. The driver of the spark job posts back results to the Fire server.

* Check out the log for spark-submit for the workflow in **/tmp/fire/workflowlogs** to find the root cause. Maybe the spark job is just failing.

* It is also useful to ensure Spark jobs can be submitted to the Cluster from the machine on which Sparkflows is running with spark-submit. 

  Submit the **SparkPi** job from **spark-examples.jar** to test it.

  * SparkPi can be run with a command like below: ::

     spark-submit --class org.apache.spark.examples.SparkPi --master yarn --deploy-mode client spark-examples.jar 10``
 
  * spark-examples.jar is in your Apache Spark install directory on the machine.
  
* If the Spark job is running successfully (according to the logs), but the results are still not showing up in the Browser, it could be because the fire spark job is unable to post results back to the Fire web server. You should see these failures in the logs.

  * Under **Administration/Configuration**, there is the config **app.postMessageURL**. It determines the Fire URL to which the results from the spark driver are posted back to the fire server. Ensure that it is set up correctly.

3. Access Control Exception: Permission Denied for User 'admin'
------------------------

**Problem**
++++++++

When running on the Cluster, you are running into the below exception: ::

 org.apache.hadoop.security.AccessControlException: Permission denied: user=admin, access=WRITE, inode="/user":hdfs:supergroup:drwxr-xr-x


**Solution**
++++++

If the above exception is coming up when running the workflow, then it means that the logged in user does not exist on HDFS.

* In the above case, the user is logged into Fire as **admin**. So the jobs submitted by Fire on the cluster is as the user **admin**. But the user **admin** does not exist on **HDFS**.

* Please make sure to log into Fire as a user which exists on HDFS.
  

4. Spark Cluster Issue: Example Workflow Unable to Locate Input Files
--------------------------------

**Problem**
+++++

When running the example workflows on the Spark Cluster it is not able to find the input files.

**Solution**
++++++++
The example workflows read in input files.

* The input files have to be on HDFS in the home directory of the logged in user. 
   
* The data directory which comes with Sparkflows has to be uploaded onto HDFS.

* For example, if the logged in user is **john**, then the data directory would be on HDFS in the directory **/user/john**.
  
5. HTTP 405 Exception: URL Response Code Issue with Spark Job Message  
--------------------------------

**Problem**
++++++

Getting Exception: ::

 Server returned HTTP response code: 405 for URL: http://10.125.221.72:8080/ messageFromSparkJob

**Solution**
+++++++

When submitting jobs to the cluster from Fire, you are running into the exception below::

  Sending 'POST' request to URL : http://10.125.221.72:8080/messageFromSparkJob

  Response Code : 405

  java.io.IOException: Server returned HTTP response code: 405 for URL: http://10.125.221.72:8080/messageFromSparkJob

  at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)

  at sun.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:62)

  at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)

  at java.lang.reflect.Constructor.newInstance(Constructor.java:423)

  at sun.net.www.protocol.http.HttpURLConnection$10.run(HttpURLConnection.java:1944)

  at sun.net.www.protocol.http.HttpURLConnection$10.run(HttpURLConnection.java:1939)


Fire submits Spark jobs to the cluster. The spark driver, posts certain results back to the Fire server to be displayed to the user.

The cause of this error is that the postback-url has not been set correctly - ``http://10.125.221.72:8080/messageFromSparkJob``

There could be following issues with the URL::

  The machine name/IP is wrong. It has to be the machine on which Fire is running.

  The port number is wrong. Fire server is running on another port on the machine.
  
6. ClassNotFoundException: WorkflowExecuteFromFile Not Found
----------------------------
**Problem**
++++++

Getting Exception: ::

 java.lang.ClassNotFoundException: fire.execute.WorkflowExecuteFromFile

**Solution**
++++++++++

When running the jobs on the cluster, you are running into the below exception: ::


  Warning: Local jar /home/ec2-user/fire-2.1.0/fire-lib/fire-spark_1_6-core-2.1.0-jar-with-dependencies.jar does not exist, skipping.
  java.lang.ClassNotFoundException: fire.execute.WorkflowExecuteFromFile at java.net.URLClassLoader.findClass(URLClassLoader.java:381) at 
  java.lang.ClassLoader.loadClass(ClassLoader.java:424) at java.lang.ClassLoader.loadClass(ClassLoader.java:357) at
  java.lang.Class.forName0(Native Method) at java.lang.Class.forName(Class.java:348) at
  org.apache.spark.util.Utils$.classForName(Utils.scala:177) at
  org.apache.spark.deploy.SparkSubmit$.org$apache$spark$deploy$SparkSubmit$$runMain(SparkSubmit.scala:688) at
  org.apache.spark.deploy.SparkSubmit$$anon$1.run(SparkSubmit.scala:163) at 
  org.apache.spark.deploy.SparkSubmit$$anon$1.run(SparkSubmit.scala:161) at java.security.AccessController.doPrivileged(Native Method) at 
  javax.security.auth.Subject.doAs(Subject.java:422) at
  org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1917) at 
  org.apache.spark.deploy.SparkSubmit$.doRunMain$1(SparkSubmit.scala:161) at
  org.apache.spark.deploy.SparkSubmit$.submit(SparkSubmit.scala:206) at org.apache.spark.deploy.SparkSubmit$.main(SparkSubmit.scala:121) at 
  org.apache.spark.deploy.SparkSubmit.main(SparkSubmit.scala)

* The reason for it is that the **app.sparkSubmitJar** is not set up correctly. Fire comes with a JAR file which gets submitted to the cluster with spark-submit. **app.sparkSubmitJar** has to correctly point to this JAR file.
  
* You can go under **Administration/Configuration** to set it up correctly.



  
7. Getting Exception on HDInsight : No FileSystem for scheme: wasbs
----------------------------------------------------------------
**Problem**
++++++

Running into the  below exception when running the jobs on the cluster: ::

  Error : java.io.IOException: No FileSystem for scheme: wasbs at   
  org.apache.hadoop.fs.FileSystem.getFileSystemClass(FileSystem.java:2586) at 
  org.apache.hadoop.fs.FileSystem.createFileSystem(FileSystem.java:2593) at 
  org.apache.hadoop.fs.FileSystem.access$200(FileSystem.java:91) at 
  org.apache.hadoop.fs.FileSystem$Cache.getInternal(FileSystem.java:2632)

**Solution**
+++++++

* The reason for it is that it is not understanding the scheme **wasb**. In order to fix it, run **./run-fire-spark-submit.sh start** instead of **./run-fire.sh start**.
* This enables getting the distribution libraries into the executable.


8. Exception in H2O Workflows: XgBoost Model Training Issue
------------------------
  
**Problem**
+++++++
When other H2O models run fine but XgBoost fails with the below error::

  Received an Exception : ai.h2o.sparkling.backend.exceptions.RestApiCommunicationException: H2O node http://10.111.112.202:54321 responded with
  Status code: 404 : Not Found
  Server error: {\__meta\:{\schema_version\:3,\schema_name\:\H2OErrorV3\,\schema_type\:\H2OError\},\timestamp\:1695017495408,\error_url\:\POST /3/ModelBuilders/xgboost\,\msg\:\\


**Solution**
+++++++++

The most likely reason is that the base OS is blocking the REST API of xgboost. Usually happens on hardened system or when the hardware does not supports XgBoost like Windows or Apple M1.

The below can be used to check if the XgBoost is supported on the current deployment or not::

  from ai.h2o.sparkling import H2OContext
  from pyspark.sql import SparkSession
  from h2o.estimators.xgboost import H2OXGBoostEstimator
  spark = SparkSession.builder.appName("SparklingWaterApp").getOrCreate()
  hc = H2OContext.getOrCreate()
  is_xgboost_available = H2OXGBoostEstimator.available()
  print("is_xgboost_available:", is_xgboost_available)

9. Exception on Saving Apache Spark workflows
--------------------------

**Problem**
++++++++

When Spark model saving fails with the below Snappy error::

   org.apache.spark.SparkException: Task failed while writing rows.
   at org.apache.spark.sql.errors.QueryExecutionErrors$.taskFailedWhileWritingRowsError(QueryExecutionErrors.scala:500)
   at org.apache.spark.sql.execution.datasources.FileFormatWriter$.executeTask(FileFormatWriter.scala:321)
   at org.apache.spark.sql.execution.datasources.FileFormatWriter$.$anonfun$write$16(FileFormatWriter.scala:229)
   at org.apache.spark.scheduler.ResultTask.runTask(ResultTask.scala:90)
   at org.apache.spark.scheduler.Task.run(Task.scala:131)
   at org.apache.spark.executor.Executor$TaskRunner.$anonfun$run$3(Executor.scala:506)
   at org.apache.spark.util.Utils$.tryWithSafeFinally(Utils.scala:1462)
   at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:509)
   at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
   at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
   at java.lang.Thread.run(Thread.java:750)\nCaused by: java.lang.IllegalArgumentException
   at java.nio.Buffer.limit(Buffer.java:275)
   at org.xerial.snappy.Snappy.compress(Snappy.java:156)

**Solution**
+++++++++

The most likely reason is that the OS is a hardened version and is missing the below packages. Install them by running the below commands::

   sudo apt-get update -y

::

   sudo apt-get install -y libsnappy-dev


10. Getting Hangs on Training H2O Models on Big Data but Not on Small Data
------------------------------------------------------------------------------------------------------------

**Problem**
+++++

When H2O model training hangs with the last few lines of log like below::

   09-27 08:05:46.957 172.31.54.165:54321   #4311  8988233-62  INFO water.default: POST /3/InitializeFrame, parms: {key=frame_rdd_5-639583683, columns=["Col1","Col2","Col3","Col4","Col5","Col6","Col7","Col8","Col9","Col10","Col11","Col2"]}
   09-27 08:05:47.014 172.31.54.165:54321   #4311        main  INFO ai.h2o.sparkling.H2OFrame: H2O node http://172.31.54.165:54321/3/InitializeFrame successfully responded for the POST.
   09-27 08:05:54.459 172.31.54.165:54321   #4311  8988233-55  INFO water.default: GET /3/UploadPlan, parms: {number_of_chunks=3}
   09-27 08:05:54.476 172.31.54.165:54321   #4311        main  INFO ai.h2o.sparkling.H2OFrame: H2O node http://172.31.54.165:54321/3/UploadPlan?number_of_chunks=3 successfully responded for the GET.

**Solution**
++++++

The most likely reason is that the OS is a hardened version and is missing the below packages. Install them by running the below commands::

   sudo apt-get update -y

::

   sudo apt-get install libsnappy1v5

10. Error : An error occured OutofmemoryError Java heap space on Sklearn model in PySpark
-----------------

**Problem**
+++++++++

Getting Exception: ::

 An error occured OutofmemoryError Java heap space, while using Sklearn model in PySpark with large data size.

**Solution**
+++++

Sparkflows by default uses default configuration for ``1g`` for driver-memory in pyspark-shell.

you can run below export command and start Sparkflows server:

::

    export PYSPARK_SUBMIT_ARGS="--driver-memory 4g pyspark-shell"

