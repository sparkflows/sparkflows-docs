Vector Slicer
=========== 

VectorSlicer feature selection, which takes a feature vector and outputs a new feature vector with a sub-array of the original features. It is useful for extracting features from a vector column

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodeVectorSlicer

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCol
        - Features Column 
        - The features column name
      * - outputCol
        - Output Column
        - The output column name
      * - indices
        - Indices
        - comma seprated
      * - names
        - Names
        - The output column name


Details
-------


VectorSlicer is a transformer that takes a feature vector and outputs a new feature vector with a sub-array of the original features. It is useful for extracting features from a vector column.

VectorSlicer accepts a vector column with specified indices, then outputs a new vector column whose values are selected via those indices.

More details are available at : http://spark.apache.org/docs/latest/ml-features.html#vectorslicer


