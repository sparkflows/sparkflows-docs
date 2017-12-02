MapR specific details
---------------------

When running on a MapR cluster, the below are important:

* Download MapR specific binary.
* Administration / Configuration of Sparkflows
  * Turn off impersonation : Set app.impersonateUsers = false​
  * Set hdfs.namenodeURI = maprfs:///
  * Set spark-submit appropriately : spark.spark-submit = /opt/mapr/spark/xyz/bin/spark-submit
* Set http port to be different in conf/application.properties if there are other processes using the specified ports
* If you install sparkflows as mapr user
  * Create a mapr user in sparkflows and log in as that user​
  * Start using Sparkflows

