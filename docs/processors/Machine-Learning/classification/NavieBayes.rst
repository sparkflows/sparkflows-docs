NavieBayes
=========== 

Creates a NavieBayes model. It supports both Multinomial NB which can handle finitely supported discrete data. For example, by converting documents into TF-IDF vectors, it can be used for document classification. By making every vector a binary (0/1) data, it can also be used as Bernoulli NB.The input feature values must be nonnegative

Type
--------- 

ml-estimator

Class
--------- 

fire.nodes.ml.NodeNaiveBayes

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - featuresCol
        - Features Column
        - Features column of type vectorUDT for model fitting
      * - labelCol
        - Label Column
        - The label column for model fitting
      * - predictionCol
        - Prediction Columns
        - The prediction column created during model scoring
      * - rawPredictionCol
        - Raw Prediction Column
        - The raw prediction (a.k.a. confidence) column name
      * - modelType
        - modelType
        - The model type. Supported options: multinomial and bernoulli. (default = multinomial)
      * - smoothing
        - Smoothing
        - The smoothing parameter.




