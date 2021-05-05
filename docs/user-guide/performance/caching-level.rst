Caching Level
=============

Setting the right caching level of the Dataset outputs of the nodes is very important for performance in Apache Spark.

Fire allows you to set the caching output of the Dataset of any Processor.

When to use Caching
-------------------

In general the default Caching does not have to be changed.

It is important to set Caching in the following scenarios:

* If the Dataset is going to be reused later. Below are some examples.

  * A Dataset is read from HBase. Then another dataset is read and the two are joined. In this case it is a good idea to Cache the dataset read from HBase.
  * A Dataset is joined with another Dataset. The result is then joing with another Dataset. In this case it is a good idea to cache the result of the first Join.
  
* A Dataset which is used in machine learning.

* Whenever a Dataset computation is expensive (JOIN etc.), caching can help in case the executor fails, the blocks are evicted from memory.

