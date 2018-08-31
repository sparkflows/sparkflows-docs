Caching Level
=============

Setting the right caching level of the Dataset outputs of the nodes is very important for performance in Apache Spark.

Fire allows you to set the caching output of the Dataset of any Processor.

When to use Caching
-------------------

It is important to set Caching in the following scenarios:

* RDD re-use in iterative machine learning applications
* RDD re-use in standalone Spark applications
* When RDD computation is expensive, caching can help in reducing the cost of recovery in the case one executor fails.



