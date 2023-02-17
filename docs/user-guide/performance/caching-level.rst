Caching Level
=============

Setting the right caching level of the dataset outputs of the nodes is very important for performance in Apache Spark.

Fire allows you to set the caching output of the dataset of any processor.

When to use Caching
-------------------

In general the default Caching does not have to be changed. It is MEMORY ONLY for Apache Spark.

It is important to set it to MEMORY_AND_DISK in the following scenarios:

* If the dataset is going to be reused later. Below are some examples.

  * A dataset is read from HBase. Then another dataset is read and the two are joined. In this case, it is a good idea to Cache the dataset read from HBase.
  * A dataset is joined with another dataset. The result is then joining with another dataset. In this case, it is a good idea to cache the result of the first Join.
  
* A Dataset which is used in machine learning.

* Whenever a dataset computation is expensive (JOIN etc.), MEMORY_AND_DISK caching level can help in case the executor fails.

