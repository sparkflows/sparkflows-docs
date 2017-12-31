
OpenNLPNameFinder
^^^^^^ 

This node finds names using OpenNLP. It takes in the OpenNLP model. Models can be downloaded from http://opennlp.sourceforge.net/models-1.5/

type

transform

nodeClass

fire.nodes.opennlp.NodeOpenNLPNameFinder

Fields

+-----------+-------------------+--------------------------------------------------------------+
| Name      | Title             | Description                                                  |
+===========+===================+==============================================================+
| model     | Model             | Path to the model file (on HDFS when running on the cluster) |
+-----------+-------------------+--------------------------------------------------------------+
| inputCol  | Input Text Column | input column name                                            |
+-----------+-------------------+--------------------------------------------------------------+
| outputCol | Output Column     | Output Column containing the results                         |
+-----------+-------------------+--------------------------------------------------------------+