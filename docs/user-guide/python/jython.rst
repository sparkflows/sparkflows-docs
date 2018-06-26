Jython
======

Sparkflows has a Jython Processor.

The Jython Processor allows writing Jython code to process the incoming DataFrame. It then produces a resulting DataFrame.

In the Jython node, the following variables are available:

**inDF** : Incoming Spark DataFrame which is distributed.
**spark** : The Spark session object

Example Jython Code
-------------------

Below are some example Jython code which can be used.

Select a specific column from the DataFrame
++++++++++++++++++++++++++++++++++++++++++++

outDF = inDF.select("c2")

Count the number of records after grouping them
++++++++++++++++++++++++++++++++++++++++++++

outDF = inDF.groupBy("c2").count()

Run a SQL on the input DataFrame
++++++++++++++++++++++++++++++++++++++++++++

outDF = spark.sql("SELECT c1, c2 FROM fire_temp_table")

Run a SQL followed by further grouping and count
++++++++++++++++++++++++++++++++++++++++++++

outDF = spark.sql("SELECT c1, c2 FROM fire_temp_table")
outDF = outDF.groupBy("c2").count()

Read from HDFS and create a new DataFrame
++++++++++++++++++++++++++++++++++++++++++++

outDF = spark.read().json("data/people.json")





