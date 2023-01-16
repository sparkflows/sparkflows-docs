Repartioning
============

Repartioning splits the datasets into the specified number of partitions.

This can help with performance

When saving to JDBC/File etc.
------------------------------

When saving a Dataset, the parallelism depends on the number of partitions of the Dataset. In case there are too few partitions, repartitioning the Dataset before saving would increase the parallelism.

Parallelism is also a double-edged sword. It is not a good idea to say have too many parallel connections to a Relational Database as it would put heavy load on the RDBMs.
