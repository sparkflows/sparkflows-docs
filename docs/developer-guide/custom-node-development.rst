Custom Node Development & Deployment
====================================

Sparkflows follows an open and extensible architecture allowing developers to add custom nodes that can be exposed in the UI and embedded into workflows.
 
 
Examples of Custom  nodes
--------------------------
 
  * https://github.com/sparkflows/writing-new-node
  * https://github.com/sparkflows/sparkflows-stanfordcorenlp
 
 

Coding the Custom nodes
------------------------
 
  * Include the fire jar file in your Java/Scala project.
  * Write the new Node extending the ``Node`` class.
  * Implement/Override the ``execute()`` method.
  * If the node is changing the incoming schema, also implement/override the ``getOutputSchema()`` method.
 
Deploying the Custom node in fire-ui
-------------------------------------
 
  * Create a jar file and place it in the ``user-lib`` directory of sparkflows
  * Create a json for the new node and place it under the ``nodes`` directory. The json file defines the fields that the user can edit in the UI and also the class file for the node.
  * Restart the fire server.
  * The new node would be picked up by the UI framework.
  
Using the custom node in spark submit when running on the Spark cluster
-------------------------------------------------------------------------  
 
  * Include the custom node with ``--jars <...>`` when running the workflow on the cluster


