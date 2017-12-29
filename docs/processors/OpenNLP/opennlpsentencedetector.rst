
OpenNLPSentenceDetector
^^^^^^ 

This node detects sentences using OpenNLP - https://opennlp.apache.org/documentation/1.7.2/manual/opennlp.html#tools.sentdetect. It takes in the OpenNLP model. Models can be downloaded from http://opennlp.sourceforge.net/models-1.5/

type

transform

nodeClass

fire.nodes.opennlp.NodeOpenNLPSentenceDetector

Fields

+-----------+-------------------+--------------------------------------------------------------+
|    Name   |       Title       |                         Description                          |
+-----------+-------------------+--------------------------------------------------------------+
|   model   |       Model       | Path to the model file (on HDFS when running on the cluster) |
|  inputCol | Input Text Column |                      input cpulmn name                       |
| outputCol |   Output Column   |             Output Column containing the results             |
+-----------+-------------------+--------------------------------------------------------------+