Spark Pipeline
=========== 

This node represents Pipeline from Spark ML

Input
--------------
It takes in a DataFrame as input.

Output
--------------
The incoming DataFrame is passed to the output.

Type
--------- 

ml-pipeline

Class
--------- 

fire.nodes.ml.NodePipeline

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description


Details
-------


This node represents Pipeline from Spark ML.

In machine learning, it is common to run a sequence of algorithms to process and learn from data. 
E.g., a simple text document processing workflow might include several stages:


*  Split each document’s text into words.
*  Convert each document’s words into a numerical feature vector.
*  Learn a prediction model using the feature vectors and labels.


MLlib represents such a workflow as a Pipeline, which consists of a sequence of PipelineStages (Transformers and Estimators) to be run in a specific order. 

More at Spark MLlib/ML docs page : http://spark.apache.org/docs/latest/ml-pipeline.html#pipeline


