Troubleshooting
===============
I do not see anything in my browser after I start Sparkflows.
-------------------------------------------------------------

Do check in the logs for exceptions and the root cause. On Linux & Mac, the log files are in nohup.out. Possible causes are:

The H2 database was not created and it is failing to the find the table.
The server did not start properly because some other Application is running on the configured port. The default configured port for Sparkflows is :8080

Sparkflows UI does not get displayed when I go to :8080. Some other UI is displayed
-----------------------------------------------------------------------------------
Sparkflows by default runs on port 8080. It is possible that you have some other application running on port 8080, and you are seeing its output.

The solution is to run Sparkflows on some other port which is not being used by any other application.
Details here : https://www.sparkflows.io/run-fire-on-different-port

When running on a Spark Cluster, I am getting the exception 'User: ec2-user is not allowed to impersonate ec2-user
------------------------------------------------------------------------------------------------------------------
Sparkflows impersonates the logged in user when submitting the jobs onto the Cluster. So, the user with which Sparkflows is running has to be configured on HDFS as a proxy user.

Details for allowing the sparkflows user to impersonate other users is available at : https://www.sparkflows.io/connecting-sparkflows-with-spark-cl

Where do I find the logs of the workflows when running on my Cluster
--------------------------------------------------------------------
The logs are in /tmp/fire/workflowlogs directory on the machine on which Sparkflows is running. Each workflow execution has its own log file.

The json representation of the workflow is in /tmp/fire/workflows

My cluster is Kerberised. How do I setup Sparkflows for it.
-----------------------------------------------------------
The steps to setup Sparkflows on a Kerberised cluster are here : https://www.sparkflows.io/kerberos

When running the workflows on my Spark Cluster, nothing is happening
--------------------------------------------------------------------
This is probably because there is some configuration error. Sparkflows uses spark-submit to submit the jobs to the cluster.

Check out the log for spark-submit for the workflow in /tmp/fire/workflowlogs to find the root cause.

It is also useful to ensure Spark jobs can be submitted to the Cluster from the node on which Sparkflows is running with spark-submit. Submit the Pi job from spark examples to test it.

If the Spark job is running successfully (according to the logs), but the results are still not showing up in the Browser, it could be because the fire spark job is unable to post results back to the Sparkflows web server. You should see these failures in the logs.

Under Administration/Configuration, there is the config app.postMessageURL. It determines the Sparkflows URL to which the results from the spark driver are posted.

I am getting an error when clicking 'Update' button on the Create/Update Dataset page.
--------------------------------------------------------------------------------------
You may see the error below:

Unable to retrieve schema for this path :: Bad header for field, should start with a character or _ and can contain only alphanumerics and _ 0:" id 1 "

This is because one of the column names of the header is not in the right format. In this case "id 1" column contains a space.

Only alphanumerics and _ are permitted in the header and column names.

If your data does not have a header column, set the "Header" field to "false".

When I am running the workflow on the cluster, I get 'Running on Cluster' and nothing happens
---------------------------------------------------------------------------------------------
There could be a few reasons for this. Check the log file under /tmp/fire/workflowlogs. It would show you an exception indicating the root cause.

Most common causes are:

- Under Administration/Configuration, app.sparkSubmitJar is not set correctly. The jar file does not exist. In this case you would get ClassNotFound exception in your log file.

- Under Administration/Configuration, app.postMessageURL is not set correctly. Make sure that the machine and port number are set correctly to the machine on which Sparkflows is running. The spark job posts messages to this URL to be displayed in the user's browser.

When running a Workflow on the cluster I am getting an Exception
----------------------------------------------------------------
org.apache.hadoop.security.AccessControlException: Permission denied: user=admin, access=WRITE, inode="/user":hdfs:supergroup:drwxr-xr-x

If the above exception is coming up when running the workflow, then it means that the logged in user does not exist on HDFS.

In the above case, the user is logged into Fire as 'admin'. So the jobs submitted by Fire on the cluster is as the user 'admin'. But the user 'admin' does not exist on HDFS.

Please make sure to log into Fire as a user which exists on HDFS.

When running the example workflows on the Spark Cluster it is not able to find the input files
----------------------------------------------------------------------------------------------
The example workflows read in input files. They have to be on HDFS in the home directory of the logged in user. The data directory which comes with Sparkflows has to be uploaded onto HDFS.

For example, if the logged in user is 'john', then the data directory would be on HDFS in the directory /user/john
