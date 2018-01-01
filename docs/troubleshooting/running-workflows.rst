Running Workflows
=================


Getting Exception : 'User: ec2-user is not allowed to impersonate ec2-user
--------------------------------------------------------------------------

Sparkflows impersonates the logged in user when submitting the jobs onto the Cluster.

So, the user with which Sparkflows is running has to be configured on HDFS as a proxy user.

Details for allowing the sparkflows user to impersonate other users is available at : https://www.sparkflows.io/connecting-sparkflows-with-spark-cl



When running the workflows on my Spark Cluster, results are not showing up in the Browser
-----------------------------------------------------------------------------------------

This is probably because there is some configuration error. Sparkflows uses spark-submit to submit the jobs to the cluster. The driver of the spark job posts back results to the Fire server.

* Check out the log for spark-submit for the workflow in /tmp/fire/workflowlogs to find the root cause. Maybe the spark job is just failing.

* It is also useful to ensure Spark jobs can be submitted to the Cluster from the machine on which Sparkflows is running with spark-submit. Submit the SparkPi job from spark-examples.jar to test it.

* If the Spark job is running successfully (according to the logs), but the results are still not showing up in the Browser, it could be because the fire spark job is unable to post results back to the Fire web server. You should see these failures in the logs.

* Under Administration/Configuration, there is the config app.postMessageURL. It determines the Fire URL to which the results from the spark driver are posted. Ensure that it is set up correctly.
