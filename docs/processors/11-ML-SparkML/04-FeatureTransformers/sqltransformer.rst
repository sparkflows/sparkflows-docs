SQL Transformer
=========== 

This node runs the given SQL on the incoming DataFrame using Spark ML SQLTransformer

Type
--------- 

transform

Class
--------- 

fire.nodes.ml.NodeSQLTransformer

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - tempTable
        - Temp Table
        - Temp Table Name to be used
      * - sql
        - SQL
        - SQL to be run
      * - outputColNames
        - Output Column Names
        - Name of the Output Columns
      * - outputColTypes
        - Output Column Types
        - Data Type of the Output Columns
      * - outputColFormats
        - Output Column Formats
        - Format of the Output Columns


Details
-------


SQLTransformer implements the transformations which are defined by SQL statement. Currently we only support SQL syntax like "SELECT ... FROM __THIS__ ..." where "__THIS__" represents the underlying table of the input dataset. 

More at Spark MLlib/ML docs page : https://spark.apache.org/docs/2.0.0/ml-features.html#sqltransformer


Examples
-------


The below example is available at : https://spark.apache.org/docs/2.0.0/ml-features.html#sqltransformer
+++++++++++++++

A PolynomialExpansion class provides this functionality. The example below shows how to expand your features into a 3-degree polynomial space.
import org.apache.spark.ml.feature.SQLTransformer

val df = spark.createDataFrame(
  Seq((0, 1.0, 3.0), (2, 2.0, 5.0))).toDF("id", "v1", "v2")

val sqlTrans = new SQLTransformer().setStatement(
  "SELECT *, (v1 + v2) AS v3, (v1 * v2) AS v4 FROM __THIS__")

sqlTrans.transform(df).show()
