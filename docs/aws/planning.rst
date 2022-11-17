Planning Guide
=================

This document describes details to help you plan on deploying and using Fire Insights on AWS.

Installation
--------

Fire Insights is installed on an EC2 machine. It can also be installed in AWS Fargete or AWS EKS. The jobs fired by the users would be able to access and process data on S3, HDFS, Redshift, Kinesis.

Costs
-----

The main costs involved when using Fire Insights are around the EMR cluster. EMR cluster has master nodes and workflow nodes.

Pricing for EMR can be found here: https://aws.amazon.com/emr/pricing/

The more processing capacity needed, the larger should be the size of the EMR cluster.

Fire Insights can also run Machine Learning Modeling jobs onto SageMaker. If this is used, there would be a cost associated with using AWS SageMaker. Amazon SageMaker Pricing details are here: https://aws.amazon.com/sagemaker/pricing/


Sizing
------

AWS EMR cluster normally starts with a minimum of 1 master node and 2 worker nodes. 

We recommend using at least 16GB machines for the master and worker nodes.

As your data volume and the number of concurrent users increases, we recommend increasing the size of the EMR cluster. Memory for the worker nodes can be increased from16 GB to 32GB to 64GB to 512GB. Since Apache Spark has the ability to use as much memory you provide, it's a good idea to give it more memory.

The same goes for the number of disks and scores.
