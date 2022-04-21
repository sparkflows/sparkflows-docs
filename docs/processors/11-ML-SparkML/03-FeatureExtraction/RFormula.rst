R Formula
=========== 

RFormula feature selection, RFormula selects columns specified by an R model formula. Currently we support a limited subset of the R operators, including ‘~’, ‘.’, ‘:’, ‘+’, and ‘-‘

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodeRFormula

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
      * - formula
        - Formula
        - formula
      * - labelCol
        - Label Column
        - The label column name


Details
-------


RFormula selects columns specified by an R model formula. Currently we support a limited subset of the R operators, including ‘~’, ‘.’, ‘:’, ‘+’, and ‘-‘. 

More details are available at : https://spark.apache.org/docs/latest/ml-features.html#rformula


Examples
-------


The below example is available at : https://spark.apache.org/docs/latest/ml-features.html#rformula
+++++++++++++++


import org.apache.spark.ml.feature.RFormula

val dataset = spark.createDataFrame(Seq(
  (7, "US", 18, 1.0),
  (8, "CA", 12, 0.0),
  (9, "NZ", 15, 0.0)
)).toDF("id", "country", "hour", "clicked")

val formula = new RFormula()
  .setFormula("clicked ~ country + hour")
  .setFeaturesCol("features")
  .setLabelCol("label")

val output = formula.fit(dataset).transform(dataset)
output.select("features", "label").show()
