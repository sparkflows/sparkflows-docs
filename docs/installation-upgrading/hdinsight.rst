HDInsight Specific Details
==========================

Fire Insights can be installed on the master nodes.

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

Now port 8090 needs to be opened.

- https://stackoverflow.com/questions/45239566/accessing-http-on-custom-port-in-azure-hdinsight-cluster
