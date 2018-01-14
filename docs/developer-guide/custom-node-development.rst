Custom Node Development & Deployment
====================================

Sparkflows follows an open and extensible architecture allowing developers to add custom nodes that can be exposed in the UI and embedded into workflows.
 
 
**The details for building New Nodes are available at:**
 
  * https://github.com/sparkflows/writing-new-node
  
**Examples of more complex Nodes are at:**

  * https://github.com/sparkflows/sparkflows-stanfordcorenlp
 
Start with cloning the github repo : writing-new-node
-----------------------------------------------------

The easiest way to start writing a new Node/Processor for Fire is to clone the ``writing-new-node`` repo::

    git clone https://github.com/sparkflows/writing-new-node.git

Use the appropriate branch based on your requirements::

    master branch for Spark 1.6.X
    
    spark-2.x branch for Spark 2.X
  

Code the New Custom Node
------------------------
 
  * Write the new Node extending the ``Node`` class.
  * Implement/Override the ``execute()`` method. It would ``transform`` the incoming DataFrame and and then pass on the resulting DataFrame to its output Nodes.
  * In case this Node creates a ``new DataFrame`` by reading data from a Data Source, the incoming DataFrame to this Node would be null. This Node would create a new DataFrame from the Data read directory from the Data Source. Example of Data Sources could be:
  
    * Files on HDFS
    * HIVE tables
    * HBase tables
    * Cassandra
    * MongoDB
    * Salesforce / Marketo
    * etc.
  * If the node is updating the incoming schema, also implement/override the ``getOutputSchema()`` method.
  
**Examples of Custom Nodes:**

  * https://github.com/sparkflows/writing-new-node/tree/master/src/main/java/fire/nodes/examples
  * https://github.com/sparkflows/writing-new-node/tree/spark-2.x/src/main/java/fire/nodes/examples
  * https://github.com/sparkflows/writing-new-node/blob/master/src/main/scala/fire/nodes/examples/NodeTestDateToAge.scala
  
There is minor difference between the code for Spark 1.6.X and Spark 2.X.

``DataFrames`` are used for Spark 1.6.X, while ``Dataset<Row>`` is used for Spark 2.X.
 
Create the Node JSON file
-------------------------

Create the JSON file for the new Node. Fire server uses it for displaying it in the ``Workflow Editor`` and capturing the user inputs of the various fields of the Node through a ``Dialog box``. It also captures the name of the ``Java/Scala class`` which has the implementation code for the Node.

Fire supports various ``widgets types`` for capturing the details of the fields from the user through the ``Node Dialog Box``. 

**The details of the various widget types is available at:**

* https://github.com/sparkflows/writing-new-node/blob/master/docs/README_Processor_JSON.md

**Examples of Node JSON:**

* https://github.com/sparkflows/writing-new-node/blob/master/testprintnrows.json
* https://github.com/sparkflows/sparkflows-stanfordcorenlp/tree/master/nodes/StanfordCoreNLP


Deploy the Custom Node in the Fire Server
-----------------------------------------
 
  * Create a jar file and place it in the ``user-lib`` directory of sparkflows
  
    * ``mvn clean package``
  * Place the JSON file for the new node under the ``nodes`` directory.
  * Restart the Fire Server.
  * The new node would be picked up by the Fire Server and be visible in the Workflow Editor.
  
Use the Custom Node in spark submit when running on the Spark cluster
--------------------------------------------------------------------- 
 
  * Include the custom node with ``--jars <...>`` when running the workflow on the cluster


