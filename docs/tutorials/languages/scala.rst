Scala Examples
----------------------

Fire provides a Scala processer in which Scala code can be written.

The Scala node does the below:

  * Receives an input DataFrame.
  * Passes the input DataFrame to the Scala code as a variable called `inDF`.
  * The scala code written operated on the DataFrame `inDF`.
  * Finally the scala code produces a resulting DataFrame to be passed on to the next node. It does so by registering a temporary table in registerTempTable. Add the temptable name in the `OUTPUT TEMP TABLE` field.

Below are a few code examples in Scala.

Calculate Count of Houses by Bathrooms
======================================

::

    val outDF = inDF.groupBy("bathrms").count()
    outDF.registerTempTable("outDF")


For Each Bedroom Type, Find the House with the Lowest Price
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


Drop certain columns
====================

::

    val columns_to_drop = Array("C6", "C7", "C8", "C9")
    val outDF = inDF.drop(columns_to_drop: _*)
    outDF.registerTempTable("outDF")

Lag function
====================

::

    import org.apache.spark.sql.functions._
    import org.apache.spark.sql.expressions.Window

    val windowSpec  = Window.partitionBy("C4").orderBy("C6")
    val outDF = inDF.withColumn("lag_7",lag("sell_price",7).over(windowSpec))
    outDF.registerTempTable("outDF")

Columns in StructType
======================
Code to get the columns 0 and 1 in the probability column which is StructType.

::

    import org.apache.spark.sql.functions._
    val outDF = inDF.select(col("*"), col("probability.0").as("probability_0"), col("probability.1").as("probability_1"))
    outDF.registerTempTable("outDF")

    .. figure:: ../../_assets/tutorials/languages/scala/scala.png
       :alt: Scala Node
       :width: 60%

    
