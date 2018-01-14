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
  

Code the Custom nodes
---------------------
 
  * Write the new Node extending the ``Node`` class.
  * Implement/Override the ``execute()`` method. It would transform the incoming DataFrame and and then pass on the resulting DataFrame to its output Nodes.
  * In case this Node creates a new DataFrame by reading some data, the incoming DataFrame would be null and this Node would create a new DataFrame from the Data in the store.
  * If the node is updating the incoming schema, also implement/override the ``getOutputSchema()`` method.
 
Create the Node JSON file
-------------------------

Create the JSON file for the new Node. Fire server uses it for displaying it in the User Interface and capturing the details of it fields through a Dialog box. It also captures the Java/Scala class which has the implementation code for the Node.

Fire supports various widgets types for capturing the details of the fields from the user. Their details of the various widget types is available at:

* https://github.com/sparkflows/writing-new-node/blob/master/docs/README_Processor_JSON.md

Deploy the Custom node in fire-ui
---------------------------------
 
  * Create a jar file and place it in the ``user-lib`` directory of sparkflows
  * Place the JSON file for the new node under the ``nodes`` directory.
  * Restart the fire server.
  * The new node would be picked up by the UI framework.
  
Use the custom node in spark submit when running on the Spark cluster
--------------------------------------------------------------------- 
 
  * Include the custom node with ``--jars <...>`` when running the workflow on the cluster


