Connecting to Apache Spark Cluster
==================================

Fire can be configured to submit the spark jobs to run on an Apache Spark Cluster.
 
* **Install Fire on an edge node of your Apache Spark Cluster. The edge node has the hadoop/hive/spark configuration files set up. You should already be able to run your spark jobs from this node using spark-submit.**
* **Update the below configurations under the menu, ``Administration/Configuration``** 


.. note:: In order for Fire to connect to the Apache Spark Cluster, it needs to be installed as a user which can impersonate other users. More details are below in the page. For the rest of the documentation on this page, we assume that it has been installed as the user ``sparkflows``.


Infer Hadoop Configs
--------------------

**Infer Hadoop Configs** button under Configuration automatically infers some of the configurations of the cluster from the hadoop config files on the edge node to help with the process. Use it to get the initial set of configurations.

.. figure:: ../_assets/installation/infer-hadoop-configs.png
   :scale: 100%
   :alt: Infer Hadoop Configs
   :align: center


Fire Configurations for connecting to an Apache Spark Cluster
-------------------------------------------------------------

Below are the configuration details for connecting Fire to an Apache Spark Cluster.

+--------------------+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Parameter**      | **Value**                                                                  | **Description**                                                                                                                                                                                                                   |
+--------------------+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| app.runOnCluster   | true                                                                       | Indicate to run on the spark cluster. By default it is set to false                                                                                                                                                               |
+--------------------+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| app.postMessageURL | http://localhost:8080/messageFromSparkJob                                  | Indicate the URL on fire server which receives messages from the spark jobs running on the cluster. Set localhost to the machine name on which Fire is running. Replace 8080 with the port number on which Fire is running. |
+--------------------+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| app.sparkSubmitJar | /user/centos/fire-1.4.3/fire-lib/fire-core-1.4.3-jar-with-dependencies.jar | fire-lib directory of the Sparkflows install contains the fire core jar used in submitting the workflows to the Spark cluster. Set it correctly to be the absolute path of the fire core jar.                                     |
+--------------------+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hdfs.namenodeURI   | hdfs://localhost:8020                                                      | Update the hdfs namenode URI. Set localhost to the machine on which the namenode is running. Set it to maprfs:/// for mapr                                                                                                       |
+--------------------+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hdfs.namenodeURI   | file://                                                                    | Set it to file:// when the files are on the local filesystem. This can be the case when HDFS is not there.                                                                                                                        |
+--------------------+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hive.JDBC_DB_URL   | jdbc:hive2://localhost:10000                                               | Update the hive JDBC DB URL if you would be accessing HIVE from Sparkflows. This is the URL of the HiveServer 2 server.                                                                                                           |
+--------------------+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| spark.sql-context  | HIVEContext                                                                | Set it to either HIVEContext or SQLContext based on whether you want to use HIVEContext or SQLContext in your job. Use HIVEContext if you would be accessing the HIVE tables.                                                     |
+--------------------+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| spark.master       | yarn                                                                       | Set it to yarn for connecting to a spark cluster running YARN                                                                                                                                                                     |
+--------------------+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| spark.master       | spark://spark_master_hostname:port                                         | Set it to the spark master URL when connecting to a spark cluster running in standalone mode. Port is normally 7077.                                                                                                              |
+--------------------+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| spark.spark-submit | spark-submit                                                               | Spark Submit command for submitting the Spark jobs to the cluster. It can be spark2-submit for Spark2 CDH clusters. Make sure to provide the full path or spark-submit should be in the path.                                     |
+--------------------+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Create Users in Fire
--------------------

Fire allows creating multiple users. Create the users in Fire under ``Administration/Users`` who would be building and running workflows.

``These users have to exist on HDFS. So ensure that these users exist on HDFS``


Update core-site.xml of Hadoop to allow sparkflows user to impersonate
----------------------------------------------------------------------


https://www.cloudera.com/documentation/enterprise/5-8-x/topics/admin_hdfs_proxy_users.html


* In your core-site.xml file for Hadoop, allow sparkflows user to impersonate other users. Without impersonation enabled for this user, your Sparkflows application users trying to run jobs against a hadoop cluster would not be able to do so. 
 
* Also, allow the appropriate groups that the sparkflows users will be able to impersonate belong to.

* In the following example snippet, user ``sparkflows`` is allowed to impersonate users from hosts ``host1`` and ``host2``.  The users being impersonated belong to the groups ``hive,hfs,hadoop,spark``. Your permissions are likely going to be different and more restrictive. 

Below is an example::


  <property>
     <name>hadoop.proxyuser.sparkflows.hosts</name>
     <value>host1,host2</value>
  </property>

  <property>
     <name>hadoop.proxyuser.sparkflows.groups</name>
     <value>hive,hfs,hadoop,spark</value>
   </property>
 

Cloudera Manager
^^^^^^^^^^^^^^^^

If you are using Cloudera Manager, you can set the above settings for impersonation in ``HDFS/Configuration``.

.. figure:: ../_assets/installation/cloudera-manager-hdfs-configuration.png
   :scale: 100%
   :alt: Cloudera Configs
   :align: center
   
   
Ambari
^^^^^^

If you are using Ambari, you can set the above settings for impersonation in ``HDFS/Configuration under Custom core-site``

.. figure:: ../_assets/installation/ambari-hdfs-configuration.png
   :scale: 100%
   :alt: Ambari Configs
   :align: center
   
   
 
 




