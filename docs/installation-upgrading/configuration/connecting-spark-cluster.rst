Connecting Fire with Apache Spark Cluster
-----------------------------------------

Fire can be configured to submit the spark jobs to run on an Apache Spark Cluster.
 
* Install Fire on an edge node of your Apache Spark Cluster. The edge node has the hadoop/hive/spark configuration files set up. You should already be able to run your spark jobs from this node using spark-submit.
* Update the below configurations under the menu, Administration/Configuration 

**Note: In order for Fire to connect to the Apache Spark Cluster, it needs to be installed as a user which can impersonate other users. More details are below in the page. For the rest of the documentation on this page, we assume that it has been installed as the user 'sparkflows'.**

**Infer Hadoop Configs** button under Configuration automatically infers some of the configurations of the cluster from the hadoop config files on the edge node to help with the process. Use it to get the initial set of configurations.







