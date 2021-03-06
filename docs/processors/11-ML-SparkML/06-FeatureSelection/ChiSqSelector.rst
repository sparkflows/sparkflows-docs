ChiSq Selector
=========== 

Chi-Squared feature selection, which selects categorical features to use for predicting a categorical label.

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodeChiSqSelector

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
        - The features column name
      * - outputCol
        - Output Column
        - The output column name
      * - labelCol
        - Label Column
        - The label column name
      * - numTopFeatures
        - NumTopFeatures
        - Number of features that selector will select (ordered by statistic value descending).


Details
-------


ChiSqSelector stands for Chi-Squared feature selection. It operates on labeled data with categorical features. ChiSqSelector uses the Chi-Squared test of independence to decide which features to choose.

More details are available at : http://spark.apache.org/docs/latest/ml-features.html#chisqselector


