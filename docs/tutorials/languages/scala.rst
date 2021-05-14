Scala Examples in Fire
----------------------

Fire provides a Scala processer in which Scala code can be written.

The Scala node does the below:

  * Receives an input dataframe.
  * Passes the input dataframe to the Scala code as a variable called `inDF`.
  * The scala code written operated on the dataframe `inDF`.
  * Finally the scala code produces a resulting dataframe to be passed on to the next node. It does so by registering a temporary table called `outDF`.

Below are a few code examples in Scala.

Calculate count of houses by bathrooms
======================================

::

    val outDF = inDF.groupBy("bathrms").count()
    outDF.registerTempTable("outDF")


For each bedroom type, find the house with the lowest price
===========================================================

::

    import org.apache.spark.sql.expressions.Window
    import org.apache.spark.sql._
    import org.apache.spark.sql.functions._
    val window = Window.partitionBy("bedrooms").orderBy("price")
    val rankDF = inDF.withColumn("rank", rank() over window)
    val lowestPriceDF = rankDF.filter(col("rank") === 1)
    val outDF = lowestPriceDF.drop(col("rank"))
    outDF.registerTempTable("outDF")

