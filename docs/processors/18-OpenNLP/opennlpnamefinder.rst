OpenNLPNameFinder
=========== 

This node finds names using OpenNLP. It takes in the OpenNLP model. Models can be downloaded from http://opennlp.sourceforge.net/models-1.5/

Input
--------------
It takes in a DataFrame as input.

Output
--------------
It extracts the names from the specified column and stores the result in the specified output column.

Type
--------- 

transform

Class
--------- 

fire.nodes.opennlp.NodeOpenNLPNameFinder

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
        - input column name
      * - outputCol
        - Output Column
        - Output Column containing the results


Details
-------


This node performs  namefinder using OpenNLP to easily detect named entities and numbers in text.

To be able to detect entities the Name Finder needs a model. The model is dependent on the language and entity type it was trained for.

https://opennlp.apache.org/documentation/1.6.0/manual/opennlp.html#tools.namefind.recognition.cmdline

The OpenNLP project offers a number of pre-trained name finder models which are trained on various freely available corpora. They can be downloaded at the OpenNLP download page.

http://opennlp.sourceforge.net/models-1.5/


