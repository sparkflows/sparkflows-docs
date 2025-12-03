Scalability
===========

Overview
--------

Sparkflows is architected to scale horizontally both for the number of users and number of jobs.

Sparkflows achieves this in a few ways:

* Sparkflows can be installed on one or more machines. They can be running in Kubernetes or behind a load balancer.
* All of the instances connect to an RDBMS (RDS, MySQL, Postgres etc.). The external RDBMS can be scaled up as needed. Sparkflows only stores the metadata into the RDBMS and hence its size is small.
* Sparkflows pushes all compute to the cluster. The cluster can be Databricks, AWS EMR, AWS Glue, Cloudera, Azure HDInsights, Google Data Proc, Apache Spark Standalone, Kubernetes etc. Since, all compute is pushed to the cluster which can be scaled horizontally, Sparkflows scales horizontally end to end.


Maintenance
-----------

Sparkflows stores the metadata of the various executions in the RDBMS. This is the only data that can grow relatively large. 

This can be easily managed by:

* Scaling up the size of the RDBMS as needed.
* Configuring Sparkflows to delete old tasks.


Number of Parallel Users
------------------------

All the pages in Sparkflows are built to be fast and lean. Let us take the following scenario:

* Development environment in which many users are logging in and creating and executing workflows and pipelines.
* QA environment in which the QA is testing out the various projects. Not much workflow editing is happening in this environment. 
* Production environment in which the scheduled jobs are executing. They could also be getting triggers by external programs or events. Not much workflow editing is happening in this environment. However, many jobs are getting executed on an hourly basis.

Each development instance of Sparkflows can handle 200-500 users, assuming 30+ GB of RAM and 10+ vCPU cores for the machine. As the number of users increase, the size of the machine can be increased or more machines added. 

Each production instance can handle thousands of jobs running hourly. For high workload environments 30+ GB of RAM is recommended per instance. Also a scaled up RDBMS is recommended.


Caching, Performance and Scalability
----------------

Sparkflows caches the records in both the web server layer and in the backend, for the workflow editor. This results in sub-second response times and also scalability of the end to end system.

Pushdown
--------

Sparkflows is built to push down all compute to the cluster. The jobs also run distributed in the cluster. The clusters provide their own queuing mechanisms. They can also be easily scaled up and down automatically. Thus, Sparkflows seamlessly scales for all compute needs.





