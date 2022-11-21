Scalability
===========

Fire Insights is build to scale horizontally for the number of users and number of jobs which can be run.

Fire Insights achieves this in a few ways:

* Fire Insights can be installed on one or more machines. They can be running in Kubernetes or behind a load balancer.
* All of the instances connect to an RDBMS (RDS, MySQL, Postgress etc.). The external RDBMS can be scaled up as needed. Fire Insights only store the metadata into the RDBMS and hence its size is small.
* Fire Insights pushes all compute to the cluster. The cluster can be Databricks, AWS EMR, AWS Glue, Cloudera, Azure HDInsights, Google Data Proc, Apache Spark Standalone, Kubernetes etc. Since, all compute is pushed to the cluster which can be scaled horizontally, Fire Insights scales horizontally end to end.
