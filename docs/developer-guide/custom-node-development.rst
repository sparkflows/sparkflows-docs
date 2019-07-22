Custom Node Development & Deployment
====================================

Fire Insights follows an open and extensible architecture allowing developers to add custom nodes that can be exposed in Fire UI and embedded into workflows.
 
 
**The details for building new nodes are available at the URL below:**
 
  * https://github.com/sparkflows/writing-new-node
  
**Examples of more complex nodes are at the URL below :**

  * https://github.com/sparkflows/sparkflows-stanfordcorenlp
 
Start by cloning the github repo: writing-new-node
-----------------------------------------------------

The easiest way to start writing a new node or processor is by cloning the ``writing-new-node`` repo using the command below:

    git clone https://github.com/sparkflows/writing-new-node.git
  

Code the new custom node
------------------------
 
 Start by creating a new class that extends ``Node`` class.
  * Override the ``execute()`` method to write custom code. The ``execute()`` method wiill ``transform`` the incoming DataFrame and then pass on the resulting DataFrame to output node(s).
  * In case this new node creates a ``new DataFrame`` by reading data from a Data Source, the incoming DataFrame would be null. The new node will create a new DataFrame from the data directory from the Data Source. Example of data sources include:
  
    * Files on HDFS
    * HIVE tables
    * HBase tables
    * Cassandra
    * MongoDB
    * Salesforce / Marketo
    * etc.
  * If the node is updating the incoming schema, also override the ``getOutputSchema()`` method.
  
**Examples of Custom Nodes:**

  * https://github.com/sparkflows/writing-new-node/tree/master/src/main/java/fire/nodes/examples
  * https://github.com/sparkflows/writing-new-node/tree/spark-2.x/src/main/java/fire/nodes/examples
  * https://github.com/sparkflows/writing-new-node/blob/master/src/main/scala/fire/nodes/examples/NodeTestDateToAge.scala
  
There is minor difference between the code for Apache Spark 1.6.X and Apache Spark 2.X.

``DataFrames`` are used for Apache Spark 1.6.X, while ``Dataset<Row>`` is used for Apache Spark 2.X.
 
Create the node JSON file
-------------------------

Create the JSON file for the new node. The JSON file is used for displaying the new node in the ``Workflow Editor`` and capturing the user inputs of the various fields of the node through a ``Dialog box``. The JSON for the node also captures the name of the ``Java/Scala class`` which has the implementation code for the Node.

Fire supports various ``widgets types`` for capturing the details of the fields from the user through the ``Node Dialog Box``. 

**The details of the various widget types is available at the hyperkink below:**

* https://github.com/sparkflows/writing-new-node/blob/master/docs/README_Processor_JSON.md

**Examples of Node JSON:**

* https://github.com/sparkflows/writing-new-node/blob/master/testprintnrows.json
* https://github.com/sparkflows/sparkflows-stanfordcorenlp/tree/master/nodes/StanfordCoreNLP


Deploy the Custom Node in the Fire Server
-----------------------------------------

Now that you have created a new node, follow the steps below to deploy it:
 
  * Create a jar file with ``mvn clean package``
  * Copy the jar file create above into ``fire-user-lib`` directory of sparkflows
  * Place the JSON file for the new node under the ``nodes`` directory.
  * ``Restart`` the Fire Server.
  * The new node will be picked up by the Fire Server and be visible in the ``Workflow Editor``
  * Check that new node is available as expected in the ``Workflow Editor``
  
Use the custom node in Spark submit when running on the Spark cluster
--------------------------------------------------------------------- 
 
  * Include the custom node with ``--jars <...>`` when running the workflow on the cluster


