PCA
=========== 

Trains a model to project vectors to a low-dimensional space using PCA.

Input
--------------
This takes in a DataFrame as input

Output
--------------
The output DataFrame is a projection of the vectors in the incoming DataFrame to a low-dimensional space using PCA

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodePCA

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCol
        - Input Column
        - The input column name
      * - outputCol
        - Output Column
        - The output column name
      * - k
        - K
        - The number of principal components


Details
======


PCA trains a model to project vectors to a low-dimensional space using PCA.

More at Spark MLlib/ML docs page : http://spark.apache.org/docs/latest/ml-features.html#pca


