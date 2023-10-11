Overview
=================

This document serves as a detailed guide to help you to deploy Fire Insights on AWS.

Installation
--------

Fire Insights can be installed on a standalone EC2 machine,  AWS Fargate or AWS EKS. The jobs triggered by the users would be able to access and process data stored in S3, HDFS, Redshift, Kinesis and other EC2 storage. Compute connections can also be created in Fire Insights to connect to AWS EMR, AWS Glue.


Costs
-----

The main costs incurred when using Fire Insights is the cost of running the EMR cluster which has master nodes and workflow nodes. The more processing capacity needed, the larger should be the size of the EMR cluster. Pricing details for EMR can be found here: https://aws.amazon.com/emr/pricing/

Fire Insights can also run Machine Learning jobs onto SageMaker. There would be some additional costs associated with using AWS SageMaker. Pricing details for AWS SageMaker can be found here: https://aws.amazon.com/sagemaker/pricing/


Sizing
------

* AWS EMR cluster normally starts with a minimum of 1 master node and 2 worker nodes. It is recommended to use machines with at least 16GB of space for the master and worker nodes. As the size of data and the number of concurrent users increases, it is recommended to increase the size of EMR cluster accordingly. Memory for the worker nodes can be increased from a minimum of 16GB to a maximum of 512GB. Since Apache Spark can use the additional memory to process faster and more efficiently, it is ideal to increase the memory base on the compute load. The same holds true for the number of disks and scores.

* AWS ECS container is expected to have a minimum of 6 vCPU and 16GB memory.
