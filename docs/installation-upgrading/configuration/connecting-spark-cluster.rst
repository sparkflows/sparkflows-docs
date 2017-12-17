Connecting to Apache Spark Cluster
----------------------------------

Fire can be configured to submit the spark jobs to run on an Apache Spark Cluster.
 
* Install Fire on an edge node of your Apache Spark Cluster. The edge node has the hadoop/hive/spark configuration files set up. You should already be able to run your spark jobs from this node using spark-submit.
* Update the below configurations under the menu, Administration/Configuration 

**Note: In order for Fire to connect to the Apache Spark Cluster, it needs to be installed as a user which can impersonate other users. More details are below in the page. For the rest of the documentation on this page, we assume that it has been installed as the user 'sparkflows'.**

**Infer Hadoop Configs** button under Configuration automatically infers some of the configurations of the cluster from the hadoop config files on the edge node to help with the process. Use it to get the initial set of configurations.

.. figure:: ../../_assets/installation/infer-hadoop-configs.png
   :scale: 100%
   :alt: Infer Hadoop Configs
   :align: center


**Configurations for connecting Fire to an Apache Spark Cluster**

Below are the configuration details for connecting Fire to an Apache Spark Cluster.


**Update core-site.xml of Hadoop to allow sparkflows user to impersonate**

https://www.cloudera.com/documentation/enterprise/5-8-x/topics/admin_hdfs_proxy_users.html


In your core-site.xml file for Hadoop, allow sparkflows user to impersonate other users. Without impersonation enabled for this user, your Sparkflows application users trying to run jobs against a hadoop cluster would not be able to do so. 
 
Also, allow the appropriate groups that the sparkflows users will be able to impersonate belong to.

In the following example snippet, user “sparkflows” is allowed to impersonate users from hosts “host1” and host2”.  The users being impersonated belong to the groups hive,hfs,hadoop,spark. Your permissions are likely going to be different and more restrictive. 

Below is an example::


  <property>
     <name>hadoop.proxyuser.sparkflows.hosts</name>
     <value>host1,host2</value>
  </property>

  <property>
     <name>hadoop.proxyuser.sparkflows.groups</name>
     <value>hive,hfs,hadoop,spark</value>
   </property>
 

**Cloudera Manager**

If you are using Cloudera Manager, you can set the above settings in HDFS/Configuration.

**Ambari**

If you are using Ambari, you can set the above settings in HDFS/Configuration under Custom core-site

 
 




