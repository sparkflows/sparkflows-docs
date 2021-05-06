NodeOpenNLPDocumentCategorizer
=========== 

This node classifies text into pre-defined categories using OpenNLP - https://opennlp.apache.org/documentation/1.7.2/manual/opennlp.html#tools.doccat. It takes in the OpenNLP model. Models can be downloaded from http://opennlp.sourceforge.net/models-1.5/

Input
--------------
It takes in a DataFrame as input.

Output
--------------
It finds the Document Category and stores the result in the specified output column.

Type
--------- 

transform

Class
--------- 

fire.nodes.opennlp.NodeOpenNLPDocumentCategorizer

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - model
        - Model
        - Path to the model file (on HDFS when running on the cluster)
      * - inputCol
        - Input Text Column
        - input cpulmn name
      * - outputCol
        - Output Column
        - Output Column containing the results


Details
-------


This node classifies text into pre-defined categories using OpenNLP


https://opennlp.apache.org/documentation/1.7.2/manual/opennlp.html#tools.doccat.


It takes in the OpenNLP model. Models can be downloaded from http://opennlp.sourceforge.net/models-1.5/


