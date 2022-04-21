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


Examples
-------


The below example is available at : http://spark.apache.org/docs/latest/ml-features.html#vectorslicer
+++++++++++++++

import java.util.Arrays

import org.apache.spark.ml.attribute.{Attribute, AttributeGroup, NumericAttribute}
import org.apache.spark.ml.feature.VectorSlicer
import org.apache.spark.ml.linalg.Vectors
import org.apache.spark.sql.Row
import org.apache.spark.sql.types.StructType

val data = Arrays.asList(Row(Vectors.dense(-2.0, 2.3, 0.0)))

val defaultAttr = NumericAttribute.defaultAttr
val attrs = Array("f1", "f2", "f3").map(defaultAttr.withName)
val attrGroup = new AttributeGroup("userFeatures", attrs.asInstanceOf[Array[Attribute]])

val dataset = spark.createDataFrame(data, StructType(Array(attrGroup.toStructField())))

val slicer = new VectorSlicer().setInputCol("userFeatures").setOutputCol("features")

slicer.setIndices(Array(1)).setNames(Array("f3"))
// or slicer.setIndices(Array(1, 2)), or slicer.setNames(Array("f2", "f3"))

val output = slicer.transform(dataset)
println(output.select("userFeatures", "features").first())
