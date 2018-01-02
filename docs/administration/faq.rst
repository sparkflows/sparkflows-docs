FAQ
---

``Does Sparkflows allow me to create my own custom nodes?``

Yes, new Nodes can be easily to added to SparkFlows. Develop nodes in Java or in Scala and dop the definition JSON for the node on the server. The newly added nodes will become visible in the Sparkflows User Interface.


``How can I schedule the workflows I create ?``

Sparkflows saves workflow definitions as JSON files. These workflows are executed through spark-submit.

Sparkflows platform does not have its own scheduling capabilities implemented at this time but its on our roadmap. As of now, users can schedule Sparkflows workflows using their preferred scheduling systems.


``Can I run Sparkflows on my Amazon AWS cluster or Microsoft Azure or Google Cloud?``

Yes, all Sparkflows needs for successful deployment is a Apache Spark cluster. Sparkflows is deployed on the edge node of the cluster.


``Can I invoke a workflow from within another workflow?``

No, Sparkflows at this time does not allow triggering one workflow from another. But stayput, this capability will be added to the product during one of the new few iterations. 


``What distributions or platforms are supported with Sparkflows?``

Sparkflows Fire has been tested with CDH, AWS EMR, Databricks Apache Spark distributions.
 
Note: Any cluster with Apache Spark 1.6+ will work fine with Sparkflows.


``How does the Sparkflows platform handle multi-user support (i.e. Can user 1 see or edit user 2’s data sources, pipelines, etc)``

Sparkflows supports various user types and enables users to easily share datasets and workflows with each other to foster collaboration.

``Do Sparkflows workflow nodes write to an audit log that is accessible by users of the system?``


``How does one export/import workflows between instances?``

Sparkflows allows users to view workflows as JSON. They can be  copied and pasted into the workflow JSON editor of another instance.

A more automated way to export and import the workflows is on the roadmap.


``How does one define a new data source and establish a connection?``
 
Sparkflows platform has various OOTB connectors to HIVE, Flume, Kafka, HBase, Solr.
For all other structured or unstructured datasets on HDFS or CloudBricks, Sparkflows platform can identify the schema on the fly when a new dataset is created in Sparkflows pointing to a data source. The schema can be updated right there as well.
Sparkflows workflow execution writes a summary of its output to MySQL/Oracle/H2 which is accessible by the users of the system.


``When running on a Spark cluster how does Sparkflows submit the spark jobs?``
 
Sparkflows uses spark-submit to submit the Spark jobs to the cluster. Hence it is important that spark-submit work from the maching on which Sparkflows is installed.
