Custom Node Development & Deployment
====================================

Sparkflows follows an open and extensible architecture allowing developers to add custom nodes that can be exposed in the UI and embedded into workflows.
 
 
**The details for building New Nodes are available at:**
 
  * https://github.com/sparkflows/writing-new-node
  
**Examples of more complex Nodes are at:**

  * https://github.com/sparkflows/sparkflows-stanfordcorenlp
 
Start with the writing-new-node repo
------------------------------------

The easiest way to start writing a new Node/Processor for Fire is to clone the ``writing-new-node`` repo::

    git clone https://github.com/sparkflows/writing-new-node.git

Use the appropriate branch based on your requirements::

    master branch for Spark 1.6.X
    
    spark-2.x for Spark 2.X
  

Code the Custom nodes
---------------------
 
  * Write the new Node extending the ``Node`` class.
  * Implement/Override the ``execute()`` method. It would transform the incoming DataFrame and and then pass on the resulting DataFrame to its output Nodes.
  * If the node is updating the incoming schema, also implement/override the ``getOutputSchema()`` method.
 
Create the Node JSON file
-------------------------

Fire supports various widgets. Their details are available at:

* https://github.com/sparkflows/writing-new-node/blob/master/docs/README_widgets.md

Deploy the Custom node in fire-ui
---------------------------------
 
  * Create a jar file and place it in the ``user-lib`` directory of sparkflows
  * Create a json for the new node and place it under the ``nodes`` directory. The json file defines the fields that the user can edit in the UI and also the class file for the node.
  * Restart the fire server.
  * The new node would be picked up by the UI framework.
  
Use the custom node in spark submit when running on the Spark cluster
--------------------------------------------------------------------- 
 
  * Include the custom node with ``--jars <...>`` when running the workflow on the cluster


