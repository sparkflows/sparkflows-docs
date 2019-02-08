Scala Examples in Fire
----------------------

Fire provides a Scala processer in which Scala code can be written.

Below are a few code examples in Scala.

Calculate count of houses by bathrooms
======================================

val outDF = inDF.groupBy("bathrms").count()

outDF.registerTempTable("outDF")

