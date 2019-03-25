HDInsight Specific Details
==========================

Fire Insights runs seamlessly on Azure HDInsight.

Fire can be installed on the master or edge nodes of the cluster.

HDInsights and Ports
--------------------

https://docs.microsoft.com/en-us/azure/hdinsight/hdinsight-hadoop-port-settings-for-services

Linux-based HDInsight clusters only expose three ports publicly on the internet; 22, 23, and 443. These ports are used to securely access the cluster using SSH and services exposed over the secure HTTPS protocol.

Internally, HDInsight is implemented by several Azure Virtual Machines (the nodes within the cluster) running on an Azure Virtual Network. From within the virtual network, you can access ports not exposed over the internet. For example, if you connect to one of the head nodes using SSH, from the head node you can then directly access services running on the cluster nodes.

To join additional machines to the virtual network, you must create the virtual network first, and then specify it when creating your HDInsight cluster. For more information, see Extend HDInsight capabilities by using an Azure Virtual Network

https://docs.microsoft.com/en-us/azure/hdinsight/hdinsight-extend-hadoop-virtual-network


Port Configuration
------------------

Fire Insights by default listens on ports 8080 and 8443.

On HDInsight, port 8080 generally is already in use. So configure Fire Insights to listen on another port, say 8090.

Edit conf/application.properties::

    #Configure http and https port numbers : Default 8080 for http and 8443 for https
    http.port=8090
    https.port=8443
    
    
Open the Port for access
------------------------

Now the port 8090 needs to be opened to be accessed by the users using their Browser.

- https://stackoverflow.com/questions/45239566/accessing-http-on-custom-port-in-azure-hdinsight-cluster


Connecting Fire Insights to the HDInsight Cluster
----------------------------

In Fire Insights, under Administration/Configuration, configure the following for it to be able to connect to the HDInsight cluster.

* hdfs.namenodeURI=wasb://
* app.runOnCluster=true
* app.postMessageURL=
* app.sparkSubmitJar=

Clicking on ``Infer Hadoop Configuration`` would correctly infer these. Hit ``Save`` after that.



