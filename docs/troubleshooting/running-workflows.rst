Running Workflows
=================


Getting Exception : 'User: ec2-user is not allowed to impersonate ec2-user
--------------------------------------------------------------------------

Sparkflows impersonates the logged in user when submitting the jobs onto the Cluster.

So, the user with which Sparkflows is running has to be configured on HDFS as a proxy user.

Details for allowing the sparkflows user to impersonate other users is available at:

* :doc:`../installation/configuration/connecting-spark-cluster`


When running the workflows on my Spark Cluster, results are not showing up in the Browser
-----------------------------------------------------------------------------------------

This is probably because there is some configuration error. Sparkflows uses spark-submit to submit the jobs to the cluster. The driver of the spark job posts back results to the Fire server.

* Check out the log for spark-submit for the workflow in ``/tmp/fire/workflowlogs`` to find the root cause. Maybe the spark job is just failing.

* It is also useful to ensure Spark jobs can be submitted to the Cluster from the machine on which Sparkflows is running with spark-submit. Submit the ``SparkPi`` job from ``spark-examples.jar`` to test it.

  * ``SparkPi`` can be run with a command like : ``spark-submit --class org.apache.spark.examples.SparkPi --master yarn --deploy-mode client spark-examples.jar 10``
  * ``spark-examples.jar`` is in your Apache Spark install direction on the machine.
  
* If the Spark job is running successfully (according to the logs), but the results are still not showing up in the Browser, it could be because the fire spark job is unable to post results back to the Fire web server. You should see these failures in the logs.

  * Under Administration/Configuration, there is the config ``app.postMessageURL``. It determines the Fire URL to which the results from the spark driver are posted back to the fire server. Ensure that it is set up correctly.


Getting Exception: org.apache.hadoop.security.AccessControlException: Permission:denied : user=admin 
-----------------------------------------------------------------------------------------------------

When running on the Cluster, you are running into the exception below::

  org.apache.hadoop.security.AccessControlException: Permission denied: user=admin, access=WRITE, inode="/user":hdfs:supergroup:drwxr-xr-x

* If the above exception is coming up when running the workflow, then it means that the logged in user does not exist on HDFS.

* In the above case, the user is logged into Fire as ``admin``. So the jobs submitted by Fire on the cluster is as the user ``admin``. But the user 'admin' does not exist on HDFS.

* Please make sure to ``log into Fire as a user which exists on HDFS``.
  
  
When running the example workflows on the Spark Cluster it is not able to find the input files
-----------------------------------------------------------------------------------------------

The example workflows read in input files.

* They have to be on HDFS in the home directory of the logged in user. 
   
* The data directory which comes with Sparkflows has to be uploaded onto HDFS.

* For example, if the logged in user is ``john``, then the data directory would be on HDFS in the directory ``/user/john``
  
  
Getting Exception : Server returned HTTP response code: 405 for URL: http://10.125.221.72:8080/ messageFromSparkJob
--------------------------------------------------------------------------------------------------------------------
  
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
  
  
Getting Exception : java.lang.ClassNotFoundException: fire.execute.WorkflowExecuteFromFile
------------------------------------------------------------------------------------------

When running the jobs on the cluster, you are running into the exception below.

* The reason for it is that the ``app.sparkSubmitJar`` is not set up correctly. Fire comes with a jar file which gets submitted to the cluster with spark-submit. app.sparkSubmitJar has to correctly point to this jar file.
  
* You can go under ``Administration/Configuration`` to set it up correctly.


Exception::

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
  
Getting Exception on HDInsight : No FileSystem for scheme: wasbs
----------------------------------------------------------------

When running the jobs on the cluster, you are running into the exception below.

* The reason for it is that it is not understanding the scheme ``wasb``. In order to fix it, run ``./run-fire-spark-submit.sh start`` instead of ``./run-fire.sh start``.
* This enables getting the distribution libraries into the executable.

Exception::

  Error : java.io.IOException: No FileSystem for scheme: wasbs at   
  org.apache.hadoop.fs.FileSystem.getFileSystemClass(FileSystem.java:2586) at 
  org.apache.hadoop.fs.FileSystem.createFileSystem(FileSystem.java:2593) at 
  org.apache.hadoop.fs.FileSystem.access$200(FileSystem.java:91) at 
  org.apache.hadoop.fs.FileSystem$Cache.getInternal(FileSystem.java:2632)

Getting Exception on running H2O workflows only when building XgBoost models. Other models get trained fine:
------------------------------------------------------------------------------------------------------------

When other H2O models run fine but XgBoost fails with the below error::

  Received an Exception : ai.h2o.sparkling.backend.exceptions.RestApiCommunicationException: H2O node http://10.111.112.202:54321 responded with
  Status code: 404 : Not Found
  Server error: {\__meta\:{\schema_version\:3,\schema_name\:\H2OErrorV3\,\schema_type\:\H2OError\},\timestamp\:1695017495408,\error_url\:\POST /3/ModelBuilders/xgboost\,\msg\:\\

The most likely reason is that the base OS is blocking the REST API of xgboost. Usually happens on hardened system or when the hardware does not supports XgBoost like Windows or Apple M1.

The below can be used to check if the XgBoost is supported on the current deployment or not::

  from ai.h2o.sparkling import H2OContext
  from pyspark.sql import SparkSession
  from h2o.estimators.xgboost import H2OXGBoostEstimator
  spark = SparkSession.builder.appName("SparklingWaterApp").getOrCreate()
  hc = H2OContext.getOrCreate()
  is_xgboost_available = H2OXGBoostEstimator.available()
  print("is_xgboost_available:", is_xgboost_available)
