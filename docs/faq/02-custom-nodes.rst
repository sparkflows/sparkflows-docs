Custom Nodes
-------------

Does Sparkflows allow me to create my own custom nodes?
===========

Yes, new Nodes can be easily to added to SparkFlows. Develop nodes in Java or in Scala and dop the definition JSON for the node on the server. The newly added nodes will become visible in the Sparkflows User Interface.


How does one define a new data source and establish a connection?
=============
 
Sparkflows platform has various OOTB connectors to HIVE, Flume, Kafka, HBase, Solr.
For all other structured or unstructured datasets on HDFS or CloudBricks, Sparkflows platform can identify the schema on the fly when a new dataset is created in Sparkflows pointing to a data source. The schema can be updated right there as well.
Sparkflows workflow execution writes a summary of its output to MySQL/Oracle/H2 which is accessible by the users of the system.


