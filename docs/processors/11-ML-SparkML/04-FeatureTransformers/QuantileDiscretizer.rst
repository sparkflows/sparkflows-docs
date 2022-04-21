Quantile Discretizer
=========== 

QuantileDiscretizer takes a column with continuous features and outputs a column with binned categorical features.

Input
--------------
It takes in a DataFrame and transforms it to another DataFrame

Output
--------------
The output DataFrame contains a new column of binned categorical features.

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodeQuantileDiscretizer

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
        - The Input column name
      * - outputCol
        - Output Column
        - Output column name
      * - numBuckets
        - NumBuckets
        - Maximum number of buckets (quantiles or categories) into which the data points are grouped. Must be >= 2.


Details
-------


QuantileDiscretizer takes a column with continuous features and outputs a column with binned categorical features. The number of bins is set by the numBuckets parameter.

More at Spark MLlib/ML docs page : https://spark.apache.org/docs/2.0.0/ml-features.html#quantilediscretizer


Examples
-------


The below example is available at : https://spark.apache.org/docs/2.0.0/ml-features.html#quantilediscretizer
+++++++++++++++

import org.apache.spark.ml.feature.QuantileDiscretizer

val data = Array((0, 18.0), (1, 19.0), (2, 8.0), (3, 5.0), (4, 2.2))
var df = spark.createDataFrame(data).toDF("id", "hour")

val discretizer = new QuantileDiscretizer()
  .setInputCol("hour")
  .setOutputCol("result")
  .setNumBuckets(3)

val result = discretizer.fit(df).transform(df)
result.show()
