
##Tune the Big Data Infrastructure (Elastic Map Reduce Computes)

- Getting the Right Partition Size and Instance Type.
- The general principles to be followed when tuning partition for Spark application are as follows:
  - Too few partitions – Cannot utilize all cores available in the cluster.
  - Too many partitions – Excessive overhead in managing many small tasks.
  - Reasonable partitions – Helps us to utilize the cores availab
