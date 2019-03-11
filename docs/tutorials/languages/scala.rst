Scala Examples in Fire
----------------------

Fire provides a Scala processer in which Scala code can be written.

Below are a few code examples in Scala.

Calculate count of houses by bathrooms
======================================

val outDF = inDF.groupBy("bathrms").count()

outDF.registerTempTable("outDF")


For each bedroom type, find the house with the lowest price
===========================================================

import org.apache.spark.sql.expressions.Window
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
val window = Window.partitionBy("bedrooms").orderBy("price")
val rankDF = inDF.withColumn("rank", rank() over window)
val lowestPriceDF = rankDF.filter(col("rank") === 1)
val outDF = lowestPriceDF.drop(col("rank"))
outDF.registerTempTable("outDF")

